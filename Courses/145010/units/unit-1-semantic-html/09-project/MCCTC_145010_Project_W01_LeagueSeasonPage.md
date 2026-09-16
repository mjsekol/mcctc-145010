# Project · The League Season Page
## 145010 Web Design & Senior Capstone · Week 1 · Semantic HTML & the Browser

**100 points. Projects category, 35 percent of your grade.**
**Due Week 1, Friday, at the end of the 14-minute commit window.**

**Competencies:** 6.1.1, 6.1.3, 6.1.4, 6.1.5, 6.1.6, 6.2.1, 6.2.2, 6.2.3, 2.7.2, 2.7.8.

---

## The brief

> From: Dana, volunteer coordinator, Cedar Hollow Youth Rec League
>
> Every Saturday parents ask me the same five things. When is my kid's game, which field,
> what do they bring, what happens if it rains, and who do I ask. I want one page that
> answers all five so I can point at it.
>
> Coaches will be reading this on their phones standing at the field, so it has to work on a
> phone. I do not care what it looks like yet. I care that people can find things.
>
> Every family has to print and sign the medical release before round 1. Put it on the page.
>
> The code of conduct should be its own page, because the board wants to be able to send a
> link to only that.
>
> Please do NOT put my home email on the page. The league has its own address now.
>
> When it rains I decide by 7 and then I have to tell everybody. Right now that is 40 texts.
> Can the page do that?

**The league is invented.** So is Dana. The brief is a composite of the kind of request a
volunteer-run group sends, and everything Dana attached is in
[project-files/client-notes.md](project-files/client-notes.md), with the medical release form
beside it.

**That is the whole brief.** It does not list sections, headings, or links. It does not say
which of the attached notes are right, and some of them disagree with each other. **Pulling
requirements out of it, and noticing where the notes contradict themselves, is the first thing
you are graded on.**

Your instructor plays Dana this week. You may ask Dana up to three questions, in writing, by
the end of Monday's Build 2. Choose them carefully. A question you could have answered by
reading the notes costs you one of the three.

---

## What you are building

A two-page static site with a semantic document structure, correct heading hierarchy, and zero
generic `div` elements where a real element exists. No CSS. Structure first, appearance next
week.

**Why no CSS.** Next week Dana writes back and asks for it to look like the league and work
properly on a phone. Everything you style next week sits on the structure you build this week.
A page with good structure is quick to style. A page with bad structure fights you for a week.

---

## Technical requirements

Every one of these exists for a reason, and the reason is next to it.

| # | Requirement | Why |
|---|---|---|
| R1 | One `h1` per page. Headings never skip a level. | A screen reader user moves through a page by its headings. A skipped level reads as a missing section. |
| R2 | `header`, `nav`, `main`, and `footer` on both pages. **No `div` or `span` where an element exists for the job.** | Landmarks are how assistive technology jumps between regions, and how the next developer reads your file. |
| R3 | The schedule is a data table with a `caption`, a `thead`, and `th` cells with `scope`. | A table with no header cells is a grid of words. Chrome's accessibility tree labels one a layout table. |
| R4 | At least one ordered list and one unordered list, each used for content that has that shape. | Order matters in the code of conduct and the directions. It does not matter in the packing list. |
| R5 | A jump menu at the top links to every section of the home page, and every link lands. | Coaches on a phone at the field are not going to scroll through a schedule to find the rain policy. |
| R6 | Relative links from the home page to the code of conduct page and back. The code of conduct page lives in a `pages/` folder. | The board sends that page on its own, and it has to find its way home. |
| R7 | At least one absolute link, to a real site you are certain exists. | Some answers live on somebody else's site. You link to them, you do not copy them. |
| R8 | One email link, to the league address and **never** to Dana's home address. | The client said so. Everything in page source is public, including to scrapers. |
| R9 | One download link to the medical release that tells people the file type and size before they click. | A parent on a phone deserves to know a PDF is about to arrive. |
| R10 | `web-check` reports PASS at 360, 768, and 1280 px on both pages. `structure_check` reports zero FAIL lines. | The checkers catch what you stopped seeing an hour ago. |
| R11 | A decision log with at least three entries, including the rain-out question. | Dana asked whether the page can send 40 texts. The answer is a decision, and you have to be able to defend it. |
| R12 | A proofreading log showing all four passes: draft, revise, edit, proofread. | The notes have errors in them. The page cannot. |
| R13 | No CSS, no JavaScript, no framework. | Next week's work. |
| R14 | Every period ends with a commit. | Version control is a daily ritual, not a unit. |

### The two checkers

You set both up in Lab W01-01. The page checker's own instructions are in
[tools/web-check/README.md](../../../../../tools/web-check/README.md). From the root of the course
repository:

```
node tools/web-check/check.js <your-folder>/index.html <your-folder>/pages/code-of-conduct.html --widths 360,768,1280
python Courses/145010/units/unit-1-semantic-html/05-labs/structure-check/structure_check.py <your-folder>/index.html <your-folder>/pages/code-of-conduct.html
```

**Know what each one cannot see.** `web-check` passes a page made entirely of `div` elements,
with no headings at all. `structure_check` cannot tell whether your headings say anything
useful or whether the kickoff time in your table is the right one. You can, and the rubric
checks.

---

## Required repository structure

```
league-season-page/
  index.html
  pages/
    code-of-conduct.html
  files/
    cedar-hollow-medical-release.pdf
  decision-log.md
  proofreading-log.md
  evidence/
    web-check.txt          the full output of your last web-check run
    structure-check.txt    the full output of your last structure_check run
  README.md                what this is, how to check it, what is not finished
```

Save checker output with a redirect, for example `... > evidence/web-check.txt`. Run it from
`cmd` or Git Bash if PowerShell gives you a file full of odd characters.

---

## The decision log

Three entries minimum. Each entry has four parts: **the question**, **the options you
considered**, **what you chose**, and **what it costs**.

Two entries are required:

1. **Can the page tell everybody about a rain-out?** Dana asked. This page is static: it
   changes only when somebody edits the file and publishes it again. Say what a static page can
   and cannot do here, what a dynamic site would add, and what you recommend to Dana for this
   season. There is more than one defensible answer. There is no defensible answer that
   pretends a static page sends texts.
2. **How should this schedule reach coaches at the field?** A responsive web page, a mobile
   app, a desktop application, or a web application. Say who each would serve and what each
   costs a volunteer league. Pick one for now and say why.

The third is yours. Good candidates: which of the contradictory notes you trusted and why, or
why a piece of content is a list and not a table.

### Decision log rubric, inside Documentation

| Points | What it looks like |
|---|---|
| 8 | Three or more entries, each with all four parts. The static and dynamic entry names what the page cannot do. The presentation entry names a real cost for each option. |
| 6 | Three entries, one missing its cost, or a presentation entry that compares only two options. |
| 4 | Two entries, or entries that state a choice with no options considered. |
| 2 | One entry, or entries that describe what the page does rather than a decision. |
| 0 | Missing. |

---

## The proofreading pass

The notes Dana sent contain at least five errors and contradictions. Some are typos. Some are
facts that disagree with other facts. The full procedure is in
[the proofreading guide](MCCTC_145010_Guide_W01_ProofreadingPass.md).

Your `proofreading-log.md` has four headed sections, one per pass: **Draft**, **Revise**,
**Edit**, **Proofread**. Under each, a list of what you found and what you did. For a
contradiction, say which version you used and why, or which question you asked Dana.

### Proofreading log rubric, inside Documentation

| Points | What it looks like |
|---|---|
| 7 | All four passes. Five or more real corrections, including at least two contradictions between notes, each resolved with a reason. The final page matches the log. |
| 5 | All four passes, three or four corrections, contradictions noticed but one left unresolved. |
| 3 | Passes named but merged, or only typos found. |
| 1 | A list of changes with no passes. |
| 0 | Missing, or the log claims a fix the page does not have. |

---

## DMAIC checkpoints

Same framework you have used since 145060, sized to one week.

### Define · Monday

Read the brief and every note. Write the requirements you extracted as a numbered list in your
README. Write your three questions for Dana.

**Checkpoint, Monday end of Build 2:** README committed with the requirements list, and your
questions handed in.

### Measure · Tuesday

Build the skeleton: both pages, every landmark, every heading, no content yet beyond a
sentence per section. Run both checkers. That output is your baseline.

**Checkpoint, Tuesday end of Build 2:** skeleton committed, `evidence/` has a first run of each
checker.

### Analyze · Wednesday

Map every link before you write it: from which page, to which file, by what path. Decide the
rain-out question and write that decision log entry.

**Checkpoint, Wednesday end of Build 2:** every link works from where it lives, and the
rain-out entry is committed.

### Improve · Wednesday and Thursday

Fill in the content. Build the schedule table. Write the presentation entry.

**Checkpoint, Thursday end of Build 2:** full content, table included, both checkers run.

### Control · Friday

The proofreading pass, the final checker runs, the evidence files, the README.

**Checkpoint, Friday commit window:** the last commit pushed is the submission.

---

## Milestones

| # | Milestone | Due | Finished when |
|---|---|---|---|
| M1 | Requirements extracted | Week 1 Mon, end of Build 2 | README lists them, and your three questions are handed in |
| M2 | Skeleton and baseline | Week 1 Tue, end of Build 2 | both pages have every landmark and heading, `structure_check` shows the outline you intended |
| M3 | Links land | Week 1 Wed, end of Build 2 | `structure_check` reports no ANCHORS or FILES failures, and the rain-out entry is committed |
| M4 | Content and table | Week 1 Thu, end of Build 2 | the schedule table has a caption and header cells, and all five of Dana's questions are answered on the page |
| **Due** | **Everything** | **Week 1 Fri** | both checkers pass, both logs are complete, evidence is committed |

---

## Three worked scope examples

All three can earn full marks. They differ in ambition, not quality.

### Small, and completely finished

Two pages exactly as required. The home page answers Dana's five questions in five sections,
plus the forms section. Three decision log entries. Five proofreading corrections.

**Why somebody would choose it:** you are submitting to BPA State this week and Period 8 is
spoken for.

**The risk:** finishing Wednesday and adding things nobody asked for. Spend spare time on the
proofreading pass instead. That is where most points are lost.

### Medium, and the one most people should aim for

Everything in Small, plus a third page, `pages/fields.html`, with the directions for each
field, linked from the home page and linking back to a specific section of it with a fragment,
such as `../index.html#schedule`.

**What it adds:** a relative link that carries a fragment across folders, which is the link
most likely to break silently.

**The risk:** the home page and the fields page both describing the fields, and disagreeing.
Say it in one place and link to it.

### Large, only if the medium version is done by Wednesday

Everything in Medium, plus one page per team in `pages/teams/`, each listing that team's six
games in its own table, linked from the schedule.

**What it adds:** relative paths two folders deep (`../../index.html`), and twelve more links
that all have to land.

**The risk, and it is real:** four more tables means four more places for a kickoff time to be
wrong. If one team page disagrees with the main schedule, that is a Functionality deduction
and a proofreading deduction. **Your cut list puts team pages first.**

### Scope calibration, three signals

| If you | Aim for |
|---|---|
| are submitting to BPA State this week | Small |
| had a working skeleton by the end of Tuesday | Medium |
| had every link landing by the end of Wednesday's Build 1 | Large |

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

**Functionality, 25.** Both pages answer every question in the brief. Every link lands,
including the jump menu, the download, and the page in `pages/`. The schedule is correct
against the notes, with the contradictions resolved. `web-check` passes at all three widths.

**Code Quality, 20.** Scored on the five-dimension standard. **Correctness:** valid markup,
nothing the browser had to repair. **Security:** no personal address, nothing in a comment that
should not be public. **Readability:** headings in order, landmarks present, no generic
containers where an element exists, indentation a reader can follow. **Performance:** no
files linked that are not needed. **Requirements Fit:** R1 through R13.

**Documentation, 20.** README 5, decision log 8, proofreading log 7, using the two rubrics
above for the logs. The README says what the site is, how to run both checkers on it, and what
is not finished.

**Process, 15.** A commit at the end of every period. The four checkpoints visible in your
history. Three questions to Dana handed in on Monday. Evidence files from real runs.

**Demonstration, 10.** The script below.

**Polish, 10.** The page reads well out loud. Link text makes sense on its own. The caption
says what the table is. Nothing on the page is a leftover from the notes.

---

## The five-minute demo script

One person demos at Friday's close. Everybody else runs the same script as a desk demo with
your instructor early in Week 2.

| Minutes | What |
|---|---|
| 0:00 to 0:30 | **Dana's five questions.** Point at the section that answers each one. |
| 0:30 to 1:30 | **The outline.** Run `structure_check` and read the heading outline out loud. |
| 1:30 to 2:30 | **Links.** Use the jump menu. Open the code of conduct page and come back. Show the download link text. |
| 2:30 to 3:30 | **The table.** Show the caption and the header cells in DevTools. Say why `scope` is there. |
| 3:30 to 4:30 | **One decision.** Read your rain-out entry. Say what it costs Dana. |
| 4:30 to 5:00 | **The question.** |

### The question

Every demo ends with one question, answered without notes:

> Your page and a page built fresh by a server for every visitor look identical in the browser.
> What is different, and when would Dana need the second kind?

### The ten-point demonstration checklist

| # | | Points |
|---|---|---|
| 1 | All five of Dana's questions located on the page | 2 |
| 2 | Heading outline read out and correct | 2 |
| 3 | Jump menu, relative link, and download shown working | 2 |
| 4 | Table header cells and `scope` explained | 1 |
| 5 | A decision and its cost | 1 |
| 6 | The question, answered without notes | 2 |
| | **Total** | **10** |

---

## Submission checklist

- [ ] `index.html` and `pages/code-of-conduct.html` both pass `web-check` at 360, 768, 1280
- [ ] `structure_check` reports zero FAIL lines on both pages
- [ ] Every heading is in order, and each page has exactly one `h1`
- [ ] No `div` or `span` doing the job of a real element
- [ ] The schedule table has a `caption` and `th` cells with `scope`
- [ ] The jump menu reaches every section
- [ ] The download link says PDF and the size
- [ ] The email link goes to the league address, and Dana's home address is nowhere in any file
- [ ] View Source on both pages: nothing in a comment you would not want public
- [ ] `decision-log.md` has three entries, including rain-outs and presentation
- [ ] `proofreading-log.md` has all four passes
- [ ] `evidence/` has both checker outputs from your final run
- [ ] `README.md` says what is not finished
- [ ] No CSS, no JavaScript
- [ ] Committed and pushed inside the Friday commit window
