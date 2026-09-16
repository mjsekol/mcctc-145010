# Project · The Published Site
## 145010 Web Design · Unit 6 · Week 6

**100 points. Projects category, 35 percent of your grade.**
**Due Week 6, Friday, at the end of the review and close commit window.**

This is the last deliverable of the instruction phase. Next week the capstone starts.

---

## The brief

**The person below is a composite**, written for this course from the kind of reviewer who reads
student portfolios. No real person or organization wrote it.

> From: a reviewer at a regional web studio who reads student portfolios every spring
>
> I look at a lot of student work. Here is what usually happens. I get a link and it does not open.
> Or it opens on the student's laptop and nowhere else. Or it opens, and every page has the same
> title, so I cannot tell my browser tabs apart. Or the menu is different on every page because
> somebody copied it five times and fixed four.
>
> I want to see what you built in your web course, in one place, at an address I can open from my
> own desk. I will look at it on my phone first, because that is what I have with me.
>
> I care whether it is put together properly. I will run it through a validator, because I do that
> with everything.
>
> And I want to know one more thing. When you put something online, do you know whether anyone
> used it? Tell me what you know and how you know it. If you tracked your visitors to find out, do
> not bother sending it. Your visitors are teenagers.

**That is the whole brief.** It does not say how many pages. It does not say what "put together
properly" means. It does not say which host. Turning it into requirements is the first thing you
are graded on.

---

## What you are building

Your instruction-phase work as one site: built from one template, valid, tested in more than one
engine, published at an address someone else can reach, counting visits without identifying
anyone, and reported on honestly.

You built every piece of it this week in Labs W06-01, W06-02, and W06-03. The project is those
pieces finished, true, and yours.

---

## Technical requirements

Every one exists for a reason, and the reason is next to it.

| # | Requirement | Why |
|---|---|---|
| R1 | Every page is generated from one template and a content file. | The reviewer's copied-menu complaint. |
| R2 | At least one page for each of Weeks 1 to 5, plus a home page. | "What you built in your web course, in one place." |
| R3 | A media page with captioned video or audio, a transcript, and a download link. | 6.5.9, and a public video needs captions. |
| R4 | Every page has its own title and its own description. `python build.py --strict` prints no warnings. | The reviewer's browser-tab complaint, and 6.5.14. |
| R5 | Every page passes `tools/web-check` at 360, 768, and 1280. | "I will run it through a validator." "On my phone first." |
| R6 | A cross-browser matrix, filled by hand, with an honest engine count. | 6.5.11. One engine is not a cross-browser test. |
| R7 | Published at an address a classmate can open from their own machine. | "An address I can open from my own desk." |
| R8 | `robots.txt` and `sitemap.xml` correct for that address. `check_site.py` prints `No problems found.` against it. | 6.5.14, and every link has to work. |
| R9 | A counter that stores the page and the day, and a yes or no question, and **nothing that identifies anyone**. No cookie, no stored or logged address, no ID. | "If you tracked your visitors, do not bother." Your visitors are minors. |
| R10 | The counter never slows a page down. | A slow page is a failed page. |
| R11 | A privacy section on the home page that says exactly what is counted. | People have a right to know what a site records. |
| R12 | No form on the public site collects personal information. | A class site does not collect strangers' personal details. |
| R13 | A traffic report with real output from your published site and a "what these numbers cannot tell me" section. | "Tell me what you know and how you know it." |
| R14 | No commercial AI API. AI usage, if any, logged. | Program rule. |
| R15 | Every server started with an explicit port, and stopped. | A server on the wrong port looks like a working one. |
| R16 | Every period ends with a commit. | Version control is a daily habit. |

---

## Required repository structure

```
week6-site/
  README.md                 what the site is, its address, how to build and run it, what is not finished
  site-plan.md              audience, page table, navigation, what you left off and why
  measurement-plan.md       the two questions, the fields and why, what the numbers cannot tell you
  crossbrowser-matrix.md    filled by hand
  traffic-report.md         real report.py output and your reading of it
  decision-log.md           at least four entries, one per day Monday to Thursday
  ai-usage-log.md           every AI use, or one line saying there was none
  launch-messages.md        the three messages you sent
  sitekit/
    build.py  serve.py  report.py  check_site.py  test_counter.py
    site.json  template.html
    content/
    static/                 style.css, count.js, robots.txt, media/
    site/                   built by your last --strict build
  .gitignore                includes data/
```

`data/` is not committed. It is your visitors' activity, not your code.

---

## DMAIC checkpoints

### Define · Monday

What does the reviewer need, in your own words? Who is the site for?

**Checkpoint, Monday end of Build 1:** `site-plan.md` committed, with an audience sentence and a page
table.

### Measure · Tuesday

What will you measure, and what will you refuse to collect?

**Checkpoint, Tuesday end of Build 2:** `measurement-plan.md` committed, and `test_counter.py` prints
`OK`.

### Analyze · Wednesday

What is actually wrong with the markup, and what does each engine do with it?

**Checkpoint, Wednesday end of Build 2:** every page passes web-check, and the matrix is committed.

### Improve · Monday to Thursday

Build, check, fix at the source, rebuild. The template is where most improvements land.

**Checkpoint, Thursday end of Build 2:** published, `check_site.py` passing against the live address,
three launch messages sent.

### Control · Friday

Report what happened, honestly, and say what you would change.

**Checkpoint, Friday commit window:** `traffic-report.md` with real output, and everything above
still true.

---

## Milestones

| # | Milestone | Due | Finished when |
|---|---|---|---|
| M1 | One template | Week 6 Mon, end of Build 2 | `build.py --strict` passes; every page from the template |
| M2 | Counting, safely | Week 6 Tue, end of Build 2 | 13 tests OK; the log and crash report print no address |
| M3 | Valid and tested | Week 6 Wed, end of Build 2 | every page PASS; matrix committed |
| M4 | Live | Week 6 Thu, end of Build 2 | a classmate opened it; `check_site.py` passes against the live address |
| **Due** | **Everything** | **Week 6 Fri** | the last commit pushed inside the review and close window |

---

## Constraints, and why each exists

- **No framework.** The standards for this course are HTML, CSS, and client-side script. React and
  Vue are side quests.
- **No third-party analytics.** You cannot promise a visitor what another company's script collects,
  and this week's point is that you can build what you need. Your instructor may demonstrate one;
  you do not install one.
- **No account on any service without your instructor.** Hosting terms, age rules, and payment
  requirements are your instructor's to check.
- **No personal information on the site.** First name at most. No email address, no school
  schedule, no photos of people.
- **Lab route counts.** If your pages are on a static host, your counter runs on the lab route, and
  your report says so.

---

## Three worked scope examples

All three can earn full marks. They differ in ambition, not quality.

### Small, and completely finished

Six pages: Home and one page per week. A media page that uses the demo video from the lab files,
with its captions and a transcript. Published on the lab route. Four classmates visited.

**Why somebody would choose it:** a student who was at BPA for part of an earlier week and has one
unfinished weekly page to bring in.

**The risk:** a thin traffic report. Four visitors is fine. Pretending four visitors is a trend is
not. Say it is four.

### Medium, and the one most students should aim for

Seven or eight pages: Home, one per week, a media page with your own captioned clip, and a short
"How this site is built" page that shows the template idea. Published on the lab route and, if your
instructor approved it, a static host for the pages. A clear note in the report about which route
the counts came from.

**Why:** the "how this site is built" page is a portfolio piece in itself, and it is what a reviewer
asks about.

**The risk:** two routes, two addresses, and a sitemap that matches only one. `check_site.py --as`
catches it.

### Large, and only if Monday to Wednesday went smoothly

Everything in Medium, plus the Lab W06-03 stretch goal (a generated 404 page with the real status)
and the Lab W06-02 stretch goal (a `--no-count` switch for your own testing), both with tests.

**Why:** both make the report more honest and the site more usable.

**The risk:** starting either before M4. A live site with a simple counter beats a clever site on
your laptop. **Your cut list puts both stretches first.**

### Scope calibration, three signals

| If you | Aim for |
|---|---|
| finished M1 on Tuesday, or have a weekly page still missing | Small |
| hit M1 and M2 on their days | Medium |
| hit M3 before the end of Wednesday Build 1 | Large |

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

**Functionality, 25.** R1 to R5 and R7 to R10. The site builds strictly, validates, is reachable
from another machine, passes `check_site.py` live, counts real visits, and asks its question with
script on and off.

**Code Quality, 20.** Scored on the five-dimension standard: Correctness, Security, Readability,
Performance, Requirements Fit. **Security here means R9 and R12.** A cookie, a stored or printed
address, or a public form that collects personal data **caps Code Quality at 10 and Functionality at
15**, whatever else is right.

**Documentation, 20.** `README.md`, `site-plan.md`, `measurement-plan.md`, `crossbrowser-matrix.md`,
and `traffic-report.md`, all present and all true. The traffic report is half of this dimension, and
its "cannot tell me" section is half of that. See the writing rubric below.

**Process, 15.** A commit every period. Four decision log entries, each naming what was rejected.
The AI usage log. Milestones on their days, or a decision log entry saying why not.

**Demonstration, 10.** The five-minute demo below.

**Polish, 10.** The site reads well on a phone. Titles and descriptions are sentences a person would
write. The README says what is not finished. Nothing is left over from a lab: no `STARTER` comments,
no placeholder text, no `portfolio.example`.

### Writing rubric: the traffic report (10 of the 20 Documentation points)

| Points | What it looks like |
|---|---|
| 10 | Real output pasted. States the two questions. Reads the numbers accurately in words. The "cannot tell me" section names at least four limits, including that views are not people and that the student's own visits are included, and says how many answers the usefulness figures rest on. One change the student would make, tied to a number. |
| 7 | Real output and an accurate reading, with two or three limits. |
| 4 | Output pasted, reading mostly restates the table, one limit. |
| 1 | Output pasted with no reading, or a reading that calls views "visitors" or "people". |
| 0 | Missing, or numbers not from the student's site. |

---

## The five-minute demo script

Five minutes. Timed. You will be stopped. You demo on **someone else's machine**, at your live
address.

| Minutes | What |
|---|---|
| 0:00 to 0:30 | **The reviewer's problem, in the reviewer's words.** |
| 0:30 to 1:30 | **Open the site on the other machine.** Click through three pages. Point at the tab titles. |
| 1:30 to 2:15 | **Change the template, live, and rebuild.** Show the change on every page. |
| 2:15 to 3:00 | **Show `check_site.py` passing against the live address.** Then the web-check line for one page. |
| 3:00 to 4:00 | **Read one line of your traffic report, and one limit.** |
| 4:00 to 4:30 | **One decision and one rejection** from your decision log. |
| 4:30 to 5:00 | **The question.** |

### The question

Asked of you, without notes:

> What does your site record about the person who opened it a moment ago, and how do you know?

**Full credit** names the page and the day, the yes or no if they answered, and nothing else, and
points at the evidence: the counts file, the server log, and the empty cookie list.

### The ten-point demonstration checklist

| # | | Points |
|---|---|---|
| 1 | The problem stated in the reviewer's terms | 1 |
| 2 | The site opened from another machine | 2 |
| 3 | A template change shown reaching every page | 2 |
| 4 | `check_site.py` passing live | 1 |
| 5 | A report line and a limit, read accurately | 1 |
| 6 | A decision and a rejection | 1 |
| 7 | The question, answered without notes, with evidence | 2 |
| | **Total** | **10** |

---

## Submission checklist

- [ ] `python build.py --strict` prints no warnings
- [ ] Every page PASS in web-check at 360, 768, 1280
- [ ] `python test_counter.py` prints `Ran 13 tests` and `OK`
- [ ] `python check_site.py <live address> --as <live address>` prints `No problems found.`
- [ ] A classmate opened the site from their own machine
- [ ] No cookie, no stored address, no printed address. Checked in DevTools and in the log.
- [ ] All eight documents present and true
- [ ] `data/` in `.gitignore`
- [ ] Server stopped
- [ ] Committed and pushed inside the Friday window

---

## What cannot be verified in this course's build, and what that means for you

Your instructor confirms these before the week starts:

- **Hosts.** Cloudflare Pages and Render were not tested when this project was written. Their terms,
  age rules, limits, and payment requirements are not stated here for that reason. **[VERIFY]**
- **The lab network.** Whether a classmate can reach your lab machine depends on the network and
  firewall. **[VERIFY]**
- **Safari.** It does not run on Windows. Your matrix says so.

---

# Instructor appendix

**Reference implementation:** `09-project/reference-implementation/`. Instructor-only. A six-page
site with every document, verified on the build machine: strict build clean, 25 tests OK, six pages
PASS web-check at three widths, `check_site.py` clean, and a headless Chrome run that counted six
loads and one answer and left no cookie. Its README has the full record. Its traffic report uses
invented sample data and says so.

## The three ways this project goes wrong, and the intervention

**1. The counter tracks people after all.** Usually a cookie copied from an AI answer to "count
unique visitors", or a log file the student redirected the unmodified server output into. You see
it on Tuesday in `data/`, or on Friday in the Application tab.

**The intervention, Tuesday:** open the student's Application tab and their terminal, together. Ask
what the site promised on the home page. The fix takes five minutes on Tuesday and costs the Code
Quality cap on Friday.

**2. The site is not live on Thursday.** Hosting questions eat Build 2, or the lab network blocks it.

**The intervention:** the lab route is the default and needs no account. Decide the route per student
before Thursday, and do not let a host sign-up start during class. A student on the lab route with
real counts has met R7 and R9.

**3. The traffic report is written from imagination.** Numbers that are too round, "visitors" instead
of views, or a report finished before Period 8 on Thursday.

**The intervention:** ask the student to run `report.py` on the projector and read one row aloud,
then find that row in their report.

## What to say to a student whose scope is too big

> Is your site live? Then show me that before you show me anything else.

A stretch goal on a laptop scores nothing on R7. Cut the stretch, publish, then add it back.

## What to say to a student whose scope is too small

Do not add pages. Ask:

> Open your site on my phone. Now tell me what your site knows about me.

A small site that works on a phone and answers that question exactly is a full-marks site. Spend the
remaining time on the report.

## Grading notes

- The traffic report cannot be graded on the size of the numbers. A student with four visits and an
  honest reading scores above a student with forty and a careless one.
- A student whose Week 5 form collects personal data and who left it off the site with a reason has
  met R12 and should get Documentation credit for the reason.
- The project grade goes in Projects. The Instruction Phase Exam goes in Quiz & Exam. Gate 2 W06 goes
  in Written & Documentation.
