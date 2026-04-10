# Script Usage

Use this file when the user wants to run the asset assembly and cross-reference scripts directly.

## 1. Assemble figures and screenshots

```bash
py scripts/assemble_thesis_assets.py templates/asset-manifest.template.json --save-as thesis.assets.docx
```

Use when you need to batch-insert:

- drawio figures,
- Playwright screenshots,
- white-background code screenshots.

Start from the built-in template if you do not already have a manifest:

- [templates/asset-manifest.template.json](../templates/asset-manifest.template.json)

## 2. Normalize image paragraph spacing

```bash
py scripts/normalize_figure_paragraphs.py thesis.assets.docx --save-as thesis.assets.normalized.docx
```

Use when you need to enforce:

- `1.5` line spacing for image paragraphs,
- zeroed paragraph spacing around the figure block.

This script only targets image blocks. It does not convert the whole document to `1.5` line spacing.

## 3. Build cross-reference citations

```bash
py scripts/build_reference_crossrefs.py thesis.assets.normalized.docx --save-as thesis.final.docx
```

Use when the document still has plain-text citations like `[1]` and you want Word cross-references that support `Ctrl + 点击` to the corresponding reference item.

## 4. Build figure-caption cross-references

```bash
py scripts/build_figure_crossrefs.py thesis.assets.normalized.docx --save-as thesis.fig-crossref.docx
```

Use when the document still has plain-text figure references such as `如图4-1所示` and you want `Ctrl + 点击` on `图4-1` to jump to the matching figure caption.

## 5. Build table-caption cross-references

```bash
py scripts/build_table_crossrefs.py thesis.assets.normalized.docx --save-as thesis.tbl-crossref.docx
```

Use when the document still has plain-text table references such as `如表4-1所示` or `见表4-2` and you want `Ctrl + 点击` on `表4-1` to jump to the matching table caption.

## 6. Recommended order

1. generate images with `$drawio` and `$playwright-cli`
2. assemble them into the thesis with `assemble_thesis_assets.py`
3. normalize picture-block spacing with `normalize_figure_paragraphs.py`
4. convert body figure references to caption cross-references with `build_figure_crossrefs.py`
5. convert body table references to caption cross-references with `build_table_crossrefs.py`
6. convert body citations to cross-references with `build_reference_crossrefs.py`
7. use `$doc` to do the final Word layout review

## 7. Safety notes

- Always keep a backup copy of the source `.docx`.
- Prefer `--save-as` during early iterations.
- Use `--in-place` only when the output has already been checked.
- Cross-reference generation assumes the references section starts at a paragraph exactly named `参考文献`.
- Figure cross-reference generation assumes figure captions start with `图X-X`.
- Table cross-reference generation assumes table captions start with `表X-X`, and正文 `表X-X中的...` 这类句子不会被当作表题。
- After figure or table cross-reference generation, re-check that bibliography cross-references are still superscript.
- After figure or table cross-reference generation, re-check that正文 `图X-X` / `表X-X` still use body text size rather than caption size.
- Figure and table cross-reference scripts only rebuild正文主文中的图表交叉引用，不清理主文之外已经存在的合法字段。
