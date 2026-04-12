# DOCX Review Playbook

Use this file when the user gives a real `.docx` path and wants a concrete review or finalization task against the compliant GZCU submission baseline.

This playbook is optimized for the three highest-frequency real-document tasks:

1. write a complete heading map / TOC plan by school template,
2. check whether a `.docx` meets header, footer, section, and page-number rules,
3. convert body citations into clickable Word cross-references to bibliography items.

For actual `.docx` inspection, also use `$doc` whenever layout-sensitive verification matters.

## 1. Usage rule

When the user provides a real `.docx`:

- first align to `submission-template-baseline.md`,
- then apply `review-severity-policy.md` if the task is a review,
- then use this playbook to choose the concrete review/finalization path.

Do not answer these tasks with generic thesis-writing advice when the user is clearly asking about the current document.

## 2. Task A: write a complete heading map by school template

Use when the user asks:

- `按学校模板写完整目录`
- `给我一个可以直接照着排的目录结构`
- `按提交版结构列出目录`

Recommended output shape:

```text
Assumptions
- [默认采用提交版兼容 6 章结构]

TOC heading map
摘  要
Abstract
目  录
第一章 绪论
1.1 ...
...
致  谢

Manual checks
- [最终目录仍需由 Word 自动生成并刷新]
```

Default heading map should prefer:

1. 第一章 绪论
2. 第二章 相关技术与理论基础
3. 第三章 系统需求分析
4. 第四章 系统总体设计
5. 第五章 系统详细设计与实现
6. 第六章 系统测试与部署

## 3. Task B: check headers, sections, and page numbers in a real `.docx`

Use when the user asks:

- `检查我的 docx 是否符合学校页眉页码要求`
- `看看这个 Word 分节是不是对的`
- `检查奇数页起章、目录、页码`

Review focus:

- cover + explanation page unchanged,
- 4-section Word model,
- Roman numerals on abstract pages,
- hidden page numbers on TOC,
- Arabic page numbers starting from Chapter 1,
- odd/even header behavior in the main-body section,
- odd-page chapter starts for chapters, conclusion, references, acknowledgements.

Recommended output shape:

```text
Findings
1. [问题标题]
优先级：Critical / Major / Minor / Enhancement
违反规则：
问题说明：
建议修改：

Rule coverage
- [已满足]
- [未满足]

Manual checks
- [仍需在 Word 中人工确认]

Open risks
- [如果现在提交仍有何风险]
```

Classification hints:

- wrong Roman/Arabic switching -> `Critical`
- chapter not starting on odd page -> `Critical`
- odd-page header not following level-1 title -> `Major`
- TOC not refreshed but structure likely correct -> usually `Major` or `Manual check`

## 4. Task C: make body citations clickable to references

Use when the user asks:

- `把正文引用做成可点击跳转参考文献`
- `把 [1][2] 变成 Word 交叉引用`
- `检查正文引用能不能跳到参考文献`

Default behavior:

- treat clickable body-to-reference jumping as baseline final-docx work,
- only rebuild citations in the main body,
- do not inject citation fields into abstract, `本章小结`, or conclusion,
- preserve superscript appearance after field generation.

Recommended output shape:

```text
Assumptions
- [参考文献节标题为“参考文献”]
- [最终目标是正文引用跳转到参考文献]

Processing plan
1. 检查参考文献区是否可建立 `gzcu_ref_n`
2. 只处理正文中的引用编号
3. 转为 Word 交叉引用
4. 复核上标显示和跳转行为

Manual checks
- [Ctrl + 点击跳转]
- [上标格式]
- [禁引区域未被误处理]
```

## 5. Recommended prompt snippets

### A. TOC structure

```text
使用 $gzcu-thesis-spec，根据提交版模板给我一份可直接用于排版的完整目录结构，默认采用 6 章结构，并说明哪些地方最终仍需由 Word 自动生成。
```

### B. Header/page-number review

```text
使用 $gzcu-thesis-spec 和 $doc，按提交版模板基线检查这个 docx 的四段分节、页眉页码、目录和奇数页起章，并按 Critical、Major、Minor、Enhancement 输出 Findings。
```

### C. Citation cross-reference processing

```text
使用 $gzcu-thesis-spec 和 $doc，检查这篇 docx 的正文引用是否已经支持点击跳转到参考文献；如果还没有，请给我正文引用交叉引用处理方案，并明确禁引区域不要处理。
```

## 6. What not to do

- Do not treat real `.docx` review as a generic chapter-writing task.
- Do not classify missing clickable figure/table jumping as a blocking issue unless the user explicitly asked for it.
- Do not confuse TOC planning text with an actual Word-generated TOC.
- Do not recommend editing the cover page or explanation page.
