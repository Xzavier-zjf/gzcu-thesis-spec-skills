# Project Evidence Intake

Use this file before writing. It is a structured intake template for collecting real project evidence so the thesis stays grounded in the actual software project.

## 1. Intake usage rule

Use this template before any chapter-generation task if the user has not already provided a complete project package.

Goal:

- reduce fabrication risk,
- map each thesis chapter to real project evidence,
- expose missing artifacts early.

## 2. Minimal intake package

Collect at least the following before asking AI to draft a full thesis:

```text
项目基本信息
- 项目名称：
- 项目类型：Web / Java / Vue / Spring Boot / 小程序 / 桌面应用 / 其他
- 所属专业方向：软件工程 / 计算机科学 / 大数据 / 其他
- 论文拟定题目：
- 项目一句话简介：
- 项目解决的实际问题：
- 目标用户：

项目代码与结构
- 仓库路径或压缩包路径：
- 前端目录：
- 后端目录：
- 数据库脚本路径：
- 部署脚本或配置路径：
- 关键配置文件路径：

技术栈
- 前端技术：
- 后端技术：
- 数据库与缓存：
- 鉴权或权限技术：
- AI / 算法 / 推荐 / 调度相关技术：
- 第三方服务：

功能模块
- 模块 1：名称 + 作用 + 主要页面/接口
- 模块 2：名称 + 作用 + 主要页面/接口
- 模块 3：名称 + 作用 + 主要页面/接口
- 管理端或后台模块：

数据库与数据结构
- 主要数据表：
- 每张表的核心字段：
- 表之间关系：
- 是否已有 ER 图：有 / 无

业务流程
- 关键业务流程 1：
- 关键业务流程 2：
- 关键业务流程 3：
- 是否已有流程图/用例图/时序图：有 / 无

测试与验证
- 是否有测试用例：有 / 无
- 是否有自动化测试：有 / 无
- 是否有构建结果：有 / 无
- 是否有接口测试记录：有 / 无
- 是否有性能测试或压测记录：有 / 无
- 可引用的测试截图或日志：

部署与运行
- 开发环境：
- 运行环境：
- 部署步骤：
- Nginx / Docker / 脚本 / 云服务器信息：
- 启动日志或运行截图：

图表与截图素材
- 首页/主要页面截图：
- 后台页面截图：
- 数据库截图：
- 测试截图：
- 部署截图：
- 代码截图候选位置：

创新点与局限性
- 项目创新点：
- 与普通课程设计相比更深入的地方：
- 当前缺陷：
- 后续优化方向：

参考文献准备
- 已收集中文文献：
- 已收集英文文献：
- 是否已有学校要求的至少 12 篇文献：是 / 否

人工信息
- 导师全名：
- 学院名称：
- 专业班级：
- 学号、姓名是否后续手填：是 / 否
```

## 3. Chapter-to-evidence mapping

Use this mapping before writing:

- Chapter 1 Introduction:
  - project background,
  - research significance,
  - related literature,
  - thesis objective.
- Requirements analysis:
  - user roles,
  - business scenarios,
  - use cases,
  - workflow evidence.
- Overall design:
  - architecture,
  - module split,
  - database,
  - interfaces.
- Detailed design and implementation:
  - real code structure,
  - real module logic,
  - real algorithms,
  - screenshots and code-image candidates.
- Testing:
  - test cases,
  - test logs,
  - build output,
  - result summaries.
- Deployment:
  - scripts,
  - configs,
  - startup process,
  - verification screenshots.
- Conclusion:
  - completed work,
  - measurable effect,
  - limitations,
  - future work.

## 4. Missing-evidence output template

If the intake is incomplete, report the gaps using this format:

```text
缺失项目材料
- [高优先级缺失项]
- [会导致论文失真的缺失项]
- [可以后补但建议尽快提供的缺失项]

可先写的章节
- [已有足够证据支持的章节]

暂不建议写的章节
- [缺少测试/部署/数据库/图表等证据的章节]
```

## 5. High-risk fabrication zones

Never draft these from guesswork:

- database table names and fields,
- API endpoints and request/response logic,
- test results and performance data,
- deployment environment details,
- innovation points that are not visible in the project,
- supervisor full name.

## 6. Fast intake prompt

Use this prompt when the user has not organized materials yet:

```text
使用 $gzcu-thesis-spec，先不要写论文。请根据广州城市理工学院本科毕业论文要求，给我一份“真实项目材料采集清单”，并按“项目基本信息、代码结构、技术栈、功能模块、数据库、业务流程、测试、部署、图表素材、创新点、参考文献、人工信息”分类列出我需要补齐的内容。若某项缺失会直接影响论文真实性，请单独标注高优先级。
```
