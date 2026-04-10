#!/usr/bin/env python
"""Convert body citations like [1] into clickable Word cross-references."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import pythoncom
import win32com.client


BODY_START_PATTERNS = [
    re.compile(r"^第[一二三四五六七八九十]+章"),
    re.compile(r"^1(\.\d+)*\s"),
]
BODY_END_PATTERNS = [
    re.compile(r"^结论$"),
    re.compile(r"^结\s*论$"),
    re.compile(r"^参考文献$"),
]
SUMMARY_PATTERN = re.compile(r"本章小结$")
HEADING_LIKE_PATTERNS = [
    re.compile(r"^第[一二三四五六七八九十]+章"),
    re.compile(r"^\d+(\.\d+){0,2}\s"),
    re.compile(r"^(摘要|ABSTRACT|目录|结论|结\s*论|参考文献|致谢|致\s*谢)$"),
]
CITATION_RE = re.compile(r"\[(\d+)\]")
REF_BOOKMARK_PREFIX = "gzcu_ref_"
DEFAULT_REF_SIZE = 10.5


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build clickable Word cross-references for body citations."
    )
    parser.add_argument("docx_path", help="Source docx path")
    parser.add_argument("--save-as", dest="save_as", help="Output docx path")
    parser.add_argument("--in-place", action="store_true", help="Overwrite source docx")
    return parser.parse_args()


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def is_heading_like(text: str) -> bool:
    return any(p.search(text) for p in HEADING_LIKE_PATTERNS)


def in_main_body(text: str, started: bool) -> tuple[bool, bool]:
    if not started and any(p.search(text) for p in BODY_START_PATTERNS):
        return True, True
    if started and any(p.search(text) for p in BODY_END_PATTERNS):
        return False, False
    return started, started


def collect_reference_paragraphs(paragraphs) -> dict[str, object]:
    refs_started = False
    ref_map: dict[str, object] = {}
    for p in paragraphs:
        text = norm(p.Range.Text)
        if not refs_started:
            if text == "参考文献":
                refs_started = True
            continue
        if text in {"致谢", "致 谢"}:
            break
        match = re.match(r"^\[(\d+)\]", text)
        if match:
            ref_map[match.group(1)] = p
    return ref_map


def ensure_bookmarks(document, ref_map: dict[str, object]) -> dict[str, str]:
    bookmark_map: dict[str, str] = {}
    for index, paragraph in ref_map.items():
        bookmark_name = f"{REF_BOOKMARK_PREFIX}{index}"
        rng = paragraph.Range.Duplicate
        start = rng.Start
        end = min(rng.End, start + len(f"[{index}]"))
        bookmark_range = document.Range(Start=start, End=end)
        if document.Bookmarks.Exists(bookmark_name):
            document.Bookmarks(bookmark_name).Delete()
        document.Bookmarks.Add(bookmark_name, bookmark_range)
        bookmark_map[index] = bookmark_name
    return bookmark_map


def resolve_range_font_size(rng) -> float:
    size = getattr(rng.Font, "Size", 0) or 0
    if size:
        return float(size)
    if rng.Characters.Count > 0:
        size = getattr(rng.Characters(1).Font, "Size", 0) or 0
        if size:
            return float(size)
    return DEFAULT_REF_SIZE


def apply_ref_result_format(result_range, font_size: float) -> None:
    result_range.Font.Size = font_size
    result_range.Font.Superscript = True
    for i in range(1, result_range.Characters.Count + 1):
        char = result_range.Characters(i)
        char.Font.Size = font_size
        char.Font.Superscript = True


def apply_ref_charformat(field, font_size: float) -> None:
    field.Code.Characters(1).Font.Size = font_size
    field.Code.Characters(1).Font.Superscript = True
    field.Update()
    apply_ref_result_format(field.Result, font_size)


def replace_citations_in_paragraph(document, paragraph, bookmark_map: dict[str, str]) -> int:
    original = paragraph.Range.Text
    matches = list(CITATION_RE.finditer(original))
    if not matches:
        return 0

    inserted = 0
    for match in reversed(matches):
        ref_no = match.group(1)
        bookmark = bookmark_map.get(ref_no)
        if not bookmark:
            continue
        rng = paragraph.Range.Duplicate
        rng.Start = paragraph.Range.Start + match.start()
        rng.End = paragraph.Range.Start + match.end()
        if rng.Fields.Count > 0:
            continue
        font_size = resolve_range_font_size(rng)
        rng.Text = ""
        document.Fields.Add(
            rng,
            Type=3,
            Text=f"{bookmark} \\h \\* CHARFORMAT",
            PreserveFormatting=False,
        )
        field = document.Fields(document.Fields.Count)
        apply_ref_charformat(field, font_size)
        inserted += 1
    return inserted


def paragraph_has_ref_field(paragraph) -> bool:
    for i in range(1, paragraph.Range.Fields.Count + 1):
        field = paragraph.Range.Fields.Item(i)
        if field.Type == 3 and REF_BOOKMARK_PREFIX in field.Code.Text:
            return True
    return False


def process_body_citations(document, bookmark_map: dict[str, str]) -> int:
    started = False
    skip_summary = False
    converted = 0
    for paragraph in document.Paragraphs:
        text = norm(paragraph.Range.Text)
        if not text:
            continue
        if skip_summary:
            if is_heading_like(text) and not SUMMARY_PATTERN.search(text):
                skip_summary = False
            else:
                continue
        started, active = in_main_body(text, started)
        if not active:
            continue
        if SUMMARY_PATTERN.search(text):
            skip_summary = True
            continue
        if paragraph_has_ref_field(paragraph):
            continue
        converted += replace_citations_in_paragraph(document, paragraph, bookmark_map)
    return converted


def normalize_ref_field_format(document) -> None:
    for i in range(1, document.Fields.Count + 1):
        field = document.Fields.Item(i)
        code = field.Code.Text.strip()
        if field.Type == 3 and REF_BOOKMARK_PREFIX in code:
            font_size = resolve_range_font_size(field.Result)
            apply_ref_charformat(field, font_size)


def main() -> int:
    args = parse_args()
    source = Path(args.docx_path).expanduser().resolve()
    if not source.exists():
        raise FileNotFoundError(source)

    if args.save_as:
        output = Path(args.save_as).expanduser().resolve()
    elif args.in_place:
        output = source
    else:
        output = source.with_name(f"{source.stem}.crossref{source.suffix}")

    pythoncom.CoInitialize()
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    document = None
    try:
        document = word.Documents.Open(str(source))
        ref_map = collect_reference_paragraphs(document.Paragraphs)
        if not ref_map:
            raise RuntimeError("No reference entries found under the references section.")
        bookmark_map = ensure_bookmarks(document, ref_map)
        converted = process_body_citations(document, bookmark_map)
        document.Fields.Update()
        normalize_ref_field_format(document)
        if output == source:
            document.Save()
        else:
            document.SaveAs2(str(output))
        print(
            f"Created {len(bookmark_map)} reference bookmarks and converted {converted} body citations."
        )
        return 0
    finally:
        if document is not None:
            document.Close(SaveChanges=False)
        word.Quit()
        pythoncom.CoUninitialize()


if __name__ == "__main__":
    raise SystemExit(main())
