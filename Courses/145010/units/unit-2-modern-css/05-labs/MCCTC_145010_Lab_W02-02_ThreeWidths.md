# Lab W02-02 · Three Widths
## 145010 Web Design & Senior Capstone · Week 2, Wednesday (Part 1) and Thursday (Part 2)

**Competencies:** 6.5.8 (format website layout for targeted platforms, including tables and
lists), 6.5.13 (integrate responsive design), 6.2.4 (wrap text around an image, now only where it
fits)

**Grade category:** Lab & Practice. Part 1 is due at the end of Wednesday. Part 2 is due at the end
of Thursday.

---

## The situation

The Eastgate Esports Club page you styled on Monday and Tuesday now looks like the club, and it is
still one long column on every screen. The officers want the sign-up box beside the bracket on a
laptop, the team cards in a grid, and a qualifier standings table that a player can read on a
phone at the station. The club is invented, and so are the teams and their results.

**What you will build:** a responsive layout for the bracket page with grid and flexbox, a media
query, a container query, and a table that scrolls in its own box, checked at 360, 768, and 1280
pixels.

---

## Before you start

You work on your own `eastgate/` folder from Lab W02-01.

**If your Lab W02-01 page does not pass `web-check`,** tell your instructor at the start of Build 1.
After Lab W02-01 is graded, your instructor can give you a copy of a finished Lab W02-01 page to
start from. Say so in the first line of `observations.md`.

Read the Wednesday notes, `03-lecture-notes/MCCTC_145010_Notes_FlexboxAndGrid.md`, and before
Part 2 the Thursday notes, `03-lecture-notes/MCCTC_145010_Notes_MediaAndContainerQueries.md`.

**Rules for this lab:** no `float` for layout, no table for layout, no fixed pixel widths on
anything that holds text. The photo float from Tuesday is allowed, because it wraps text around an
image.

---

## The starter

| File | What it is |
|---|---|
| `lab-w02-02-files/standings-section.txt` | A new section for your page: the qualifier standings table, seven columns wide. It is plain HTML. Paste it in at step 1. |
| your `eastgate/` folder | Everything else |

Put all your layout rules in a new block at the bottom of `styles/site.css`, under a comment that
says `Part 3: layout`.

---

## Part 1 · Wednesday · Grid for the page, flexbox for the line

**Step 1.** Open `standings-section.txt`. Copy everything below the dashed line into `index.html`,
inside `<main>`, directly above `<section id="teams">`. Run `web-check`.

*Observable result:* `FAIL`, with `OVERFLOWS by` a number at 360 and nothing at 768 or 1280. On the
reference page the number was 86. Write yours in `observations.md`. The table is too wide for a
phone. You fix it on Thursday.

If the command itself errors instead of printing `PASS` or `FAIL`, follow
[the web-check README](../../../../../tools/web-check/README.md) before you go on.

**Step 2.** Make `body` a grid. Give it `grid-template-areas` with four rows, `"header"`, `"main"`,
`"aside"`, `"footer"`, a column gap, a `max-width` of about 72rem, and `margin: 0 auto`. Give the
header, `main`, `aside`, and footer each a `grid-area`.

*Observable result:* the page looks almost the same, one column. In DevTools Elements, a `grid`
badge appears next to `<body>`. Click it. The overlay shows your four named areas.

**Step 3.** Give `main` `min-width: 0`, and write a comment above it saying what it prevents. You
test that comment on Thursday.

*Observable result:* nothing changes yet.

**Step 4.** Make the header a flex row that wraps, with the club name and the nav spread apart.
Make the nav's `ul` a flex row that wraps, with a gap, no bullets, no margin, and no padding.

*Observable result:* the nav links sit in a row. Narrow the window to about 360 pixels in DevTools'
device toolbar. The links wrap onto a second line and nothing scrolls sideways.

**Step 5.** Make `.team-list` a grid with
`grid-template-columns: repeat(auto-fit, minmax(min(15rem, 100%), 1fr))`, a gap, no bullets, no
margin, and no padding. Give `.team-card` a border, rounded corners, padding, and `height: 100%`.

*Observable result:* at 1280 the cards form a grid. On the reference page, before Thursday's query,
that was four columns of 276 pixels. At 768 it was two columns. At 360 it was one.

**Step 6.** Give the `aside` a light background, padding, and rounded corners, and
`align-self: start`.

**Step 7.** Run both checkers, write down what `web-check` said, and commit.

*Observable result:* `structure_check` reports `0 fail`. `web-check` still fails only at 360, with
the same overflow as step 1. That is the table, and it is expected until Thursday.

---

## Part 2 · Thursday · Ask the screen, ask the box

**Step 8.** Add a media query, `@media (min-width: 60em)`, that gives `body` two columns,
`3fr minmax(15rem, 1fr)`, and redraws the areas so the aside sits beside `main`.

*Observable result:* at 1280, the aside is beside the main content at the top of the page. At 768
it is still below. Drag the device toolbar width across 960 pixels and watch it move.

**Step 9.** Move the photo float into a query. Change Tuesday's `.photo` rule so it only sets a
bottom margin. Add `@media (min-width: 40em)` that floats `.photo` right at 45% with its margins.

*Observable result:* at 360 the photo sits above the club night text at full column width. At 768
and 1280 the text wraps beside it.

**Step 10.** Wrap the standings table in a scroll box. Put a `<section>` around the `<table>` with
`class="table-scroll"`, `tabindex="0"`, and `aria-labelledby` pointing at an `id` you add to the
table's `<caption>`. In CSS, give `.table-scroll` `overflow-x: auto`, give it a visible
`:focus-visible` outline, and give the standings cells `white-space: nowrap`.

*Observable result:* `web-check` passes at 360. At 360 the table scrolls sideways inside its own box
and the page does not. Press Tab until the box is focused, then press the right arrow key. The
table scrolls.

**Step 11.** Break it on purpose. Delete `min-width: 0` from `main`, run `web-check`, write the
result in `observations.md`, and put it back.

*Observable result:* `OVERFLOWS by` a number at 360. On the reference page it was 199. The table was
inside a scroll box and the page still overflowed, because `main` grew to fit the table. That is
the sentence your step 3 comment should say.

**Step 12.** Add a container query. Give `.team-list > li` `container-type: inline-size`. Add
`@container (min-width: 22rem)` that turns `.team-card` into a two-column grid, `5rem 1fr`, with
the seed spanning two rows.

*Observable result:* on the reference page, at 768 the seed sits beside the team name. At 360 and
at 1280 the cards are stacked. Measure the card slots in DevTools at each width and write down why.

**Step 13.** Prove the base works without it. Comment out the whole `@container` block, run
`web-check` at all three widths, then restore it.

*Observable result:* `PASS` with the block commented out. Your cards are stacked everywhere, and
nothing breaks. That is the point: a browser without container queries still gets a working page.

**Step 14.** Take the screenshots.

```
node tools/web-check/check.js <your path>/eastgate/index.html --widths 360,768,1280 --shots <your path>/eastgate/screenshots
```

*Observable result:* `PASS`, and three files: `index-360.png`, `index-768.png`, `index-1280.png`.
**Open every one and look at it.** A pass does not tell you the page looks right.

**Step 15.** Write `observations.md`: one paragraph per width saying what the layout does there and
which rule is responsible, plus your step 1 and step 11 numbers. Commit.

---

## Acceptance criteria

1. The page layout is a grid with named areas. The nav and header are flex rows that wrap. The team
   list is an auto-fit grid.
2. No `float` except the photo, and the photo only floats at 40em and wider. No table for layout.
   No fixed pixel width on anything that holds text.
3. One `min-width` media query changes the page from one column to two.
4. The container query changes the card layout, and the page passes `web-check` with it removed.
5. The standings table scrolls inside a named, focusable box at 360, and the page never scrolls
   sideways.
6. `web-check` passes at 360, 768, and 1280, and `structure_check` reports zero FAIL lines.
7. `screenshots/` holds three screenshots from your final run.
8. `observations.md` has a paragraph per width, the step 1 number, and the step 11 number.

---

## If it breaks

Layout bugs almost never produce an error. These are the likeliest, with what you actually see.

**`OVERFLOWS by 199px` at 360 after step 10 (your number may differ).** `main` has no `min-width: 0`,
so the grid column grew to the table's width. A grid item will not shrink below its content unless
you tell it to.

**`OVERFLOWS by 8px` at 360 after step 5 (or some small number).** Your card minimum is wider than
the list. On the build machine, `minmax(22rem, 1fr)` with no `min()` overflowed by 8 pixels at 360.
Wrap the minimum in `min(..., 100%)`.

**The container query never changes anything.** No ancestor has `container-type`. The `@container`
rule has nothing to ask, so it never applies. On a test page the card stayed `display: block` at
1280 until `container-type: inline-size` went on the list item.

**A card or list item shrinks to nothing.** `container-type: inline-size` stops a box from sizing
itself from its content. On the build machine, an item with it inside a plain flex row with no
width measured 0 pixels wide. In a grid track, as in this lab, it is fine.

**The aside never moves beside `main`.** Check the query in the Styles pane at 1280. If the rule is
listed and not struck through, check that your area names in the query match the `grid-area`
names exactly. A typo in an area name makes the whole `grid-template-areas` declaration invalid, and
the browser drops it.

---

## Stretch goal

At 1280 the aside is shorter than `main` and leaves empty space below it. Make it stay on screen
while `main` scrolls, without JavaScript, and explain in `observations.md` what happens at 360 and
why.

---

## Submission checklist

- [ ] `eastgate/index.html` with the standings section wrapped in a named, focusable scroll box
- [ ] `eastgate/styles/site.css` with a Part 3 block: grid areas, flex header and nav, card grid,
      one media query for the page, one for the photo, one container query
- [ ] `eastgate/screenshots/` with three screenshots from the final run, each one looked at
- [ ] `eastgate/observations.md` with a paragraph per width and the step 1 and step 11 numbers
- [ ] `web-check` passes at 360, 768, and 1280
- [ ] `structure_check` reports zero FAIL lines
- [ ] Committed and pushed at the end of Wednesday and again at the end of Thursday

---

## Extended options

Choose one, or your instructor will hand you one. All four are graded on the same scale and
assess the same competencies.

### Three observable signals for choosing

| What you see in the first 20 minutes of Wednesday | Give them |
|---|---|
| Lab W02-01 does not pass yet, or the grid badge never appears at step 2 | SCAFFOLDED |
| Grid overlay open and reading the area names without being asked | STANDARD or EXTENDED |
| Asks how to make the columns line up across different cards | EXTENDED |
| Asks when anyone would use a container query outside a school page | APPLIED |

### SCAFFOLDED

Same page, same targets, fewer moving parts. Skip the container query (steps 12 and 13) and the
break-it step (step 11). Your instructor gives you the area picture to copy:

```css
grid-template-areas:
  "header"
  "main"
  "aside"
  "footer";
```

You still write the media query that redraws it, the card grid, and the scroll box.
**Extra checkpoints:** show your instructor after step 2, step 5, and step 10.

### STANDARD

The lab as written.

### EXTENDED

Everything in STANDARD, plus **cards whose insides line up.** Right now each card sizes its own
rows, so a card with a long captain line has its text start lower than its neighbor. Make the seed,
the name, and the captain line sit on shared rows across every card in the same grid row.

Then write in `observations.md` what happens to your container query when you do this, and why.

*Hint, not the answer:* MDN's page on `subgrid` explains how a grid item can use its parent's
tracks. Chrome 153 on the build machine reports support for it. Check support in the other browsers
you care about before you depend on it.

### APPLIED

Same skills, a different domain. Build a one-page dashboard for something you track: a fantasy
league, a practice log, a savings goal for a car, a reading list. It needs a page grid with at least
three named areas, a flex row, a card component that uses a container query with a working base,
and a data table with at least six columns that scrolls in its own box on a phone. Invented data
only.

Then answer in `observations.md`: where would this dashboard's cards appear at two different sizes
on the same screen, and why is a container query the right tool for that and a media query not.

All four options are graded with the same rubric as STANDARD.
