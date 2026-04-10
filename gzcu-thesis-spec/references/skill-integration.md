# Skill Integration

Use this file when the thesis workflow must coordinate `$drawio`, `$playwright-cli`, and `$doc` with `$gzcu-thesis-spec`.

## 1. Integration principle

`$gzcu-thesis-spec` is the rule and orchestration layer.

- `$gzcu-thesis-spec` decides what the thesis must contain and what the school requires.
- `$drawio` produces formal diagrams and thesis figures.
- `$playwright-cli` captures browser-visible evidence from the real system.
- `$doc` handles `.docx` editing, Word layout, page-number sections, headers/footers, TOC, and final visual review.
- `gzcu-thesis-spec/scripts/*` batch-assembles those assets into the `.docx`, normalizes picture-paragraph spacing, and upgrades plain-text citations into clickable Word cross-references.

Do not use these skills interchangeably. Use each one for the artifact it is best suited to produce.

## 2. When to use each skill

### `$drawio`

Use `$drawio` for:

- system architecture diagrams,
- ER diagrams,
- business flowcharts,
- use-case support diagrams,
- sequence diagrams,
- deployment topology diagrams,
- paper-quality figures for the thesis body.

Prefer `$drawio` over screenshots when the figure is meant to explain structure or logic.

### `$playwright-cli`

Use `$playwright-cli` for:

- homepage screenshots,
- user workflow screenshots,
- admin-page screenshots,
- verifying that a feature actually runs in the browser,
- collecting visible evidence for testing and deployment chapters,
- checking page text, button labels, charts, and UI states before writing about them.

Prefer `$playwright-cli` over manually describing the UI from memory.

### `$doc`

Use `$doc` for:

- editing `.docx` files,
- fixing section breaks,
- fixing headers and page numbers,
- generating or checking the Word TOC,
- placing figures and tables into the thesis,
- checking whether the final layout is visually correct,
- validating references, conclusion, and acknowledgements layout.

Prefer `$doc` whenever layout fidelity matters.

### `gzcu-thesis-spec/scripts/*`

Use the local scripts for:

- batch insertion of Draw.io exports, UI screenshots, and code screenshots into a `.docx`,
- normalization of figure-block spacing after insertion,
- conversion of body figure references such as `如图4-1所示` into clickable figure-caption cross-references,
- conversion of body table references such as `如表4-1所示` into clickable table-caption cross-references,
- conversion of body citation text such as `[1]` into Word cross-reference fields,
- final refresh of clickable bibliography links before submission.

Prefer these scripts over manual repetitive editing when the thesis already has a stable insertion plan or reference list.

## 3. Recommended combined workflow

### A. Write thesis content from a real project

1. Use `$gzcu-thesis-spec` to build the compliance matrix and evidence map.
2. Use `$playwright-cli` to capture the real UI screenshots and visible runtime proof.
3. Use `$drawio` to generate architecture, ER, and flow diagrams.
4. Use `$gzcu-thesis-spec` to draft chapters using those artifacts as evidence.
5. Use `$doc` to assemble or edit the `.docx` and apply school formatting.
6. Use `$gzcu-thesis-spec` again to run the final compliance review.

### B. Produce figures for the thesis

1. Identify which diagrams are explanatory and which are screenshots.
2. Use `$drawio` for explanatory figures.
3. Use `$playwright-cli` for runtime screenshots.
4. Insert both into the thesis via `$doc`.
5. Use `gzcu-thesis-spec/scripts/assemble_thesis_assets.py` and `gzcu-thesis-spec/scripts/normalize_figure_paragraphs.py` to batch-insert and normalize the figure blocks.
6. Use `$gzcu-thesis-spec` to confirm the body includes `如图X-X所示` references and explanatory text.

### C. Build the final Word manuscript

1. Use `$gzcu-thesis-spec` to list all Word rules that apply.
2. Use `$doc` to implement section breaks, headers, footers, page numbering, references, and TOC.
3. If figures are still missing, generate them with `$drawio` or `$playwright-cli` first.
4. Use `gzcu-thesis-spec/scripts/assemble_thesis_assets.py` and `gzcu-thesis-spec/scripts/normalize_figure_paragraphs.py` to place and normalize image assets.
5. Use `gzcu-thesis-spec/scripts/build_figure_crossrefs.py` to turn body figure references into clickable caption cross-references.
6. Use `gzcu-thesis-spec/scripts/build_table_crossrefs.py` to turn body table references into clickable caption cross-references.
7. Use `gzcu-thesis-spec/scripts/build_reference_crossrefs.py` to turn body citations into clickable Word cross-references and keep them superscript.
8. Re-render and inspect with `$doc`.
9. Use `$gzcu-thesis-spec` to audit the final version for school-rule compliance.

## 4. Artifact routing rules

Route artifacts like this:

- Architecture / ER / flow / sequence / topology figure -> `$drawio`
- Browser page screenshot / UI interaction proof -> `$playwright-cli`
- Final `.docx` editing and pagination -> `$doc`
- Bulk figure insertion / figure-paragraph spacing normalization / figure-caption, table-caption, and reference cross-reference build -> `gzcu-thesis-spec/scripts/*`
- Rule interpretation, citation logic, chapter writing, final compliance judgment -> `$gzcu-thesis-spec`

## 5. Output expectations by skill

### If using `$drawio`

Require:

- clear figure purpose,
- thesis-safe labels,
- chapter-consistent numbering plan,
- exportable assets that can be inserted into Word.

### If using `$playwright-cli`

Require:

- the page or route being captured,
- the user flow being demonstrated,
- the screenshot meaning in the thesis,
- any visible evidence that should be described in text.

### If using `$doc`

Require:

- exact `.docx` path,
- target chapter or section,
- layout objective,
- whether visual review or render checking is required.

## 6. Prompt patterns for combined use

### Combined evidence collection

```text
使用 $gzcu-thesis-spec，结合 $playwright-cli 和 $drawio，为这篇论文准备真实项目证据：
1. 用 $playwright-cli 收集系统关键页面截图和交互证据；
2. 用 $drawio 补齐系统架构图、流程图或 ER 图；
3. 最后按学校论文要求列出这些材料分别适合放在哪一章。
```

### Combined Word finalization

```text
使用 $gzcu-thesis-spec 和 $doc，对论文 docx 做终稿处理；若缺少图示，再结合 $drawio 生成正式图，若缺少页面运行截图，再结合 $playwright-cli 补齐证据。随后调用 gzcu-thesis-spec 的装配脚本批量插图、统一图片段落 1.5 倍行距，并把正文引用、`如图X-X所示` 这类图片引用和 `如表X-X所示` 这类表格引用改成可 Ctrl+点击跳转的交叉引用。最终按学校规则检查页眉页码、奇数页起章、目录、参考文献和图表引用。
```

### Combined chapter writing

```text
使用 $gzcu-thesis-spec 撰写“系统总体设计”章节。请先判断哪些证据需要来自 $drawio 生成的架构/ER 图，哪些需要来自 $playwright-cli 获取的系统截图，再据此组织正文和图表引用说明。
```

## 7. Hard constraints in combined workflows

- Do not use low-quality browser screenshots in place of diagrams that should be formal structured figures.
- Do not use diagrams in place of real runtime screenshots when the thesis needs visible evidence of system operation.
- Do not insert figures into the thesis without body references and explanatory prose.
- Do not leave inserted picture paragraphs with inconsistent spacing after batch insertion.
- Do not leave final body figure references as plain text when the required deliverable is a Word document with clickable figure-caption jumps.
- Do not leave final body table references as plain text when the required deliverable is a Word document with clickable table-caption jumps.
- Do not leave final body citations as plain text when the required deliverable is a Word document with clickable bibliography jumps.
- Do not let bibliography cross-references lose superscript formatting after figure or table cross-reference updates.
- Do not finalize the `.docx` without a `$doc`-style layout check when page-number and header rules matter.
- Do not describe UI pages, architecture, or test flows from memory when the actual system or repo can be inspected.

