# Example Call Card

Use this file when the user wants a one-page quick reference for the most common `$gzcu-thesis-spec` calls.

## GZCU Thesis Spec 示例调用总览卡

### 1. 先收集项目材料

```text
使用 $gzcu-thesis-spec，先不要写论文。请根据广州城市理工学院本科毕业论文要求和提交版模板，给我一份真实项目材料采集清单，并标出高优先级缺失项。
```

### 2. 生成摘要

```text
使用 $gzcu-thesis-spec，根据以下项目材料生成中文摘要、英文摘要和中英文关键词。中文摘要控制在 400-600 字，不引用文献；英文摘要必须准确翻译中文摘要。
```

### 3. 生成章节草稿

```text
使用 $gzcu-thesis-spec，根据以下项目材料撰写“[章节名称]”草稿，要求严格遵守广州城市理工学院本科毕业设计（论文）规范，内容必须基于真实项目材料，不得虚构。
```

### 4. 检查引用与参考文献

```text
使用 $gzcu-thesis-spec，检查这篇论文的正文引用与参考文献是否符合学校要求，重点检查禁引区域、引用顺序、未引用文献、正文引用是否可点击跳转到参考文献、以及 [J]/[M] 页码范围缺失问题。
```

### 5. 做 Word 终稿处理

```text
使用 $gzcu-thesis-spec 和 $doc，给我这篇论文的 Word 终稿处理方案，重点覆盖四段分节、页眉页码、目录、奇数页起章、正文引用交叉引用、以及结论/参考文献/致谢连续编号规则。
```

### 6. 做模板基线审查

```text
使用 $gzcu-thesis-spec，按提交版模板基线审查这篇论文，并把 Findings 分成 Critical、Major、Minor、Enhancement 四类。
```

### 7. 检查 docx 页眉页码

```text
使用 $gzcu-thesis-spec 和 $doc，检查这个 docx 是否符合四段分节、页眉页码、目录和奇数页起章要求，并按 Critical、Major、Minor、Enhancement 输出。
```

### 8. 处理正文引用跳转

```text
使用 $gzcu-thesis-spec 和 $doc，检查这个 docx 的正文引用是否已经支持点击跳转到参考文献；如果没有，请给我交叉引用处理方案。
```

## 使用顺序建议

1. 先用调用 1 收集材料
2. 再用调用 2 或 3 生成内容
3. 完成后用调用 4 检查引用与参考文献
4. 最后用调用 5 做 Word 终稿处理
5. 如需提交前判断，再用调用 6 做一次基线审查
6. 遇到真实 docx 时，优先用调用 7 和 8 做版式与引用检查

## 一句话原则

先收集真实项目证据，再写；先审查内容与引用，再做 Word 终稿。
