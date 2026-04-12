# Content and Structure Rules

Use this file when drafting or revising thesis content.

This file is aligned to a real compliant GZCU submission draft. Treat the submission-ready chapter organization as the preferred default unless the user's school or supervisor gives a newer mandatory structure.

## 1. Scope and baseline

- Apply all thesis formatting and content rules starting from the Chinese abstract page.
- Do not modify the cover page or the second school explanation page.
- Keep the whole manuscript in formal written language.
- Do not use first-person narrative in the body. Only acknowledgements may use first person.
- Keep prose as the primary carrier. Figures, tables, and code screenshots only support the prose.

## 2. Length and chapter completeness

- Main text must be at least `1.5万字`.
- Each chapter should satisfy the school's `每章不少于3页` expectation after final Word layout.
- The thesis must cover at least: background analysis, related technology or theoretical basis, requirements analysis, overall design, detailed design and implementation, system testing with concrete test cases and result analysis, and deployment or operation support.
- Testing and deployment may be written as two separate chapters or combined into one chapter when the combined structure is closer to the compliant submission template.
- Every body chapter, including Chapter 1, must end with `本章小结`.
- `本章小结` only summarizes the chapter. Do not introduce new content there.

## 3. Preferred chapter structure

Use or verify a structure compatible with the compliant submission template:

1. Chinese abstract
2. English abstract
3. TOC
4. 第一章 绪论
5. 第二章 相关技术与理论基础
6. 第三章 系统需求分析
7. 第四章 系统总体设计
8. 第五章 系统详细设计与实现
9. 第六章 系统测试与部署
10. 结论
11. 参考文献
12. 致谢

Do not rigidly force an older generic skeleton such as "需求分析 directly after 绪论" if the submission-ready template already proves a different structure is compliant.

## 4. Chapter substance requirements

### 第一章 绪论

- Usually contains `1.1 选题背景与研究意义`、`1.2 国内外研究现状`、`1.3 本文研究内容与目标`、`1.4 论文结构`、`1.5 本章小结`.
- `论文结构` must match the real final chapter arrangement, not a generic placeholder outline.

### 第二章 相关技术与理论基础

- This chapter is part of the preferred software-engineering thesis structure and should not be omitted by default.
- It should explain the real technical or theoretical basis actually used by the project, not textbook padding unrelated to the implementation.

### 第三章 系统需求分析

- Cover real user roles, business goals, functional requirements, non-functional requirements, and key workflows.

### 第四章 系统总体设计

- Cover architecture, module division, database design, interface design, and supporting design decisions.

### 第五章 系统详细设计与实现

- Focus on core modules, key business flows, key algorithms, and implementation logic.
- Explain implementation in prose. Do not paste long raw code blocks.

### 第六章 系统测试与部署

- This chapter may combine testing and deployment when that matches the compliant template.
- It should still cover testing environment, test strategy, concrete test cases, result analysis, deployment process, and runtime support evidence as applicable.

## 5. Abstract, conclusion, acknowledgements

### Chinese abstract

- Keep the Chinese abstract within `400-600` words/characters according to the school requirement.
- Use `3-5` keywords.
- Do not include background padding or literature citations.
- Keep it focused on the project goal, method, implementation, and effect.

### English abstract

- Make it an accurate translation of the Chinese abstract.
- Translate the keywords accurately.
- Do not introduce extra claims or omit the Chinese abstract's key points.
- Do not add literature citations.

### Conclusion

- Start on a new page and on an odd-numbered page in final Word layout.
- Do not include literature citations.
- Do not write learning experience or personal feelings.
- Summarize completed work, actual results, limitations, and future improvements.

### Acknowledgements

- Start on a new page and on an odd-numbered page in final Word layout.
- Keep the tone sincere and factual.
- The supervisor's full name must appear.

## 6. Citation and bibliography rules

- The body must cite the references list. Do not leave uncited references at the end.
- Cite other people's achievements, methods, viewpoints, data, or technical sources, not common knowledge.
- Citation numbering must start at `[1]` and follow the order of first appearance in the body.
- The reference list order must match the in-text citation order exactly.
- Put citations in superscript form at the end of the relevant sentence or clause.
- Never cite references in the abstract, any `本章小结`, or the conclusion.
- Include at least `12` references.
- Include at least `2` English references.
- Prefer `80%+` references from the most recent 5 years or `2022` and later when possible.
- Ensure journal `[J]` and monograph `[M]` entries include page ranges.
- For final `.docx` delivery, treat clickable body-to-reference cross-references as the default target state.

## 7. Originality and duplication risk

- Repetition above `30%` blocks defense.
- Repetition above `20%` blocks excellence awards.
- Avoid over-copying background and technology introduction text.
- Ground every major chapter in the real project instead of generic textbook prose.

## 8. Figures, tables, code, and diagrams in content

- Every figure and table must be cited in the body, for example `如图1-1所示` or `如表1-1所示`.
- Explain what each figure/table demonstrates. Do not leave figures or tables unexplained.
- In detailed design, explain code in prose. Do not paste long raw code blocks.
- If code must be shown, use white-background code screenshots.
- Flowcharts must use arrows.
- ER diagrams must not use arrows on relationship lines.
- Clickable figure/table cross-references are optional enhancements, not the minimum compliance baseline, unless the user explicitly asks for them in the final `.docx`.

## 9. Writing checklist before delivery

Confirm all of the following:

- the thesis uses formal language,
- the body avoids first person,
- every body chapter ends with `本章小结`,
- the abstract, chapter summaries, and conclusion contain no citations,
- the thesis includes concrete test cases and result analysis,
- deployment or operation support is covered either in an independent chapter or inside a combined `系统测试与部署` chapter,
- the references are all cited in the body and numbered in citation order,
- all figures and tables are cited and explained in prose,
- acknowledgements include the supervisor's full name.
