# Gate 2: Adversarial Review · Week 1
## 145010 Web Design & Senior Capstone · Week 1, Friday

**40 minutes.** Individual. Silent. You may and should open the page, read its source, and run
both checkers on it. You may not ask a model whether it is correct, because a model is what is
being reviewed. **Grade category:** Written & Documentation.

The page is `gate2-w01-files/game-night.html`, with its `images/` and `files/` folders. Copy the
whole `gate2-w01-files/` folder and work on your copy.

**The community center, the event, and every name here are invented.**

---

## What you are looking at

A community center's program coordinator pasted the requirements in Part A, along with the
staff's setup notes, into an AI assistant and asked for the event page. The assistant produced
`game-night.html`. It is tidy, it is commented, it uses landmarks, and it looks fine in a
browser. Your job is to find what is wrong with it.

**Five defects, one in each category:** Correctness, Security, Readability, Performance,
Requirements Fit.

**Only one of the five is reported by `web-check`.** The other four pass every automated check
this course has given you, or need you to look somewhere a checker does not.

---

## PART A: The requirements

> Build `game-night.html`, the public page for Teen Game Night at the Hollis Street Community
> Center. It must:
>
> 1. Use `header`, `nav`, `main`, and `footer`, with one `h1` and headings that form a correct
>    outline.
> 2. Open with a jump menu that links to each section: Schedule, What to bring, and Sign up.
> 3. Show the event banner at the top in a 320 by 160 pixel space. Guests open this page on the
>    center's guest Wi-Fi, usually on a phone, so keep it light.
> 4. Give every image a text alternative that says what the image shows.
> 5. Link to the downloadable permission slip, which is a PDF.
> 6. Give families a way to email the teen program with questions.
> 7. This page is public. Staff-only information stays off it.

---

## PART B: What the AI produced

`gate2-w01-files/`:

```
game-night.html
images/
  game-night-banner.jpg
  maple-room-map.png
files/
  permission-slip.pdf
```

Open `game-night.html` in Chrome. Then, from the repository root:

```
node tools/web-check/check.js <your copy>/game-night.html
python Courses/145010/units/unit-1-semantic-html/05-labs/structure-check/structure_check.py <your copy>/game-night.html
```

**Read the page against the seven requirements before you read the source.** Then read the
source, all of it, including the parts a browser does not show.

---

## What to submit

For each defect: **the line number**, **the dimension**, **what goes wrong for a real person**,
and **the fix**. Name the person. "A guest on a phone" or "a screen reader user" is a person.
"The user" is not.

Then two more entries:

- **What I was unsure about.** Name something specific on the page you could not decide was a
  defect, and say why. This entry is scored, and a blank costs more than a wrong guess.
- **The email link.** Requirement 6 is met. Is the way it is met a problem? Give the strongest
  case on each side, then decide.

### How to spend 40 minutes

- **First 5:** open the page. Use the jump menu. Every link.
- **Next 5:** run both checkers. Write down what each one reports.
- **Next 10:** read Part A one requirement at a time and point at the line that meets it.
- **Next 10:** View Source, Ctrl+U. Read every line, including every comment.
- **Rest:** check everything the page loads, not only what it shows. DevTools, the Network
  panel, lists each file the page asked for.

---

## Scoring

Five defects, one point each, plus one point for the unsure-about entry and one for the email
link entry. Your instructor states the security weighting before you start.

**Four of five is a strong score.**
