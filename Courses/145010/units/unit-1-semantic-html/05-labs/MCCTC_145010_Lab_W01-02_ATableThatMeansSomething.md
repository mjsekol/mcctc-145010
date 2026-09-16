# Lab W01-02: A Table That Means Something
## 145010 Web Design & Senior Capstone · Week 1 · Thursday

**Gate:** 3 (open). **Duration:** Build 1, 40 minutes. **Grade category:** Lab & Practice.
**Competencies:** 6.1.6, 2.7.2, with 6.1.3 and 6.2.1 carried from Lab W01-01.

Files: [lab-w01-02-files/shifts.html](lab-w01-02-files/shifts.html). You also need your
finished Lab W01-01 folder.

---

## The scenario

Harbor Lane Bike Kitchen posts its Repair Night volunteer shifts on a page that a volunteer
built with two tables: one to hold the page together, one to hold the schedule. On a laptop it
looks tidy. Chrome's accessibility tree calls both of them layout tables, which means a screen
reader user gets a pile of names with no way to tell which station or which hour each one
belongs to. **The organization and every volunteer name are invented.**

## What you will build

The shifts page rebuilt with no layout table and one data table whose every cell can be read
with its row and column headers, linked into the site you built this week.

---

## The starter

`shifts.html` has an outer table that lays out the page: a narrow left cell with the site name
and a link, and a wide right cell with everything else. Inside the right cell is the shift
table. Its first row and first column are made to look like headers with `<b>`. They are not
headers.

---

## Steps

1. **Copy `shifts.html` into your `lab-w01-01/` folder**, next to `index.html`, and commit it
   untouched.
   *You see:* `git log --oneline` shows the new commit.

2. **Run `web-check` on it.**
   *You see:* `FAIL`, `validation: 4 error(s)`: `width` is deprecated on `<table>` and on
   `<td>`, and two `prefer-tbody` errors. Zero axe violations at every width.

3. **Run `structure_check` on it.**
   *You see:* `FAIL`, `5 fail, 3 warn`, including two lines that say
   `table has no <th> header cells`.

4. **Look at what Chrome thinks the tables are.** DevTools, Elements, then the Accessibility
   pane. Select the inner table.
   *You see:* its role is `LayoutTable`, not `table`. So is the outer one. Write down, in
   `notes.md`, what that means for someone who cannot see the grid.

5. **Remove the layout table.** Replace the outer `table`, `tr`, and both `td` elements with a
   `header` for the site name, the Repair Night line, and the link, and a `main` for everything
   else. Delete both `width` attributes with them.
   *You see:* `web-check` no longer reports `width` errors. The page is now one column.

6. **Give the page its heading.** "Repair Night volunteer shifts" becomes the `h1`. Put the
   "Back to home" link in a `nav` with a list, like your other pages.
   *You see:* `structure_check` shows `h1  Repair Night volunteer shifts` and landmarks.

7. **Make the first row a header row.** Put it in a `thead`. Change its four cells to `th`
   with `scope="col"`, and delete the `<b>` tags. Write the times as `5:30 p.m.` so a person
   hearing a column name knows it is evening.
   *You see:* the header row is bold and centered without any `<b>`. That is the browser's
   default style for `th`.

8. **Make the first column a header column.** In each station row, change the first cell to
   `th scope="row"`.
   *You see:* the station names are bold.

9. **Group the rows.** Wrap the three station rows in `tbody`. The "Open spots" row is a
   summary of the columns above it: put it in `tfoot`, with its first cell as
   `th scope="row"`.
   *You see:* `web-check` reports `validation: 0 error(s)`.

10. **Add a caption** as the first thing inside `table`. Say what the table is, including what
    the columns are.
    *You see:* the caption appears centered above the table.

11. **Change `OPEN` to `Open`.** Capitals read as shouting.
    *You see:* nothing else changes.

12. **Link it into the site.** Point "Back to home" at `index.html`. Add a "Volunteer shifts"
    item to the menu on `index.html` and on `pages/volunteer.html`. From `pages/`, the path is
    `../shifts.html`.
    *You see:* `structure_check` on all three pages reports no FILES or ANCHORS failures.

13. **Check the accessibility tree again.** Select the table.
    *You see:* role `table` with the caption as its name, `columnheader` cells, and
    `rowheader` cells. Select the cell that says Jonah and read what the pane says about it.

14. **Check it at phone width.** Run
    `node tools/web-check/check.js <your path>/lab-w01-01/shifts.html --shots <your path>/lab-w01-01/evidence/shots`
    and open the 360 px screenshot.
    *You see:* `PASS` at all three widths, and at 360 px the table fits, with the longest
    station name and the times wrapped onto two lines. No sideways scrolling.

15. **Write `presentation.md`.** Four short paragraphs. The shift lead wants volunteers to see
    this schedule. For each of these, say who it would serve and what it would cost a volunteer
    shop: this responsive web page, a mobile app, a desktop application on the shop computer,
    and a web application where volunteers log in and claim open shifts. End with which one you
    would build first and why.
    *You see:* a file you could hand to the shift lead.

16. **Run both checkers on all three pages, save the output to `evidence/`, and commit.**
    *You see:* six PASS lines. `git commit -am "Lab W01-02: a table that means something"`.

---

## Acceptance criteria

- [ ] No `table` is used for layout anywhere in the site
- [ ] The shift table has a `caption`, a `thead`, a `tbody`, and a `tfoot`
- [ ] Every header cell is a `th` with the right `scope`
- [ ] `web-check` PASS on all three pages at 360, 768, 1280
- [ ] `structure_check` PASS on all three pages
- [ ] `notes.md` says what a layout table means for a screen reader user
- [ ] `presentation.md` covers all four options with a real cost for each

---

## If it breaks

**1. `prefer-tbody  Prefer to wrap <tr> elements in <tbody>`.** You have rows sitting directly
inside `table`. The browser adds a `tbody` for you, which you can see in Elements, but the
validator wants it in the file. Wrap the rows.

**2. `element-permitted-order  Element <caption> must be used before <thead> in this
context`.** The `caption` must be the first child of `table`. Move it up.

**3. `no-implicit-close  Element <th> is implicitly closed by sibling` and
`close-order  Stray end tag '</td>'`.** You changed `td` to `th` in the opening tag and not the
closing tag. The page still looks right, because the browser closed the `th` for you when the
next cell started. The validator reports the file as written. If you changed only the closing
tag instead, you also get `Attribute "scope" is deprecated on <td> element`.

**4. `structure_check` says `shifts.html points at a file that is not there` on the volunteer
page.** From `pages/volunteer.html`, `shifts.html` means `pages/shifts.html`. You want
`../shifts.html`.

---

## Stretch goal

A screen reader reading the Jonah cell can announce its row and column headers because of
`scope`. Some tables are too complex for `scope`: a cell under two levels of column headers,
for instance. Find the other way HTML connects a data cell to its headers, and add it to the
shift table. Keep `scope` as well: `web-check` reports
`wcag/h63  <th> element must have a valid scope attribute` on any `th` without one. Then
write two sentences on which technique does the work for this table and why.

---

## Submission checklist

- [ ] `shifts.html` in `lab-w01-01/`, linked from both other pages
- [ ] `notes.md` has the layout table paragraph
- [ ] `presentation.md` with four options and a recommendation
- [ ] `evidence/` has the final output of both checkers and the three screenshots
- [ ] Committed and pushed

---

## Extended options

Choose one with your instructor. All four assess 6.1.6 and 2.7.2 and are graded on the same
scale.

### Three observable signals for choosing

| What you see in the first 10 minutes | Give them |
|---|---|
| Lab W01-01 is not finished, or the student is unsure what `thead` is for | SCAFFOLDED |
| Step 5 done and the student is reading the Accessibility tab | STANDARD |
| Step 10 done before minute 20 | EXTENDED |
| The student asks why anyone uses tables when spreadsheets exist | APPLIED |

### SCAFFOLDED

Your instructor gives you a skeleton with the `table`, `caption`, `thead`, `tbody`, and `tfoot`
tags already in place and empty. You move the rows into it and change the header cells.
Skip step 12 if Lab W01-01 is not finished; link the page back to `index.html` only.

**Extra checkpoints:** after step 5 and after step 9.

**Then answer in writing:** the starter looked like a table with headers. What, exactly, made
the headers not headers?

### STANDARD

The lab as written.

### EXTENDED

Everything in STANDARD, plus **two levels of column headers.** Repair Night is adding a second
night. Rebuild the table so the top header row says "Tuesday" and "Thursday", each spanning its
three shift times, and the row below it has the six times. A screen reader on any cell should
be able to name the station, the night, and the time.

*Hint, not the answer:* `scope` alone is not enough for this shape. Read the W3C WAI tables
tutorial, the page on tables with multi-level headers, at
`https://www.w3.org/WAI/tutorials/tables/multi-level/`, and pick the technique it recommends. Keep a
`scope` on every `th`, because `web-check` requires one. Verify with the Accessibility
pane, not by looking: a table with wrong header references still passes both checkers.

### APPLIED

Same skill, your own data. Pick a real schedule from your own life that has two axes: your
work shifts across a week, a team's practice times by day and location, or a game's raid
rotation by night and role. **Invent the names. No real person's schedule goes on a page.**

Build it as a data table with a caption, both kinds of header cell, and a summary row in
`tfoot`. Then write `presentation.md` for your own data, comparing the same four options for
the people who would actually use it.
