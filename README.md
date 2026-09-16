# Web Design & Senior Capstone · 145010
## AI Automation & Software Development · Mahoning County Career & Technical Center

Student materials for **145010 Web Design & Senior Capstone**, senior year, semester 2.
Instructor: Michael Sekol.

Everything here is written to you, the student. Read it, run it, argue with it.

---

## What this course is

This is the final course in the program. It has two phases, and they work differently.

**Weeks 1-6 are instruction.** Six weeks of web fundamentals: markup, styling,
accessibility, client-side scripting, forms, and publishing. No framework. The Ohio
standards for this course are written around plain HTML, CSS, and JavaScript, and a
framework would hide the parts you are here to learn.

**Weeks 7-18 are the capstone.** Twelve weeks solving a real problem for a real person
outside this classroom, run as DMAIC. Only 30% of the capstone grade is the code.
The rest is process and documentation, what your stakeholder got out of it, and how well
you present and defend it.

**You arrive having finished three courses.** You write Python and C#, you use Git without
thinking about it, you have deployed a database-backed app, and you have run usability
studies. None of that is re-taught.

---

## How this course runs

**149-minute block, Periods 4/5B through 7.**

During instruction, Weeks 1-6:

| Minutes | What happens |
|---|---|
| 10 | Bell ringer, including a timed Gate 1 rep |
| 15 | Instruction. One concept, demonstrated live |
| 50 | Build 1 |
| 5 | Reset |
| 55 | Build 2 |
| 14 | Review and commit |

During the capstone, Weeks 7-18:

| Minutes | What happens |
|---|---|
| 10 | Standup: finished, working on, blocked by |
| 15 | Clinic. Whatever the room needs this week, not a lecture |
| 110 | Build. Your instructor conferences with two teams a day |
| 14 | Demo and commit |

**Friday in the capstone is stakeholder day**: client contact, feedback review, and your
weekly written progress update.

**Period 8 is yours.** Self-directed time for capstone work, credentials, BPA, and side
quests.

## The three gates

| Gate | AI use | What it is here |
|---|---|---|
| **Gate 1, Closed** | None | Timed reps in a plain editor. Write the markup, the selector, the event handler from memory. |
| **Gate 2, Adversarial** | AI is the opponent | You critique AI-generated pages and code with planted defects: invalid markup, broken layouts, accessibility failures, security holes. |
| **Gate 3, Open** | Full tooling | Build with every tool you have. Every build carries a decision log. |

## The capstone, in one table

| Weeks | Phase | What you deliver |
|---|---|---|
| 7-8 | Define | Proposal and a named stakeholder. **A signed agreement is required to proceed.** |
| 9-10 | Measure and Analyze | Requirements, baseline data, wireframes, architecture, test plan |
| 11-14 | Improve | Build sprints, weekly demos, weekly written stakeholder updates |
| 15-16 | Control | Usability testing with real users, acceptance against the agreed criteria |
| 17-18 | Control | Rollout, handoff, final presentation and defense |

**Three tracks:** Industrial/HMI, Full-Stack Application, AI-Integrated. The track sets the
technical shape. The problem is always your own.

**Scope locks after Week 12.** It may be reduced after that, never expanded.

**The two ways a capstone fails:** scope that is too big, and no real stakeholder. Both are
caught early on purpose. An oversized project is cut in Week 8, not discovered in Week 14.

## The rules that matter most

- **No work is graded that is not in a repository.** Every period ends with a commit.
- **Every page you ship is valid, accessible, and works at phone width.** Automated checks
  catch part of that. You check the rest with a keyboard and a screen reader.
- **AI runs locally.** Commercial AI developer APIs require users to be 18 or older, so this
  course never uses them.
- **No personal information, real names, or school data enters any AI tool.** That includes
  anything your stakeholder shares with you.
- **Anything you publish is public.** A live site is reachable by anyone. Treat every page,
  form, and analytics choice that way.
- **The only way to fail outright is to submit work you cannot explain.**

---

## What is in here

| Week | Topic | Folder |
|---|---|---|
| 1 | Semantic HTML & the Browser | `unit-1-semantic-html/` |
| 2 | Modern CSS & Responsive Layout | `unit-2-modern-css/` |
| 3 | Accessibility & Compliance | `unit-3-accessibility/` |
| 4 | Client-Side Scripting | `unit-4-client-side-scripting/` |
| 5 | Forms & Data | `unit-5-forms-and-data/` |
| 6 | Publishing, Standards & Measurement | `unit-6-publishing-and-measurement/` |
| 7-18 | Senior Capstone | `Courses/145010/capstone/` |

The instruction units are under `Courses/145010/units/`. Every unit, and the capstone, has
the same shape:

```
03-lecture-notes/      read these if you missed class, or before you build
04-slides/             slide outlines from class
05-labs/               the guided labs and the files they use
07-gate2-adversarial/  the weekly AI critiques and the artifacts to review
09-project/            project briefs, templates, and problem drops
10-resources/          readings, practice, documentation
```

The course runs 18 weeks. **Grading Period 3 is Weeks 1-9** and **Grading Period 4 is
Weeks 10-18.** Course milestones are fixed by week: proposal signed in Week 8, scope locked
in Week 12, the WebXam post-test in Week 16, final presentations in Week 18. Everything is
scheduled by week and day, so your teacher will tell you how the weeks line up with this
year's calendar.

Plus `Courses/Misc/` for the Side Quest Catalog, the Lab Acceptable Use and Safety
Agreement, and the side quest bundles.

**Lecture notes are written so you can learn a concept from the file alone.** If you were
out, start there rather than asking someone what you missed.

## What is not in here, and why

Answer keys, quizzes, exams, lesson plans, the exemplar capstone, and the instructor's notes
live in a separate private repository. That is not secrecy for its own sake. A published
answer key is not recoverable, and the work is worth more to you unspoiled.

---

## Getting set up

Your toolchain from the first three courses still applies. This course adds:

- **A current browser with developer tools.** Chrome or Edge.
- **A code editor** for HTML, CSS, and JavaScript. Gate 1 reps use a plain editor with no
  autocomplete.
- **A local web server** to test your pages the way a visitor sees them. Python's built-in
  one works: `python -m http.server`.
- **A screen reader.** Windows Narrator is built in.
- **The page checker**, in `tools/web-check/`. It validates your HTML, audits accessibility,
  and checks for sideways scrolling at three widths. You set it up in Week 1. See
  [tools/web-check/README.md](tools/web-check/README.md).
- **Flask**, the same Python web framework you used in 145130, for the Week 5 forms and any
  capstone with a server.

Hosting and design tools for the capstone are set up by your instructor. Nothing here
requires an AI account, an API key, or a credit card, and nothing you write should ever
need one.
