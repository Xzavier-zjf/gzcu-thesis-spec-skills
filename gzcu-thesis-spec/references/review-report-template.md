# Review Report Template

Use this file when the user wants a repeatable standard report for checking multiple thesis versions.

For stable severity decisions, also load `review-severity-policy.md`.
For template-aligned review against the compliant final manuscript, also load `submission-template-baseline.md`.

## 1. Usage rule

Use this template for versioned review reports such as:

- first full review,
- citation-only review,
- Word-format review,
- pre-submission review,
- advisor feedback follow-up review.

The report must stay comparable across versions so the user can see what improved and what still blocks submission.

## 2. Standard report structure

```text
论文审查结果报告

版本信息
- 文档名称：
- 版本标识：
- 审查日期：
- 审查范围：全文 / 指定章节 / 引用与参考文献 / Word 终稿格式 / 其他

总体结论
- 当前状态：可继续完善 / 基本合规但仍有风险 / 不建议提交
- 最高优先级问题数量：
- 主要风险概览：

Findings
1. [问题标题]
优先级：Critical / Major / Minor / Enhancement
所在位置：
违反规则：
问题说明：
建议修改：

2. [问题标题]
优先级：...
所在位置：
违反规则：
问题说明：
建议修改：

Rule coverage
- 已满足规则：
- 未满足规则：
- 待人工确认规则：

Version delta
- 相比上一版已修复：
- 相比上一版新增问题：
- 仍未解决的问题：

Manual checks
- 必须在 Word 中人工复核的项目：
- 必须由作者补充的项：

Open risks
- 若现在提交，仍可能出现的问题：
- 影响答辩或评优的风险：
```

## 3. Severity policy

Use this severity mapping consistently. Keep `Enhancement` separate from blocking compliance issues.

### Critical

Issues that can block submission, defense, or formal compliance:

- missing mandatory chapters,
- abstract / chapter summary / conclusion citation violations,
- references not cited in body,
- citation order inconsistent with reference order,
- chapter does not start on a new page when required,
- odd-page start rule violated,
- missing test cases and result analysis,
- fabricated project facts.

### Major

Issues that do not immediately block submission but materially weaken compliance or quality:

- chapter summary missing,
- body uses first person,
- figure/table not cited in text,
- Word section/page-number logic likely wrong,
- journal or monograph references missing page ranges,
- deployment or testing chapter too generic.

### Minor

Presentation or consistency issues:

- inconsistent wording,
- caption placement drift,
- English/numeric font inconsistency,
- spacing and title formatting inconsistencies,
- wording not formal enough.

### Enhancement

Optional improvements beyond the compliant submission baseline:

- clickable figure cross-references,
- clickable table cross-references,
- extra asset-normalization polish,
- other final-docx improvements not proven mandatory by the submission baseline.

## 4. Quick review variants

### A. Citation review

```text
论文审查结果报告
版本信息
- 审查范围：正文引用与参考文献

总体结论
- 当前状态：
- 主要风险概览：

Findings
1. 引用顺序问题
2. 未引用参考文献问题
3. 禁引区域引用问题
4. [J]/[M] 页码缺失问题

Manual checks
- 上标位置
- 句末标点位置
```

### B. Word format review

```text
论文审查结果报告
版本信息
- 审查范围：Word 终稿格式

总体结论
- 当前状态：
- 主要风险概览：

Findings
1. 四段分节与页眉页码问题
2. 章节奇数页起始问题
3. 目录自动生成或未更新问题
4. 正文引用交叉引用问题
5. 图表/代码截图格式问题

Manual checks
- 目录域更新
- 空白过渡页是否正确
- 页眉线 1.5 磅
```

### C. Full compliance review

```text
论文审查结果报告
版本信息
- 审查范围：全文

总体结论
- 当前状态：
- 主要风险概览：

Findings
1. 结构问题
2. 内容真实性问题
3. 引用与参考文献问题
4. 图表与代码问题
5. 测试与部署问题
6. Word 终稿格式问题

Version delta
- 已修复：
- 新增问题：
- 遗留问题：

Manual checks
- 导师全名
- 每章页数
- 奇数页起章
- TOC 刷新
- 正文引用点击跳转
```

## 5. Version comparison note

When the user is iterating across versions, always include:

- what improved from the last version,
- what regressed,
- what is still blocking final submission.

Do not just restate the full issue list without a delta.

## 6. Final submission recommendation template

End with one of these recommendation lines:

```text
提交建议
- 当前版本仍不建议提交，需先修复 Critical 问题。
```

```text
提交建议
- 当前版本基本合规，但仍建议在提交前完成 Manual checks 中的 Word 终稿复核。
```

```text
提交建议
- 当前版本已接近提交状态，仅剩少量 Minor 格式问题可继续打磨。
```

```text
提交建议
- 当前版本已达到提交基线，剩余主要为 Enhancement 项，可按时间决定是否继续打磨。
```
