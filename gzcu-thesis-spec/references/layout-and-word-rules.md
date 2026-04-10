# Layout and Word Rules

Use this file when the task involves Word layout, final DOCX preparation, or format review.

## 1. Activation boundary

- The cover page and the second explanation page are fixed school template pages.
- Do not change their fonts, sizes, spacing, headers, footers, or page numbers.
- Apply the following layout rules starting from the Chinese abstract page.

## 2. Headers

### Where headers appear

- Show headers in the body, conclusion, references, and acknowledgements.
- Hide headers on the cover page, explanation page, Chinese abstract, English abstract, and TOC.

### How headers are controlled

- Use Word section breaks, not one global header for the entire document.
- Keep header line thickness at `1.5 磅`.

### Header text

- Body even-page header: `广州城市理工学院本科毕业设计（论文）`
- Body odd-page header: current chapter title
- Conclusion header: `结 论`
- References header: `参考文献`
- Acknowledgements header: `致 谢`

## 3. Page numbers

- Chinese and English abstracts use Roman numerals.
- The body, conclusion, references, and acknowledgements use Arabic numerals.
- The body starts a new page-numbering scheme from Chapter 1.
- References and acknowledgements continue the Arabic numbering and do not restart.
- Hide page numbers on the cover page, explanation page, and TOC.

## 4. Chapter opening rules

- Every chapter starts on a new page.
- Every chapter must start on an odd-numbered page.
- If the next chapter would start on an even-numbered page, insert a blank transition page before it.
- Apply the same odd-page rule to `结论`, `参考文献`, and `致谢`.

## 5. Fonts, sizes, spacing

### Global font principle

- All English and all numbers use `Times New Roman`.

### Headings

- Level 1 chapter title: `三号` Songti or Heiti, bold, centered, with one blank line above and below.
- Level 2 heading: `小三号` Songti, bold, left aligned, with one blank line above and below.
- Level 3 heading: `四号` Songti, bold, left aligned, with no extra blank line.

### Body text

- `小四号` Songti
- fixed line spacing `20 磅`
- first-line indent of `2` Chinese characters

### References and acknowledgements

- title: `三号` Songti, bold, centered, with one blank line above and below
- body text: `五号` Songti
- fixed line spacing `20 磅`

## 6. Widow/orphan and heading placement

- Do not allow any heading to appear as the last line on a page.
- Adjust page breaks or pagination to keep headings with following content.

## 7. Figures and tables

- Figure titles go below the figure.
- Table titles go above the table.
- Figure titles, table titles, and table text use `宋体五号`.
- Number figures and tables by chapter, such as `图1-1` and `表1-1`.
- Body references to figures and tables keep body formatting, not caption formatting. In practice, `图X-X` and `表X-X` inside正文 must stay at `小四` (`12.0` pt) rather than inheriting the caption's `五号`.
- Prefer Word cross-references for figure references in the body so `Ctrl + 点击` jumps to the matching figure caption.
- If the manuscript is delivered as `.docx`, figure references such as `如图X-X所示` should be implemented as clickable cross-references rather than left as plain text where feasible.
- Prefer Word cross-references for table references in the body so `Ctrl + 点击` jumps to the matching table caption.
- If the manuscript is delivered as `.docx`, table references such as `如表X-X所示` or `见表X-X` should be implemented as clickable cross-references rather than left as plain text where feasible.
- Treat the figure block as one unit: lead-in sentence, picture paragraph, caption paragraph, and follow-up analysis paragraph should stay contiguous and readable.
- The paragraph that contains the inserted figure must use `1.5` line spacing.
- Check and normalize the spacing before and after the figure block so the figure is not visually stuck to the body text or split awkwardly.
- Tables must not have vertical border lines on the left and right sides.
- If a table spans pages, repeat the table header and append `（续）` to the table number on the continued page.

## 8. Code and diagrams

- Do not paste long code blocks into the body.
- If code must be shown, use code screenshots with a white background only.
- Flowcharts must have arrows.
- ER diagram relationship lines must not have arrows.

## 9. Reference citations and cross-references

- Prefer Word cross-references over plain-text citation numbers in the final `.docx`.
- Body citations should point to the matching bibliography item so `Ctrl + 点击` jumps to the reference entry.
- Build or refresh clickable cross-references only in the main body. Do not insert them into the abstract, any `本章小结`, or the conclusion.
- If the working draft still contains plain-text citation numbers, convert them during final Word processing rather than leaving them as-is.
- Bibliography cross-references must remain superscript after all field refreshes.
- Figure and table cross-references stay in normal body baseline and must not be formatted as superscript.
- Figure and table cross-references must display at body-text size `小四` (`12.0` pt) instead of inheriting figure/table caption size.

## 10. Word implementation checklist

When producing a final DOCX plan or editing a Word file, verify:

- sections are split correctly,
- abstract and TOC have no visible headers,
- Roman and Arabic page-number schemes are separated correctly,
- TOC is generated by Word and includes 3 heading levels,
- each chapter starts on an odd page,
- required blank transition pages exist where needed,
- references and acknowledgements continue Arabic page numbering,
- heading styles do not drift from the required font and size rules,
- figures, tables, and captions use the required placement and fonts,
- figure references in the body are cross-references when the final Word deliverable requires clickable jumping,
- table references in the body are cross-references when the final Word deliverable requires clickable jumping,
- figure and table cross-references in the body still display at body-text size `小四` (`12.0` pt),
- inserted picture paragraphs use `1.5` line spacing,
- figure blocks have normalized before/after spacing,
- body citations are Word cross-references when clickable jumping is required,
- bibliography cross-references still display as superscript after figure/table cross-reference updates.
