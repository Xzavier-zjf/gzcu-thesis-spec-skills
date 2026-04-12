# Evals

This directory contains lightweight regression cases for `gzcu-thesis-spec-skills`.

Its purpose is not to grade generic thesis writing quality. It exists to catch drift away from the submission-ready GZCU baseline already reflected in this repository.

## What These Evals Check

- default software-engineering thesis structure stays aligned to the 6-chapter submission-compatible model
- Word layout guidance stays aligned to the 4-section implementation model
- header and page-number guidance still reflects Roman / Arabic switching and STYLEREF-based odd-page headers
- bibliography jumping remains a baseline final-docx requirement
- figure/table clickable jumps remain optional enhancements unless explicitly requested

## What These Evals Do Not Replace

- `gzcu-thesis-spec/scripts/check_docx_baseline.py`

That script checks real `.docx` structure and XML-level evidence.

This `evals/` directory checks the skill's stated behavior, output expectations, and review language so the documentation and prompts do not drift back to the old template assumptions.

## Directory Layout

- `cases/`: prompt-style requests and expected response scope
- `expected/`: concise checklist-style assertions for each case
- `checks/`: lightweight review instructions plus a small semi-automated checker

## Pass Criteria

A case passes when the output or document under review clearly hits all checklist items in the matching `expected/*.checklist.md` file without:

- reverting to the old chapter skeleton
- treating figure/table jumping as a baseline submission hard requirement
- omitting the 4-section Word model
- omitting clickable body-to-reference cross-references from the baseline final-docx target

For quick smoke checks, you can run:

```bash
py evals/checks/run_eval_check.py toc-request --response-file answer.txt
```

The checker is intentionally lightweight. It is designed to catch obvious regressions in wording and default behavior, not to replace expert review.

## Assets Policy

This repository intentionally does not add a generic top-level `assets/` directory at this stage.

Reasons:

- reusable asset schema guidance already exists in `references/asset-assembly-schema.md`
- the asset manifest template already exists in `gzcu-thesis-spec/templates/asset-manifest.template.json`
- no fixed image fixtures are currently required to verify the new submission baseline

If future regressions require fixed screenshots or figures for script testing, prefer `evals/fixtures/` over a broad catch-all `assets/` directory.
