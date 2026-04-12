# Submission Template Baseline

Use this file when the task must align to the compliant submission-ready `.docx` instead of only relying on generic school-rule summaries.

This file captures the most important template facts observed from the compliant final manuscript and should be treated as the highest-priority local baseline unless the user provides a newer mandatory template from the school.

## 1. Baseline principle

- This baseline comes from a real submission-ready GZCU thesis `.docx`.
- When generic wording in other docs is looser than this baseline, prefer this baseline.
- When the compliant `.docx` shows a stable implementation mechanism, preserve the mechanism rather than copying incidental paragraph-level manual formatting.

## 2. Observed document structure

The compliant manuscript follows this order:

1. cover page
2. explanation page
3. Chinese abstract
4. English abstract
5. TOC
6. Chapter 1 through Chapter 6
7. conclusion
8. references
9. acknowledgements

Preferred software-engineering chapter structure:

1. 第一章 绪论
2. 第二章 相关技术与理论基础
3. 第三章 系统需求分析
4. 第四章 系统总体设计
5. 第五章 系统详细设计与实现
6. 第六章 系统测试与部署

## 3. Observed Word section model

The compliant manuscript is compatible with this 4-section implementation:

1. cover + explanation page
2. Chinese abstract + English abstract
3. TOC
4. main body through acknowledgements

Interpretation:

- Section 1 has no visible headers or page numbers.
- Section 2 uses Roman page numbers starting from `I`.
- Section 3 belongs to the Roman-numbering part but hides page numbers.
- Section 4 starts Arabic numbering from Chapter 1 and continues through conclusion, references, and acknowledgements.

Do not split `结论`、`参考文献`、`致谢` into separate numbering sections by default unless the user explicitly wants a different structure.

## 4. Observed header behavior

- Even-page header is fixed as `广州城市理工学院本科毕业设计（论文）`.
- Odd-page header follows the current level-1 heading by `STYLEREF`.
- Conclusion, references, and acknowledgements continue this same odd/even header mechanism.
- Hidden-header sections may still contain empty header definitions in XML; the important requirement is that no visible header appears on abstract or TOC pages.

## 5. Observed page-number behavior

- Chinese and English abstracts use uppercase Roman numerals.
- TOC hides visible page numbers.
- Chapter 1 starts Arabic page number `1`.
- Conclusion, references, and acknowledgements continue Arabic numbering and do not restart.

## 6. Observed heading and body behavior

- Level-1 headings are centered and act as the source for odd-page `STYLEREF` headers.
- Body text uses `20 磅` fixed line spacing and first-line indentation.
- Chinese body text is `宋体`; English and numeric text use `Times New Roman`.
- Every body chapter ends with `本章小结`.

## 7. Observed citation baseline

- The compliant manuscript contains body-to-reference Word field references.
- Reference entries are bookmarkable as `gzcu_ref_n`.
- Body citations are rebuilt only in the main body.
- Abstract, chapter summaries, and conclusion remain non-citation zones.

Therefore, clickable body-to-reference jumping should be treated as the baseline target state for final `.docx` delivery.

## 8. Observed figure/table baseline

- Figures and tables are cited in the body and numbered by chapter.
- Figure captions are below the figure.
- Table captions are above the table.
- A table style compatible with no left/right outer vertical borders is acceptable.

The compliant manuscript does not provide enough evidence to prove that clickable figure/table jumping is mandatory for submission. Treat it as an optional enhancement unless the user explicitly asks for it.

## 9. What this baseline should influence

Use this baseline to decide:

- default chapter organization,
- review severity,
- Word implementation plans,
- which missing items are true compliance problems,
- which items are only optional final-docx enhancements.
