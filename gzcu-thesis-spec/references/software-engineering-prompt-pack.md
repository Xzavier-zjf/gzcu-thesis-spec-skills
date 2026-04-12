# Software Engineering Prompt Pack

Use this file when the thesis is for a software engineering undergraduate project and the user wants ready-made prompts by chapter or deliverable.

This prompt pack uses the compliant submission-ready 6-chapter structure as the default:

1. 绪论
2. 相关技术与理论基础
3. 系统需求分析
4. 系统总体设计
5. 系统详细设计与实现
6. 系统测试与部署

## 1. Project grounding prompt

```text
使用 $gzcu-thesis-spec，先不要直接写论文，先根据以下软件工程项目材料建立论文写作的 evidence map 和 compliance matrix。

任务：
1. 提取真实项目目标、用户角色、业务流程、技术栈、数据库、接口、测试、部署信息。
2. 对照广州城市理工学院本科毕业设计（论文）规范和提交版模板，列出必须写进论文的章节与证据来源。
3. 标记缺失信息和不能虚构的部分。
4. 输出后续各章应重点使用哪些项目材料。

输出格式：
- Assumptions
- Compliance matrix
- Evidence map
- Missing project evidence
```

## 2. Introduction prompt

```text
使用 $gzcu-thesis-spec，根据以下软件工程项目材料撰写“第一章 绪论”。

要求：
1. 包含 1.1 选题背景与研究意义、1.2 国内外研究现状、1.3 本文研究内容与目标、1.4 论文结构、1.5 本章小结。
2. 正文为正式书面语，不使用第一人称。
3. 国内外研究现状可以引用文献，但本章小结不能引用文献。
4. 论文结构部分必须贴合真实最终章节安排，不得写成通用模板套话。
5. 必须明显服务于软件工程项目，而不是泛泛教育技术论文。

项目材料：
[在此粘贴项目背景、立项目的、技术关键词、已有参考文献等]
```

## 3. Related technology prompt

```text
使用 $gzcu-thesis-spec，根据以下软件工程项目材料撰写“第二章 相关技术与理论基础”。

要求：
1. 只写与本项目真实实现直接相关的技术或理论基础。
2. 可以覆盖前后端架构、关键框架、算法机制、缓存策略、模型接入方式等。
3. 不要堆砌与项目无关的教材式定义。
4. 章节最后必须有本章小结，且不能引用文献。

项目材料：
[在此粘贴真实技术栈、关键机制、框架使用说明、算法依据等]
```

## 4. Requirements analysis prompt

```text
使用 $gzcu-thesis-spec，根据以下软件工程项目材料撰写“第三章 系统需求分析”。

要求：
1. 结合真实用户角色、业务流程和功能边界写作。
2. 必须体现功能需求、非功能需求、关键业务流程。
3. 如涉及用例图、流程图、数据流图，请在正文中预留“如图X-X所示”的位置并说明该图要表达的内容。
4. 不要写成教材式定义堆砌，要紧贴项目真实业务。
5. 章节最后必须有本章小结，且不能引用文献。

项目材料：
[在此粘贴角色、业务流程、需求说明、界面模块、接口说明等]
```

## 5. Overall design prompt

```text
使用 $gzcu-thesis-spec，根据以下软件工程项目材料撰写“第四章 系统总体设计”。

要求：
1. 覆盖总体架构、功能模块、数据库设计、接口设计。
2. 数据库设计必须基于真实表结构，不得虚构字段。
3. 如果涉及 ER 图或架构图，请在正文中明确图示用途，并预留“如图X-X所示”。
4. 接口设计必须来源于真实后端接口，而不是空泛描述。
5. 章节最后必须输出本章小结，不引入新内容，不引用文献。

项目材料：
[在此粘贴架构说明、数据库表、接口文档、模块划分等]
```

## 6. Detailed design and implementation prompt

```text
使用 $gzcu-thesis-spec，根据以下软件工程项目材料撰写“第五章 系统详细设计与实现”章节。

要求：
1. 重点写核心模块、关键业务流程、关键算法和实现说明。
2. 必须用文字解释实现逻辑，不得直接粘贴大段代码。
3. 如需说明代码，只能描述关键逻辑，或说明后续配白底代码截图。
4. 要突出真实项目的工程实现，而不是泛泛技术介绍。
5. 如涉及算法、缓存、权限控制、AI 生成链路等，必须解释其在项目中的具体作用。
6. 章节最后必须有本章小结，且不能引用文献。

项目材料：
[在此粘贴核心模块说明、关键代码逻辑、业务流程、算法说明等]
```

## 7. Testing and deployment prompt

```text
使用 $gzcu-thesis-spec，根据以下软件工程项目材料撰写“第六章 系统测试与部署”章节。

要求：
1. 必须同时覆盖测试环境、测试策略、功能测试、性能测试、测试结果分析、部署过程与运行支撑。
2. 必须有具体测试用例和结果分析，不能只写测试意义。
3. 部署内容必须基于真实脚本、配置、服务启动步骤和运行证据。
4. 不得虚构测试数据、服务器规格或上线效果。
5. 如果测试或部署材料不足，请先列出缺失项。
6. 章节最后必须输出本章小结，且不引用文献。

项目材料：
[在此粘贴测试用例、测试结果、构建日志、部署脚本、nginx 配置、运行截图说明等]
```

## 8. Full thesis assembly prompt

```text
使用 $gzcu-thesis-spec，根据以下软件工程项目材料组装一篇广州城市理工学院本科毕业设计（论文）完整草稿。

硬性要求：
1. 必须包含中文摘要、英文摘要、目录、绪论、相关技术与理论基础、系统需求分析、系统总体设计、系统详细设计与实现、系统测试与部署、结论、参考文献、致谢。
2. 每章必须另起页，且按学校要求准备奇数页起始的 Word 实施说明。
3. 每章最后必须有本章小结。
4. 正文必须有参考文献引用，摘要、本章小结、结论不得有引用。
5. 参考文献不少于 12 篇，英文文献不少于 2 篇。
6. 必须基于真实项目材料，不得虚构模块、数据、测试结果、部署事实。
7. 输出标题必须明确且便于直接粘贴到 Word。

项目材料：
[在此粘贴完整项目证据]
```

## 9. Final software-engineering review prompt

```text
使用 $gzcu-thesis-spec，按广州城市理工学院软件工程本科毕设要求和提交版模板，审查这篇论文是否已经达到可提交状态。

重点检查：
1. 是否完整体现绪论、相关技术与理论基础、需求分析、总体设计、详细设计与实现、系统测试与部署。
2. 是否所有章节都基于真实软件工程项目证据。
3. 是否存在代码堆砌、图表无引用、测试空泛、部署失真等问题。
4. 是否满足学校的四段分节、页眉页码、奇数页起章、摘要禁引、参考文献顺序与正文引用交叉引用等硬规则。

输出格式：
- Findings
- Rule coverage
- Manual checks
- Open risks

材料：
[在此粘贴论文内容或文档路径]
```

## 10. Usage note

Prefer this prompt pack when:

- the thesis comes from a software engineering project repository,
- the user needs chapter-by-chapter prompts,
- the user wants prompts already aligned with the compliant GZCU submission template,
- the user wants reusable prompts for repeated AI-assisted drafting and review.
