# Layout and Word Rules

Use this file when the task involves Word layout, format review, or final manuscript guidance.

Evidence priority:

1. school format document,
2. submitted sample `.docx` baseline.

## 1. Activation boundary

- The cover page and school declaration pages should follow the school template.
- Apply the main formatting rules starting from the Chinese abstract page.

## 2. School hard rules

### Abstract pages

- Chinese abstract title uses centered bold heading style.
- Chinese abstract body uses `小四` `宋体`.
- English abstract uses `Times New Roman`.
- Line spacing is fixed at `20 磅`.
- Chinese and English abstracts should each occupy one page.

### TOC

- TOC title should be centered.
- TOC entries use school-specified heading hierarchy.
- TOC should reflect the actual chapter structure.

### Body text

- Level-1 heading: `三号` `宋体` bold, centered, with one blank line above and below.
- Level-2 heading: `小三` `宋体` bold, left aligned, with one blank line above and below.
- Level-3 heading: `四号` `宋体` bold, left aligned, no blank line after the heading line.
- Body text: `小四` `宋体`.
- Line spacing: fixed `20 磅`.
- First-line indent: `2` Chinese characters.
- English and numbers use `Times New Roman`.

### Figures and tables

- Figure and table text use `五号` `宋体`.
- Figure title below figure.
- Table title above table.
- Figures and tables must be numbered by chapter.
- Do not split a figure and its caption across pages.
- Tables should not use left and right outer vertical borders.

### References and acknowledgements

- References title and acknowledgements title follow the chapter-title style.
- References body uses `五号` `宋体`, fixed `20 磅` line spacing.
- Acknowledgements body uses `五号` `宋体`, fixed `20 磅` line spacing.

## 3. Sample-based baseline suggestions

The submitted sample `.docx` supports the following as a stable reference implementation:

- a `4`-section model,
- Roman numerals for abstract pages,
- TOC in its own section,
- Arabic numbering starting from Chapter 1,
- odd/even header behavior in the main body section,
- a software-engineering 6-chapter reference structure.

These are reference-baseline suggestions, not automatic school hard rules.

## 4. Section and page-number guidance

When the user needs Word guidance close to the submitted sample, a practical reference model is:

1. cover + declaration pages,
2. Chinese abstract + English abstract,
3. TOC,
4. main body through acknowledgements.

Recommended interpretation:

- section 1: no visible headers or page numbers,
- section 2: Roman numbering,
- section 3: separate TOC section,
- section 4: Arabic numbering starting from Chapter 1.

## 5. Chapter opening guidance

- Every chapter should start on a new page.
- In final Word layout, odd-page chapter starts are recommended to match the submitted sample baseline.
- If pagination changes after edits, odd-page starts must be checked manually in Word.

## 6. Header guidance

The submitted sample shows an odd/even header mechanism in the main body:

- even-page header fixed as `广州城市理工学院本科毕业设计（论文）`
- odd-page header follows the current chapter heading

In the sample, Word `STYLEREF` is one observed way to implement the odd-page header. Treat it as a reference implementation, not as the only legal method.

## 7. What should not be defaulted

- Do not default to clickable bibliography cross-references.
- Do not default to clickable figure or table cross-references.
- Do not default to screenshot-evidence workflows, asset assembly, or diagram-generation workflows.
- Do not present sample-based Word implementation details as school hard rules unless the school document also confirms them.

## 8. Manual Word checks

Always call out items that need manual confirmation:

- actual page occupancy after final pagination,
- odd-page chapter starts,
- TOC refresh,
- Roman and Arabic numbering display,
- header visibility on abstract and TOC pages,
- figure-caption and table-caption pagination,
- consistency between body formatting and school rules.
