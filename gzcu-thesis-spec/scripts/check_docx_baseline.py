#!/usr/bin/env python3
"""Check whether a DOCX matches the GZCU submission baseline."""

from __future__ import annotations

import argparse
import json
import re
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET


NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}
W_NS = NS["w"]
R_NS = NS["r"]
REL_NS = NS["rel"]
REF_BOOKMARK_PREFIX = "gzcu_ref_"
TOC_BOOKMARK_PREFIX = "_Toc"


@dataclass
class CheckResult:
    name: str
    ok: bool
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check a DOCX or unpacked DOCX directory against the GZCU submission baseline."
    )
    parser.add_argument("input_path", help="Path to a .docx file or an unpacked DOCX directory")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON instead of plain text",
    )
    return parser.parse_args()


def qn(name: str) -> str:
    prefix, local = name.split(":")
    return f"{{{NS[prefix]}}}{local}"


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def extract_input(input_path: Path) -> tuple[Path, tempfile.TemporaryDirectory[str] | None]:
    if input_path.is_dir():
        return input_path, None
    if input_path.suffix.lower() != ".docx":
        raise SystemExit("Input must be a .docx file or an unpacked DOCX directory.")
    if not input_path.exists():
        raise SystemExit(f"Input not found: {input_path}")
    tempdir = tempfile.TemporaryDirectory(prefix="gzcu_docx_check_")
    with zipfile.ZipFile(input_path) as zf:
        zf.extractall(tempdir.name)
    return Path(tempdir.name), tempdir


def load_xml(path: Path) -> ET.Element:
    return ET.parse(path).getroot()


def relationship_map(unpacked_root: Path) -> dict[str, str]:
    rels_path = unpacked_root / "word" / "_rels" / "document.xml.rels"
    root = load_xml(rels_path)
    mapping: dict[str, str] = {}
    for rel in root.findall(f"{{{REL_NS}}}Relationship"):
        rid = rel.attrib.get("Id")
        target = rel.attrib.get("Target")
        if rid and target:
            mapping[rid] = target
    return mapping


def document_parts(unpacked_root: Path) -> tuple[ET.Element, ET.Element]:
    root = load_xml(unpacked_root / "word" / "document.xml")
    body = root.find("w:body", NS)
    if body is None:
        raise SystemExit("Invalid DOCX: missing word/document.xml body")
    return root, body


def collect_sections(body: ET.Element, rel_map: dict[str, str]) -> list[dict[str, object]]:
    sections: list[dict[str, object]] = []
    para_index = 0
    for child in body:
        if child.tag != qn("w:p"):
            continue
        ppr = child.find("w:pPr", NS)
        sect = ppr.find("w:sectPr", NS) if ppr is not None else None
        if sect is not None:
            sections.append(build_section_record(sect, rel_map, para_index))
        para_index += 1
    tail = body.find("w:sectPr", NS)
    if tail is not None:
        sections.append(build_section_record(tail, rel_map, "body-end"))
    return sections


def build_section_record(sect: ET.Element, rel_map: dict[str, str], para_index: object) -> dict[str, object]:
    headers = []
    for ref in sect.findall("w:headerReference", NS):
        rid = ref.attrib.get(qn("r:id"))
        headers.append(
            {
                "type": ref.attrib.get(qn("w:type"), "default"),
                "target": rel_map.get(rid or "", ""),
            }
        )
    footers = []
    for ref in sect.findall("w:footerReference", NS):
        rid = ref.attrib.get(qn("r:id"))
        footers.append(
            {
                "type": ref.attrib.get(qn("w:type"), "default"),
                "target": rel_map.get(rid or "", ""),
            }
        )
    pg = sect.find("w:pgNumType", NS)
    return {
        "para_index": para_index,
        "headers": headers,
        "footers": footers,
        "page_start": (pg.attrib.get(qn("w:start")) if pg is not None else None),
        "page_fmt": (pg.attrib.get(qn("w:fmt")) if pg is not None else None),
    }


def collect_instr_text(root: ET.Element) -> list[str]:
    return [text.text or "" for text in root.findall(".//w:instrText", NS)]


def collect_bookmarks(root: ET.Element) -> list[str]:
    return [node.attrib.get(qn("w:name"), "") for node in root.findall(".//w:bookmarkStart", NS)]


def strip_trailing_page_number(text: str) -> str:
    return re.sub(r"\d+$", "", text).strip()


def is_chapter_heading_text(text: str) -> bool:
    if not re.search(r"^第[一二三四五六七八九十]+章", text):
        return False
    if len(text) > 40:
        return False
    if any(mark in text for mark in "，。；："):
        return False
    return True


def main_body_headings(body: ET.Element, sections: list[dict[str, object]]) -> list[str]:
    headings: list[str] = []
    body_start_index = 0
    if len(sections) >= 3 and isinstance(sections[2]["para_index"], int):
        body_start_index = int(sections[2]["para_index"]) + 1
    body_ended = False
    for idx, p in enumerate(body.findall("w:p", NS)):
        if idx < body_start_index:
            continue
        text = norm("".join(t.text or "" for t in p.findall(".//w:t", NS)))
        if not text:
            continue
        clean = strip_trailing_page_number(text)
        if clean in {"结论", "结 论", "参考文献", "致谢", "致 谢"}:
            body_ended = True
        if not body_ended and is_chapter_heading_text(clean):
            headings.append(clean)
    return headings


def count_reference_fields(instr_texts: Iterable[str]) -> int:
    joined = "|".join(instr_texts)
    return len(re.findall(rf"REF\s+{REF_BOOKMARK_PREFIX}\d+", joined))


def count_toc_pageref_fields(instr_texts: Iterable[str]) -> int:
    joined = "|".join(instr_texts)
    return len(re.findall(rf"PAGEREF\s+{TOC_BOOKMARK_PREFIX}\w+", joined))


def has_toc_field(instr_texts: Iterable[str]) -> bool:
    joined = "|".join(instr_texts)
    return " TOC " in joined or joined.startswith("TOC ")


def header_targets_by_type(section: dict[str, object]) -> dict[str, str]:
    return {item["type"]: item["target"] for item in section["headers"]}  # type: ignore[index]


def footer_targets_by_type(section: dict[str, object]) -> dict[str, str]:
    return {item["type"]: item["target"] for item in section["footers"]}  # type: ignore[index]


def inspect_header_xml(unpacked_root: Path, relative_path: str) -> str:
    if not relative_path:
        return ""
    path = unpacked_root / "word" / relative_path
    if not path.exists():
        return ""
    root = load_xml(path)
    return norm("".join(t.text or "" for t in root.findall(".//w:t", NS)))


def check_section_count(sections: list[dict[str, object]]) -> CheckResult:
    ok = len(sections) == 4
    return CheckResult(
        "section_count",
        ok,
        f"found {len(sections)} sections; expected 4",
    )


def check_page_number_model(sections: list[dict[str, object]]) -> CheckResult:
    if len(sections) != 4:
        return CheckResult("page_number_model", False, "section count mismatch prevents baseline check")
    section2_ok = sections[1]["page_fmt"] == "upperRoman" and sections[1]["page_start"] == "1"
    section3_ok = sections[2]["page_fmt"] == "upperRoman" and sections[2]["page_start"] == "1"
    section4_ok = sections[3]["page_fmt"] in {None, ""} and sections[3]["page_start"] == "1"
    ok = section2_ok and section3_ok and section4_ok
    return CheckResult(
        "page_number_model",
        ok,
        (
            f"section2 fmt/start={sections[1]['page_fmt']}/{sections[1]['page_start']}, "
            f"section3 fmt/start={sections[2]['page_fmt']}/{sections[2]['page_start']}, "
            f"section4 fmt/start={sections[3]['page_fmt']}/{sections[3]['page_start']}"
        ),
    )


def check_main_header_model(unpacked_root: Path, sections: list[dict[str, object]]) -> CheckResult:
    if len(sections) != 4:
        return CheckResult("main_header_model", False, "section count mismatch prevents baseline check")
    header_map = header_targets_by_type(sections[3])
    even_target = header_map.get("even", "")
    odd_target = header_map.get("default", "")
    even_text = inspect_header_xml(unpacked_root, even_target)
    odd_xml = inspect_header_xml(unpacked_root, odd_target)
    odd_path = unpacked_root / "word" / odd_target if odd_target else None
    odd_has_styleref = False
    if odd_path and odd_path.exists():
        odd_has_styleref = "STYLEREF" in odd_path.read_text(encoding="utf-8", errors="ignore")
    ok = even_text == "广州城市理工学院本科毕业设计（论文）" and odd_has_styleref
    return CheckResult(
        "main_header_model",
        ok,
        f"even_header='{even_text}', odd_header_styleref={odd_has_styleref}",
    )


def check_toc_fields(instr_texts: list[str]) -> CheckResult:
    toc = has_toc_field(instr_texts)
    pageref_count = count_toc_pageref_fields(instr_texts)
    ok = toc and pageref_count > 0
    return CheckResult(
        "toc_fields",
        ok,
        f"toc_field={toc}, toc_pageref_count={pageref_count}",
    )


def check_reference_crossrefs(instr_texts: list[str], bookmark_names: list[str]) -> CheckResult:
    ref_fields = count_reference_fields(instr_texts)
    bookmark_count = sum(1 for name in bookmark_names if name.startswith(REF_BOOKMARK_PREFIX))
    ok = ref_fields > 0 and bookmark_count > 0
    return CheckResult(
        "reference_crossrefs",
        ok,
        f"ref_field_count={ref_fields}, ref_bookmark_count={bookmark_count}",
    )


def check_body_structure(body: ET.Element, sections: list[dict[str, object]]) -> CheckResult:
    headings = main_body_headings(body, sections)
    expected = [
        "第一章 绪论",
        "第二章 相关技术与理论基础",
        "第三章 系统需求分析",
        "第四章 系统总体设计",
        "第五章 系统详细设计与实现",
        "第六章 系统测试与部署",
    ]
    ok = headings[:6] == expected
    return CheckResult(
        "body_structure",
        ok,
        f"detected headings={headings[:6]}",
    )


def build_report(unpacked_root: Path) -> dict[str, object]:
    root, body = document_parts(unpacked_root)
    rel_map = relationship_map(unpacked_root)
    sections = collect_sections(body, rel_map)
    instr_texts = collect_instr_text(root)
    bookmark_names = collect_bookmarks(root)
    checks = [
        check_section_count(sections),
        check_page_number_model(sections),
        check_main_header_model(unpacked_root, sections),
        check_toc_fields(instr_texts),
        check_reference_crossrefs(instr_texts, bookmark_names),
        check_body_structure(body, sections),
    ]
    summary = {
        "pass_count": sum(1 for item in checks if item.ok),
        "fail_count": sum(1 for item in checks if not item.ok),
    }
    return {
        "summary": summary,
        "checks": [item.__dict__ for item in checks],
        "observed": {
            "section_count": len(sections),
            "reference_bookmark_count": sum(1 for name in bookmark_names if name.startswith(REF_BOOKMARK_PREFIX)),
            "reference_field_count": count_reference_fields(instr_texts),
            "toc_pageref_count": count_toc_pageref_fields(instr_texts),
        },
    }


def print_text_report(report: dict[str, object]) -> None:
    summary = report["summary"]
    print("DOCX baseline check")
    print(f"Passed: {summary['pass_count']}  Failed: {summary['fail_count']}")
    print("")
    for item in report["checks"]:
        status = "PASS" if item["ok"] else "FAIL"
        print(f"[{status}] {item['name']}: {item['detail']}")


def main() -> int:
    args = parse_args()
    source = Path(args.input_path).expanduser().resolve()
    unpacked_root, tempdir = extract_input(source)
    try:
        report = build_report(unpacked_root)
        if args.json:
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            print_text_report(report)
        return 0 if report["summary"]["fail_count"] == 0 else 1
    finally:
        if tempdir is not None:
            tempdir.cleanup()


if __name__ == "__main__":
    raise SystemExit(main())
