# Week 3 Project · The Accessibility Rebuild
## 145010 Web Design & Senior Capstone · Week 3

**100 points. Projects category, 35 percent of your grade.**
**Due Week 3, Friday, at the end of the 14-minute review and commit window.**

This project is the syllabus deliverable for Week 3: **the Accessibility Rebuild**, **keyboard-only
navigation demonstrated end to end**, and **a screen reader walkthrough recorded**. Lab W03-01 is the
procedure. This file is the client's brief, the requirements, and how it is graded.

---

## The brief

*The pantry and the coordinator are invented for this course. The situation is a composite.*

> From: the volunteer coordinator, Lantern Street Community Pantry
>
> One of our best volunteers told me last week that she could not sign up for a shift on our website.
> She is blind and uses a screen reader. I looked at the page and I honestly could not see anything
> wrong with it. It looks nice. My nephew built it.
>
> I have since found out that this might be a legal problem and not only an embarrassing one. I do not
> know what the rules are and I cannot afford a lawyer to find out, so please do not tell me we are
> "compliant." Tell me what you checked.
>
> I would like three things. Fix the page so she can sign up. Keep it looking the way it looks, because
> people like it. And give me something in plain English I can keep, that says what was wrong, what you
> changed, and how I would check it myself next time somebody edits the page.
>
> Two more things. A lot of our families speak Spanish, and I want them to feel welcome on that page
> too. And please do not collect anything more about volunteers than we already ask for.

**That is the whole brief.** It does not name WCAG. It does not say which problems exist. It asks you
not to promise legal compliance, which is the correct request and one you honour.

**Pulling requirements out of that brief is the first thing you are graded on.**

---

## What you are building

| # | Deliverable | Where | DMAIC phase |
|---|---|---|---|
| 1 | **Access plan**, one page | `week3-rebuild/audit/access-plan.md` | Define |
| 2 | **Audit log**, from Lab W03-01 | `week3-rebuild/audit/audit-log.md` | Measure and Analyze |
| 3 | **Rebuilt page** | `week3-rebuild/index.html` and its files | Improve |
| 4 | **Walkthrough record**: keyboard, screen reader, partner test | `week3-rebuild/audit/walkthrough.md` | Control |
| 5 | **Screen reader recording**, or a partner's listening log | Submitted where your instructor says. **Never committed** | Control |
| 6 | **Note to the coordinator**, one page, plain English | `week3-rebuild/audit/client-note.md` | Control |
| 7 | **Decision log**, at least four entries | `week3-rebuild/decision-log.md` | Every phase |

Templates for 1 and 6 are in this folder:
`MCCTC_145010_Template_W03_AccessPlan.md` and `MCCTC_145010_Template_W03_ClientNote.md`. The audit log
and walkthrough templates are in `05-labs/lab-w03-01-files/`.

---

## Technical requirements

Every requirement has a reason next to it.

| # | Requirement | Why |
|---|---|---|
| R1 | `web-check` exits 0 at 360, 768, and 1280 pixels | The floor. A page that fails the tool fails people the tool can see |
| R2 | Every control reachable and usable by keyboard, with a visible focus ring, and no trap | The volunteer in the brief navigates by keyboard |
| R3 | Every image has alt text that answers "what would I need to know if it were gone," or `alt=""` if decorative | A present but useless name passes the tool and fails the person |
| R4 | Real headings in an outline that does not skip, and landmarks for header, navigation, main, and footer | Screen reader users navigate by them |
| R5 | No meaning carried by colour alone | 1.4.1, Level A |
| R6 | The Spanish sentence is marked as Spanish | The client asked for Spanish-speaking families to feel welcome |
| R7 | The form collects name, email, optional phone, shift, and the yes or no question. Nothing more. It uses POST | The client asked you not to collect more. POST keeps it out of the address bar |
| R8 | The page looks like the same page | The client asked. A redesign is scope nobody requested |
| R9 | No JavaScript is required for the page to work, and no script touches the Tab key | The trap was a script |
| R10 | **No statement anywhere says the page is compliant, fully accessible, or legally safe** | You are not qualified to say it, and the client asked you not to |
| R11 | No real personal data in any test, recording, or file. Invented names and `example.com` or `example.org` addresses only | Program rule |
| R12 | Every period ends with a commit | Daily ritual |

---

## Required repository structure

```
week3-rebuild/
  index.html
  thanks.html
  logo.svg  calendar-icon.svg  entrance-map.svg  shifts.ics
  decision-log.md
  audit/
    access-plan.md
    audit-log.md
    walkthrough.md
    client-note.md
```

`hours.svg` may be deleted once the hours are real text. Say so in the decision log.

---

## DMAIC checkpoints

### Define · Monday, Build 2

Read the brief. Write the access plan: who uses the page, on what, with which assistive technology,
the colour pairs and their ratios, the link plan, the images and their purpose, and the standard you are
building to. **Checkpoint:** `access-plan.md` committed.

### Measure · Tuesday, Build 2

Tool pass and structure pass. Numbers first: how many validation errors, how many axe rules, how many
headings the tree reports. **Checkpoint:** Pass 1 pasted into the audit log.

### Analyze · Wednesday, Build 2

Keyboard pass and reading pass. Every row gets a person it stops and a criterion. **Checkpoint:**
`audit-log.md` committed with the message `Audit complete`, **before** any change to `index.html`.

### Improve · Thursday, Build 1 and Build 2

The rebuild. Agile inside Improve: work the log top to bottom in short loops of fix, rerun web-check,
commit. **Checkpoint:** web-check passes at three widths, committed as `Rebuild passes web-check`.

### Control · Thursday Build 2 and Friday Build 2

Keyboard walk, partner test, one change from the test, screen reader walkthrough and recording, and the
note to the coordinator that tells her how to check it herself. **Checkpoint:** everything committed by
the end of Friday's commit window.

---

## Milestones

| Milestone | Due | Finished when |
|---|---|---|
| M1 Access plan | Week 3 Mon, end of Build 2 | All seven plan questions answered, committed |
| M2 Audit complete | Week 3 Wed, end of Build 2 | Twelve or more rows, six or more marked `me`, committed before any fix |
| M3 Rebuild passes | Week 3 Thu, end of Build 2 | web-check exit 0 at three widths; K1 to K10 filled in; partner test done |
| **Due** | **Week 3 Fri, end of commit window** | Walkthrough record complete, recording submitted, client note and decision log committed |

---

## Three worked scope examples

All three can earn full marks. They differ in ambition, not quality.

### Small, and completely finished

The supplied page, rebuilt to pass every requirement. Twelve to fourteen audit rows. A walkthrough
record whose S-rows quote what Narrator said. A client note that fits on half a page and gives her three
checks she can do herself.

**Who should choose it:** anyone who was out a day this week, or who is also preparing for BPA State.
**The risk:** finishing Thursday and spending Friday polishing the colours. Spend it on the client note,
which is half of the Documentation points.

### Medium, and the one most people should aim for

Small, plus a strong audit: eighteen or more rows, the arguable rows argued both ways, and a partner test
whose change is visible in the diff. The client note includes a short "when you edit this page" checklist.

**The risk:** writing eighteen rows and fixing twelve. Every row is fixed or carries a reason.

### Large, only if you are ahead by Wednesday

Medium, plus **your own Week 1 or Week 2 page**, run through passes 1 to 4 with its own short audit log
and fixes, and a second partner test on it.

**The risk, and it is real:** your own page is more interesting than the client's. The client's page is
the one being graded. **Your cut list puts your own page first.**

### Scope calibration, three signals

| If you | Aim for |
|---|---|
| missed a day this week, or had fewer than six audit rows at the end of Tuesday | Small |
| had ten rows by the end of Tuesday and the keyboard pass done Wednesday | Medium |
| committed `Audit complete` before Wednesday's Build 2 started | Large |

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

**Functionality, 25.** R1, R2, R3, R5, R6, and R9 hold. The instructor tabs through your page with the
mouse away and runs web-check. Ten points for web-check at three widths. Ten for a clean keyboard walk to
a working Sign up. Five for R3, R5, and R6 checked by hand.

**Code Quality, 20.** Scored on the five-dimension standard: Correctness, Security, Readability,
Performance, Requirements Fit. Native elements, not ARIA patches. Ids and classes that say what things
are. R7 holds. No leftover script.

**Documentation, 20.** This dimension is the writing.

| Document | Points | Full marks looks like |
|---|---|---|
| Access plan | 5 | Every question answered with specifics: a named kind of user, measured ratios, a decision for every image |
| Walkthrough record | 5 | K-rows, S-rows, and T-rows complete, each saying what was seen or heard rather than "pass." The audit log itself is graded in the lab, not here |
| Client note | 10 | Plain English, no jargon without a definition. Says what was wrong, what changed, and three checks she can do herself. **Makes no legal promise (R10).** Points her to where the rules are published |

**Client note partial credit.** 7 for a note that is accurate but written for a developer. 5 for a note
that lists changes without telling her how to check anything. **0 for a note that says the page is
compliant, fully accessible, or legally safe**, whatever else it does well.

**Process, 15.** The five checkpoint commits, in order, with the audit committed before the first fix.
A decision log with four real decisions, each with what you rejected. A commit at the end of every
period.

**Demonstration, 10.** The five-minute demo below, or the same checklist at your desk.

**Polish, 10.** The page still looks like the client's page. The walkthrough record quotes what you
heard. The client note is one page, proofread, and would not embarrass you if she forwarded it.

---

## The five-minute demo

Two students demo in Friday's review and close. Everyone else runs the same checklist at their desk with
the instructor, during Friday's Build 2 or the following Monday's Period 8.

| Time | What |
|---|---|
| 0:00 to 0:30 | **The volunteer's problem, in the client's words** |
| 0:30 to 1:30 | **Mouse away.** Tab from the top of the page to Sign up. Say the tab count |
| 1:30 to 2:30 | **One problem the tool missed.** Show the before, the after, and who it stopped |
| 2:30 to 3:30 | **Thirty seconds of your recording**, or read four lines of the listening log |
| 3:30 to 4:15 | **One thing your partner test changed** |
| 4:15 to 5:00 | **The question** |

### The question

Asked of every student, without notes:

> The coordinator asks you, "So are we compliant now?" What do you say?

**Full marks:** you describe what you checked and against which standard, you say you are not able to
make a legal determination, and you point her to where the rules are published.

### Demonstration checklist

| # | | Points |
|---|---|---|
| 1 | The problem stated in the client's terms | 1 |
| 2 | A keyboard walk to Sign up, with the count | 2 |
| 3 | One tool-missed problem, before and after, with the person it stopped | 2 |
| 4 | Recording or listening log shown | 2 |
| 5 | One change from the partner test | 1 |
| 6 | The question, answered without a legal promise | 2 |
| | **Total** | **10** |

---

## Submission checklist

- [ ] `web-check` exit 0 at 360, 768, 1280
- [ ] Mouse-away walk from the top to Sign up, with the count written down
- [ ] `audit-log.md` committed before the first fix
- [ ] `access-plan.md`, `walkthrough.md`, `client-note.md`, `decision-log.md` committed
- [ ] Recording submitted, not committed; or a listening log in `walkthrough.md`
- [ ] No real names or addresses anywhere. Search your files for `@`
- [ ] No sentence anywhere says compliant, fully accessible, or legally safe
- [ ] Pushed inside Friday's commit window

---

# Instructor appendix

**Reference implementation:** `09-project/reference-implementation/`. Instructor-only. It contains the
rebuilt page, a model access plan, a model audit log, a walkthrough record with the keyboard rows
verified and the screen reader rows **marked for you to confirm**, a model client note, and a decision
log. **Verified on the build machine:** web-check exit 0 at 360, 768, and 1280; the tab walk in the Lab
W03-01 key.

## The three ways this project goes wrong, and the intervention

**1. The student fixes as they audit.** You see it on Tuesday: `index.html` changed before `Audit
complete` exists. The record of what was wrong is gone, and so is half of the learning.
**Intervention, Tuesday:** have them `git diff` the starter commit and write the rows from the diff.
Tell them this costs them the Process points for the order, and why.

**2. web-check passes on Thursday and the student stops.** You see it Thursday Build 2: no K-rows, and
the student is restyling. **Intervention:** "Mouse behind the monitor. Tab to Sign up. Tell me the count."
Stand there while they do it.

**3. The client note promises compliance.** You see it Friday. It usually reads "your site is now ADA
compliant." **Intervention:** read R10 aloud, then ask the demo question. The rewrite takes ten minutes
and is the most valuable ten minutes of the week for a student who will have a real client in Week 7.

## What to say to a student whose scope is too big

> Which rows in your audit log are not fixed yet? Those come before your own page.

## What to say to a student whose scope is too small

Do not add a feature. Ask:

> Turn on Narrator and find the Spanish sentence. What did it sound like?

A student who finished early and never listened to the page has not finished.

## Grading time

About twelve minutes per student: three for web-check and the tab walk, two for the recording, seven for
the three documents. The client note takes longest and is worth the most per minute.
