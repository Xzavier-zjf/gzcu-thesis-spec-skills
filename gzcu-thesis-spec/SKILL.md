---
name: gzcu-thesis-spec
description: School-specific thesis writing, formatting, and compliance workflow for Guangzhou City University of Technology undergraduate graduation theses. Use when Codex must write sections, review an existing draft, fix citation order, check chapter structure, or produce Word-ready guidance against the Guangzhou City University of Technology rules, especially for requests such as "根据学校要求写论文", "按广州城市理工学院格式写毕业论文", "检查论文是否符合学校规范", "调整页眉页码/参考文献/摘要格式", or "按学校模板做终稿".
---

# GZCU Thesis Spec

Use this skill to apply Guangzhou City University of Technology undergraduate thesis rules as hard constraints, not soft style suggestions.

For `.docx` editing, section breaks, headers, footers, page numbering, TOC refresh, figure/table placement, and final Word inspection, also use [$doc](/Users/zjf20/.codex/skills/doc/SKILL.md).
For thesis diagrams such as architecture figures, ER diagrams, flowcharts, and research workflow figures, also use [$drawio](/Users/zjf20/.codex/skills/drawio/SKILL.md).
For browser-based evidence collection such as page screenshots, UI flow verification, and visible runtime proof from the real system, also use [$playwright-cli](/Users/zjf20/.codex/skills/playwright-cli/SKILL.md).
For batch asset insertion, figure-paragraph spacing normalization, and clickable reference, figure-caption, or table-caption cross-references inside Word, use this skill's local `scripts/` helpers together with `$doc`.

This skill is school-specific. Keep general thesis generation behavior in [`thesis-content-formatter`], but let this skill override it whenever the school rules are stricter or more explicit.

## Quick Loading Guide

Read only what the task needs:

- Load [references/content-and-structure.md](references/content-and-structure.md) when writing or revising chapter content, abstracts, conclusion, acknowledgements, reference usage, chapter summaries, or section completeness.
- Load [references/layout-and-word-rules.md](references/layout-and-word-rules.md) when the task involves Word layout, headers, footers, page numbers, section breaks, odd-page chapter starts, figure/table layout, fonts, spacing, or final manuscript formatting.
- Load [references/compliance-checklist.md](references/compliance-checklist.md) when reviewing an existing thesis, preparing a final delivery checklist, or reporting unresolved risks and manual follow-ups.
- Load [references/output-blueprint.md](references/output-blueprint.md) when the user wants a stable output template for abstracts, TOC, chapter drafts, review reports, or final delivery packages.
- Load [references/prompt-library.md](references/prompt-library.md) when the user wants ready-to-paste prompts such as abstract generation, citation checking, format review, or Word finalization requests.
- Load [references/software-engineering-prompt-pack.md](references/software-engineering-prompt-pack.md) when the thesis is for a software engineering project and the user wants a Guangzhou City University of Technology oriented prompt pack by chapter or task.
- Load [references/project-evidence-intake.md](references/project-evidence-intake.md) when the user needs a structured checklist to collect real project material before asking AI to write the thesis.
- Load [references/review-report-template.md](references/review-report-template.md) when the user wants a repeatable standard report format for thesis compliance reviews across multiple versions.
- Load [references/first-use-guide.md](references/first-use-guide.md) when the user is using this skill for the first time and needs a quick-start guide plus recommended calling examples.
- Load [references/example-call-card.md](references/example-call-card.md) when the user wants a one-page quick reference with the 5 most common calling patterns.
- Load [references/skill-integration.md](references/skill-integration.md) when the thesis task needs diagrams, browser screenshots, runtime evidence, or final Word document production using `$drawio`, `$playwright-cli`, and `$doc` together.
- Load [references/thesis-production-pipeline.md](references/thesis-production-pipeline.md) when the user wants a fixed end-to-end workflow from project evidence intake to final Word submission.
- Load [references/asset-assembly-schema.md](references/asset-assembly-schema.md) when the task needs a manifest for bulk insertion of Draw.io figures, UI screenshots, or code screenshots into a `.docx`.
- Load [references/asset-manifest-field-guide.md](references/asset-manifest-field-guide.md) when the user needs a field-by-field guide for filling the asset manifest template correctly and avoiding common insertion failures.
- Load [references/script-usage.md](references/script-usage.md) when the task needs concrete script commands for asset assembly, figure-paragraph spacing normalization, or Word reference cross-reference construction.

## Default Workflow

### 1. Build the compliance matrix first

Extract the school rules that apply to the current task before writing anything. Track at least:

- required sections and forbidden sections,
- length and chapter-page constraints,
- citation and bibliography constraints,
- Word layout constraints,
- figure/table/code-display constraints,
- manual-review items that AI cannot fully guarantee.

Treat the cover page and the second explanation page as locked template pages. Do not propose edits there. Apply the school formatting rules starting from the Chinese abstract page.

### 2. Ground the thesis in project evidence

Before drafting, collect evidence from the real project:

- system goal and scenario,
- actual modules and business flow,
- real tech stack and deployment path,
- real database, APIs, tests, screenshots, and diagrams,
- real constraints, defects, and future work.

Do not invent modules, metrics, tests, or deployment facts to satisfy the chapter structure.

When the thesis needs evidence from a running UI or browser workflow, use `$playwright-cli` to capture screenshots, verify flows, and collect observable runtime proof instead of describing the interface from memory.

When the thesis needs architecture diagrams, ER diagrams, flowcharts, or paper figures, use `$drawio` instead of ad hoc ASCII diagrams or low-quality screenshots.

When the final deliverable is a `.docx`, use `$doc` for layout-sensitive editing and visual verification.

### 3. Choose the task mode

Pick one mode and stay consistent:

- Constraint mode: output the rule matrix and task applicability first.
- Chapter generation mode: write a requested chapter or section against the matrix.
- Review mode: inspect an existing thesis and list violations first, ordered by severity.
- Word implementation mode: give concrete Word-oriented instructions for section breaks, headers, page numbers, TOC, figures, tables, references, figure-caption cross-references, table-caption cross-references, and odd-page chapter starts.
- Asset assembly mode: assemble Draw.io figures, Playwright screenshots, and white-background code screenshots into the thesis via `scripts/assemble_thesis_assets.py`, then normalize figure-block spacing via `scripts/normalize_figure_paragraphs.py`.
- Cross-reference mode: convert plain-text body citations into Word cross-references via `scripts/build_reference_crossrefs.py`, convert body figure references into caption cross-references via `scripts/build_figure_crossrefs.py`, and convert body table references into caption cross-references via `scripts/build_table_crossrefs.py`, so `Ctrl + 点击` jumps to the matching bibliography item, figure caption, or table caption.

### 4. Enforce the hard bans

Never do these unless the user explicitly overrides the school rules:

- cite references in the abstract, chapter summaries, or conclusion,
- use first-person narrative outside acknowledgements,
- write colloquial body text,
- paste long raw code blocks into the body,
- omit chapter summaries,
- ignore odd-page chapter starts and required blank transition pages,
- ignore Word section separation for headers and page numbers,
- let figure/table numbering exist without in-text references,
- leave figure references as plain text when the final Word manuscript should support clickable figure-caption cross-references,
- leave table references as plain text when the final Word manuscript should support clickable table-caption cross-references,
- leave inserted figure blocks without normalized picture-paragraph spacing,
- keep plain-text reference numbers in the body when the user explicitly wants clickable Word cross-references,
- let bibliography cross-references lose their superscript formatting after figure or table cross-reference processing,
- leave journal `[J]` or monograph `[M]` references without page ranges,
- rewrite the cover page or school statement page.

### 5. End every delivery with a compliance audit

Before finishing, report:

- what rules were satisfied,
- what risks remain,
- what must still be checked manually in Word,
- what placeholders still need real project evidence.

## Output Rules

Prefer this order when responding:

1. assumptions,
2. compliance-focused output,
3. placeholders or manual replacements,
4. final checklist.

When reviewing an existing thesis, report findings first and tie each finding to a school rule instead of a generic style preference.
