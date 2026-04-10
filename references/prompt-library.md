# Prompt Library

Use this file when the user wants ready-to-paste prompts instead of workflow explanations.

## 1. Abstract generation prompt

```text
使用 $gzcu-thesis-spec，根据以下项目材料生成本科毕业论文的中文摘要、英文摘要和中英文关键词。

硬性要求：
1. 严格按广州城市理工学院本科毕业设计（论文）规范执行。
2. 中文摘要控制在 400-600 字，只写项目目标、方法、实现、结果与意义，不写背景铺垫，不引用文献。
3. 英文摘要必须是中文摘要的准确翻译，不新增事实，不引用文献。
4. 中英文关键词均为 3-5 个，中文关键词之间使用分号分隔，最后一个关键词后不加标点。
5. 输出内容必须便于直接粘贴到 Word。
6. 若项目材料不足，请先列出缺失信息，不要自行虚构。

项目材料：
[在此粘贴项目背景、功能、技术栈、测试结论、部署情况等]
```

## 2. Citation check prompt

```text
使用 $gzcu-thesis-spec，检查这篇论文正文中的参考文献引用是否符合广州城市理工学院要求。

检查目标：
1. 摘要、本章小结、结论中不得出现参考文献引用。
2. 正文中的引用必须对应文末参考文献。
3. 引用编号必须从 [1] 开始，并按正文首次出现顺序与文末参考文献顺序一致。
4. 引用应位于句末最后一个字的右上角位置。
5. 找出未引用的参考文献、乱序引用、禁引区域中的引用、以及疑似常识性滥引。

输出格式：
- Findings
- Rule coverage
- Manual checks
- Open risks

论文内容：
[在此粘贴论文正文和参考文献，或说明文档路径]
```

## 3. Chapter draft prompt

```text
使用 $gzcu-thesis-spec，根据以下项目材料撰写“[章节名称]”草稿。

硬性要求：
1. 严格遵守广州城市理工学院本科毕业设计（论文）结构与写作规范。
2. 正文使用正式书面语，不使用第一人称。
3. 内容必须基于真实项目材料，不得虚构模块、数据、测试结果或部署事实。
4. 需要引用文献时，只能在正文中引用，且编号顺序可追踪。
5. 如果这是本章最后一节，必须输出“本章小结”，且本章小结不能引入新内容、不能引用文献。
6. 输出标题必须明确，便于直接粘贴到 Word 并套用标题样式。

项目材料：
[在此粘贴模块说明、数据库、接口、测试记录、部署记录、图表说明等]
```

## 4. Full review prompt

```text
使用 $gzcu-thesis-spec，按广州城市理工学院本科毕业设计（论文）规范，对这篇论文做一次完整合规审查。

请重点检查：
1. 章节结构是否完整。
2. 每章是否有本章小结。
3. 摘要、结论、本章小结是否禁引。
4. 参考文献数量、英文文献数量、近年文献占比是否达标。
5. 引用顺序与参考文献顺序是否一致。
6. 图表、代码截图、测试章节、部署章节是否合规。
7. 页眉页码、分节符、奇数页起章、目录自动生成等 Word 终稿风险。

输出格式：
- Findings
- Rule coverage
- Manual checks
- Open risks

材料：
[在此粘贴论文文本，或说明 docx 路径]
```

## 5. Word finalization prompt

```text
使用 $gzcu-thesis-spec 和 $doc，给我生成这篇论文的 Word 终稿处理方案。

目标：
1. 从摘要页开始应用学校格式规则，封面和说明页保持原样。
2. 正确设置分节符、页眉、页脚、页码。
3. 中文摘要、英文摘要使用罗马数字页码；正文从第一章开始使用阿拉伯数字页码 1。
4. 目录不显示页码，且必须由 Word 自动生成三级目录。
5. 每一章、结论、参考文献、致谢都必须另起页，并从奇数页开始；必要时插入空白页。
6. 检查图表标题位置、表格无竖线、代码截图为白底。

输出格式：
- 假设
- Word 处理步骤
- 最终核查
- 人工复核项

文档路径或材料：
[在此粘贴 docx 路径或说明当前文档情况]
```

## 6. Reference normalization prompt

```text
使用 $gzcu-thesis-spec，检查并规范这篇论文的参考文献列表。

要求：
1. 至少 12 篇参考文献，至少 2 篇英文文献。
2. 参考文献顺序必须与正文首次引用顺序一致。
3. [J] 和 [M] 类型不能缺页码范围。
4. 优先保留 2022 年及以后的文献，若比例不足请指出风险。
5. 不新增虚假文献，不编造 DOI、页码或来源。

输出格式：
- Findings
- 建议后的顺序
- 缺失项
- 风险提示

论文材料：
[在此粘贴正文引用和参考文献区，或说明文档路径]
```

## 7. Prompt writing rule

When adapting these prompts:

- keep `$gzcu-thesis-spec` explicit,
- add `$doc` whenever `.docx` layout or finalization is in scope,
- keep the output format explicit,
- include a “do not fabricate” line whenever the prompt depends on project evidence.
