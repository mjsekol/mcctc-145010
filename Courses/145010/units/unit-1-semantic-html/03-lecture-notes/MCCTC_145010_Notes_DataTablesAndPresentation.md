# Lecture Notes: Data Tables, and Choosing How to Present Data
## 145010 Web Design & Senior Capstone · Unit 1 · Week 1 · Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W01_DataTables.md)
· no exported deck yet. Generate it from the repository root with
`node tools/gamma.js Courses/145010/units/unit-1-semantic-html/04-slides/MCCTC_145010_Slides_W01_DataTables.md --export pptx`

If you missed class, you can learn this concept from this file alone. You need Chrome with the
Accessibility tab, and both checkers.

**Competencies:** 6.1.6 (create and format a table with HTML table tags and attributes) and 2.7.2
(ways to present data: responsive web, mobile apps, desktop apps, web apps).

---

## Why this exists

A sighted person reads a schedule by glancing up to the column header and left to the row header.
A screen reader user cannot glance. They move cell by cell, and the only way they know that
"Theo" means the front desk at 6:30 is if the table tells the screen reader which headers belong
to that cell.

A table that only **looks** like it has headers tells it nothing. Chrome does not even treat it as
a data table.

The second half of the day asks a bigger version of the same question: this data has to reach real
people. Should it be a page, an app, or an application?

---

## The concept in plain language

A **data table** has two axes. Every cell sits where a row and a column meet, and both have
headers.

| Element | Job |
|---|---|
| `caption` | Names the table. First thing inside `table`. |
| `thead`, `tbody`, `tfoot` | Group the header rows, the body rows, and summary rows |
| `th scope="col"` | A header for the cells below it |
| `th scope="row"` | A header for the cells to its right |
| `td` | A data cell |

**Never use a table for layout.** Page layout is CSS's job, and next week you do it with grid and
flexbox. A table used to position things tells assistive technology that unrelated content is
related.

**Presenting data.** The same data can reach people four ways:

| Way | Good for | Costs |
|---|---|---|
| Responsive web page | Anyone with a link and a browser, reading | Cheap. Someone edits it by hand. |
| Mobile app | Frequent users who will install it, notifications | Two phone platforms, store accounts, updates |
| Desktop application | One person at one computer, heavy work | Useless away from that computer |
| Web application | People who log in and change shared data | A server, accounts, and the data to protect |

Ask three questions: **who** needs it, **where** are they, and do they **read** it or **change**
it.

---

## Worked example 1: what Chrome thinks your table is

```html
<!-- every cell a td -->
<table>
  <tr><td>Route</td><td>Leaves</td><td>Last stop</td></tr>
  <tr><td>12</td><td>3:05 p.m.</td><td>Oak Street</td></tr>
</table>
```

```html
<!-- a data table -->
<table>
  <caption>Buses leaving the east loop after school</caption>
  <thead>
    <tr><th scope="col">Route</th><th scope="col">Leaves</th><th scope="col">Last stop</th></tr>
  </thead>
  <tbody>
    <tr><th scope="row">12</th><td>3:05 p.m.</td><td>Oak Street</td></tr>
  </tbody>
</table>
```

Chrome's accessibility tree for each, captured on the build machine:

```
first table                        second table
LayoutTable                        table "Buses leaving the east loop after school"
  LayoutTableRow                     caption
    LayoutTableCell "Route"          rowgroup
    LayoutTableCell "Leaves"           row
    LayoutTableCell "Last stop"          columnheader "Route"
  LayoutTableRow                         columnheader "Leaves"
    LayoutTableCell "12"                 columnheader "Last stop"
    ...                              row
                                       rowheader "12"
                                       cell "3:05 p.m."
```

The first one is `LayoutTable`. Chrome decided it was for layout. The second is a `table` with
column headers and row headers.

---

## Worked example 2: both axes, and a summary row

```html
<table>
  <caption>Who is working each station, by shift start time</caption>
  <thead>
    <tr>
      <th scope="col">Station</th>
      <th scope="col">5:30 p.m.</th>
      <th scope="col">6:30 p.m.</th>
      <th scope="col">7:30 p.m.</th>
    </tr>
  </thead>
  <tbody>
    <tr><th scope="row">Front desk</th><td>Marisol</td><td>Theo</td><td>Theo</td></tr>
    <tr><th scope="row">Tire and tube bench</th><td>Priya</td><td>Jonah</td><td>Open</td></tr>
  </tbody>
  <tfoot>
    <tr><th scope="row">Open spots</th><td>0</td><td>1</td><td>1</td></tr>
  </tfoot>
</table>
```

The caption names both axes, so a listener knows how to read the grid before hearing one cell.
"Open spots" sits in `tfoot` because it summarizes the columns. In `tbody` it would read as a
station called Open spots. At 360 px wide this table fits without sideways scrolling, with the
longer station names wrapped.

---

## Worked example 3: what the validator checks, and what it does not

`web-check` enforces the structure. Each message below was produced by breaking a correct table
on purpose:

```
line 7:25  wcag/h63  <th> element must have a valid scope attribute: row, col, rowgroup or colgroup
line 7:25  attribute-allowed-values  Attribute "scope" has invalid value "column"
line 8:4   element-permitted-order  Element <caption> must be used before <tbody> in this context
```

**The validator requires a `scope` on every `th`.** A table that only uses the `id` and `headers`
technique for complex headers fails until each `th` has a `scope` too.

**What no checker catches.** A two-night table whose `headers` attributes pointed at the wrong
night, with every `th` scoped, passed both `web-check` and `structure_check`. Only a person
reading the Accessibility tab, or listening with a screen reader, finds that.

---

## Worked example 4: choosing a presentation

**Situation.** Youth league referees, most of them 15, need their game assignments. They want to
trade games with each other.

- A **responsive page** lets every referee read the assignments. Nobody can trade.
- A **mobile app** could send reminders. Few 15-year-olds install an app for six Saturdays.
- A **desktop application** helps whoever makes the assignments. It does nothing at the field.
- A **web application** lets referees log in and trade. It needs accounts, and it stores
  information about minors that the league must protect.

**A defensible recommendation:** the responsive page now, because reading is the need this
season. A web application if trading becomes the real problem, and only with a plan for
protecting the referees' information.

You have built two of these already, both in 145065: a web application, your Flask CRUD app, and
a desktop application, the WPF operator panel.

---

## The wrong version, and what it produces

```html
<table width="100%">
  <tr>
    <td width="30%"><b>Harbor Lane Bike Kitchen</b><br>Tuesdays</td>
    <td>
      <table>
        <tr><td><b>Station</b></td><td><b>5:30</b></td></tr>
        <tr><td>Front desk</td><td>Marisol</td></tr>
      </table>
    </td>
  </tr>
</table>
```

A table to lay out the page, and a data table faked with bold. From the Lab W01-02 starter,
`web-check` reports:

```
no-deprecated-attr  Attribute "width" is deprecated on <table> element
prefer-tbody  Prefer to wrap <tr> elements in <tbody>
no-deprecated-attr  Attribute "width" is deprecated on <td> element
prefer-tbody  Prefer to wrap <tr> elements in <tbody>
```

and `structure_check` reports, twice:

```
table has no <th> header cells. A data table needs them, and a layout table should not exist
```

Chrome's accessibility tree calls both tables `LayoutTable`. Axe reported zero violations.

### Write this down

> A table is for data with two axes. If nothing in it is a header, it is not a data table.

---

## Why the wrong version is tempting

Before CSS could lay out a page, tables were how people put things side by side, and plenty of old
pages and old tutorials still do it. Bold text in the first row looks exactly like a header row.
And the automated audit said nothing. It all looks finished to the person who built it.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Data table** | A table whose cells relate to row and column headers |
| **Layout table** | A table used to position content. Do not build one. |
| **`caption`** | The table's name |
| **`th` / `td`** | Header cell, data cell |
| **`scope`** | Which way a header applies: `col`, `row`, `colgroup`, `rowgroup` |
| **`thead` / `tbody` / `tfoot`** | Header rows, body rows, summary rows |
| **Responsive web page** | One page that adapts to the screen it is viewed on |
| **Web application** | A site where users log in and change data |

---

## Self-check

**Question 1.** A table's first row uses `<td><b>...</b></td>`. It passes the automated audit. What
does Chrome's accessibility tree call it, and what does that cost a screen reader user?

**Question 2.** Why does "Open spots" belong in `tfoot` and not `thead`?

**Question 3.** A food pantry wants volunteers to see the week's shifts, and the coordinator wants
to stop editing the page by hand every time someone swaps. Recommend a way to present the data, and
name one cost.

---

### Answers

**1.** `LayoutTable`. The screen reader is not told it is in a data table, so it cannot announce
which header goes with a cell. The user hears the values in reading order with no station and no
time attached.

**2.** It does not name the columns. It summarizes them. `thead` holds rows that describe the
columns, and `tfoot` holds rows that total or summarize them.

**3.** A web application, where volunteers log in and swap shifts themselves, so the coordinator
stops hand editing. Costs: a server to keep running, accounts to manage, and volunteers' personal
information to protect. A defensible alternative is a responsive page now with a web application
later, if the coordinator can live with hand editing for a season.
