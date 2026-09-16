# Gate 2: Adversarial Review · Week 11
## 145010 Senior Capstone · Week 11, Thursday · first 40 minutes of the build period

**40 minutes. Individual. Silent. No AI tool.** You may and should run the code. You may not ask a
model whether it is correct, because a model is what you are reviewing.

The program is `W11/parts_board.py`. It comes with `W11/render_page.py` and
`W11/requirements-excerpt.md` in the same folder. Copy the whole `W11` folder somewhere you own.

Everything in this folder is invented for teaching. The co-op is a composite, not a real
organization, and every bin, account, and record in the code is made up.

---

## What you are looking at

This is the Improve phase, so the rubric changes. The last four weeks you scored an AI document on
the AI Output Evaluation parameters. This week you score AI code on the **Five-Dimension Code
Review**, the same standard your peer reviews and your final Technical Execution grade use.

Someone handed an AI assistant the requirements in `requirements-excerpt.md` and asked for the
Sprint 1 walking skeleton for the Parts Bin Board. It produced `parts_board.py`. It runs. It has
docstrings, sensible names, and comments that sound sure of themselves. It looks like a skeleton
you would be glad to have deployed on a Friday.

**Five defects, one in each dimension:**

| Dimension | What to look for |
|---|---|
| **Correctness** | It does not do what it says it does |
| **Security** | It accepts input it should refuse, or trusts what it was given |
| **Readability** | A name or comment that will mislead the next reader |
| **Performance** | Work done more times than it needs to be |
| **Requirements Fit** | Something the requirements asked for that is missing or wrong |

**One defect does not show up on the happy path.** With a working database in place, that part
looks fine. Read requirement R7 and think about the day the database is not there.

**One of the six items is genuinely arguable.** It is a design choice with a real case on each
side. You are scored on your reasoning, not on which side you pick.

---

## The requirements

Read `W11/requirements-excerpt.md` first. It is the signed scope this skeleton has to reach: R1
mark a bin low, R2 the coordinator's low list, R4 the board-open counter, R7 a health endpoint that
reports whether the service can reach its real data, and the non-functional requirements
including NF3 accessibility, NF6 security, and NF8 data size and speed. The numbers match the
full specification, so R3 is missing on purpose: it is Sprint 2 work.

A requirement you cannot point at a line of code for is a finding.

---

## How to run it

Set the database path to a file in your own folder, so nothing is written where it should not be.
The app creates and seeds the database on first run.

Windows, from the folder you copied:

```
set PARTS_DB=%CD%\parts_board.db
python parts_board.py
```

The service listens on port 5310. Open `http://127.0.0.1:5310/` in a browser to see the board.
Stop the server with Ctrl+C when you are done.

The other addresses:

- `http://127.0.0.1:5310/restock` is the coordinator's low list.
- `http://127.0.0.1:5310/health` is the health endpoint.

To mark a bin low from the page, use the form. To mark one low without the browser, from a second
terminal:

```
python -c "import urllib.request, urllib.parse; d=urllib.parse.urlencode({'bin_code':'B-01','note':'invented test note'}).encode(); print(urllib.request.urlopen('http://127.0.0.1:5310/report', d).read().decode())"
```

Use invented values, never your own name or anyone's real data.

## How to render the page for the accessibility tools

You cannot point a page checker at a running route directly, so `render_page.py` renders the home
page to an HTML file using Flask's test client. No server needed.

```
set PARTS_DB=%CD%\parts_board.db
python render_page.py %CD%\restock-home.html
```

That writes `restock-home.html`, which you can open in a browser and run through the tools you used
in the instruction phase. **`node tools/web-check/check.js` is one of those tools.** Deciding when
to reach for it, and reading what it says and what it does not say, is part of the review.

---

## What to submit

For each defect: **file and line number**, **which of the five dimensions**, **what goes wrong for
a real person** (a volunteer, the coordinator, or the next developer), **how you proved it** (the
command you ran, the page you read, or what you clicked, and what you saw), and **the fix**.

Then the arguable item, with the strongest case on each side and your own position with a reason.

Then one final entry: **what I was unsure about**, naming something specific. That entry is scored,
and a blank costs more than a wrong guess.

### How to spend 40 minutes

- **First 5:** read `requirements-excerpt.md`. For each requirement, point at the line meant to
  meet it.
- **Next 10:** run it. Mark a bin low. Open the coordinator list and the health endpoint. Compare
  what each returns to what its requirement asked for.
- **Next 10:** try the things the happy path does not. What does the health endpoint say if the
  database is not there? What does a form field accept that it should not? Feed the report form a
  value with a single quote in it and read what comes back.
- **Next 10:** render the page and decide which tools to run on it. Read every comment against the
  code under it, and ask whether each one is true.
- **Last 5:** decide what you think about the arguable item, and write down why.

---

## Scoring

Five defects, one point each, plus one for the unsure-about entry. **The security defect counts
double: missing it costs 2 points.** Your instructor states this before you start.

**Four of five defects is a strong score.**
