# Project · The League Goes Mobile
## 145010 Web Design & Senior Capstone · Week 2 · Modern CSS & Responsive Layout

**100 points. Projects category, 35 percent of your grade.**
**Due Week 2, Friday, at the end of the 14-minute commit window.**

**Competencies:** 6.1.7, 6.2.4, 6.2.5, 6.2.6, 6.2.7, 6.5.7, 6.5.8, 6.5.13.

---

## The brief

> From: Dana, volunteer coordinator, Cedar Hollow Youth Rec League
>
> The page is working. Parents found the rain policy on their own last Saturday, which has never
> happened before. Thank you.
>
> Now the problems. I watched two of our coaches try to use it at the field. They were squinting and
> dragging the schedule back and forth with a thumb. The schedule is the whole reason they open it,
> and on a phone it is cramped. When I open it on the laptop at home it looks like a plain document,
> and honestly it does not look like us. We are green and white. Our jerseys are green and white. Can
> it look like the league? One of our board members is color blind, so please do not make anything
> depend on telling two greens apart.
>
> The list of links at the top is long. On my laptop I would like it across the top in a row. On a
> phone, do whatever works, as long as nobody has to scroll sideways to find "When it rains".
>
> I am attaching a photo from opening day. I would love the welcome text to sit next to it on a big
> screen, like a newsletter. On a phone that probably will not fit, and that is fine.
>
> A parent recorded a short highlight clip of the season opener and a family asked if we could add
> captions, because their son is hard of hearing. Please do that. They were very kind about asking.
>
> The park district sent a snippet to put their field map on our page. I attached a copy of what it
> shows. I would like it under the directions.
>
> On the laptop, the forms section and the contact section could sit side by side. They are both
> short and there is a lot of empty space.
>
> I do not know what any of this involves. Tell me if something I asked for is a bad idea.

**The league is invented.** So are Dana, the park, the photo, the clip, and the map. Everything Dana
attached is in [project-files/](project-files/). The brief is a composite of the kind of follow-up a
volunteer client sends after a first version works.

**That is the whole brief.** It does not list breakpoints, colors, or selectors. It asks for some
things in words that are not CSS words. **Turning it into requirements is the first thing you are
graded on.**

Your instructor plays Dana again. You may ask up to two written questions by the end of Monday's
Build 2.

---

## What you are building

Your own Week 1 season page, now with **one external stylesheet** that makes it look like the league,
a **responsive layout built with grid and flexbox**, the opening-day photo, the captioned highlight
clip, and the embedded field map, **verified at 360, 768, and 1280 pixels**. Plus a decision log that
records your float decision and your breakpoints.

**Start from your own Week 1 page.** Your structure is the foundation for everything this week.

**If your Week 1 page does not pass both checkers,** Monday's Build 2 is for fixing that first. If it
still does not pass by the end of Monday, tell your instructor. After Week 1 grades are entered, your
instructor may give you a finished Week 1 page to build on. If that happens, your decision log's first
entry says so.

---

## What Dana attached

| File | What it is |
|---|---|
| `project-files/opening-day.jpg` | The opening-day photo, 1600 by 1067, about 168 KB |
| `project-files/season-opener.webm` and `.mp4` | The season opener highlight, about 9 seconds, narrated, the same clip in two formats |
| `project-files/season-opener.vtt` | Captions for the clip, three timed lines |
| `project-files/season-opener-poster.jpg` | A still frame to show before the clip plays |
| `project-files/field-map.html` | A local page that **stands in for the park district's map embed**. A real site would paste the district's snippet. This one needs no account and no network. |

The photo, clip, and map were generated for this course. The narration is a computer voice.

---

## Technical requirements

Every one of these exists for a reason, and the reason is next to it.

| # | Requirement | Why |
|---|---|---|
| R1 | One external stylesheet, linked from **both** pages. No `<style>` blocks. No inline styles. | One place to change the league's look. Week 2 Monday. |
| R2 | League green and white, with every text color at 4.5:1 or better against its background, each ratio written in a comment. No meaning carried by color alone. | A board member is color blind, and the WCAG AA minimum is 4.5:1 for body text. |
| R3 | Links change on hover **and** on keyboard focus, the same way, with a visible focus outline. | Some visitors never touch a mouse. |
| R4 | Mobile first. Base styles are the phone layout. Every media query uses `min-width`. | Coaches read it on phones. The phone layout should be the simple one. |
| R5 | The page layout uses grid, the nav uses flexbox, and **no float or table is used for layout**. | Floats and layout tables break in ways no checker reports. Week 2 Wednesday. |
| R6 | The nav is one row on a laptop and wraps on a phone. Nothing scrolls sideways at any width. | Dana asked, and "When it rains" has to be reachable in one thumb. |
| R7 | The schedule table scrolls sideways inside its own named, keyboard-focusable box on a phone. The page itself never does. | The schedule is why coaches open the page. |
| R8 | The opening-day photo has real alt text, never gets wider than its column, keeps its shape, and has text wrapping beside it **only** at widths where that fits. | Dana asked for the newsletter look on big screens and accepted that phones differ. |
| R9 | The highlight clip has controls, both sources, a captions track that is on by default, and fallback content with a download link. | A family asked for captions. Captions are not optional for a narrated clip. |
| R10 | The field map is an iframe with a `title`, sized with `aspect-ratio`, and with **no `allow` attribute**. | A map needs nothing from the visitor's device. Grant nothing it does not need. |
| R11 | Forms and contact sit side by side on a laptop and stack on a phone. | Dana asked. |
| R12 | `web-check` passes both pages at 360, 768, and 1280. `structure_check` reports zero FAIL lines on both. | The checkers catch what you stopped seeing. |
| R13 | Three screenshots of the home page from your final run, committed. | A PASS does not tell you the page looks right. You have to look. |
| R14 | A decision log with the entries listed below. | Dana asked you to tell her when something is a bad idea. |
| R15 | Every period ends with a commit. | Version control is a daily ritual, not a unit. |

### The two checkers, and the screenshots

From the root of the course repository:

```
node tools/web-check/check.js <your-folder>/index.html <your-folder>/pages/code-of-conduct.html --widths 360,768,1280 --shots <your-folder>/screenshots
python Courses/145010/units/unit-1-semantic-html/05-labs/structure-check/structure_check.py <your-folder>/index.html <your-folder>/pages/code-of-conduct.html
```

**Know what they cannot see.** `web-check` passed a page this week with a collapsed float layout, a
layout table, a narrated video with no captions, a stylesheet that never loaded, and no viewport tag.
Each of those is in this week's lecture notes. **Captions only show when you serve the folder:** run
`python -m http.server 8000` inside your folder, open `http://127.0.0.1:8000/`, and stop the server
with Ctrl+C when you are done.

---

## Constraints, and why each one exists

| Constraint | Why |
|---|---|
| No framework, no CSS library, no JavaScript | The Ohio standards for this course are vanilla CSS, and every line on the page should be one you can explain. |
| No AI tool writes your stylesheet | Gate 3 work allows tools, but this is the week the cascade has to live in your head. You may use an AI tool to explain an error message, and you log it in the decision log. |
| Only Dana's attached media, and media you made yourself without people's faces | The families did not agree to be on a class project. |
| Only `.example` addresses | No real inbox should receive anything from a class project. |
| No commercial embed, account, or key | The map stand-in exists so nobody needs one. |

---

## Required repository structure

```
league-season-page/
  index.html
  pages/
    code-of-conduct.html
  files/
    cedar-hollow-medical-release.pdf
  css/
    league.css             the only stylesheet
  media/
    opening-day.jpg
    season-opener.webm
    season-opener.mp4
    season-opener.vtt
    season-opener-poster.jpg
  embeds/
    field-map.html
  screenshots/
    index-360.png          from your final web-check --shots run
    index-768.png
    index-1280.png
  evidence/
    web-check.txt          the full output of your last web-check run
    structure-check.txt    the full output of your last structure_check run
  decision-log.md          Week 1 entries stay, Week 2 entries added below them
  proofreading-log.md      from Week 1
  README.md                what it is, how to check it, how to see captions, what is not finished
```

`--shots` also saves screenshots of the code of conduct page. Keep them or delete them. Only the three
home page screenshots are required.

---

## The decision log

Add a **Week 2** heading below your Week 1 entries. Each entry keeps the four parts: **the question**,
**the options you considered**, **what you chose**, and **what it costs**.

Three Week 2 entries are required:

1. **The float.** The requirements say no floats for layout, and Dana asked for text beside the photo.
   Is your float a layout float? Say what float is for, what you used it for, and what keeps it from
   breaking the next section.
2. **The breakpoints.** Every `min-width` you used, what changes there, and why that number. "Because
   768 is a tablet" is not a reason. "Because at 640 the text beside the photo gets 310 pixels, and
   narrower than that a line holds only a few words" is.
3. **The schedule on a phone.** A scroll box, a stacked layout, fewer columns, or something else. Say
   what each costs a coach at the field and what you chose.

A fourth is recommended: **captions and the map's permissions**, or anything Dana asked for that you
think is a bad idea.

### Decision log rubric, inside Documentation (10 points)

| Points | What it looks like |
|---|---|
| 10 | All three required entries with all four parts. The float entry separates wrapping text from laying out a page. Every breakpoint has a reason tied to the content, with a measured or observed number. The schedule entry names a real cost for at least two options. |
| 8 | All three entries, one missing its cost, or breakpoints with reasons that are not tied to content. |
| 6 | All three entries, but the float entry only says "it is allowed" with no reason, or the schedule entry considers one option. |
| 4 | Two of the three required entries. |
| 2 | One entry, or entries that describe what the page does instead of a decision. |
| 0 | No Week 2 entries. |

### Three-width observations, inside Documentation (5 points)

In your README, under a heading **Checked at three widths**, one short paragraph per width: what the
layout does there, which rule makes it happen, and one thing you changed after looking at the
screenshot.

| Points | What it looks like |
|---|---|
| 5 | Three paragraphs, each naming a rule, and at least one change made because of a screenshot. |
| 3 | Three paragraphs that describe the page without naming rules. |
| 1 | "Passes at all widths" and nothing else. |
| 0 | Missing. |

---

## DMAIC checkpoints

The same framework you have used since 145060, sized to one week.

### Define · Monday

Turn Dana's letter into a numbered list of requirements in your README, in your own words. Mark each
one with the requirement number from the table above, or "not a CSS requirement" if it is not one.
Two written questions to Dana, if you need them.

**Checkpoint, Monday end of Build 2:** the requirements list is committed.

### Measure · Monday

Before you write any CSS, run both checkers on your Week 1 page and take the three screenshots with
`--shots`. Save them as `evidence/before-web-check.txt` and `screenshots/before-360.png` and so on.
That is your baseline.

**Checkpoint, Monday end of Build 2:** both pages pass both checkers, the baseline is committed, and
`css/league.css` is linked from both pages with your league colors and their contrast ratios.

### Analyze · Tuesday

Decide where the photo goes and whether it floats, and draft decision log entry 1. Look at the
baseline screenshots and write down where the page is cramped at 360.

### Improve · Tuesday to Thursday

Build it. Tuesday is media. Wednesday is layout. Thursday is responsiveness.

**Checkpoints:** end of Tuesday's Build 2, the photo, clip, and map are in and `web-check` passes.
End of Wednesday's Build 2, the page is a grid and the nav is a flex row. End of Thursday's Build 2,
every query is in, the schedule scrolls in its own box, and decision log entries 2 and 3 are drafted.

### Control · Friday

Final run of both checkers into `evidence/`, final screenshots, decision log finished, README
finished, demo.

**Checkpoint, Friday commit window:** everything in the required structure is committed and pushed.

---

## Milestones

| # | Milestone | Due | Finished when |
|---|---|---|---|
| M1 | Requirements and baseline | Week 2 Mon, end of Build 2 | the README requirements list, the `before` evidence, and a linked stylesheet in league colors are committed, and both pages pass both checkers |
| M2 | Media in | Week 2 Tue, end of Build 2 | the photo, captioned clip, and map are on the page, the captions show on a served page, and `web-check` passes |
| M3 | Layout | Week 2 Wed, end of Build 2 | the page is a grid with named areas, the nav is a flex row, and there is no layout float or table |
| M4 | Responsive | Week 2 Thu, end of Build 2 | every query is in, the schedule scrolls in its own box at 360, forms and contact sit side by side at 1280, and decision log entries 1 to 3 are drafted |
| **Due** | **Everything** | **Week 2 Fri** | both checkers pass both pages at all three widths, evidence and screenshots are from the final run, the log and README are finished |

---

## Three worked scope examples

All three can earn full marks. They differ in ambition, not in quality.

### Small, and completely finished

Every requirement, and nothing more. One stylesheet with two media queries. The code of conduct page
shares the stylesheet and needs no layout of its own. Three decision log entries.

**Why somebody would choose it:** you are preparing for BPA State this week and Period 8 is spoken
for.

**The risk:** finishing Wednesday and then decorating. Spend the spare time on the three screenshots
and the observations, where points are actually lost.

### Medium, and the one most people should aim for

Everything in Small, plus a **"This Saturday" card**: a short component with the next round's two
kickoff times, used in two places, near the top of `main` and again in the footer. The same card uses a
container query so it lays out side by side where it has room and stacks where it does not, whatever
the screen width. Its base, with no query, works everywhere.

**What it adds:** a reason to use a container query that a media query cannot handle, because the same
card has different room in two places on the same screen.

**The risk:** the card and the schedule disagreeing about a kickoff time. Put the time in one place in
your head and check both against the schedule before Friday.

### Large, only if the medium version is done by Wednesday

Everything in Medium, plus a **print layout** so Dana can print the schedule for the board at the
field: `@media print` rules that hide the nav, the video, and the map, and print the schedule table in
full.

**What it adds:** a media query that asks about the medium, not the width. It is not taught this week,
so you research it. MDN's page on using media queries is the place to start.

**The risk, and it is real:** print layouts are hard to check. `web-check` does not print. You would
need Chrome's print preview and a written note of what you saw. **Your cut list puts the print layout
first.**

### Scope calibration, three signals

| If you | Aim for |
|---|---|
| are competing at BPA State or your Week 1 page failed a checker on Monday | Small |
| had M1 done by the end of Monday's Build 2 | Medium |
| had M2 done by the end of Tuesday's Build 1 | Large |

---

## Grading · the 100-point project rubric

| Dimension | Points |
|---|---|
| Functionality | 25 |
| Code Quality | 20 |
| Documentation | 20 |
| Process | 15 |
| Demonstration | 10 |
| Polish | 10 |

### What each dimension means here

**Functionality, 25.** Every request in Dana's letter is met or answered in the decision log. Both
pages pass `web-check` at 360, 768, and 1280 and `structure_check` with zero FAIL lines. Captions show on
a served page. The schedule scrolls in its box at 360. The nav wraps without sideways scrolling. Forms
and contact sit side by side at 1280.

**Code Quality, 20.** Scored on the five-dimension standard. **Correctness:** no fixed widths on text
containers, `height: auto` wherever a ratio matters, `min-width: 0` where a grid item holds a wide
table. **Security:** no `allow` on the map frame, no personal address anywhere, nothing in a comment that
should not be public. **Readability:** one rule per job, comments that agree with the code under them,
contrast ratios in comments, grouped by section. **Performance:** no `transition: all` on everything,
`preload="metadata"` on the clip, `loading="lazy"` on the map, no rule that only undoes another.
**Requirements Fit:** R1 through R15, including no layout float and no layout table.

**Documentation, 20.** README 5 (what it is, how to run both checkers, how to see the captions, what is
not finished), decision log 10, three-width observations 5, using the two rubrics above.

**Process, 15.** A commit at the end of every period. The four milestones visible in your history. The
baseline evidence from Monday. Evidence files from real runs, dated by week and day in the commit
message, not in the file.

**Demonstration, 10.** The script below.

**Polish, 10.** The page looks like the league at every width. Nothing is cramped at 360 that a query
could fix. Alt text describes the photo. The caption track is labelled. The link text still makes sense
on its own.

---

## The five-minute demo script

Two people demo at Friday's close. Everybody else runs the same script as a desk demo with your
instructor early in Week 3.

| Minutes | What |
|---|---|
| 0:00 to 0:30 | **Dana's requests.** Read two of them in her words and point at where each is met. |
| 0:30 to 1:30 | **Three widths.** Open your three screenshots. Say what changes at each and which rule does it. |
| 1:30 to 2:30 | **The phone, live.** DevTools device toolbar at 360. Scroll the schedule inside its box. Tab to a link and show the focus style. |
| 2:30 to 3:30 | **The clip.** Served page, captions on. Say who asked and why it matters. |
| 3:30 to 4:30 | **One decision.** Read your float entry or your breakpoint entry. Say what it costs. |
| 4:30 to 5:00 | **The question.** |

### The question

Every demo ends with one question, answered without notes:

> Your page passes `web-check` at 360. Name two things that PASS does not promise Dana, and how you
> checked each one yourself.

### The ten-point demonstration checklist

| # | | Points |
|---|---|---|
| 1 | Two of Dana's requests located on the page | 1 |
| 2 | Three widths explained, with the rule named for each change | 2 |
| 3 | Schedule scrolled in its box, and keyboard focus shown | 2 |
| 4 | Captions shown on a served page | 1 |
| 5 | A decision and its cost | 2 |
| 6 | The question, answered without notes | 2 |
| | **Total** | **10** |

---

## Submission checklist

- [ ] Both pages link `css/league.css`, and there is no `<style>` block or `style` attribute anywhere
- [ ] Every text color has its contrast ratio in a comment, and every ratio is at least 4.5:1
- [ ] Hover and keyboard focus look the same on every link, and focus has an outline
- [ ] Every media query uses `min-width`
- [ ] No `float` except the photo, and no table used for layout
- [ ] The schedule scrolls in a named, focusable box at 360, and the page does not
- [ ] The photo has alt text, keeps its shape, and only floats where text fits beside it
- [ ] The clip has two sources, a default captions track, and fallback content, and you watched it with
      captions on a served page
- [ ] The map iframe has a `title`, a ratio, and no `allow` attribute
- [ ] Forms and contact sit side by side at 1280 and stack at 360
- [ ] `web-check` passes both pages at 360, 768, and 1280
- [ ] `structure_check` reports zero FAIL lines on both pages
- [ ] `screenshots/` holds three home page screenshots from the final run, and you looked at each one
- [ ] `evidence/` holds both checkers' final output and Monday's baseline
- [ ] `decision-log.md` has the three required Week 2 entries
- [ ] `README.md` has the requirements list, the checker commands, the captions note, the three-width
      observations, and what is not finished
- [ ] Committed and pushed inside Friday's commit window
