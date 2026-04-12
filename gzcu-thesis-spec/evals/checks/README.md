# Eval Checks

Use these evals as a lightweight guardrail, not a heavyweight benchmark suite.

## Recommended Review Flow

1. Pick a case in `../cases/`.
2. Produce or inspect the candidate response, prompt output, or rule text.
3. Compare it against the matching file in `../expected/`, either manually or with `run_eval_check.py`.
4. Mark any missing baseline item as a regression.
5. If the task is about a real `.docx`, also run `gzcu-thesis-spec/scripts/check_docx_baseline.py`.

## Semi-Automated Check

Run from the repository root:

```bash
py gzcu-thesis-spec/evals/checks/run_eval_check.py toc-request --response-file answer.txt
```

Run all cases against one response file:

```bash
py gzcu-thesis-spec/evals/checks/run_eval_check.py --all --response-file answer.txt
```

Or pipe text in through stdin:

```bash
Get-Content answer.txt | py gzcu-thesis-spec/evals/checks/run_eval_check.py bibliography-crossref
```

Use `--json` when you want machine-readable output:

```bash
py gzcu-thesis-spec/evals/checks/run_eval_check.py header-footer-review --response-file answer.txt --json
```

Run the repository self-check against the main skill-facing documents:

```bash
py gzcu-thesis-spec/evals/checks/run_eval_check.py --all --repo-self-check
```

This scans:

- `README.md`
- `gzcu-thesis-spec/SKILL.md`
- `使用指南.md`

## What The Script Does

- resolves the matching `cases/<case>.md` and `expected/<case>.checklist.md`
- evaluates the candidate text against lightweight keyword rules for the chosen case
- can batch all cases with `--all`
- can run built-in repository document checks with `--repo-self-check`
- reports `PASS` / `FAIL` plus missing checkpoints

This is intentionally a shallow regression guard. It helps catch obvious drift quickly, but it does not replace manual review.

## Evaluation Boundaries

- `gzcu-thesis-spec/evals/` checks skill wording, default behavior, and compliance framing.
- `check_docx_baseline.py` checks actual `.docx` structure.
- figure/table clickable jumps should only be required when the task explicitly asks for them.

## Minimal Regression Rule

Treat the following as immediate regressions:

- output falls back to the old software-thesis chapter skeleton
- output omits Chapter 2 `相关技术与理论基础`
- output describes conclusion / references / acknowledgements as requiring separate dedicated header rules
- output treats clickable figure/table jumps as mandatory baseline submission requirements
- output omits body-to-reference clickable bibliography jumping from the baseline final-docx target
