# Layout and Word Rules

Use this file when the task involves Word layout, final DOCX preparation, or format review.

This file is calibrated against a real Guangzhou City University of Technology submission-ready `.docx`. When the school rule text is generic but the compliant template is more specific, prefer the template-compatible implementation below.

## 1. Activation boundary

- The cover page and the second explanation page are fixed school template pages.
- Do not change their fonts, sizes, spacing, headers, footers, or page numbers.
- Apply the following layout rules starting from the Chinese abstract page.

## 2. Default section model

Use the compliant manuscript's 4-section structure as the default Word implementation:

1. cover page + explanation page
2. Chinese abstract + English abstract
3. TOC
4. main body through acknowledgements

Default behavior by section:

- Section 1: no headers, no page numbers.
- Section 2: no headers, Roman page numbers starting from `I`.
- Section 3: no headers, Roman numbering continues in the section model but page numbers stay hidden.
- Section 4: even/odd headers enabled, Arabic page numbers starting from `1`.

Do not assume `结论`、`参考文献`、`致谢` must each become a separate header/page-number section. In the compliant template they continue inside the same main-body header/page-number scheme and only require correct chapter starts.

## 3. Headers

### Where headers appear

- Hide headers on the cover page, explanation page, Chinese abstract, English abstract, and TOC.
- Show headers from Chapter 1 through `致谢`.

### How headers are controlled

- Use Word section breaks, not one global header for the entire document.
- Enable odd/even headers in the main-body section.
- Keep the header bottom border at `1.5 磅`.
- Hidden-header sections may still contain empty header definitions; this is acceptable if the rendered page shows no visible header.

### Header text

- Even-page header: `广州城市理工学院本科毕业设计（论文）`
- Odd-page header: use Word `STYLEREF` to pull the current level-1 heading text.

Do not hard-code separate odd-page headers such as `结 论`、`参考文献`、`致 谢` unless the user is intentionally deviating from the compliant template. The default should follow the current level-1 title automatically.

## 4. Page numbers

- Chinese and English abstracts use uppercase Roman numerals and start from `I`.
- TOC belongs to its own section; keep its page numbers hidden.
- The main body starts a new Arabic numbering scheme from Chapter 1 and begins at `1`.
- `结论`、`参考文献`、`致谢` continue the main body's Arabic numbering and do not restart.
- Hide page numbers on the cover page, explanation page, and TOC.

## 5. Chapter opening rules

- Every chapter starts on a new page.
- Every chapter must start on an odd-numbered page.
- If the next chapter would start on an even-numbered page, insert a blank transition page before it.
- Apply the same odd-page rule to `结论`、`参考文献`、`致谢`.

## 6. Fonts, styles, and spacing

### Global font principle

- All English and all numbers use `Times New Roman`.
- Chinese body text uses `宋体`.
- When a compliant template already defines built-in Word heading styles, follow the template style implementation first rather than re-imposing an abstract font description paragraph by paragraph.

### Template-compatible heading behavior

- Level 1 headings are centered and treated as the chapter-level style that also drives odd-page `STYLEREF` headers.
- Level 2 and Level 3 headings should stay on the page with following content.
- If the template heading styles differ slightly from a simplified textual rule but match the compliant submission template, prefer the template styles.

### Body text

- body text size: `小四` (`12.0 pt`)
- Chinese body text font: `宋体`
- English and numeric text font: `Times New Roman`
- fixed line spacing: `20 磅`
- first-line indent: `2` Chinese characters

### References and acknowledgements

- section title style follows the template's level-1 heading behavior
- reference entries and acknowledgement body text should remain visually compliant with the school template
- if a local template already defines the final appearance, keep it rather than reformatting manually paragraph by paragraph

## 7. Widow/orphan and heading placement

- Do not allow any heading to appear as the last line on a page.
- Keep headings with the following content.
- Adjust page breaks or pagination to preserve odd-page chapter starts without creating awkward heading or figure splits.

## 8. Figures and tables

- Figure titles go below the figure.
- Table titles go above the table.
- Figure titles, table titles, and table text use `宋体五号` unless the compliant template already enforces an equivalent caption/table style.
- Number figures and tables by chapter, such as `图1-1` and `表1-1`.
- Body references to figures and tables must stay at body-text size `小四` (`12.0 pt`) and must not inherit caption size.
- Every figure and table must be cited in the body.
- Treat the figure block as one unit: lead-in sentence, picture paragraph, caption paragraph, and follow-up analysis paragraph should stay contiguous and readable.
- The paragraph that contains the inserted figure must use `1.5` line spacing.
- Check and normalize the spacing before and after the figure block so the figure is not visually stuck to the body text or split awkwardly.
- Tables should be compatible with the compliant template's no-left/right-outer-border style.
- If a table spans pages, repeat the table header and append `（续）` to the table number on the continued page.
- If the repository template or script uses a custom table style such as `论文格式`, keep it compatible with this no-left/right-outer-border presentation instead of forcing a generic full-grid style.

### Figure/table cross-references

- Clickable figure/table cross-references are recommended enhancements for final `.docx` delivery, not the default baseline compliance threshold.
- Do not mark a thesis non-compliant only because figure/table references remain plain text, unless the user explicitly requires clickable figure/table jumping in the final manuscript.
- When figure/table cross-references are built, keep them on the body-text baseline and at body-text size `小四` (`12.0 pt`).

## 9. Code and diagrams

- Do not paste long code blocks into the body.
- If code must be shown, use code screenshots with a white background only.
- Flowcharts must have arrows.
- ER diagram relationship lines must not have arrows.

## 10. Reference citations and cross-references

- Clickable body-to-reference Word cross-references are part of the compliant-template baseline for final `.docx` delivery.
- Prefer Word cross-references over plain-text citation numbers in the final `.docx`.
- Body citations should point to the matching bibliography item so `Ctrl + 点击` jumps to the reference entry.
- Reference items should be bookmarkable as `gzcu_ref_n` in order of the final bibliography list.
- Build or refresh clickable reference cross-references only in the main body.
- Do not insert reference cross-references into the abstract, any `本章小结`, or the conclusion.
- If the working draft still contains plain-text citation numbers, convert them during final Word processing rather than leaving them as-is.
- Bibliography cross-references must remain superscript after all field refreshes.

## 11. Word implementation checklist

When producing a final DOCX plan or editing a Word file, verify:

- sections match the 4-part template-compatible model,
- abstract section shows Roman numerals starting from `I`,
- TOC is in its own section and shows no visible headers or page numbers,
- main body starts Arabic page numbering from Chapter 1,
- `结论`、`参考文献`、`致谢` continue Arabic numbering without restart,
- even/odd headers are enabled only in the main-body section,
- even-page header is `广州城市理工学院本科毕业设计（论文）`,
- odd-page header follows the current level-1 heading through `STYLEREF`,
- TOC is generated by Word and includes 3 heading levels,
- each chapter starts on an odd page,
- required blank transition pages exist where needed,
- heading styles stay compatible with the compliant template,
- figures, tables, and captions use the required placement and numbering,
- body citations are Word cross-references when final clickable reference jumping is required,
- bibliography cross-references still display as superscript after updates,
- figure/table cross-references are only required when the user explicitly wants clickable figure/table jumping,
- any figure/table cross-references still display at body-text size `小四` (`12.0 pt`),
- inserted picture paragraphs use `1.5` line spacing,
- figure blocks have normalized before/after spacing.
