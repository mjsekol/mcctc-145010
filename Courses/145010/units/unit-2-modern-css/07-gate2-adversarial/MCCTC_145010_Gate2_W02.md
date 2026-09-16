# Gate 2: Adversarial Review · Week 2
## 145010 Web Design & Senior Capstone · Week 2, Friday

**40 minutes.** Individual and silent. You may and should open the page, use DevTools, and run both
checkers. You may not ask an AI tool whether the page is correct, because an AI tool is what is being
reviewed.

The page is `gate2-w02-files/index.html` with its stylesheet `gate2-w02-files/css/fair.css`. Copy
the whole `gate2-w02-files/` folder and work on your copy.

---

## What you are looking at

The Pine Ridge Teen Makers Fair is invented. A volunteer handed an AI assistant the requirements in
Part A and got this page back. It looks finished on a laptop. Your job is to find what is wrong
before it goes live.

**Five defects, one in each category:** Correctness, Security, Readability, Performance,
Requirements Fit.

**One of the five is genuinely arguable.** For that one, your reasoning is scored, not only whether
you called it a defect.

**About the floor map.** The iframe's `src` is a local file, `embeds/venue-map.html`. It stands in
for the venue's real map page, which would live on the venue's own site. Treat the page inside the
frame as a page somebody else controls.

---

## PART A: The requirements

> Build one event page for the Pine Ridge Teen Makers Fair. It must:
>
> 1. Use one external stylesheet and no inline styles.
> 2. Work on a phone, a tablet, and a laptop. We will check it at 360, 768, and 1280 pixels wide,
>    and nothing may scroll sideways.
> 3. Show the fair logo at the top, next to the welcome text.
> 4. Show the three workshops as cards that lift slightly when you point at them or tab into them.
> 5. List the exhibitors in two columns on wide screens and one column on phones.
> 6. Embed the venue's floor map from the venue's map page, with a title. It is a map. It shows
>    where the tables are.
> 7. Lay out the page with grid or flexbox. **No floats. No tables for layout.** A table for real
>    data, like the schedule, is fine.
> 8. Mobile first, and commented so the next volunteer can maintain it.

---

## PART B: What the AI produced

The files are in `gate2-w02-files/`:

```
gate2-w02-files/
  index.html
  css/fair.css
  media/fair-logo.png
  embeds/venue-map.html
```

Open `index.html` in Chrome at a normal laptop width first. **Read it against the eight
requirements before you read any code.** Then narrow the window.

From the root of the course repository, the two checkers are:

```
node tools/web-check/check.js <your copy>/index.html --widths 360,768,1280
python Courses/145010/units/unit-1-semantic-html/05-labs/structure-check/structure_check.py <your copy>/index.html
```

**The checkers find some of the five. They do not find all of them.** Several of the defects in this
page pass both tools cleanly.

---

## What to submit

One entry per defect, five entries:

| Field | What to write |
|---|---|
| **File and line** | `index.html` line 40, or `css/fair.css` line 12 |
| **Dimension** | Correctness, Security, Readability, Performance, or Requirements Fit |
| **What goes wrong for a real person** | A family on a phone, the next volunteer, a visitor to the fair. Name who and what. |
| **The fix** | The changed line or rule, written out |

Then one final entry: **what I was unsure about.** Name something specific in this page that you
could not decide was a defect, and say what would settle it. **This entry is scored, and a blank
costs more than a wrong guess.**

### How to spend 40 minutes

- **First 5:** read the page at laptop width against Part A, one requirement at a time.
- **Next 10:** run both checkers. Then set DevTools to 360 and 768 and look.
- **Next 10:** read `fair.css` top to bottom. Read every comment and ask whether the code under it
  does what the comment says.
- **Next 10:** read every attribute on every element in `index.html` that loads something from
  somewhere else. Ask what it lets that thing do.
- **Last 5:** write the unsure entry.

---

## Scoring

Five defects, one point each, plus one point for the unsure entry. Your instructor states the
security weighting before you start.

**Four of five is a strong score.**
