# Project · The Sign-Up That Holds Up
## 145010 Web Design & Senior Capstone · Unit 5 · Week 5

**100 points. Projects category, 35 percent of your grade.**
**Due Week 5, Friday, at the end of the commit window.**

**Competencies:** 6.4.1 to 6.4.7 and 1.4.6.

---

## The brief

> From: the volunteer who runs the league website
>
> The schedule page you built last week cut my Saturday messages in half. Thank you. Now the other
> half.
>
> Every season I need people to run the snack table, set up the fields, and keep score. Right now
> parents reply to a group email, and I copy their names into a spreadsheet by hand. I lose some. I
> double-book some. Last spring I had six people for the snack table on one Saturday and nobody for
> scorekeeping.
>
> I want a sign-up page. Each job only needs so many people. When a job is full, it is full. I want to
> see who signed up for what without asking anyone.
>
> Please remember our coach who uses a screen reader, and the parent who cannot use a mouse. When
> somebody gets something wrong, I do not want them to give up. And I have been told that anything on
> a website can be sent by anybody, so please do not trust the page to keep my list clean.
>
> I do not want to collect anything I do not need. Some of these volunteers are high school students.

*The league and the volunteer are the same composite from Week 4, invented for this course.*

**That is the whole brief.** It does not list the fields, the jobs, the limits, or what "see who
signed up" means. **Pulling requirements out of it is the first thing you are graded on.**

---

## What you are building

A sign-up form, a Flask server, and a SQLite database, working together:

- a form, written from your own specification, with **at least one of each**: text input, radio
  group, checkbox group, drop-down, and submit and reset buttons, in fieldsets with legends
- **client-side checks** that help people, and **server-side checks** that defend the list
- the **accessible error pattern**, all six parts, from the server and in the browser
- a **live data source**: the database, plus at least one JSON web service that the page's script
  reads
- a page where the volunteer can see who signed up for what

Start from your Lab W05 app if you like. Say so in your decision log. The form, the rules, the
database table, and the pages must be your own design for this brief.

---

## Technical requirements

| # | Requirement | Why |
|---|---|---|
| R1 | Flask and SQLite. No other server framework, no front-end framework. | The week's stack. The standards are vanilla. |
| R2 | A **specification table** in your README, written before the form: label, control, `name`, `id`, values and rules. | 6.4.1: a form designed from specifications. |
| R3 | At least one text input, radio group, checkbox group, select, submit button, and reset button, with labels, in fieldsets with legends. | 6.4.2, 6.4.3, 6.4.5, 6.4.6 |
| R4 | The form posts to your server. A successful sign-up answers **303** and shows a confirmation. | 6.4.4, Post/Redirect/Get |
| R5 | **Every rule is checked on the server** with an allow list or a range, and a refused request answers **400** and stores nothing. | The brief's last warning. |
| R6 | A **job limit** enforced by the server from the database. | "When a job is full, it is full." |
| R7 | Every query uses `?` placeholders. | Injection. Gate 2 W05. |
| R8 | The **six-part accessible error pattern** on the server's error page. | The coach and the parent in the brief. |
| R9 | The same pattern in the browser, with `novalidate` set by your script, not your HTML. | So the page still protects people when the script fails. |
| R10 | **No positive tabindex.** `tabindex="-1"` only where script moves focus. | 6.4.6 |
| R11 | At least one **JSON web service** your page's script reads with `fetch`. | 6.4.7 |
| R12 | A **list page** for the volunteer. It shows no email addresses or other contact details. | "See who signed up", and "nothing I do not need". |
| R13 | Collect **only what the job needs**. Say in the README why each field exists. Every test value is invented. | Minors' data. The brief. |
| R14 | The server takes `--port`, refuses a busy port, and runs on **8425**. | The Windows trap from Monday. |
| R15 | `web-check` PASS on the saved form page **and** the saved error page. | The floor. |
| R16 | A **test file** with at least ten tests of your server rules, all passing. | Proof the defence works. |
| R17 | Every period ends with a commit. | Always. |

---

## Required repository structure

```
projects/w05-signup/
  app.py
  validation.py
  test_validation.py         or test_app.py
  schema.sql                 or the schema inside app.py
  templates/
  static/
  saved/                     pages saved for web-check
  README.md                  specification table, why each field exists, how to run, test results
  decision-log.md
  attack-log.md              every request you sent past the browser, and what came back
```

**`attack-log.md`** is where you prove R5. Use `send_raw.py` from the lab, changed for your fields,
or dev tools. At least four attacks: an empty required field, a value outside your allow list, a full
job, and a field the form cannot send at all. For each, what you sent, the status, and what was
stored.

---

## DMAIC checkpoints

### Define · Wednesday, Build 2

In `decision-log.md`: which jobs, how many people each, and which person in the brief each field
serves. Then the **specification table**, before any markup. The table goes in the README.

### Measure · Wednesday to Thursday

Count what the form collects. For each field, write one sentence on why the volunteer needs it. Any
field you cannot justify comes out. Record the job limits as numbers.

### Analyze · Thursday

Write the server rules as a list before you write `validation.py`. For each rule, name the attack
that would get past the browser without it.

### Improve · Thursday to Friday

Build: the form, the route, the rules and tests, the error pattern, the web service, the list page.

### Control · Friday

Run the tests, the four attacks, and `web-check` on both saved pages. Walk the error pattern by
keyboard. Update the README.

---

## Milestones

| Milestone | Due | Finished when |
|---|---|---|
| Define | Week 5 Wed, end of Build 2 | Decision log and specification table committed |
| Rules | Week 5 Thu, Period 8 | `validation.py` and at least ten passing tests committed |
| **Due** | **Week 5 Fri, commit window** | The last commit pushed in the window is the submission |

---

## Three worked scope examples

All three can earn full marks.

### Small: one job at a time

**What it is.** Name, email, one radio group of three jobs, a checkbox group of Saturdays, a shirt
size select, an agreement box. One limit per job. A list page grouped by job. A web service that
returns places left per job.

**Choose it if** Lab W05-02 took you all of Thursday.

**The risk.** Treating Small as permission to skip the browser-side error pattern. R9 is required at
every size.

### Medium: a limit per Saturday

**What it is.** The same fields, but each job has a limit **per Saturday**, so the snack table can be
full in Week 3 and open in Week 4. The server checks every chosen Saturday. The web service returns
places left per job per week, and the script disables full combinations.

**What it adds.** A rule that needs a query per chosen week, a message that names which Saturday is
full, and a harder error pattern for a checkbox group.

**Choose it if** your lab was finished on Thursday with time to spare. This is the scope the
volunteer's brief most directly asks for.

**The risk.** The message. "That job is full" is not enough when four Saturdays were chosen.

### Large: a change and cancel link

**What it is.** Medium, plus a confirmation code that lets a volunteer view or cancel their own
sign-up, and nobody else's.

**What it adds.** A lookup that must return exactly one sign-up, a POST to cancel it, and a new
failure mode: a code that belongs to somebody else.

**Choose it if** Medium passes every requirement by Thursday's Period 8.

**The risk.** Gate 2 W05 exactly. A lookup is where injection lives, and a guessable code is a
privacy problem. Write in your decision log how long your code is and why.

### Scope calibration

| If you | Aim for |
|---|---|
| finished Lab W05-02 in Thursday's Build 2 or later | Small |
| finished Lab W05-02 in Thursday's Build 1 | Medium |
| have Medium passing R1 to R16 by Thursday's Period 8 | Large |

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

**Functionality, 25.** The form stores good sign-ups and refuses bad ones, whatever sent them. The
limit holds. The error pattern works from the server and in the browser. The web service answers and
the page uses it. The list page shows who is doing what.

**Code Quality, 20.** The five-dimension standard. **A query built from text loses the Security share
in full.** Nothing stored on a refused request. Rules in one place, tested. No `innerHTML`. No
positive tabindex.

**Documentation, 20.** The specification table, a sentence for every field saying why it exists, how
to run it with the port, the test output, and `attack-log.md` with at least four real attacks.

**Process, 15.** Commits every period. Define on time. A decision log that records what you chose not
to collect.

**Demonstration, 10.** The script below.

**Polish, 10.** `web-check` PASS on both saved pages. Messages a volunteer would understand. The
server stopped at the end.

---

## The three-minute demo

| Time | What |
|---|---|
| 0:00 to 0:30 | **The brief, and one field you chose not to collect.** Why. |
| 0:30 to 1:15 | **Sign up with the keyboard.** Every control, then Sign up, then the confirmation. |
| 1:15 to 2:00 | **Get it wrong on purpose.** Empty submit: where does focus go? Follow one summary link. |
| 2:00 to 2:30 | **Attack it.** One request from your attack log, sent live, and the 400. |
| 2:30 to 3:00 | **The question.** |

### The question

> Your form already has `required` on that field. Show me the line on your server that makes it
> unnecessary to trust that.

---

## Submission checklist

- [ ] `python test_validation.py` (or your test file) passes with at least ten tests
- [ ] `attack-log.md` with four attacks, each refused, nothing stored
- [ ] `web-check` PASS on `saved/form.html` and `saved/form-errors.html`
- [ ] Empty submit with the keyboard moves focus to one summary
- [ ] Every query uses `?`
- [ ] No positive tabindex, no `innerHTML`
- [ ] The list page shows no contact details
- [ ] README: specification table, why each field exists, how to run on 8425, test output
- [ ] Every value in the database and the tests is invented
- [ ] Server stopped
- [ ] Committed and pushed inside Friday's commit window

---

# Instructor appendix

**Reference implementation:** `09-project/reference-implementation/`, **instructor only**. It is the
Small scope, done completely: a volunteer sign-up with three jobs, a season limit per job, a JSON
service, a list page that shortens names and hides emails, 15 unit tests, and 14 browser checks. Its
README has the verification record.

## The three ways this project usually goes wrong, and the intervention

**1. The server trusts the page again.** Students rebuild their form from scratch, get the markup
right, and forget to check a new field on the server. **Intervention:** "Show me your attack log."
If it has fewer than four entries, the next ten minutes are attacks.

**2. The limit is checked on the page only.** The script disables full jobs and the student stops
there. **Intervention:** re-enable a disabled option in dev tools and submit, while they watch.

**3. The form collects too much.** Phone number, address, date of birth, a parent's name. The brief
said not to. **Intervention:** ask for the README sentence that justifies each field. Most students
remove two fields in the next five minutes, and that is the lesson.

## What to say to a student whose scope is too big

"Which of R5, R8, and R9 is not finished?" A per-week limit with a half-built error pattern scores
below a season limit with a complete one. The brief names the coach and the parent before it names
Saturdays.

## What to say to a student whose scope is too small

"The volunteer said last spring she had six people on the snack table on one Saturday. Does your
limit stop that?" A season limit does not. That is Medium, and it is one more query.
