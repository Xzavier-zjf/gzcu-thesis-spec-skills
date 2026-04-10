# Asset Assembly Schema

Use this file when preparing a manifest for `scripts/assemble_thesis_assets.py`.

## 1. Supported manifest formats

- JSON is the default and recommended format.
- YAML is also allowed if `PyYAML` is installed.
- Ready-to-copy JSON template: [templates/asset-manifest.template.json](../templates/asset-manifest.template.json)

## 2. Required top-level fields

```json
{
  "docx_path": "C:/path/to/thesis.docx",
  "items": []
}
```

- `docx_path`: target Word document.
- `items`: ordered asset insertion list.

## 3. Required item fields

Each item should include at least:

- `chapter` or `anchor_text`
- `asset_type`
- `asset_path`
- `caption`
- `figure_number`

Optional but recommended:

- `intro_text`
- `analysis_text`

## 4. Asset types

Allowed logical values:

- `drawio_figure`
- `ui_screenshot`
- `code_screenshot`

The current script treats them uniformly during insertion, but keep the type for workflow clarity.

## 5. Example manifest

```json
{
  "docx_path": "C:/work/thesis.docx",
  "items": [
    {
      "chapter": "4.1 系统总体架构设计",
      "asset_type": "drawio_figure",
      "asset_path": "C:/work/assets/architecture.png",
      "figure_number": "图4-1",
      "caption": "系统总体架构图",
      "intro_text": "系统总体结构如图4-1所示。",
      "analysis_text": "该图展示了前端、后端、数据库与模型服务之间的调用关系。"
    },
    {
      "anchor_text": "5.2 功能测试",
      "asset_type": "ui_screenshot",
      "asset_path": "C:/work/assets/dashboard.png",
      "figure_number": "图5-2",
      "caption": "学习看板页面运行效果",
      "intro_text": "学习看板页面运行效果如图5-2所示。",
      "analysis_text": "图中可见待复习统计、趋势图与学习概览模块均已正常展示。"
    }
  ]
}
```

## 6. Anchor rule

- `chapter` is best for insertion right after a chapter or section heading.
- `anchor_text` is best for insertion after a specific sentence or paragraph marker.
- If both are provided, the script prefers `anchor_text` first.

## 7. Formatting behavior

The assembly script inserts the asset block as:

1. intro paragraph
2. image paragraph
3. caption paragraph
4. analysis paragraph

The image paragraph is centered and set to `1.5` line spacing.

For existing documents that already contain images, run `scripts/normalize_figure_paragraphs.py` afterwards to normalize nearby spacing.
