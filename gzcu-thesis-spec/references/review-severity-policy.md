# Review Severity Policy

Use this file when reviewing an existing thesis and you need a stable severity model that distinguishes true submission blockers from optional polish items.

This policy is aligned to the compliant submission-ready `.docx` baseline.

## 1. Severity model

Use these four buckets in review mode:

1. `Critical`
2. `Major`
3. `Minor`
4. `Enhancement`

The first three are compliance-oriented findings. `Enhancement` is for non-blocking improvements that may strengthen the final `.docx` but are not required to reach submission baseline.

## 2. Critical

Use `Critical` when the issue can directly block submission, defense readiness, or formal compliance.

Typical examples:

- missing mandatory chapter substance,
- missing `本章小结`,
- abstract, chapter summary, or conclusion contains citations,
- references are not cited in the body,
- citation order does not match bibliography order,
- odd-page chapter-start rule is violated,
- Roman/Arabic page-number logic is wrong,
- TOC is not Word-generated in the final manuscript,
- no concrete test cases or no result analysis,
- project facts are fabricated,
- final `.docx` still leaves body citations as plain-text numbers when clickable reference jumping is required.

## 3. Major

Use `Major` when the issue may not immediately block submission but materially weakens compliance, credibility, or final-manuscript quality.

Typical examples:

- body uses first person,
- chapter length likely fails the school's minimum after final layout,
- missing figure/table in-text references,
- testing or deployment content is too generic and not grounded in project evidence,
- Word section/header logic is likely wrong but not yet fully verified,
- journal `[J]` or monograph `[M]` entries lack page ranges,
- bibliography cross-references lose superscript formatting.

## 4. Minor

Use `Minor` for presentation, consistency, or style drift that should be fixed but does not usually define submission readiness by itself.

Typical examples:

- inconsistent heading spacing,
- caption placement drift,
- inconsistent English/numeric font,
- table continuation marks inconsistent,
- acknowledgement wording or formatting polish,
- terminology not consistent across chapters.

## 5. Enhancement

Use `Enhancement` for optional improvements beyond the compliant submission baseline.

Typical examples:

- figure references are not clickable but the user wants a more polished final `.docx`,
- table references are not clickable but the user wants clickable jumping,
- additional automation for asset assembly,
- extra template normalization that improves appearance without affecting compliance.

Do not label an issue `Critical`、`Major`、or `Minor` if the only problem is that the manuscript lacks an enhancement not proven mandatory by the compliant baseline.

## 6. Reporting rule

In review mode:

- list `Critical` findings first,
- then `Major`,
- then `Minor`,
- then `Enhancement`,
- keep `Enhancement` separate from blocking issues.

If there are no blocking findings, say so explicitly. Do not bury that conclusion under optional improvements.

## 7. Example distinction

Correct classification examples:

- body citation order wrong -> `Critical`
- TOC not refreshed after edits -> `Major` if likely wrong, manual check if not confirmed
- body `图4-1` is plain text but user did not ask for clickable figure jumps -> not a blocking finding; at most `Enhancement`
- body `[1]` remains plain text in final `.docx` -> `Critical`

## 8. Recommended review summary line

At the top of a review, summarize using one of these shapes:

- `当前版本不建议提交，存在 Critical 问题。`
- `当前版本基本合规，但仍有 Major 风险需要处理。`
- `当前版本接近提交状态，主要剩余 Minor 与 Enhancement 项。`
