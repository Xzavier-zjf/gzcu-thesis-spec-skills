---
name: gzcu-thesis-spec
description: School-specific thesis writing, formatting, and compliance workflow for Guangzhou City University of Technology undergraduate graduation theses. Use when Codex must explain school rules, draft thesis sections, review an existing draft, or provide Word-oriented formatting guidance aligned first to the school format document and secondarily to a submitted sample docx baseline.
---

# GZCU Thesis Spec

Use this skill to apply Guangzhou City University of Technology undergraduate thesis rules with the correct evidence order:

1. school format document first,
2. submitted sample `.docx` second.

This skill is for school-rule interpretation, thesis drafting constraints, compliance review, and Word-format guidance. It is not a thesis production pipeline.

## Load Only What You Need

- Load [references/content-and-structure.md](references/content-and-structure.md) when drafting or revising abstracts, chapter structures, chapter content, conclusion, references, or acknowledgements.
- Load [references/layout-and-word-rules.md](references/layout-and-word-rules.md) when the task involves Word layout, headers, footers, page numbers, chapter starts, fonts, spacing, figures, tables, or final manuscript formatting.
- Load [references/compliance-checklist.md](references/compliance-checklist.md) when reviewing an existing thesis or preparing a final compliance checklist.
- Load [references/submission-template-baseline.md](references/submission-template-baseline.md) only when a submitted sample `.docx` is relevant as a reference baseline.

## Default Workflow

### 1. Build the school-rule matrix first

Before writing or reviewing, identify:

- which requirements come directly from the school format document,
- which suggestions come only from the submitted sample `.docx`,
- which items still require manual Word confirmation.

Always present the task as:

1. school-rule matrix,
2. current thesis adaptation points,
3. requested chapter content or formatting advice.

### 2. Keep the evidence boundary explicit

- Treat the school `.doc` as the primary source of truth.
- Treat the submitted `.docx` as a reference baseline, not as an automatic hard rule.
- Do not turn one sample implementation detail into a universal school requirement unless the school document also supports it.

### 3. Choose one task mode

- Rule explanation mode: explain the school requirements and their applicability.
- Chapter drafting mode: draft a chapter against the rule matrix.
- Review mode: list compliance problems first, then manual review items.
- Word guidance mode: provide formatting guidance and distinguish hard rules from sample-based suggestions.

## Hard Output Rules

- Do not default to screenshot-evidence workflows.
- Do not default to Draw.io or browser-automation workflows.
- Do not default to asset assembly or Word automation enhancements.
- Do not default to clickable bibliography, figure, or table cross-references.
- Do not present the submitted sample `.docx` as higher priority than the school format document.

## Content Defaults

When the task is a software-engineering thesis and the user has not provided a newer mandatory structure, a 6-chapter structure may be suggested as a reference default. It must still be framed as a sample-compatible structure, not the only legal structure.

When the task is Word formatting, prioritize:

- abstract and keyword rules,
- heading hierarchy,
- body fonts and spacing,
- figure/table placement and numbering,
- references formatting,
- conclusion and acknowledgements formatting,
- chapter page-break and odd-page-start recommendations.

## Final Response Rules

Prefer this order:

1. school-rule matrix,
2. thesis adaptation points,
3. requested output,
4. manual checks.

When reviewing an existing thesis, report findings first and label whether each issue is:

- a school hard-rule issue,
- a sample-baseline suggestion,
- or a manual Word confirmation item.
