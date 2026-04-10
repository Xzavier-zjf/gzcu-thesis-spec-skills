#!/usr/bin/env python3
import argparse
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.shared import Pt


HEADING_STYLES = {'Heading 1', 'Heading 2', 'Heading 3', '标题 1', '标题 2', '标题 3'}


def is_picture_paragraph(paragraph) -> bool:
    return bool(paragraph._p.xpath('.//w:drawing'))


def is_heading_like(paragraph) -> bool:
    style_name = getattr(getattr(paragraph, 'style', None), 'name', '') or ''
    return style_name in HEADING_STYLES


def is_empty(paragraph) -> bool:
    return not paragraph.text.strip()


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

    neighbor_indexes = []
    if idx - 1 >= 0 and not is_empty(paragraphs[idx - 1]) and not is_heading_like(paragraphs[idx - 1]):
        neighbor_indexes.append(idx - 1)
    if idx + 1 < len(paragraphs) and not is_empty(paragraphs[idx + 1]) and not is_heading_like(paragraphs[idx + 1]):
        neighbor_indexes.append(idx + 1)
    if idx + 2 < len(paragraphs) and not is_empty(paragraphs[idx + 2]) and not is_heading_like(paragraphs[idx + 2]):
        neighbor_indexes.append(idx + 2)

    for i in neighbor_indexes:
        zero_spacing(paragraphs[i])


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
