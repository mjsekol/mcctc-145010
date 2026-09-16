# Lecture Notes: Landmarks, Headings, and Lists
## 145010 Web Design & Senior Capstone · Unit 1 · Week 1 · Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W01_LandmarksHeadingsAndLists.md)
· no exported deck yet. Generate it from the repository root with
`node tools/gamma.js Courses/145010/units/unit-1-semantic-html/04-slides/MCCTC_145010_Slides_W01_LandmarksHeadingsAndLists.md --export pptx`

If you missed class, you can learn this concept from this file alone. You need Chrome, both
checkers, and the Accessibility tab in DevTools.

**Competencies:** 6.1.3 (format content with HTML formatting tags) and 6.1.5 (ordered and
unordered lists).

---

## Why this exists

A sighted person reads a page by looking at it: big bold text is a heading, a row of links at the
top is a menu, dots down the left are a list. A person using a screen reader cannot look. They
move through the page by **structure**: jump to the main content, list the headings, jump to the
next one, hear "list, 4 items."

That structure only exists if the markup says so. CSS can make a `div` look like a heading. It
cannot make it one. This week's deliverable forbids generic containers where a real element
exists, and this is why.

---

## The concept in plain language

Pick the element for **what the content is**, not how it should look.

**Landmarks** divide the page into regions a screen reader can jump between:

| Element | Chrome exposes it as | Use it for |
|---|---|---|
| `header` | `banner` | The site name and top matter |
| `nav` | `navigation` | A group of links for getting around |
| `main` | `main` | The page's own content. Exactly one. |
| `footer` | `contentinfo` | Small print at the bottom |
| `section` with a name | `region` | A thematic group with a heading |

**Headings** are an outline. One `h1` says what this page is about. `h2` for its main sections,
`h3` inside those. Going down, you may skip back any number of levels. Going deeper, you add one
level at a time.

**Lists.** `ul` when order does not matter, `ol` when it does. Only `li` goes directly inside
either one. `ol` does the numbering, so never type the numbers yourself.

**Emphasis.** `strong` means important. `em` means stressed. `b` and `i` only change the look.

---

## Worked example 1: two pages that look the same

```html
<!-- div soup -->
<div class="top">
  <div class="title">Open Gym Nights</div>
</div>
<div class="content">
  <div class="heading">When</div>
  <div>Monday and Wednesday, 7 to 9 p.m.</div>
  <div class="heading">Bring</div>
  <div>- Court shoes</div>
  <div>- Your student ID</div>
</div>
```

```html
<!-- semantic -->
<header>
  <p>Riverside Rec Center</p>
</header>
<main>
  <h1>Open Gym Nights</h1>
  <h2>When</h2>
  <p>Monday and Wednesday, 7 to 9 p.m.</p>
  <h2>Bring</h2>
  <ul>
    <li>Court shoes</li>
    <li>Your student ID</li>
  </ul>
</main>
```

`web-check` passes **both**. The accessibility trees Chrome built are nothing alike:

```
div soup                              semantic
StaticText "Open Gym Nights"          banner
StaticText "When"                       StaticText "Riverside Rec Center"
StaticText "Monday and ..."           main
StaticText "Bring"                      heading "Open Gym Nights" level 1
StaticText "- Court shoes"              heading "When" level 2
StaticText "- Your student ID"          StaticText "Monday and ..."
                                        heading "Bring" level 2
                                        list
                                          listitem "Court shoes"
                                          listitem "Your student ID"
```

On the left, a screen reader user gets six lines of text and nothing to jump to.

---

## Worked example 2: reading an outline

```html
<h1>Esports Club</h1>          <!-- line 9 -->
<h2>Teams</h2>
<h3>Rocket League</h3>
<h2>Tryouts</h2>
<h4>What to bring</h4>         <!-- line 13 -->
<h3>Schedule</h3>
```

`structure_check` prints the outline indented by level, then the problem:

```
line    9  h1  Esports Club
line   10    h2  Teams
line   11      h3  Rocket League
line   12    h2  Tryouts
line   13        h4  What to bring
line   14      h3  Schedule
FAIL HEADINGS  line 13: h2 jumps to h4, skipping h3 ('What to bring')
```

Line 14 is fine: stepping back up from `h4` to `h3` is allowed. Line 13 is not: `h2` to `h4` skips
a level, so a listener hears Tryouts and then a sub-sub-section with nothing between.

---

## Worked example 3: lists that count for you

```html
<ol start="3">
  <li>Clutch save</li>
  <li>Double kill</li>
  <li>Buzzer beater</li>
</ol>
<ol reversed>
  <li>Bronze</li>
  <li>Silver</li>
  <li>Gold</li>
</ol>
```

Chrome shows `3.`, `4.`, `5.` on the first list and `3.`, `2.`, `1.` on the second. Read from its
accessibility tree, which lists each item's marker. The numbers belong to the list, so moving an
item renumbers everything. Type `1.` into the text and you get `1. 1. Clutch save` on screen.

---

## Worked example 4: `section` becomes a region only with a name

```html
<section id="donate" aria-labelledby="donate-heading">
  <h2 id="donate-heading">Donate a Bike</h2>
  ...
</section>
```

With `aria-labelledby`, Chrome's accessibility tree shows `region "Donate a Bike"`. The same
`section` without it shows only the heading, with no region around it. Both are valid. The named
one gives a screen reader user one more thing to jump to.

---

## The wrong version, and what it produces

```html
<h1>Teen Game Night</h1>
<!-- h4 keeps the section titles small -->
<h4>Schedule</h4>
<h4>What to bring</h4>
```

It looks tidy. `web-check` reports nothing. `structure_check` reports:

```
FAIL HEADINGS  line 3: h1 jumps to h4, skipping h2 ('Schedule')
```

The heading level was chosen for its size. Size is CSS, and that is next week.

**The fix.** `h2` for both, and delete the comment, which now says something false.

### Write this down

> A heading level is a position in an outline. It is not a font size.

---

## Why the wrong version is tempting

Browsers give each heading level a default size, so the levels look like a size menu. The
unstyled `h1` and `h2` are large, and it is natural to reach for `h4` when you want something
smaller. And a `div` with a class name reads perfectly well to you, because you wrote the class
name. The page makes sense to its author, the checker passes, and the only person who finds out
is someone who cannot see it.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Semantic element** | An element whose name says what its content is |
| **Landmark** | A region a screen reader can jump to: banner, navigation, main, contentinfo, region |
| **Accessibility tree** | The browser's model of the page for assistive technology |
| **Heading outline** | The headings in order, indented by level |
| **Div soup** | A page built from generic `div` elements where real elements exist |
| **`ul` / `ol` / `li`** | Unordered list, ordered list, list item |
| **`strong` / `em`** | Importance, and stress |

---

## Self-check

**Question 1.** A classmate's page passes `web-check` with zero violations at every width. It has
no headings, only `div class="title"`. What is still wrong, and which tool shows it?

**Question 2.** Is `h2`, `h3`, `h2`, `h4` a correct outline? Name the line that is wrong.

**Question 3.** Steps to register for a tournament must be done in order. A student types
`1.`, `2.`, `3.` at the start of each `li` inside a `ul`. What is wrong, and what does the page
show if someone later changes the `ul` to an `ol`?

---

### Answers

**1.** The page has no heading structure a screen reader can use. `structure_check` reports
`no headings at all`, and the Accessibility tab shows the titles as plain text. `web-check`
passes it because nothing is invalid and its audit does not require headings to exist.

**2.** No. The `h4` is wrong: it follows an `h2`, so it skips `h3`. (It also starts at `h2`
instead of `h1`, which `structure_check` reports as `the first heading is h2, expected h1`.)

**3.** The order is carried by typed text, not by the markup, so the list is announced as an
unordered list. Changed to `ol`, the page shows `1. 1.`, `2. 2.`, and `3. 3.`, because the list
numbers its items and the typed numbers are still in the text. Use `ol` and delete the typed
numbers.
