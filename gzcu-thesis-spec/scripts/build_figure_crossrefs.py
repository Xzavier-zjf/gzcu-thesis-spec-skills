#!/usr/bin/env python
"""Convert body figure references like 图3-1 into clickable Word cross-references."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

try:
    import pythoncom
    import win32com.client
except ModuleNotFoundError as exc:
    pythoncom = None
    win32com = None
    PYWIN32_IMPORT_ERROR = exc
else:
    PYWIN32_IMPORT_ERROR = None


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
FIGURE_CAPTION_RE = re.compile(r"^(图(\d+)-(\d+))")
FIGURE_REF_RE = re.compile(r"图(\d+)-(\d+)")
REF_BOOKMARK_PREFIX = "gzcu_ref_"
FIG_BOOKMARK_PREFIX = "gzcu_fig_"
CONTROL_PREFIX_RE = re.compile(r"^[\x00-\x1f]+")
DEFAULT_BODY_TEXT_SIZE = 12.0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build clickable Word cross-references for body figure references."
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


def resolve_range_font_size(rng) -> float:
    size = getattr(rng.Font, "Size", 0) or 0
    if size:
        return float(size)
    if rng.Characters.Count > 0:
        size = getattr(rng.Characters(1).Font, "Size", 0) or 0
        if size:
            return float(size)
    if getattr(rng, "Paragraphs", None) and rng.Paragraphs.Count > 0:
        paragraph_range = rng.Paragraphs(1).Range
        size = getattr(paragraph_range.Font, "Size", 0) or 0
        if size:
            return float(size)
        if paragraph_range.Characters.Count > 0:
            size = getattr(paragraph_range.Characters(1).Font, "Size", 0) or 0
            if size:
                return float(size)
    return DEFAULT_BODY_TEXT_SIZE


def apply_body_crossref_format(result_range, font_size: float) -> None:
    result_range.Font.Size = font_size
    result_range.Font.Superscript = False
    for i in range(1, result_range.Characters.Count + 1):
        char = result_range.Characters(i)
        char.Font.Size = font_size
        char.Font.Superscript = False


def apply_body_charformat(field, font_size: float) -> None:
    field.Code.Characters(1).Font.Size = font_size
    field.Code.Characters(1).Font.Superscript = False
    field.Update()
    apply_body_crossref_format(field.Result, font_size)


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
        if FIGURE_CAPTION_RE.match(norm(strip_control_prefix(text))):
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


def collect_figure_captions(paragraphs) -> dict[str, object]:
    fig_map: dict[str, object] = {}
    for p in paragraphs:
        text = norm(strip_control_prefix(p.Range.Text))
        match = FIGURE_CAPTION_RE.match(text)
        if match:
            fig_map[match.group(1)] = p
    return fig_map


def ensure_bookmarks(document, figure_map: dict[str, object]) -> dict[str, str]:
    bookmark_map: dict[str, str] = {}
    for figure_no, paragraph in figure_map.items():
        safe_name = figure_no.replace("图", "").replace("-", "_")
        bookmark_name = f"{FIG_BOOKMARK_PREFIX}{safe_name}"
        rng = paragraph.Range.Duplicate
        start = rng.Start
        end = min(rng.End, start + len(figure_no))
        bookmark_range = document.Range(Start=start, End=end)
        if document.Bookmarks.Exists(bookmark_name):
            document.Bookmarks(bookmark_name).Delete()
        document.Bookmarks.Add(bookmark_name, bookmark_range)
        bookmark_map[figure_no] = bookmark_name
    return bookmark_map


def replace_figure_refs_in_paragraph(document, paragraph, bookmark_map: dict[str, str]) -> int:
    text = paragraph.Range.Text
    matches = list(FIGURE_REF_RE.finditer(text))
    if not matches:
        return 0

    inserted = 0
    for match in reversed(matches):
        figure_no = match.group(0)
        bookmark = bookmark_map.get(figure_no)
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
        field.Update()
        apply_body_charformat(field, font_size)
        inserted += 1
    return inserted


def process_body_figure_refs(document, bookmark_map: dict[str, str]) -> int:
    started = False
    skip_summary = False
    converted = 0
    for paragraph in document.Paragraphs:
        text = norm(paragraph.Range.Text)
        if not text:
            continue
        if FIGURE_CAPTION_RE.match(norm(strip_control_prefix(text))):
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
        converted += replace_figure_refs_in_paragraph(document, paragraph, bookmark_map)
    return converted


def normalize_crossref_field_format(document) -> None:
    for i in range(1, document.Fields.Count + 1):
        field = document.Fields.Item(i)
        code = field.Code.Text.strip()
        if field.Type != 3:
            continue
        if REF_BOOKMARK_PREFIX in code:
            field.Result.Font.Superscript = True
        elif FIG_BOOKMARK_PREFIX in code:
            font_size = resolve_range_font_size(field.Result)
            apply_body_charformat(field, font_size)


def unlink_existing_figure_crossrefs(document, body_paragraph_starts: set[int]) -> None:
    for i in range(document.Fields.Count, 0, -1):
        field = document.Fields.Item(i)
        code = field.Code.Text.strip()
        if field.Type != 3 or FIG_BOOKMARK_PREFIX not in code:
            continue
        if field.Result.Paragraphs.Count < 1:
            continue
        paragraph_start = field.Result.Paragraphs(1).Range.Start
        if paragraph_start in body_paragraph_starts:
            field.Unlink()


def ensure_word_automation_ready() -> None:
    if PYWIN32_IMPORT_ERROR is not None:
        raise SystemExit(
            "pywin32 is required for Word cross-reference scripts. "
            "Install it with: py -m pip install pywin32"
        )


def main() -> int:
    args = parse_args()
    source = Path(args.docx_path).expanduser().resolve()
    if not source.exists():
        raise SystemExit(f'DOCX not found: {source}')

    if args.save_as:
        output = Path(args.save_as).expanduser().resolve()
    elif args.in_place:
        output = source
    else:
        output = source.with_name(f"{source.stem}.figure-crossref{source.suffix}")

    ensure_word_automation_ready()
    word = None
    document = None
    coinitialized = False
    try:
        pythoncom.CoInitialize()
        coinitialized = True
        try:
            word = win32com.client.DispatchEx("Word.Application")
        except Exception as exc:
            raise SystemExit(
                "Microsoft Word must be installed on Windows to use this script."
            ) from exc
        word.Visible = False
        document = word.Documents.Open(str(source))
        body_paragraph_starts = collect_body_paragraph_starts(document)
        unlink_existing_figure_crossrefs(document, body_paragraph_starts)
        figure_map = collect_figure_captions(document.Paragraphs)
        if not figure_map:
            raise RuntimeError("No figure captions found that start with 图X-X.")
        bookmark_map = ensure_bookmarks(document, figure_map)
        converted = process_body_figure_refs(document, bookmark_map)
        normalize_crossref_field_format(document)
        if output == source:
            document.Save()
        else:
            document.SaveAs2(str(output))
        print(
            f"Created {len(bookmark_map)} figure bookmarks and converted {converted} body figure references."
        )
        return 0
    finally:
        if document is not None:
            document.Close(SaveChanges=False)
        if word is not None:
            word.Quit()
        if coinitialized:
            pythoncom.CoUninitialize()


if __name__ == "__main__":
    raise SystemExit(main())
