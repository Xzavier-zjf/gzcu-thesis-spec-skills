# Thesis Production Pipeline

Use this file when the user wants a fixed production workflow that turns a real software project into a school-compliant thesis.

## 1. Purpose

This pipeline standardizes the thesis workflow into seven fixed stages:

1. collect project evidence,
2. produce formal figures,
3. capture runtime screenshots,
4. assemble assets into the manuscript,
5. draft thesis chapters,
6. run compliance review,
7. finalize the Word document.

Use this pipeline to avoid the common failure mode of “write first, patch evidence and formatting later”.

## 2. One-page pipeline overview

```text
阶段 1：采集材料
-> 阶段 2：出图
-> 阶段 3：截图取证
-> 阶段 4：资产装配
-> 阶段 5：写章节
-> 阶段 6：审查
-> 阶段 7：Word 终稿
```

## 3. Fixed workflow by stage

### Stage 1. 采集材料

Primary skill:
- `$gzcu-thesis-spec`

Supporting reference:
- `project-evidence-intake.md`

Goal:
- collect all real project evidence before writing.

Required outputs:
- project evidence intake sheet,
- compliance matrix,
- evidence map by chapter,
- missing-evidence list.

Recommended call:

```text
使用 $gzcu-thesis-spec，先不要写论文。请根据广州城市理工学院本科毕业论文要求，给我一份真实项目材料采集清单，并建立论文写作的 compliance matrix 和 evidence map。
```

Exit criteria:
- chapter-to-evidence mapping is clear,
- high-risk missing items are known,
- no chapter needs to rely on fabricated facts.

### Stage 2. 出图

Primary skill:
- `$drawio`

Orchestration skill:
- `$gzcu-thesis-spec`

Goal:
- create formal thesis figures for system explanation.

Typical figure types:
- system architecture diagram,
- ER diagram,
- business flowchart,
- use-case or sequence diagram,
- deployment topology.

Required outputs:
- formal figure assets,
- figure purpose notes,
- planned insertion chapter and caption.

Recommended call:

```text
使用 $gzcu-thesis-spec，判断我的论文需要哪些正式图示；对需要的架构图、ER 图、流程图，使用 $drawio 生成适合论文插入的正式图，并说明这些图分别放在哪一章、正文应如何引用“如图X-X所示”。
```

Exit criteria:
- each figure has a clear chapter destination,
- each figure has a narrative purpose,
- figures are not replaced by low-quality screenshots.

### Stage 3. 截图取证

Primary skill:
- `$playwright-cli`

Orchestration skill:
- `$gzcu-thesis-spec`

Goal:
- capture visible runtime proof from the real system.

Typical screenshot targets:
- login page,
- dashboard,
- word list/detail pages,
- review/quiz flow,
- assistant page,
- admin pages,
- deployment or runtime verification pages.

Required outputs:
- page screenshots,
- screenshot meaning notes,
- chapter placement notes.

Recommended call:

```text
使用 $gzcu-thesis-spec，结合 $playwright-cli，为这篇论文补齐真实运行证据。请列出应截图的关键页面、每张截图要证明什么，以及这些截图分别应插入哪一章。
```

Exit criteria:
- screenshots cover key user flows,
- screenshots are real runtime evidence,
- screenshots are mapped to specific thesis sections.

### Stage 4. 资产装配

Primary skill:
- `$gzcu-thesis-spec`

Supporting skills and references:
- `$doc`
- `asset-assembly-schema.md`
- `script-usage.md`

Goal:
- batch-insert formal figures, runtime screenshots, and code screenshots into the `.docx` before final writing and review drift accumulates.

Required outputs:
- asset manifest,
- thesis with inserted figure blocks,
- normalized picture-paragraph spacing,
- updated chapter placement map for inserted assets.

Recommended call:

```text
使用 $gzcu-thesis-spec 和 $doc，根据既有的图示与截图清单执行论文资产装配。请生成装配清单，批量插入 drawio 图片、页面截图和白底代码截图，统一图片所在段落为 1.5 倍行距，并检查图题是否位于图下方。
```

Exit criteria:
- each planned asset is inserted at the correct chapter anchor,
- each figure block remains contiguous and readable,
- picture paragraphs use `1.5` line spacing,
- captions remain below figures.

### Stage 5. 写章节

Primary skill:
- `$gzcu-thesis-spec`

Supporting references:
- `output-blueprint.md`
- `software-engineering-prompt-pack.md`
- `prompt-library.md`

Goal:
- draft each chapter against the school rules and the real project evidence.

Recommended order:
1. Chinese and English abstracts
2. Chapter 1 Introduction
3. Requirements analysis
4. Overall design
5. Detailed design and implementation
6. Testing
7. Deployment and operation verification
8. Conclusion
9. References
10. Acknowledgements

Recommended call:

```text
使用 $gzcu-thesis-spec，根据已经整理好的项目材料、图示和截图，按学校规范分章节写论文。先从“[章节名称]”开始，内容必须基于真实项目证据，不得虚构，并明确图表引用位置。
```

Exit criteria:
- each chapter is evidence-backed,
- each chapter ends with `本章小结` when required,
- abstract, chapter summaries, and conclusion contain no citations,
- body citations remain traceable.

### Stage 6. 审查

Primary skill:
- `$gzcu-thesis-spec`

Supporting references:
- `review-report-template.md`
- `compliance-checklist.md`

Goal:
- detect content, citation, structure, and formatting risks before Word finalization.

Review scopes:
- citation-only review,
- chapter review,
- full compliance review,
- pre-submission review.

Recommended call:

```text
使用 $gzcu-thesis-spec，按广州城市理工学院本科毕业设计（论文）规范，对当前论文版本输出标准审查报告，包含 Findings、Rule coverage、Version delta、Manual checks、Open risks。
```

Exit criteria:
- critical issues are identified,
- unresolved risks are explicit,
- version delta is clear across iterations.

### Stage 7. Word 终稿

Primary skill:
- `$doc`

Orchestration skill:
- `$gzcu-thesis-spec`

Goal:
- turn the reviewed manuscript into a school-compliant Word final version.

Required tasks:
- section breaks,
- Roman/Arabic page-number separation,
- TOC generation or refresh,
- odd-page chapter starts,
- headers/footers,
- figure/table insertion,
- figure-reference cross-reference build or refresh,
- table-reference cross-reference build or refresh,
- figure-block spacing normalization,
- clickable reference cross-reference build or refresh,
- references and acknowledgements formatting,
- final visual review.

Recommended call:

```text
使用 $gzcu-thesis-spec 和 $doc，对论文 docx 做终稿处理。请从摘要页开始执行学校格式规则，检查分节符、页眉页码、目录、奇数页起章、图表插入、图片段落 1.5 倍行距，并调用 `build_figure_crossrefs.py`、`build_table_crossrefs.py` 与 `build_reference_crossrefs.py` 生成图片图注交叉引用、表格图注交叉引用和参考文献交叉引用，最后检查致谢格式并列出仍需人工复核的项目。
```

Exit criteria:
- Word layout matches school rules,
- page numbering is correct,
- headers are correct,
- TOC is current,
- odd-page chapter starts are satisfied,
- body figure references are clickable cross-references when required,
- body table references are clickable cross-references when required,
- body citations are clickable Word cross-references when required,
- bibliography cross-references still display as superscript,
- final manual checks are clearly listed.

## 4. Stage handoff rules

Do not move to the next stage until the current one meets its exit criteria.

Handoffs should look like this:

- Stage 1 -> Stage 2:
  - evidence map
  - list of needed diagrams
- Stage 2 -> Stage 3:
  - chapter figure plan
  - list of UI views that still need runtime proof
- Stage 3 -> Stage 4:
  - screenshot set with meanings
  - chapter placement map
- Stage 4 -> Stage 5:
  - asset manifest
  - thesis with inserted figure blocks
- Stage 5 -> Stage 6:
  - current manuscript draft
  - current references list
- Stage 6 -> Stage 7:
  - reviewed manuscript
  - issue list already resolved
  - final manual risks list

## 5. Fixed deliverables by stage

- Stage 1 deliverable: evidence intake package
- Stage 2 deliverable: formal diagram package
- Stage 3 deliverable: runtime screenshot package
- Stage 4 deliverable: asset-ready manuscript package
- Stage 5 deliverable: chapter drafts or full manuscript draft
- Stage 6 deliverable: standard review report
- Stage 7 deliverable: Word-ready final manuscript and manual-check list

## 6. Pipeline checklist

```text
论文生产流水线检查表
- 是否已完成项目材料采集与证据映射
- 是否已列出需要 Draw.io 生成的正式图
- 是否已获取关键页面与关键流程的真实截图
- 是否已完成论文资产装配与图片段落间距规范化
- 是否已按章节顺序完成草稿写作
- 是否已做过一次引用与参考文献专项检查
- 是否已检查图片图注是否为可点击交叉引用
- 是否已检查表格图注是否为可点击交叉引用
- 是否已做过一次全文合规审查
- 是否已进入 Word 终稿处理
- 是否已完成页眉页码、目录、奇数页起章和交叉引用检查
- 是否已列出最终人工复核项
```

## 7. Best practice

Use the pipeline iteratively, not as a one-shot prompt.

The safest order is:

- collect,
- evidence-build,
- write,
- review,
- format,
- final check.

This is slower than one-shot generation, but it is much more robust for a real undergraduate thesis submission.
