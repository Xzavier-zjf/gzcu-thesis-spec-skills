# gzcu-thesis-spec-skills

[English Version](#english-version) | [中文版本](#中文版本)

---

## English Version

### Overview

**gzcu-thesis-spec-skills** is a specialized Codex Skill designed for undergraduate graduation thesis writing, formatting, and compliance review at **Guangzhou City University of Technology (GZCU)**. This skill enforces school-specific thesis rules as hard constraints, ensuring that AI-generated or AI-reviewed content strictly adheres to the university's official requirements.

The skill integrates with other Codex tools including:
- **$doc**: For `.docx` editing, section breaks, headers, footers, page numbering, TOC refresh, and final Word inspection
- **$drawio**: For thesis diagrams such as architecture figures, ER diagrams, flowcharts, and research workflow figures
- **$playwright-cli**: For browser-based evidence collection, page screenshots, UI flow verification, and runtime proof

### Key Features

#### 1. School-Specific Rule Enforcement
- Applies GZCU undergraduate thesis rules as **hard constraints**, not soft style suggestions
- Covers content structure, chapter requirements, citation rules, Word layout, headers, footers, page numbering, and figure/table formatting
- Automatically overrides general thesis generation behavior when school rules are stricter

#### 2. Comprehensive Reference Documentation
The skill includes 15+ reference documents covering:
- **Content & Structure Rules**: Chapter requirements, abstract guidelines, citation rules, length constraints
- **Layout & Word Rules**: Headers, footers, page numbers, section breaks, fonts, spacing, figure/table placement
- **Compliance Checklist**: Severity-based review criteria and manual-check items
- **Output Blueprint**: Stable templates for abstracts, TOC, chapter drafts, and delivery packages
- **Prompt Library**: Ready-to-use prompts for common thesis tasks
- **Software Engineering Prompt Pack**: GZCU-oriented prompts for software engineering theses
- **Project Evidence Intake**: Structured checklist for collecting real project material
- **Review Report Template**: Standard format for compliance reviews
- **First Use Guide**: Quick-start guide for new users
- **Example Call Card**: 5 most common calling patterns
- **Skill Integration**: How to use `$drawio`, `$playwright-cli`, and `$doc` together
- **Thesis Production Pipeline**: End-to-end workflow from evidence intake to final submission
- **Asset Assembly Schema**: Manifest template for bulk figure insertion
- **Asset Manifest Field Guide**: Field-by-field guide for asset manifests
- **Script Usage**: Concrete commands for asset assembly and cross-reference generation

#### 3. Automated Scripts
The skill provides Python scripts for Word document automation:
- **assemble_thesis_assets.py**: Batch-insert Draw.io figures, UI screenshots, and code screenshots
- **normalize_figure_paragraphs.py**: Normalize figure-block spacing (1.5 line spacing for image paragraphs)
- **build_reference_crossrefs.py**: Convert plain-text citations `[1]` to clickable Word cross-references
- **build_figure_crossrefs.py**: Convert `如图 X-X 所示` to clickable figure-caption cross-references
- **build_table_crossrefs.py**: Convert `如表 X-X 所示` to clickable table-caption cross-references

#### 4. Default Workflow
1. **Build Compliance Matrix**: Extract applicable school rules before writing
2. **Ground in Project Evidence**: Collect real project material (system goals, modules, tech stack, screenshots, diagrams)
3. **Choose Task Mode**: Constraint mode, chapter generation, review mode, Word implementation, asset assembly, or cross-reference mode
4. **Enforce Hard Bans**: Never violate critical rules (no citations in abstract/conclusion, no first-person narrative, etc.)
5. **Compliance Audit**: Report satisfied rules, remaining risks, and manual-check items

### Project Structure

```
gzcu-thesis-spec/
├── SKILL.md                          # Main skill definition and workflow
├── agents/
│   └── openai.yaml                   # Agent interface configuration
├── references/                       # 15+ reference documents
│   ├── content-and-structure.md      # Content and chapter structure rules
│   ├── layout-and-word-rules.md      # Word layout and formatting rules
│   ├── compliance-checklist.md       # Review checklist by severity
│   ├── output-blueprint.md           # Output templates
│   ├── prompt-library.md             # Ready-to-use prompts
│   ├── software-engineering-prompt-pack.md
│   ├── project-evidence-intake.md    # Evidence collection checklist
│   ├── review-report-template.md     # Review report format
│   ├── first-use-guide.md            # Quick-start guide
│   ├── example-call-card.md          # Common calling patterns
│   ├── skill-integration.md          # Integration with other skills
│   ├── thesis-production-pipeline.md # End-to-end workflow
│   ├── asset-assembly-schema.md      # Asset manifest schema
│   ├── asset-manifest-field-guide.md # Field guide for manifests
│   └── script-usage.md               # Script usage examples
├── scripts/                          # Python automation scripts
│   ├── assemble_thesis_assets.py
│   ├── normalize_figure_paragraphs.py
│   ├── build_reference_crossrefs.py
│   ├── build_figure_crossrefs.py
│   └── build_table_crossrefs.py
└── templates/
    └── asset-manifest.template.json  # Template for asset manifests
```

### Quick Start

#### When to Use This Skill
Use this skill when Codex must:
- Write thesis sections according to GZCU requirements
- Review an existing draft for compliance
- Fix citation order or bibliography format
- Check chapter structure completeness
- Adjust headers, footers, page numbers, or section breaks
- Produce Word-ready guidance against GZCU rules
- Handle requests like:
  - "根据学校要求写论文" (Write thesis according to school requirements)
  - "按广州城市理工学院格式写毕业论文" (Write graduation thesis in GZCU format)
  - "检查论文是否符合学校规范" (Check if thesis complies with school standards)
  - "调整页眉页码/参考文献/摘要格式" (Adjust header/page number/references/abstract format)
  - "按学校模板做终稿" (Prepare final manuscript according to school template)

#### Basic Usage
1. Load the skill in your Codex environment
2. Specify your task mode (constraint, generation, review, Word implementation, etc.)
3. Provide project evidence or existing thesis draft
4. Receive compliance-focused output with audit report

### Installation & Requirements

- **Python 3.x**: Required for running automation scripts
- **python-docx**: Python library for Word document manipulation
- **Codex Environment**: This skill is designed for use within the Codex AI assistant framework

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 中文版本

### 项目概述

**gzcu-thesis-spec-skills** 是专为**广州城市理工学院**本科毕业设计（论文）写作、排版与合规审查而设计的 Codex Skill。该技能将学校特定的论文规则作为**硬性约束**执行，确保 AI 生成或审查的内容严格遵守学校的官方要求。

本技能可与其他 Codex 工具集成使用：
- **$doc**：用于 `.docx` 文档编辑、分节符、页眉页脚、页码、目录刷新及最终 Word 检查
- **$drawio**：用于论文图表，如架构图、ER 图、流程图和研究工作流图
- **$playwright-cli**：用于基于浏览器的证据收集、页面截图、UI 流程验证和运行时证明

### 核心功能

#### 1. 学校特定规则执行
- 将广州城市理工学院本科论文规则作为**硬性约束**执行，而非软性风格建议
- 涵盖内容结构、章节要求、引用规则、Word 排版、页眉页脚、页码、图表格式等
- 当学校规则更严格时，自动覆盖通用论文生成行为

#### 2. 全面的参考文档
技能包含 15+ 份参考文档：
- **内容与结构规则** (`content-and-structure.md`)：章节要求、摘要指南、引用规则、字数约束
- **排版与 Word 规则** (`layout-and-word-rules.md`)：页眉页脚、页码、分节符、字体、间距、图表放置
- **合规检查清单** (`compliance-checklist.md`)：按严重程度分类的审查标准和人工检查项
- **输出蓝图** (`output-blueprint.md`)：摘要、目录、章节草稿和交付包的稳定模板
- **提示词库** (`prompt-library.md`)：常用论文任务的即用型提示词
- **软件工程提示包** (`software-engineering-prompt-pack.md`)：面向 GZCU 的软件工程论文提示词
- **项目证据收集清单** (`project-evidence-intake.md`)：收集真实项目材料的结构化清单
- **审查报告模板** (`review-report-template.md`)：合规审查的标准报告格式
- **首次使用指南** (`first-use-guide.md`)：新用户的快速入门指南
- **调用示例卡** (`example-call-card.md`)：5 种最常见的调用模式
- **技能集成** (`skill-integration.md`)：如何联合使用 `$drawio`、`$playwright-cli` 和 `$doc`
- **论文生产流水线** (`thesis-production-pipeline.md`)：从证据收集到最终提交的端到端工作流
- **素材组装模式** (`asset-assembly-schema.md`)：批量插入图表的清单模板
- **素材清单字段指南** (`asset-manifest-field-guide.md`)：素材清单的字段级填写指南
- **脚本使用说明** (`script-usage.md`)：素材组装和交叉引用生成的具体命令

#### 3. 自动化脚本
技能提供 Python 脚本用于 Word 文档自动化：
- **assemble_thesis_assets.py**：批量插入 Draw.io 图表、UI 截图和代码截图
- **normalize_figure_paragraphs.py**：规范化图块间距（图片段落使用 1.5 倍行距）
- **build_reference_crossrefs.py**：将纯文本引用 `[1]` 转换为可点击的 Word 交叉引用
- **build_figure_crossrefs.py**：将 `如图 X-X 所示` 转换为可点击的图题交叉引用
- **build_table_crossrefs.py**：将 `如表 X-X 所示` 转换为可点击的表题交叉引用

#### 4. 默认工作流程
1. **构建合规矩阵**：在写作前提取适用的学校规则
2. **基于项目证据**：收集真实项目材料（系统目标、模块、技术栈、截图、图表）
3. **选择任务模式**：约束模式、章节生成、审查模式、Word 实现、素材组装或交叉引用模式
4. **执行硬性禁令**：绝不违反关键规则（摘要/结论中无引用、正文不用第一人称等）
5. **合规审计**：报告已满足的规则、剩余风险和需人工检查的项目

### 项目结构

```
gzcu-thesis-spec/
├── SKILL.md                          # 主技能定义和工作流
├── agents/
│   └── openai.yaml                   # Agent 接口配置
├── references/                       # 15+ 份参考文档
│   ├── content-and-structure.md      # 内容和章节结构规则
│   ├── layout-and-word-rules.md      # Word 排版和格式规则
│   ├── compliance-checklist.md       # 按严重程度分类的检查清单
│   ├── output-blueprint.md           # 输出模板
│   ├── prompt-library.md             # 即用型提示词库
│   ├── software-engineering-prompt-pack.md
│   ├── project-evidence-intake.md    # 证据收集清单
│   ├── review-report-template.md     # 审查报告格式
│   ├── first-use-guide.md            # 快速入门指南
│   ├── example-call-card.md          # 常见调用模式
│   ├── skill-integration.md          # 与其他技能的集成
│   ├── thesis-production-pipeline.md # 端到端工作流
│   ├── asset-assembly-schema.md      # 素材清单模式
│   ├── asset-manifest-field-guide.md # 清单字段指南
│   └── script-usage.md               # 脚本使用示例
├── scripts/                          # Python 自动化脚本
│   ├── assemble_thesis_assets.py
│   ├── normalize_figure_paragraphs.py
│   ├── build_reference_crossrefs.py
│   ├── build_figure_crossrefs.py
│   └── build_table_crossrefs.py
└── templates/
    └── asset-manifest.template.json  # 素材清单模板
```

### 快速开始

#### 何时使用此技能
当 Codex 需要执行以下任务时使用此技能：
- 根据广州城市理工学院要求撰写论文章节
- 审查现有草稿的合规性
- 修正引用顺序或参考文献格式
- 检查章节结构完整性
- 调整页眉、页脚、页码或分节符
- 根据 GZCU 规则生成 Word 就绪的指导
- 处理如下请求：
  - "根据学校要求写论文"
  - "按广州城市理工学院格式写毕业论文"
  - "检查论文是否符合学校规范"
  - "调整页眉页码/参考文献/摘要格式"
  - "按学校模板做终稿"

#### 基本使用方法
1. 在 Codex 环境中加载此技能
2. 指定任务模式（约束模式、生成模式、审查模式、Word 实现等）
3. 提供项目证据或现有论文草稿
4. 接收带有审计报告的合规导向输出

### 安装与要求

- **Python 3.x**：运行自动化脚本所需
- **python-docx**：用于 Word 文档操作的 Python 库
- **Codex 环境**：本技能专为 Codex AI 助手框架设计

### 主要规则摘要

#### 内容结构规则
- 正文至少 `1.5 万字`
- 每章至少 `3 页`
- 每章必须以`本章小结` 结尾
- 摘要、本章小结、结论中不得引用文献
- 正文不得使用第一人称（致谢除外）
- 参考文献至少 `12` 篇，其中英文文献至少`2` 篇

#### 排版规则
- 封面和说明页为固定模板，不得修改
- 从中文摘要页开始应用排版规则
- 奇数页开始新章节，必要时插入空白过渡页
- 摘要和目录使用罗马数字页码
- 正文、结论、参考文献、致谢使用阿拉伯数字页码
- 图表标题：图下表上，编号按章（如图 1-1、表 1-1）

#### 硬性禁令
- 禁止在摘要、本章小结、结论中引用文献
- 禁止在正文中使用第一人称
- 禁止粘贴长段原始代码
- 禁止省略本章小结
- 禁止忽略奇数页章节起始规则
- 禁止让图表编号存在但正文未引用
- 禁止修改封面和学校声明页

### 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

---

### Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to improve the skill documentation, scripts, or reference materials.

欢迎贡献！请随时提交 issue 或 pull request 以改进技能文档、脚本或参考材料。

### Contact

For questions or suggestions regarding this skill, please refer to the project repository or contact the maintainer.

如有问题或建议，请参考项目仓库或联系维护者。
