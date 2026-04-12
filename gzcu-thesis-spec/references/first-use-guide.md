# First Use Guide

Use this file when the user is using `$gzcu-thesis-spec` for the first time and needs a practical quick start.

## 1. What this skill is for

`$gzcu-thesis-spec` is a Guangzhou City University of Technology undergraduate thesis rule skill. It is designed to help with three kinds of tasks:

- write thesis content against school rules,
- review an existing thesis for compliance risks,
- prepare or inspect Word finalization details such as headers, page numbers, references, TOC, and odd-page chapter starts.

It is not a generic “write me a thesis” shortcut. It works best when the user provides real project evidence.

## 2. First-use rule

Before asking it to write a full thesis, collect project evidence first. If the materials are incomplete, use `project-evidence-intake.md` before any chapter-generation request.

Recommended first-use order:

1. collect project materials,
2. ask for a compliance matrix,
3. ask for one chapter or one artifact at a time,
4. review the result,
5. only then assemble the full manuscript using the compliant 6-chapter structure by default,
6. finish with Word finalization and a compliance review.

## 3. Fast start

### Option A: collect materials first

```text
使用 $gzcu-thesis-spec，先不要写论文。请根据广州城市理工学院本科毕业论文要求，给我一份真实项目材料采集清单，并标出高优先级缺失项。
```

### Option B: build the rule matrix first

```text
使用 $gzcu-thesis-spec，根据学校规则和我的项目材料，先建立论文写作的 compliance matrix 和 evidence map，再告诉我哪些章节可以先写，哪些章节因为材料不足暂时不建议写。
```

### Option C: review an existing draft first

```text
使用 $gzcu-thesis-spec，先不要重写内容。请按广州城市理工学院规范检查我这份论文草稿，输出 Findings、Rule coverage、Manual checks、Open risks。
```

## 4. Recommended calling examples

### 4.1 Generate Chinese and English abstracts

```text
使用 $gzcu-thesis-spec，根据以下项目材料生成中文摘要、英文摘要和中英文关键词。中文摘要控制在 400-600 字，不引用文献；英文摘要必须准确翻译中文摘要。
```

### 4.2 Generate Chapter 1

```text
使用 $gzcu-thesis-spec，根据以下项目材料撰写第一章绪论，包含选题背景与研究意义、国内外研究现状、本文研究内容与目标、论文结构、本章小结。本章小结不能引用文献。
```

### 4.3 Generate requirements analysis

```text
使用 $gzcu-thesis-spec，根据以下项目材料撰写第三章系统需求分析，要求紧贴真实业务流程、角色和功能边界，不要写成教材式套话。
```

### 4.4 Generate related technology chapter

```text
使用 $gzcu-thesis-spec，根据以下项目材料撰写第二章相关技术与理论基础，只保留与项目真实实现直接相关的技术基础，并以本章小结收束。
```

### 4.5 Generate testing and deployment chapter

```text
使用 $gzcu-thesis-spec，根据以下真实测试记录和部署材料撰写第六章系统测试与部署，必须包含测试环境、功能测试、性能测试、测试结果分析、部署过程与运行支撑，不得虚构测试数据或部署事实。
```

### 4.6 Check citations and references

```text
使用 $gzcu-thesis-spec，检查这篇论文的正文引用与参考文献是否符合学校要求，重点检查禁引区域、引用顺序、未引用文献、正文引用是否已做成可点击参考文献交叉引用、以及 [J]/[M] 页码范围缺失问题。
```

### 4.7 Prepare Word finalization guidance

```text
使用 $gzcu-thesis-spec 和 $doc，给我这篇论文的 Word 终稿处理方案，重点覆盖四段分节、页眉页码、目录、奇数页起章、正文引用交叉引用，以及结论/参考文献/致谢连续编号规则。
```

### 4.8 Run a final compliance review

```text
使用 $gzcu-thesis-spec，按广州城市理工学院本科毕业设计（论文）规范，对这篇论文做一次提交前审查，并按标准报告模板输出。
```

## 5. What to provide with each request

For best results, include as many of these as possible:

- thesis topic,
- project repository path or source files,
- module list,
- screenshots,
- database schema,
- API descriptions,
- test logs,
- deployment scripts or configs,
- current thesis draft or `.docx` path,
- reference list.

## 6. Common mistakes to avoid

Do not ask the skill to:

- invent project modules or test results,
- write the full thesis from a one-line project description,
- ignore the school formatting rules until the end,
- write abstract, chapter summaries, or conclusion with literature citations,
- keep using an older generic chapter skeleton when the compliant submission template already provides a valid 6-chapter structure,
- treat Word pagination and odd-page chapter starts as optional.

## 7. Best practice

Use the skill iteratively:

- first for evidence collection,
- then for chapter drafting,
- then for review,
- finally for Word finalization.

This produces better results than asking for a full thesis in one shot.
