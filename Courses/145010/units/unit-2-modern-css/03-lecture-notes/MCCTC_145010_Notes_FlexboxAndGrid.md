# Lecture Notes: Flexbox and Grid
## 145010 Web Design & Senior Capstone · Week 2 · Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W02_FlexboxAndGrid.md) · no exported deck yet. Generate it from the repository root with `node tools/gamma.js Courses/145010/units/unit-2-modern-css/04-slides/MCCTC_145010_Slides_W02_FlexboxAndGrid.md --export pptx`

If you missed class, you can learn this concept from this file alone. The pages used below are
in [examples/wed-layout/](examples/wed-layout/).

**Competency:** 6.5.8 (format website layout for targeted platforms).

---

## Why this exists

For a long time, web pages were laid out with tools that were never meant for it:
tables, then floats. Both "worked", and both broke in ways that took hours to find. Flexbox and
grid were added to CSS specifically for layout. Every current browser supports both, and this
course uses nothing else for page layout.

You have done layout before. In WPF a `StackPanel` arranges children in a line and a `Grid`
arranges them in rows and columns, and the **container** decides where the children go. The same
idea runs the web.

**Today's rule: layout is the parent's job. Flexbox arranges a line. Grid arranges a plane.**

---

## The concept in plain language

**`display: flex` on a parent** lines its children up in one direction, a row by default.

- `gap` puts space between them. No margins to fight.
- `flex-wrap: wrap` lets them move to a new line when they run out of room.
- `flex: 1` on a child says "take a share of the leftover space". `flex: 2` takes two shares.
- Good for: a nav bar, a row of buttons, a label next to a value, a header with a logo and links.

**`display: grid` on a parent** puts its children into rows and columns at the same time.

- `grid-template-columns: 2fr 1fr` makes two columns, the first twice as wide.
- `grid-template-areas` lets you draw the page with names, then place children with
  `grid-area`.
- `repeat(auto-fit, minmax(12rem, 1fr))` means "as many columns as fit, each at least 12rem".
- Good for: the whole page, a card gallery, a form with labels in one column.

**How to choose:** if you care about one direction, use flex. If you care about rows **and**
columns lining up, use grid. Pages usually use both: grid for the page, flex inside the header.

**Two tools you do not use for layout this week:**

- **Floats.** Tuesday's photo float wraps text around an image. That is what float is for.
  Floating whole columns is not.
- **Tables.** A `<table>` is for data with rows and columns that mean something. Using one to
  put a sidebar beside content is a layout table.

---

## Worked example 1: a line with flexbox

```css
.row { display: flex; width: 600px; }
.a   { flex: 1; }
.b   { flex: 2; }
.c   { width: 150px; flex: none; }
```

Measured on the build machine:

```
.a  150px
.b  300px
.c  150px
```

`.c` takes its fixed 150 and refuses to grow or shrink. That leaves 450. `.a` gets one share and
`.b` gets two, so 150 and 300.

The nav in [examples/wed-layout/index.html](examples/wed-layout/index.html) is the everyday
version:

```css
.site-header ul {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1.5rem;
  margin: 0;
  padding: 0;
  list-style: none;
}
```

---

## Worked example 2: a page with grid areas

```css
.page {
  display: grid;
  grid-template-columns: 2fr 1fr;
  grid-template-areas:
    "head head"
    "main side"
    "foot foot";
  gap: 1rem;
  max-width: 60rem;
  margin: 0 auto;
  padding: 1rem;
}

.site-header { grid-area: head; }
main         { grid-area: main; }
aside        { grid-area: side; }
footer       { grid-area: foot; }
```

The area names are a picture of the page. Change the picture and the page changes, with no
change to the HTML.

Measured on the build machine:

```
width 1280:  columns 629.328px 314.656px
width 768:   columns 480px 240px
width 360:   columns 170.25px 141.75px
```

At 1280 and 768 the columns are exactly 2 to 1. At 360 they are not, because the sidebar's
padding plus its longest word need more than a third of 312 pixels, and grid gives it the
minimum it needs.
The page still fits, and it is cramped. **Tomorrow's media query is the fix for that.**

---

## Worked example 3: cards that fill the space

```css
.booths {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(12rem, 100%), 1fr));
  gap: 1rem;
}
```

Measured on the build machine inside the page above:

```
width 1280:  3 columns of 199.109px
width 768:   2 columns of 232px
width 360:   1 column  of 170.25px
```

No media query. Grid counts how many 12rem (192px) columns fit, makes that many, then shares the
leftover. `min(12rem, 100%)` means a column is never wider than the list itself, which matters
when the list is narrower than 12rem.

A second measurement, from a test page with `minmax(200px, 1fr)`, 20px gaps, and 20px of
padding, with no `min()`:

```
width 360:   1 column  of 320px
width 700:   3 columns of 206.672px
width 1280:  5 columns of 216px
```

---

## The wrong version, and exactly what goes wrong

[examples/wed-layout/float-layout.html](examples/wed-layout/float-layout.html) builds two columns
with floats:

```css
.columns  { border: 3px solid #1d4ed8; background-color: #dbeafe; }
.col-main { float: left; width: 65%; }
.col-side { float: right; width: 30%; }
footer    { background-color: #fde68a; }
```

Measured at 1280 on the build machine:

```
.columns  height 0px   (its two borders make a 6px blue line)
footer    top 94px     (it starts under the header, behind the floated columns)
```

A float is taken out of the normal flow, so the parent does not count it. The blue box collapses
to a line, its background disappears, and the yellow footer slides up underneath both columns,
with its text squeezed beside them. None of that is an error.

`web-check` on the build machine:

```
PASS  .../wed-layout/float-layout.html
  validation: 0 error(s), 0 warning(s)
  axe at 360px: 0 violation(s)
  axe at 768px: 0 violation(s)
  axe at 1280px: 0 violation(s)
```

It passes. The checker validates markup and accessibility rules. It does not look at whether the
footer is where you meant it.

[examples/wed-layout/table-layout.html](examples/wed-layout/table-layout.html) builds the same two
columns with `<table role="presentation">`:

```
web-check:        PASS, 0 validation errors, 0 axe violations at all three widths
structure_check:  WARN TABLES line 17: table marked role="presentation".
                  A table used for layout. Use grid or flexbox
```

`role="presentation"` tells assistive technology to ignore the table's rows and columns, which is
why axe does not complain. The table still cannot reflow: two cells stay side by side on every
screen, and making them stack means fighting the table model. Note one more thing from the build
machine: the first draft of this demo put `<tr>` straight inside `<table>`, and html-validate
reported `prefer-tbody  Prefer to wrap <tr> elements in <tbody>`.

**The grid fix** is [examples/wed-layout/index.html](examples/wed-layout/index.html). The parent
gets `display: grid`, and the collapsing, the footer, and the table all go away.

---

## Why the wrong version is tempting

Old tutorials, old forum answers, and a lot of AI output still reach for floats and tables,
because there is a mountain of that older material and much of it still shows up first. A float
layout also **looks** right for the first ten minutes, as long as the columns are the tallest
thing on the page and nothing comes after them.

The layout table is tempting because it is the one layout you already know from Week 1. It lines
things up, and it passes the checker. Ask what happens on a phone.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Flex container** | The parent with `display: flex`. Its children are flex items. |
| **Main axis** | The direction flex items line up in. A row unless you change it. |
| **`flex: 1`** | Grow to take one share of the leftover space |
| **`flex-wrap`** | Let flex items move to a new line |
| **Grid container** | The parent with `display: grid` |
| **`fr`** | A fraction of the leftover space in a grid |
| **`grid-template-areas`** | A named picture of the grid |
| **`auto-fit` and `minmax()`** | As many columns as fit, each with a minimum and a maximum |
| **`gap`** | Space between items, in flex or grid |
| **Normal flow** | How boxes stack when nothing changes their layout |
| **Layout table** | A table used to position content instead of presenting data |

---

## Self-check

**Question 1.** `.row { display: flex; width: 600px; }` has three children: `.a { flex: 1; }`,
`.b { flex: 2; }`, and `.c { width: 150px; flex: none; }`. How wide is `.b`?

**Question 2.** A card list uses `repeat(auto-fit, minmax(200px, 1fr))` with a 20px gap. The list
is 660 pixels wide and has five cards. How many columns are there, and how wide is each?

**Question 3.** A page built with floats passes `web-check` at all three widths. Your teammate
says that proves the layout is fine. Give the strongest reply.

---

### Answers

**1.** 300 pixels. `.c` keeps 150, leaving 450. `.a` takes one share and `.b` two, so 150 and
300. Verified on the build machine.

**2.** Three columns, each about 206.67 pixels. Four columns need 4 x 200 + 3 x 20 = 860, which
does not fit. Three need 640, which does, and the leftover 20 is shared. Verified on the build
machine: `206.656px 206.672px 206.672px` for a 660-pixel list, which is a 700-pixel viewport
minus 20px of padding on each side. The two cards that do not fit in the first row wrap to a second row.

**3.** `web-check` checks validity, accessibility rules, and sideways overflow. It does not check
whether a parent collapsed or whether the footer slid under the columns. The float demo passes
with a 0-pixel-tall container. Look at the page, and use grid.
