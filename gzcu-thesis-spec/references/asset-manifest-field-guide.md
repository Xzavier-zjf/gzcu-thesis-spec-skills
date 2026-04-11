# Asset Manifest Field Guide

Use this file when filling `templates/asset-manifest.template.json`.

This guide explains what each JSON field means, how to fill it, and which mistakes most often break batch insertion.

## 1. Template location

Start from:

- [templates/asset-manifest.template.json](../templates/asset-manifest.template.json)

## 2. Top-level fields

### `docx_path`

Purpose:

- absolute path to the target thesis `.docx` file.

How to fill:

- use a real absolute path for your current platform
- point to the current working thesis draft, not a folder

Correct example:

```json
"docx_path": "/path/to/thesis.docx"
```

Platform notes:

- Windows can use `D:/论文/毕业设计（论文）-提交版.docx` or escaped backslashes such as `D:\\论文\\毕业设计（论文）-提交版.docx`
- macOS and Linux should use `/Users/...` or `/home/...`
- this template defaults to forward slashes so the JSON stays portable across platforms

Common mistakes:

- writing a relative path such as `"./thesis.docx"`
- pointing to a folder instead of a `.docx`
- pointing to an old backup copy by mistake

### `items`

Purpose:

- ordered list of assets to insert into the thesis.

How to fill:

- keep the items in the same order you want them processed
- usually follow chapter order

Common mistakes:

- mixing Chapter 5 assets before Chapter 2 assets without a reason
- forgetting commas between items

## 3. Per-item fields

Each item represents one inserted figure block.

### `chapter`

Purpose:

- tells the script which chapter or section heading to insert after.

How to fill:

- use the exact heading text if possible
- best for insertion immediately after a section title

Correct examples:

```json
"chapter": "第二章 系统设计"
```

```json
"chapter": "4.1 系统总体架构设计"
```

Common mistakes:

- writing a shortened heading that does not exist in the `.docx`
- using `chapter` for a location that is actually inside a section body

### `anchor_text`

Purpose:

- tells the script to insert after a specific paragraph or marker.

How to fill:

- use a stable paragraph marker that actually exists in the document
- best for precise insertion inside a chapter
- if you prepare the draft yourself, use explicit markers such as `【ANCHOR_ARCH】`

Correct examples:

```json
"anchor_text": "【ANCHOR_ARCH】"
```

```json
"anchor_text": "系统总体结构说明如下。"
```

Common mistakes:

- using a sentence that appears multiple times
- using text with extra spaces or punctuation that does not exactly match the document
- deleting the anchor from the `.docx` after writing the manifest

Rule:

- if both `chapter` and `anchor_text` are present, the script prefers `anchor_text`

### `asset_type`

Purpose:

- classifies the asset for workflow clarity.

Allowed values:

- `drawio_figure`
- `ui_screenshot`
- `code_screenshot`

How to fill:

- use `drawio_figure` for formal diagrams
- use `ui_screenshot` for browser or system page screenshots
- use `code_screenshot` for white-background code images

Common mistakes:

- inventing a new type such as `diagram` or `screen`
- using a code screenshot with a dark background

### `asset_path`

Purpose:

- absolute path to the image file that will be inserted.

How to fill:

- use a real local image path for your current platform
- prefer `.png` for stable Word insertion
- confirm the file exists before running the script

Correct example:

```json
"asset_path": "/path/to/figures/architecture.png"
```

Common mistakes:

- writing a relative path
- pointing to a temporary file that was already deleted
- pointing to a `.drawio` source file instead of an exported image

### `figure_number`

Purpose:

- the figure number shown in the caption.

How to fill:

- follow thesis numbering by chapter
- keep it consistent with the chapter where the asset is inserted

Correct examples:

```json
"figure_number": "图2-1"
```

```json
"figure_number": "图5-3"
```

Common mistakes:

- using a number that belongs to another chapter
- skipping or duplicating figure numbers

### `caption`

Purpose:

- the descriptive caption text shown below the figure.

How to fill:

- keep it short, formal, and specific
- describe what the figure proves or shows

Correct examples:

```json
"caption": "系统总体架构图"
```

```json
"caption": "单词学习页面运行截图"
```

Common mistakes:

- writing overly long captions
- using colloquial wording
- making the caption inconsistent with the figure itself

### `intro_text`

Purpose:

- the lead-in sentence inserted before the figure.

How to fill:

- write one formal sentence
- normally include wording such as `如图X-X所示`

Correct example:

```json
"intro_text": "系统总体结构如图2-1所示。"
```

Common mistakes:

- forgetting to update the figure number in the sentence
- writing multiple long paragraphs instead of one lead-in sentence

### `analysis_text`

Purpose:

- explanatory sentence or short paragraph inserted after the caption.

How to fill:

- explain what the figure demonstrates
- keep it evidence-oriented, not decorative

Correct example:

```json
"analysis_text": "该图展示了前端、后端与数据层之间的主要关系。"
```

Common mistakes:

- leaving it empty for figures that clearly need explanation
- repeating the caption without adding meaning
- writing claims that the figure does not actually support

## 4. When to use `chapter` and when to use `anchor_text`

Use `chapter` when:

- the figure should appear right after a chapter or section heading
- the heading text is unique and stable

Use `anchor_text` when:

- the figure belongs after a specific sentence or marker inside the body
- you need precise placement

Prefer `anchor_text` when you control the draft and can place explicit markers.

## 5. Recommended filling workflow

1. prepare or export all images first
2. open the `.docx` and place anchor markers where needed
3. copy `asset-manifest.template.json`
4. fill `docx_path`
5. fill each item in chapter order
6. verify every `asset_path` exists
7. run `assemble_thesis_assets.py`
8. run `normalize_figure_paragraphs.py`
9. inspect the result in Word

## 6. Common failure cases

### Case 1. Script says anchor not found

Likely reasons:

- `anchor_text` does not exactly exist in the document
- the heading text changed after the manifest was written

Fix:

- re-check the exact paragraph text in the `.docx`
- use a unique explicit anchor marker

### Case 2. Image inserts in the wrong place

Likely reasons:

- the chosen `anchor_text` appears more than once
- `chapter` matches a similar heading earlier than expected

Fix:

- replace vague anchors with unique markers such as `【ANCHOR_UI_01】`

### Case 3. Figure number and caption do not match the chapter

Likely reasons:

- numbering was copied from another chapter

Fix:

- re-check the chapter-local numbering sequence before batch insertion

### Case 4. Asset file cannot be opened

Likely reasons:

- wrong path
- file was moved or renamed
- source file is not an exported image

Fix:

- use the exported `.png` or another Word-friendly image file

### Case 5. Inserted figure has no proper explanation in the text

Likely reasons:

- `intro_text` or `analysis_text` was left too vague

Fix:

- ensure the lead-in sentence references the figure number
- ensure the analysis sentence explains the figure's role in the thesis

## 7. Minimal safe checklist

Before running the assembly script, confirm:

- `docx_path` is correct
- every `asset_path` exists
- every `anchor_text` or `chapter` exists in the document
- figure numbers match chapter numbering
- captions are formal
- `intro_text` includes `如图X-X所示` where appropriate
- `analysis_text` explains the figure instead of repeating the caption
