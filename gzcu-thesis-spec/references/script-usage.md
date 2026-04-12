# Script Usage

Use this file when the user wants to run the asset assembly and cross-reference scripts directly.

All commands below are written so they can be executed from the repository root. If you `cd gzcu-thesis-spec` first, remove the `gzcu-thesis-spec/` prefix from script and template paths.

## 1. Baseline vs enhancement

Treat the scripts in two groups:

- baseline inspection script:
  - `check_docx_baseline.py`
- baseline final-docx scripts:
  - `build_reference_crossrefs.py`
  - optionally `assemble_thesis_assets.py`
  - optionally `normalize_figure_paragraphs.py`
- enhancement scripts:
  - `build_figure_crossrefs.py`
  - `build_table_crossrefs.py`

The compliant submission template confirms clickable body-to-reference jumping as a baseline target. It does not prove that clickable figure/table jumping is mandatory for submission. Therefore, only run the figure/table cross-reference scripts when the user explicitly wants those jumps in the final `.docx`.

## 2. Check baseline compliance of a real DOCX

```bash
py gzcu-thesis-spec/scripts/check_docx_baseline.py /path/to/file.docx
```

Or against an unpacked DOCX directory:

```bash
py gzcu-thesis-spec/scripts/check_docx_baseline.py /path/to/unpacked_docx_dir
```

Use this script for a lightweight baseline check of:

- 4-section Word model,
- Roman / Arabic page-number switching,
- odd/even header mechanism in the main-body section,
- Word TOC fields,
- `gzcu_ref_n` bookmarks and body-to-reference fields,
- submission-compatible 6-chapter structure.

This is a fast structural check, not a full visual Word review.

## 3. Assemble figures and screenshots

```bash
py gzcu-thesis-spec/scripts/assemble_thesis_assets.py gzcu-thesis-spec/templates/asset-manifest.template.json --save-as thesis.assets.docx
```

Use when you need to batch-insert:

- drawio figures,
- Playwright screenshots,
- white-background code screenshots.

Start from the built-in template if you do not already have a manifest:

- [templates/asset-manifest.template.json](../templates/asset-manifest.template.json)

## 4. Normalize image paragraph spacing

```bash
py gzcu-thesis-spec/scripts/normalize_figure_paragraphs.py thesis.assets.docx --save-as thesis.assets.normalized.docx
```

Use when you need to enforce:

- `1.5` line spacing for image paragraphs,
- figure-block spacing compatible with the school template.

This script only targets image blocks. It does not convert the whole document to `1.5` line spacing.

## 5. Build reference cross-reference citations

```bash
py gzcu-thesis-spec/scripts/build_reference_crossrefs.py thesis.docx --save-as thesis.ref-crossref.docx
```

Use when the document still has plain-text citations like `[1]` and you want Word cross-references that support `Ctrl + 点击` to the corresponding reference item.

Baseline assumptions:

- the references section starts at a paragraph exactly named `参考文献`,
- reference items are converted into bookmarkable entries such as `gzcu_ref_1`, `gzcu_ref_2`, ...
- only body citations are rebuilt; abstract, chapter summaries, and conclusion stay untouched.

## 6. Build figure-caption cross-references

```bash
py gzcu-thesis-spec/scripts/build_figure_crossrefs.py thesis.assets.normalized.docx --save-as thesis.fig-crossref.docx
```

Use only when the user explicitly wants `Ctrl + 点击` on body figure references such as `如图4-1所示` to jump to the matching figure caption.

## 7. Build table-caption cross-references

```bash
py gzcu-thesis-spec/scripts/build_table_crossrefs.py thesis.fig-crossref.docx --save-as thesis.tbl-crossref.docx
```

Use only when the user explicitly wants `Ctrl + 点击` on body table references such as `如表4-1所示` or `见表4-2` to jump to the matching table caption.

## 8. Recommended order

### Baseline final-docx order

1. run `check_docx_baseline.py` to get a quick structural baseline report
2. generate images with `$drawio` and `$playwright-cli` when needed
3. assemble them into the thesis with `assemble_thesis_assets.py` when needed
4. normalize picture-block spacing with `normalize_figure_paragraphs.py` when needed
5. convert body citations to clickable bibliography cross-references with `build_reference_crossrefs.py`
6. use `$doc` to do the final Word layout review

### Optional enhancement order

If the user explicitly wants clickable figure/table jumping:

1. run the baseline flow first
2. convert body figure references with `build_figure_crossrefs.py`
3. convert body table references with `build_table_crossrefs.py`
4. re-check that bibliography cross-references are still superscript
5. re-check that正文 `图X-X` / `表X-X` still use body-text size rather than caption size

## 9. Safety notes

- Always keep a backup copy of the source `.docx`.
- Prefer `--save-as` during early iterations.
- Use `--in-place` only when the output has already been checked.
- `check_docx_baseline.py` is a structural checker; it does not replace manual Word rendering review.
- Cross-reference generation assumes the references section starts at a paragraph exactly named `参考文献`.
- Figure cross-reference generation assumes figure captions start with `图X-X`.
- Table cross-reference generation assumes table captions start with `表X-X`, and正文 `表X-X中的...` 这类句子不会被当作表题。
- After figure or table cross-reference generation, re-check that bibliography cross-references are still superscript.
- After figure or table cross-reference generation, re-check that正文 `图X-X` / `表X-X` still use body text size rather than caption size.
- Figure and table cross-reference scripts only rebuild正文主文中的图表交叉引用，不清理主文之外已经存在的合法字段。
