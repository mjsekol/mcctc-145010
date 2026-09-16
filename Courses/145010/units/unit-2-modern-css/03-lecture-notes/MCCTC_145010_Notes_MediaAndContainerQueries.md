# Lecture Notes: Media Queries and Container Queries
## 145010 Web Design & Senior Capstone · Week 2 · Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W02_ResponsiveQueries.md) · no exported deck yet. Generate it from the repository root with `node tools/gamma.js Courses/145010/units/unit-2-modern-css/04-slides/MCCTC_145010_Slides_W02_ResponsiveQueries.md --export pptx`

If you missed class, you can learn this concept from this file alone. The pages used below are
in [examples/thu-queries/](examples/thu-queries/).

**Competencies:** 6.5.13 (integrate responsive design), 6.5.8 (format layout, including tables,
for targeted platforms).

---

## Why this exists

Yesterday's grid page fit a phone, and it was cramped: two skinny columns at 360 pixels. The fix
is not a second website for phones. It is one set of HTML with CSS that **asks a question** and
changes the layout based on the answer.

There are two questions you can ask, and they are different questions.

**A media query asks about the screen. A container query asks about the box.**

---

## The concept in plain language

**Mobile first.** Write the base styles for a phone: one column, everything stacked. Then add
`min-width` media queries that add columns when there is room. A browser that ignores every
query still gets a working phone layout.

```css
.page { display: grid; grid-template-areas: "head" "main" "side" "foot"; }

@media (min-width: 48em) {
  .page {
    grid-template-columns: 2fr 1fr;
    grid-template-areas: "head head" "main side" "foot foot";
  }
}
```

`48em` is 768 pixels at the default text size, and `min-width` includes the number itself, so
the rule applies at 768 and up. Using `em` means the breakpoint moves if someone sets a larger
default font.

**A container query** lets a component change based on the width of the box it sits in. You
mark the box as a container, then ask about it:

```css
.booths > li { container-type: inline-size; }

@container (min-width: 20rem) {
  .booth { display: grid; grid-template-columns: 5rem 1fr; }
}
```

The same card can be wide in a phone's single column and narrow in a laptop's three-column grid.
A media query cannot tell those apart. A container query can.

**Container queries are newer.** On the build machine, Chrome 153 reported support for
`container-type: inline-size`, `cqi` units, `:has()`, `clamp()`, `aspect-ratio`, `subgrid`, and
`gap`, and applied an `@container (min-width: 500px)` rule inside a 700-pixel container and not
inside a 300-pixel one. Support in Firefox, Safari, and older versions of Chrome was not tested
here **[VERIFY]**. So treat a container query as an **enhancement**: the base card, with no
query, must already work.

**The viewport meta tag** makes a phone lay the page out at the phone's own width:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Without it, a phone browser pretends to be about 980 pixels wide and shrinks the result. Your
media queries then never see a narrow screen.

**A wide data table** scrolls sideways inside its own box, so the page does not:

```html
<section class="table-scroll" aria-labelledby="times-caption" tabindex="0">
  <table>
    <caption id="times-caption">Club meeting times, spring</caption>
    ...
  </table>
</section>
```

```css
.table-scroll { overflow-x: auto; }
```

The section gets its name from the caption, and `tabindex="0"` lets a keyboard user focus it and
scroll it with the arrow keys.

---

## Worked example 1: one page, three widths

[examples/thu-queries/index.html](examples/thu-queries/index.html), measured on the build machine:

| Width | Page columns | Booth cards | Card layout (container query) | Table box, content / visible |
|---|---|---|---|---|
| 360 | 328px, one column | 1 column, 328px | applies: `80px 196px` | 599 / 328, scrolls |
| 768 | 480px 240px | 1 column, 480px | applies: `80px 348px` | 599 / 480, scrolls |
| 1280 | 629.328px 314.656px | 2 columns, 307px | does not apply, stacked | 629 / 629, fits |

Read the card column. **The laptop shows the stacked card, and the phone shows the side-by-side
card.** On the laptop, the booth list has two columns, so each card slot is 307 pixels, which is
under 20rem (320 pixels). On the phone the single slot is 328 pixels. The container query saw the
box, not the screen, and got it right both times.

The page itself never scrolled sideways at any width. `web-check` reported
`0 violation(s)` and no overflow at 360, 768, and 1280.

---

## Worked example 2: the region really has a name

Chrome's accessibility tree for the page, read on the build machine:

```
regions: [{"role":"region","name":"Club meeting times, spring"}]
```

A screen reader user tabbing into the scroll box hears what it is.

A detail from building this demo: the first version used
`<div class="table-scroll" role="region" ...>`. html-validate rejected it with
`prefer-native-element  Prefer to use the native <section> element`. A `section` with a name is a
region already, so the fix was to use the element.

---

## Worked example 3: the viewport tag, on an emulated phone

`web-check` does not emulate a phone, so it passes a page with no viewport tag. To see the real
effect, a headless Chrome on the build machine emulated a 360-pixel mobile device
(`isMobile: true`) and loaded the demo with and without the tag:

```
with the tag:     innerWidth 360   scale 1        page columns 328px
without the tag:  innerWidth 980   scale 0.367    page columns 621.328px 310.656px
```

Without the tag, the phone laid the page out as if it were 980 pixels wide. The two-column
desktop layout appeared, shrunk to about a third of its size, with text too small to read.
[examples/thu-queries/no-viewport.html](examples/thu-queries/no-viewport.html) is that page.

---

## The wrong version, and exactly what goes wrong

[examples/thu-queries/fixed-width.html](examples/thu-queries/fixed-width.html) is desktop first,
with fixed pixel widths:

```css
.page { width: 960px; margin: 0 auto; display: grid;
        grid-template-columns: 640px 300px; gap: 20px; }
```

`web-check` on the build machine:

```
FAIL  .../thu-queries/fixed-width.html
  validation: 0 error(s), 0 warning(s)
  axe at 360px: 0 violation(s), OVERFLOWS by 600px
  axe at 768px: 0 violation(s), OVERFLOWS by 192px
  axe at 1280px: 0 violation(s)
```

960 minus 360 is 600. 960 minus 768 is 192. The fix is not a `max-width` query that patches the
phone. It is a fluid base (no fixed widths, one column) plus a `min-width` query that adds the
second column, which is the index page above.

### Three quieter failures, all measured

**The grid column that will not shrink.** A grid item's default minimum width is its content.
On the Eastgate lab page, removing `min-width: 0` from `main` let the wide standings table push
the column to 543 pixels, and `web-check` reported `OVERFLOWS by 199px` at 360, even though the
table sat inside a scroll box.

**The container query that never fires.** Write `@container (min-width: 20rem)` and forget
`container-type` on any ancestor, and the rule never applies. On a test page, the card stayed
`display: block` at 1280. Adding `container-type: inline-size` to the list item made it `grid`.

**The container that collapses.** `container-type: inline-size` means the box no longer sizes
itself from its content. Put it on an item inside a plain `display: flex` row with no width, and
on the build machine that item measured **0 pixels wide**. In a grid track, or with a width, it
is fine.

---

## Why the wrong version is tempting

You design on a laptop, so the laptop layout feels like the real one and the phone feels like an
exception to patch with `max-width` queries. Every patch then has to undo something the base
did, and the rules fight. Mobile first flips it: the phone layout is the simple one, and each
query only adds.

Fixed pixel widths are tempting because they match the design mockup exactly, at exactly one
width.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Responsive design** | One page whose layout adapts to the space it has |
| **Media query** | `@media (...)`: CSS that applies only when the viewport matches |
| **Breakpoint** | A width where the layout changes |
| **Mobile first** | Base styles for phones, `min-width` queries for larger screens |
| **Viewport** | The visible area the page is laid out in |
| **Viewport meta tag** | Tells a phone to lay out at its real width |
| **Container query** | `@container (...)`: CSS that applies when a container box matches |
| **`container-type: inline-size`** | Marks a box as a container that can be asked about its width |
| **Progressive enhancement** | A base that works everywhere, with extras where supported |
| **Scroll container** | A box with `overflow: auto` that scrolls its own content |
| **`min-width: 0`** | Lets a grid or flex item shrink below its content's width |

---

## Self-check

**Question 1.** A page has `@media (min-width: 48em) { .page { grid-template-columns: 2fr 1fr; } }`
and a base of one column. How many columns at 767 pixels and at 768 pixels?

**Question 2.** On a laptop, a card shows its stacked layout. On a phone, the same card shows its
side-by-side layout. Your teammate says the CSS is backwards. Explain why it might be exactly
right.

**Question 3.** A page passes `web-check` at 360. On a real phone it looks like a tiny desktop
site. What is missing, and why did `web-check` not catch it?

---

### Answers

**1.** One column at 767 and two at 768. `min-width` includes the value, and 48em is 768 pixels
at the default text size. Verified on the build machine: `767px` at 767, and
`501.328px 250.672px` at 768 on a test page with a 1rem gap.

**2.** A container query asks about the card's box, not the screen. On the laptop the cards sit in
a multi-column grid, so each box is narrow. On the phone there is one column, so each box is
wide. The build machine measured 307-pixel slots at 1280 and 328-pixel slots at 360, with the
query set at 320.

**3.** The viewport meta tag. Without it a phone lays the page out at about 980 pixels and
shrinks it. `web-check` sets a 360-pixel window on a desktop browser without mobile emulation,
so the tag makes no difference there.
