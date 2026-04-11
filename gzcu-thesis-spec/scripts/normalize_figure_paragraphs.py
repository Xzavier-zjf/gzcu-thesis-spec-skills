#!/usr/bin/env python3
import argparse
import re
from pathlib import Path

from docx import Document
from docx.shared import Pt


HEADING_STYLES = {'Heading 1', 'Heading 2', 'Heading 3', '标题 1', '标题 2', '标题 3'}
FIGURE_CAPTION_RE = re.compile(r'^(图\d+-\d+)')
TABLE_CAPTION_RE = re.compile(r'^表\d+-\d+')


def is_picture_paragraph(paragraph) -> bool:
    return bool(paragraph._p.xpath('.//w:drawing'))


def is_heading_like(paragraph) -> bool:
    style_name = getattr(getattr(paragraph, 'style', None), 'name', '') or ''
    return style_name in HEADING_STYLES


def is_empty(paragraph) -> bool:
    return not paragraph.text.strip()


def norm(text: str) -> str:
    return ' '.join((text or '').split())


def is_figure_caption(paragraph) -> bool:
    return bool(FIGURE_CAPTION_RE.match(norm(paragraph.text)))


def is_table_caption(paragraph) -> bool:
    return bool(TABLE_CAPTION_RE.match(norm(paragraph.text)))


def is_media_boundary(paragraph) -> bool:
    return (
        is_empty(paragraph)
        or is_heading_like(paragraph)
        or is_picture_paragraph(paragraph)
        or is_table_caption(paragraph)
    )


def is_intro_paragraph(paragraph, figure_no: str) -> bool:
    text = norm(paragraph.text)
    if not text or is_heading_like(paragraph) or is_picture_paragraph(paragraph) or is_table_caption(paragraph):
        return False
    if figure_no and re.search(re.escape(figure_no) + r'(?!\d)', text):
        return True
    return bool(re.search(r'如图\d+-\d+所示', text))


def zero_spacing(paragraph) -> None:
    fmt = paragraph.paragraph_format
    fmt.space_before = Pt(0)
    fmt.space_after = Pt(0)


def normalize_block(paragraphs, idx: int) -> None:
    pic = paragraphs[idx]
    fmt = pic.paragraph_format
    fmt.line_spacing = 1.5
    fmt.space_before = Pt(0)
    fmt.space_after = Pt(0)
    next_idx = idx + 1
    if next_idx >= len(paragraphs):
        return

    caption_paragraph = paragraphs[next_idx]
    if is_media_boundary(caption_paragraph) or not is_figure_caption(caption_paragraph):
        return

    zero_spacing(caption_paragraph)
    figure_no = None
    match = FIGURE_CAPTION_RE.match(norm(caption_paragraph.text))
    if match:
        figure_no = match.group(0)

    if figure_no and idx - 1 >= 0:
        prev = paragraphs[idx - 1]
        if is_intro_paragraph(prev, figure_no):
            zero_spacing(prev)

    analysis_idx = next_idx + 1
    if analysis_idx >= len(paragraphs):
        return

    analysis_paragraph = paragraphs[analysis_idx]
    if is_media_boundary(analysis_paragraph) or is_figure_caption(analysis_paragraph):
        return

    zero_spacing(analysis_paragraph)


def main() -> None:
    parser = argparse.ArgumentParser(description='Normalize figure paragraphs to 1.5 line spacing and harmonize nearby paragraph spacing.')
    parser.add_argument('docx_path', help='Path to the docx file')
    parser.add_argument('--save-as', help='Output docx path')
    parser.add_argument('--in-place', action='store_true', help='Overwrite source docx')
    args = parser.parse_args()

    docx_path = Path(args.docx_path).expanduser().resolve()
    if not docx_path.exists():
        raise SystemExit(f'DOCX not found: {docx_path}')

    doc = Document(str(docx_path))
    paragraphs = list(doc.paragraphs)
    for idx, paragraph in enumerate(paragraphs):
        if is_picture_paragraph(paragraph):
            normalize_block(paragraphs, idx)

    if args.save_as:
        output_path = Path(args.save_as).expanduser().resolve()
    elif args.in_place:
        output_path = docx_path
    else:
        output_path = docx_path.with_name(docx_path.stem + '.normalized.docx')
    doc.save(str(output_path))
    print(f'Wrote {output_path}')


if __name__ == '__main__':
    main()
