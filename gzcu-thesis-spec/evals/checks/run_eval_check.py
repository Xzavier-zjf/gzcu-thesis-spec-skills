#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[3]
SKILL_ROOT = Path(__file__).resolve().parents[2]
EVALS_DIR = SKILL_ROOT / "evals"
CASES_DIR = EVALS_DIR / "cases"
EXPECTED_DIR = EVALS_DIR / "expected"
REPO_SELF_CHECK_TARGETS = (
    REPO_ROOT / "README.md",
    SKILL_ROOT / "SKILL.md",
    REPO_ROOT / "使用指南.md",
)


@dataclass(frozen=True)
class Rule:
    checklist_text: str
    any_of: tuple[tuple[str, ...], ...]
    forbid: tuple[str, ...] = ()


CASE_RULES: dict[str, list[Rule]] = {
    "toc-request": [
        Rule(
            "output uses a 6-chapter software-engineering default structure",
            (("6-chapter", "6 章", "六章"),),
        ),
        Rule(
            "output includes `第二章 相关技术与理论基础`",
            (("第二章 相关技术与理论基础", "Chapter 2 Related Technology and Theoretical Basis"),),
        ),
        Rule(
            "output includes `第六章 系统测试与部署`",
            (("第六章 系统测试与部署", "Chapter 6 System Testing and Deployment"),),
        ),
        Rule(
            "output does not force a separate `系统部署与运行验证` body chapter",
            (("系统测试与部署", "System Testing and Deployment"),),
            forbid=("系统部署与运行验证", "System Deployment and Operation Verification"),
        ),
        Rule(
            "output places conclusion, references, and acknowledgements after the body chapters",
            (("结论", "Conclusion"), ("参考文献", "References"), ("致谢", "Acknowledgements", "Acknowledgments")),
        ),
    ],
    "header-footer-review": [
        Rule(
            "mentions the 4-section Word model",
            (("4-section", "4 段", "四段分节", "4-section Word model"),),
        ),
        Rule(
            "mentions Roman numerals for abstract pages",
            (("Roman", "Roman numerals", "Roman 页码"),),
        ),
        Rule(
            "mentions the TOC as a separate section with hidden page numbers",
            (("TOC", "目录"), ("hidden page numbers", "隐藏页码")),
        ),
        Rule(
            "mentions Arabic numbering starting from Chapter 1 page `1`",
            (("Arabic", "Arabic numbering", "Arabic 页码"), ("Chapter 1", "第一章"), ("page `1`", "页码 `1`", "页码 1")),
        ),
        Rule(
            "mentions fixed even-page header text",
            (("偶数页页眉", "even-page header"), ("广州城市理工学院本科毕业设计（论文）",)),
        ),
        Rule(
            "mentions odd-page header following current level-1 heading via STYLEREF",
            (("奇数页页眉", "odd-page header"), ("STYLEREF",), ("一级标题", "level-1 heading", "level 1 heading")),
        ),
        Rule(
            "does not require separate dedicated header sections for conclusion, references, or acknowledgements",
            (("STYLEREF",),),
            forbid=("结论单独页眉", "参考文献单独页眉", "致谢单独页眉"),
        ),
    ],
    "bibliography-crossref": [
        Rule(
            "treats clickable body-to-reference jumping as baseline final-docx behavior",
            (("baseline", "基线"), ("reference", "参考文献"), ("click", "点击", "跳转")),
        ),
        Rule(
            "points to `build_reference_crossrefs.py`",
            (("build_reference_crossrefs.py",),),
        ),
        Rule(
            "references `gzcu_ref_n` bookmark naming",
            (("gzcu_ref_n", "gzcu_ref_1"),),
        ),
        Rule(
            "keeps abstract outside the rebuild scope",
            (("abstract", "摘要"), ("outside", "不进入", "不处理")),
        ),
        Rule(
            "keeps chapter summaries outside the rebuild scope",
            (("chapter summaries", "本章小结"), ("outside", "不进入", "不处理")),
        ),
        Rule(
            "keeps conclusion outside the rebuild scope",
            (("conclusion", "结论"), ("outside", "不进入", "不处理")),
        ),
    ],
    "optional-figure-table-jumps": [
        Rule(
            "distinguishes baseline requirements from optional enhancements",
            (("baseline", "基线", "基础要求"), ("enhancement", "增强项", "可选")),
        ),
        Rule(
            "keeps figure/table numbering as hard requirement",
            (("figure", "图"), ("table", "表"), ("numbering", "编号"), ("hard requirement", "硬要求", "基础合规")),
        ),
        Rule(
            "keeps in-text figure/table references as hard requirement",
            (("正文", "in-text"), ("figure", "图"), ("table", "表"), ("references", "引用"), ("hard requirement", "硬要求", "基础合规")),
        ),
        Rule(
            "does not require clickable figure jumps by default",
            (("clickable figure", "图表点击跳转", "图点击跳转"), ("optional", "可选", "按需")),
        ),
        Rule(
            "does not require clickable table jumps by default",
            (("clickable table", "表点击跳转", "表格点击跳转"), ("optional", "可选", "按需")),
        ),
        Rule(
            "states or implies that bibliography jumping is the verified baseline behavior",
            (("bibliography", "参考文献"), ("baseline", "基线"), ("verified", "已验证", "证明")),
        ),
    ],
    "software-thesis-6chapter-default": [
        Rule(
            "uses the 6-chapter default structure",
            (("6-chapter", "6 章", "六章"),),
        ),
        Rule(
            "includes `第二章 相关技术与理论基础`",
            (("第二章 相关技术与理论基础", "Chapter 2 Related Technology and Theoretical Basis"),),
        ),
        Rule(
            "combines testing and deployment in the default final body chapter",
            (("系统测试与部署", "System Testing and Deployment"),),
        ),
        Rule(
            "requires `本章小结`",
            (("本章小结",),),
        ),
        Rule(
            "does not force deployment into a separate standalone body chapter",
            (("系统测试与部署",),),
            forbid=("系统部署与运行验证",),
        ),
    ],
}


def normalize(text: str) -> str:
    return " ".join(text.lower().replace("`", "").split())


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_checklist_lines(case_name: str) -> list[str]:
    checklist_path = EXPECTED_DIR / f"{case_name}.checklist.md"
    if not checklist_path.exists():
        raise FileNotFoundError(f"Missing checklist file: {checklist_path}")
    lines = []
    for line in load_text(checklist_path).splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            lines.append(stripped[2:])
    return lines


def evaluate_rule(text: str, rule: Rule) -> tuple[bool, list[str]]:
    lowered = normalize(text)
    missing_groups: list[str] = []
    for group in rule.any_of:
        if not any(normalize(needle) in lowered for needle in group):
            missing_groups.append(" / ".join(group))
    forbidden_hits = [needle for needle in rule.forbid if normalize(needle) in lowered]
    return not missing_groups and not forbidden_hits, missing_groups + [f"forbidden: {hit}" for hit in forbidden_hits]


def iter_targets(args: argparse.Namespace) -> Iterable[tuple[str, str]]:
    if args.response_file:
        yield args.response_file.name, load_text(args.response_file)
    else:
        yield "<stdin>", sys.stdin.read()


def validate_case_name(case_name: str) -> None:
    case_path = CASES_DIR / f"{case_name}.md"
    checklist_path = EXPECTED_DIR / f"{case_name}.checklist.md"
    if case_name not in CASE_RULES:
        raise KeyError(f"Unsupported case: {case_name}")
    if not case_path.exists():
        raise FileNotFoundError(f"Missing case file: {case_path}")
    if not checklist_path.exists():
        raise FileNotFoundError(f"Missing checklist file: {checklist_path}")


def resolve_case_names(args: argparse.Namespace) -> list[str]:
    if args.all:
        return sorted(CASE_RULES)
    if args.case:
        return [args.case]
    raise ValueError("You must provide either a case name or --all.")


def resolve_targets(args: argparse.Namespace) -> list[tuple[str, str]]:
    if args.repo_self_check:
        return [(str(path.relative_to(REPO_ROOT)), load_text(path)) for path in REPO_SELF_CHECK_TARGETS]
    return list(iter_targets(args))


def evaluate_case(case_name: str, text: str, source_name: str) -> tuple[dict[str, object], bool]:
    validate_case_name(case_name)
    checklist_lines = load_checklist_lines(case_name)
    rules = CASE_RULES[case_name]
    if len(checklist_lines) != len(rules):
        raise ValueError(
            f"Checklist line count mismatch for {case_name}: expected {len(rules)} rules, found {len(checklist_lines)} checklist items."
        )

    rule_results = []
    passed = True
    for checklist_text, rule in zip(checklist_lines, rules):
        ok, details = evaluate_rule(text, rule)
        if not ok:
            passed = False
        rule_results.append(
            {
                "checklist": checklist_text,
                "passed": ok,
                "details": details,
            }
        )
    return {
        "case": case_name,
        "source": source_name,
        "passed": passed,
        "checks": rule_results,
    }, passed


def print_plain_results(results: list[dict[str, object]]) -> None:
    for result in results:
        status = "PASS" if result["passed"] else "FAIL"
        print(f"[{status}] case={result['case']} source={result['source']}")
        for item in result["checks"]:
            mark = "OK" if item["passed"] else "MISS"
            print(f"  - {mark}: {item['checklist']}")
            for detail in item["details"]:
                print(f"      {detail}")


def build_summary(results: list[dict[str, object]]) -> dict[str, int]:
    total = len(results)
    passed = sum(1 for result in results if result["passed"])
    failed = total - passed
    return {
        "total": total,
        "passed": passed,
        "failed": failed,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Lightweight eval checker for gzcu-thesis-spec-skills.")
    parser.add_argument("case", nargs="?", choices=sorted(CASE_RULES))
    parser.add_argument("--all", action="store_true", help="Run all eval cases.")
    parser.add_argument("--response-file", type=Path, help="Path to the candidate response text file.")
    parser.add_argument(
        "--repo-self-check",
        action="store_true",
        help="Run the selected case or all cases against README.md, gzcu-thesis-spec/SKILL.md, and 使用指南.md.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of plain text.")
    args = parser.parse_args()

    if not args.all and not args.case:
        parser.error("the following arguments are required: case or --all")
    if args.response_file and args.repo_self_check:
        parser.error("--response-file cannot be used together with --repo-self-check")
    if args.all and not args.repo_self_check and not args.response_file:
        parser.error("--all requires either --response-file or --repo-self-check")

    exit_code = 0
    results = []
    case_names = resolve_case_names(args)
    targets = resolve_targets(args)
    for source_name, text in targets:
        for case_name in case_names:
            result, passed = evaluate_case(case_name, text, source_name)
            if not passed:
                exit_code = 1
            results.append(result)

    if args.json:
        payload: object
        if len(results) == 1:
            payload = results[0]
        else:
            payload = {
                "summary": build_summary(results),
                "results": results,
            }
        json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    else:
        print_plain_results(results)
        if len(results) > 1:
            summary = build_summary(results)
            print(
                f"[SUMMARY] total={summary['total']} passed={summary['passed']} failed={summary['failed']}"
            )
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
