#!/usr/bin/env python
"""Convert body table references like 表4-1 into clickable Word cross-references."""

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
TABLE_CAPTION_HEAD_RE = re.compile(r"^(表(\d+)-(\d+))")
TABLE_REF_RE = re.compile(r"表(\d+)-(\d+)")
REF_BOOKMARK_PREFIX = "gzcu_ref_"
TABLE_BOOKMARK_PREFIX = "gzcu_tbl_"
CONTROL_PREFIX_RE = re.compile(r"^[\x00-\x1f]+")
BODY_TEXT_SIZE = 12.0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build clickable Word cross-references for body table references."
    )
    parser.add_argument("docx_path", help="Source docx path")
    parser.add_argument("--save-as", dest="save_as", help="Output docx path")
    parser.add_argument("--in-place", action="store_true", help="Overwrite source docx")
    return parser.parse_args()


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def strip_control_prefix(text: str) -> str:
    return CONTROL_PREFIX_RE.sub("", text or "")


def is_heading_like(text: str) -> bool:
    return any(p.search(text) for p in HEADING_LIKE_PATTERNS)


def apply_body_crossref_format(result_range) -> None:
    result_range.Font.Size = BODY_TEXT_SIZE
    result_range.Font.Superscript = False
    for i in range(1, result_range.Characters.Count + 1):
        char = result_range.Characters(i)
        char.Font.Size = BODY_TEXT_SIZE
        char.Font.Superscript = False


def apply_body_charformat(field, bookmark: str) -> None:
    field.Code.Characters(1).Font.Size = BODY_TEXT_SIZE
    field.Code.Characters(1).Font.Superscript = False
    field.Update()
    apply_body_crossref_format(field.Result)


def in_main_body(text: str, started: bool) -> tuple[bool, bool]:
    if not started and any(p.search(text) for p in BODY_START_PATTERNS):
        return True, True
    if started and any(p.search(text) for p in BODY_END_PATTERNS):
        return False, False
    return started, started


def collect_body_paragraph_starts(document) -> set[int]:
    started = False
    skip_summary = False
    starts: set[int] = set()
    for paragraph in document.Paragraphs:
        text = norm(paragraph.Range.Text)
        if not text:
            continue
        if is_table_caption_text(text):
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
        starts.add(paragraph.Range.Start)
    return starts


def is_table_caption_text(text: str) -> bool:
    text = strip_control_prefix(text)
    match = TABLE_CAPTION_HEAD_RE.match(text)
    if not match:
        return False
    rest = text[len(match.group(1)) :]
    if not rest:
        return False
    if rest.startswith("中的"):
        return False
    if rest[0] in {" ", "\u3000", "\t", "（", "("}:
        return True
    return bool(re.match(r"^[A-Za-z0-9\u4e00-\u9fff]", rest))


def base_table_no(text: str) -> str | None:
    text = strip_control_prefix(text)
    match = TABLE_CAPTION_HEAD_RE.match(text)
    return match.group(1) if match else None


def collect_table_captions(paragraphs) -> dict[str, object]:
    table_map: dict[str, object] = {}
    for p in paragraphs:
        text = norm(p.Range.Text)
        if not is_table_caption_text(text):
            continue
        table_no = base_table_no(text)
        if table_no and table_no not in table_map:
            table_map[table_no] = p
    return table_map


def ensure_bookmarks(document, table_map: dict[str, object]) -> dict[str, str]:
    bookmark_map: dict[str, str] = {}
    for table_no, paragraph in table_map.items():
        safe_name = table_no.replace("表", "").replace("-", "_")
        bookmark_name = f"{TABLE_BOOKMARK_PREFIX}{safe_name}"
        rng = paragraph.Range.Duplicate
        start = rng.Start
        end = min(rng.End, start + len(table_no))
        bookmark_range = document.Range(Start=start, End=end)
        if document.Bookmarks.Exists(bookmark_name):
            document.Bookmarks(bookmark_name).Delete()
        document.Bookmarks.Add(bookmark_name, bookmark_range)
        bookmark_map[table_no] = bookmark_name
    return bookmark_map


def replace_table_refs_in_paragraph(document, paragraph, bookmark_map: dict[str, str]) -> int:
    text = paragraph.Range.Text
    matches = list(TABLE_REF_RE.finditer(text))
    if not matches:
        return 0

    inserted = 0
    for match in reversed(matches):
        table_no = match.group(0)
        bookmark = bookmark_map.get(table_no)
        if not bookmark:
            continue
        rng = paragraph.Range.Duplicate
        rng.Start = paragraph.Range.Start + match.start()
        rng.End = paragraph.Range.Start + match.end()
        if rng.Fields.Count > 0:
            continue
        rng.Text = ""
        document.Fields.Add(
            rng,
            Type=3,
            Text=f"{bookmark} \\h \\* CHARFORMAT",
            PreserveFormatting=False,
        )
        field = document.Fields(document.Fields.Count)
        field.Update()
        apply_body_charformat(field, bookmark)
        inserted += 1
    return inserted


def process_body_table_refs(document, bookmark_map: dict[str, str]) -> int:
    started = False
    skip_summary = False
    converted = 0
    for paragraph in document.Paragraphs:
        text = norm(paragraph.Range.Text)
        if not text:
            continue
        if is_table_caption_text(text):
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
        converted += replace_table_refs_in_paragraph(document, paragraph, bookmark_map)
    return converted


def normalize_crossref_field_format(document) -> None:
    for i in range(1, document.Fields.Count + 1):
        field = document.Fields.Item(i)
        code = field.Code.Text.strip()
        if field.Type != 3:
            continue
        if REF_BOOKMARK_PREFIX in code:
            field.Result.Font.Superscript = True
        elif TABLE_BOOKMARK_PREFIX in code:
            apply_body_charformat(field, code.split()[1])


def unlink_existing_table_crossrefs(document, body_paragraph_starts: set[int]) -> None:
    for i in range(document.Fields.Count, 0, -1):
        field = document.Fields.Item(i)
        code = field.Code.Text.strip()
        if field.Type != 3 or TABLE_BOOKMARK_PREFIX not in code:
            continue
        if field.Result.Paragraphs.Count < 1:
            continue
        paragraph_start = field.Result.Paragraphs(1).Range.Start
        if paragraph_start in body_paragraph_starts:
            field.Unlink()


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
        output = source.with_name(f"{source.stem}.table-crossref{source.suffix}")

    pythoncom.CoInitialize()
    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    document = None
    try:
        document = word.Documents.Open(str(source))
        body_paragraph_starts = collect_body_paragraph_starts(document)
        unlink_existing_table_crossrefs(document, body_paragraph_starts)
        table_map = collect_table_captions(document.Paragraphs)
        if not table_map:
            raise RuntimeError("No table captions found that start with 表X-X.")
        bookmark_map = ensure_bookmarks(document, table_map)
        converted = process_body_table_refs(document, bookmark_map)
        normalize_crossref_field_format(document)
        if output == source:
            document.Save()
        else:
            document.SaveAs2(str(output))
        print(
            f"Created {len(bookmark_map)} table bookmarks and converted {converted} body table references."
        )
        return 0
    finally:
        if document is not None:
            document.Close(SaveChanges=False)
        word.Quit()
        pythoncom.CoUninitialize()


if __name__ == "__main__":
    raise SystemExit(main())
