# Project · The Interactive Component
## 145010 Web Design & Senior Capstone · Unit 4 · Week 4

**100 points. Projects category, 35 percent of your grade.**
**Due Week 4, Friday, at the end of the commit window.** If you missed two or more days for BPA
State, your deadline is the end of Period 8 on Week 5, Tuesday. Your instructor records it.

**Competencies:** 6.3.1, 6.3.2, 6.3.3, with 2.7.5 in the page weight requirement.

---

## The brief

> From: the volunteer who runs the league website
>
> I run the website for a youth rec league, about a hundred and twenty kids across six age groups.
> Every Saturday morning I get the same messages. When does my daughter play. Which field. Did they
> already play the Otters. The schedule is on the site. It is one long table, and on a phone it is
> a wall.
>
> I do not want an app. I do not want anybody to log in. I want the page to help a parent find their
> kid's games, fast, standing at the edge of a field with one bar of signal.
>
> Two things I care about more than how it looks. One of our coaches uses a screen reader, and one of
> our parents cannot use a mouse, so whatever you build has to work for both of them. And if the
> fancy part breaks, the plain schedule still has to be there. People need it at 8 am whether your
> code works or not.
>
> I have also been told I need an FAQ and a way to show which fields are closed. I do not know which
> of these is most useful. You tell me.

*The league and the volunteer are a composite, invented for this course. The problem is common to
nearly every volunteer-run youth league.*

**That is the whole brief.** It does not say which component to build, what "fast" means, or what
"find their kid's games" looks like on screen. **Pulling requirements out of it is the first thing
you are graded on.**

---

## What you are building

**One interactive component, built without a framework**, on one page, that solves one problem from
the brief. Plain HTML, CSS, and JavaScript. No React, no Vue, no jQuery, no library of any kind.

There are no starter files. You write your own sample data, and it must be invented. Real
schedules, real team names from a league you play in, and any real child's name are not allowed.

Components that fit the brief:

| Component | What it solves |
|---|---|
| Schedule finder | Filter a table of games by team and by played or upcoming |
| FAQ accordion with search | Find an answer without reading every question |
| Field status board | Show which fields are open, closed, or delayed, with a filter |
| Tabs for age groups | One schedule per age group without a wall of tables |

You may propose something else in your Define checkpoint. It must come from the brief.

---

## Technical requirements

| # | Requirement | Why |
|---|---|---|
| R1 | Plain HTML, CSS, and JavaScript. No framework or library. | The Ohio standards for this course are vanilla, and a framework hides the thing you are learning. |
| R2 | One external `.js` file, loaded in the `<head>` with `defer`. | Monday. The script must never run before the page exists. |
| R3 | **Every control works by keyboard alone**: Tab reaches it, Enter or Space or the arrow keys operate it, and focus is always visible. | The brief names a parent who cannot use a mouse. |
| R4 | Native controls only: `<button>`, `<select>`, `<input>`, `<a>`. No clickable `<div>` or `<span>`. | Tuesday. Native controls get keyboard support and a role for free. |
| R5 | State that a screen reader needs is in the markup: `aria-expanded`, `aria-pressed`, `hidden`, or a `role="status"` sentence. | The brief names a screen reader user. |
| R6 | **No `innerHTML`, `outerHTML`, or `insertAdjacentHTML`** anywhere. Text goes in with `textContent`. | Wednesday. Text is text. |
| R7 | **Progressive enhancement.** With JavaScript turned off, the page still shows all of its information. | The brief: "the plain schedule still has to be there." |
| R8 | State, render, events. One place holds the state, one function draws it. | Wednesday. The page must never contradict itself. |
| R9 | A header comment in the script, and a why-comment wherever the reason is not obvious. No secrets, no stale comments. | 6.3.3, and comments are public. |
| R10 | `web-check` reports PASS. | The floor, not the ceiling. |
| R11 | **Page weight measured** under Slow 4G with cache disabled, and recorded in the README: requests, transferred, Load. **Under 100 kB transferred.** | Thursday. One bar of signal. |
| R12 | Every period ends with a commit. | Always. |

---

## Required repository structure

```
projects/w04-component/
  index.html
  styles.css
  component.js          or a name that says what it is
  README.md             what it is, who it is for, how to test it, page weight, what is not finished
  decision-log.md       Define checkpoint, and every decision after
  keyboard-test.md      the keyboard test, filled in
```

---

## DMAIC checkpoints

### Define · Wednesday, Build 2

In `decision-log.md`: which component, which person in the brief it serves, and why that one first.
Then the **state** written as a code block, the **events** that change it, and the **keys** it must
support.

```js
// example shape only
const state = { team: "", hidePlayed: false };
```

**Checkpoint, end of Wednesday Build 2:** committed, and the page loads with its script deferred and
no Console errors.

### Measure · Thursday, Build 2

Measure your page under Slow 4G, cache disabled, and record requests, transferred, and Load in the
README. Record how many items your component handles.

### Analyze · Thursday

Look at your numbers against R11. If you are over 100 kB, find out why in the Network panel before
you build anything else.

### Improve · Wednesday to Friday

Build, one event at a time. After each one works with the mouse, test it with the keyboard before
starting the next.

### Control · Friday

Run `web-check`. Run the keyboard test below and fill in `keyboard-test.md`. Turn JavaScript off and
check R7. Update the README.

---

## The keyboard test

Copy this into `keyboard-test.md` and fill in every row. Hand off the mouse for the whole test.

| # | Check | Pass or fail | Notes |
|---|---|---|---|
| 1 | Tab from the address bar reaches every control, in an order that makes sense | | |
| 2 | Every control shows a visible focus ring | | |
| 3 | Every control can be operated: Enter or Space for buttons, arrows for a select | | |
| 4 | After each action, focus is somewhere sensible, never lost to the top of the page | | |
| 5 | Every change is visible **and** in the markup: an attribute or a status sentence | | |
| 6 | With JavaScript off, all of the information is still on the page | | |

To turn JavaScript off in Chrome: dev tools, press Ctrl+Shift+P, type "Disable JavaScript", press
Enter, and reload. Turn it back on the same way.

---

## Milestones

| Milestone | Due | Finished when |
|---|---|---|
| Define | Week 4 Wed, end of Build 2 | Decision log has the component, the person, the state, events, and keys. Page loads with no errors. |
| Measured | Week 4 Thu, end of Build 2 | README has three measured numbers |
| **Due** | **Week 4 Fri, commit window** | The last commit pushed in the window is the submission |
| BPA extension | Week 5 Tue, end of Period 8 | Only for students approved by the instructor |

---

## Three worked scope examples

All three can earn full marks. They differ in ambition, not quality.

### Small: an FAQ accordion

**What it is.** Eight questions a parent actually asks, each a `<button>` with `aria-expanded` that
shows and hides its answer. The answers are in the HTML, so with no script every answer shows.

**What makes it full marks.** Every button works by keyboard, every `aria-expanded` is truthful, the
page is tiny, and the README explains why the answers start visible in the HTML.

**Choose it if** you missed days for BPA this week, or Lab W04-01 took you until Wednesday.

**The risk.** Finishing Thursday and adding animations nobody asked for. Spend the time on the
keyboard test and the README instead.

### Medium: a schedule finder

**What it is.** The schedule as a real table in the HTML. The script adds a team `<select>` built
from the table, a "Hide games already played" toggle button, a reset button, and a status sentence
that says how many games are showing.

**What it adds.** Two pieces of state that combine, a render function that decides which rows show,
a status sentence that must always agree with the rows, and a "no games match" message.

**Choose it if** you finished Lab W04-01 by Tuesday. This is the scope most students should aim for.

**The risk.** The status sentence. It is the thing most often wrong, and the rubric checks it for
every combination.

### Large: a finder that remembers

**What it is.** The medium finder, plus the chosen team and toggle saved in the page address, as
`?team=Otters&upcoming=1`, so a parent can bookmark "my kid's games" and open it at the field.

**What it adds.** Reading the address when the page loads, updating it when the state changes
without reloading the page, and a new failure mode: a bookmarked team that no longer exists.

**Choose it if** your medium version passes every check by Thursday.

**The risk.** It uses a part of the browser this course did not teach. Read MDN's pages on
`URLSearchParams` and `history.replaceState`. The address is typed by people, which makes it
untrusted input. A team name from the address that is not in the list must be ignored, not shown.

### Scope calibration, three signals

| If you | Aim for |
|---|---|
| missed two or more days this week | Small |
| finished Lab W04-01, including the keyboard test, by the end of Tuesday | Medium |
| have Medium passing R1 to R11 by Thursday's close | Large |

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

**Functionality, 25.** The component solves the problem you named. Every control works by mouse and
by keyboard (R3). The page never contradicts itself. With JavaScript off, the information is all
there (R7).

**Code Quality, 20.** Scored on the five-dimension standard: Correctness, Security, Readability,
Performance, Requirements Fit. **Any `innerHTML`, `outerHTML`, or `insertAdjacentHTML` loses the
Security share in full** (R6). Native controls only (R4). State, render, events (R8). Elements looked
up once. Comments that say why (R9).

**Documentation, 20.** The README says what the component is, who it is for, how to test it, the
three measured numbers, and what is not finished. `keyboard-test.md` is complete and honest: a
failed row with a note scores better than a row marked pass that fails when the instructor tries it.

**Process, 15.** A commit at the end of every period. The Define checkpoint on time. A decision log
with real decisions: what you chose, what you rejected, and why.

**Demonstration, 10.** The three-minute demo below, keyboard only.

**Polish, 10.** `web-check` PASS (R10). Under 100 kB (R11). The page reads well at 360 pixels wide.
Nothing is left over from the lab.

---

## The three-minute demo

Keyboard only. The mouse stays on the desk. You will be stopped at three minutes.

| Time | What |
|---|---|
| 0:00 to 0:30 | **Who it is for,** in the volunteer's words. Which person in the brief. |
| 0:30 to 1:30 | **Use it with the keyboard.** Every control, out loud: "Tab, Space, the list now shows three games." |
| 1:30 to 2:00 | **Turn JavaScript off and reload.** Show that the information is still there. |
| 2:00 to 2:30 | **Your page weight.** Three numbers, and which one you would reduce first. |
| 2:30 to 3:00 | **The question.** |

### The question

Asked of every presenter, without notes:

> Show me the line where text gets onto the page, and tell me why it is safe.

The answer points at `textContent` and says that the browser never parses it, so typed or stored
text can never become an element or run code.

---

## Submission checklist

- [ ] `web-check` reports PASS on `index.html`, output pasted in the README
- [ ] `keyboard-test.md` complete, all six rows
- [ ] Searching the script for `innerHTML` finds nothing
- [ ] Script in the `<head>` with `defer`
- [ ] JavaScript-off check done and recorded
- [ ] README has requests, transferred, and Load under Slow 4G, and transferred is under 100 kB
- [ ] Decision log with the Define checkpoint and at least two later decisions
- [ ] Every data item invented, and the README says so
- [ ] AI usage log entry for any AI use
- [ ] Committed and pushed inside Friday's commit window, or the approved BPA deadline

---

# Instructor appendix

**Reference implementation:** `09-project/reference-implementation/`, **instructor only**. It is the
medium scope, a schedule finder, with an automated acceptance script. See its README for the
verification record.

## The three ways this project usually goes wrong, and the intervention

**1. The clickable div comes back.** A student styles a filter chip as a `<span>` because a button
"looks wrong." **Intervention:** hand them the reference CSS for `button[aria-pressed="true"]`, and
ask them to Tab to their chip. Do not fix it for them.

**2. The status sentence lies.** The count says six games while five rows show, usually after a
reset. **Intervention:** ask them where the count is computed. If the answer is "in the handler,"
the fix is render, and they know it from Wednesday.

**3. The fancy version replaces the plain one.** The table is built entirely by the script from a
JavaScript array, so with JavaScript off the page is empty. **Intervention:** turn JavaScript off on
their machine and read the brief's last paragraph aloud. Moving the data into the HTML is a
half-hour fix, and it is the fix.

## What to say to a student whose scope is too big

"Show me the keyboard test for what you have now." If any row fails, the scope is too big, and the
next hour goes to that row. A search box, a sort, and a saved state that fail the keyboard test
score lower than an accordion that passes it, because R3 is in Functionality and the brief names the
person.

## What to say to a student whose scope is too small

"Which person in the brief does this not help yet?" An accordion that serves the screen reader user
and the keyboard user can still add a search box that filters the questions, with a status sentence.
That is one more piece of state and one more event, and it is the difference between Small and
Medium.

## Grading the BPA extension

Grade on the same rubric. The Process row expects commits on the days the student was present, not
on the days they were competing. The Define checkpoint is due at the end of their first day back.
