# Gate 2 · Week 13 · Volunteer Shift Sign-Up
## 145010 Web Design & Senior Capstone · Week 13, Friday, first 40 minutes of the build period

**40 minutes. Individual. Silent. No AI tool**, because a model wrote the code you are reviewing.

**You may and should run it.** Files are in `W13/`. **Use port 8161.**

---

## Why this today

You did Peer Code Review 1 on Wednesday. You read someone else's project and someone read yours.
The same Five-Dimension Code Review scores your Technical Execution in Week 18, so this is one more
rehearsal of the exact standard that grades your capstone.

Here the code is not a classmate's. It is what a food pantry got when it asked an AI assistant for
a sign-up app. It runs. The pantry coordinator has been using it. That is the trap: running is not
the same as correct, and the defects that end a capstone are the ones that survive a demo.

**Maple Street Food Pantry is an invented organization, a composite of small food pantries. No real
pantry is involved, and every name and email in the seed data is invented.**

---

## What you are looking at

Someone handed an AI assistant the requirements in `W13/REQUIREMENTS.md` and got the app in `W13/`.
Read the requirements before you read a line of code. Every defect is a place where the code and the
requirements disagree.

**Five defects, one in each dimension of the Five-Dimension Code Review:**

```
Correctness       an off-by-one, a wrong operator, a bad boundary
Security          input that reaches a query unsafely, data exposed, a missing check
Readability       a name that lies, a comment that contradicts the code under it
Performance       repeated work, a query run more times than it needs to be
Requirements Fit  something the requirements asked for that is missing or wrong
```

**One of the five is subtle.** Most of the class will read past it. Take the difficulty seriously.

**There is also one item that is genuinely arguable**, and it is not one of the five. You are scored
on your reasoning for it, not on which side you land.

---

## How to run it · port 8161

The seed script builds the database. The app takes an explicit port.

```
python seed.py
python app.py --port 8161
```

Open `http://127.0.0.1:8161` in Chrome. To watch every SQL statement the app runs while you use it,
start it with the trace flag:

```
python app.py --port 8161 --trace-sql
```

Stop the server with Ctrl+C when you are done, and confirm nothing is still listening on 8161
before you move on. Run `seed.py` again at any time to reset the data.

**web-check works on saved HTML, not a running server.** Save the rendered page and run the checker
on the file:

```
node tools/web-check/check.js <your saved page>.html
```

To save the page: open `http://127.0.0.1:8161` in Chrome, right-click, Save As, and choose
"Webpage, HTML Only."

---

## What to hand in

### Five findings, one per dimension

For each finding:

```
Dimension          which of the five
File and line      the exact file and line number
The requirement    which numbered requirement it breaks
What goes wrong     for a real person, in one sentence
How you proved it   the command you ran or what you read, and what you saw
The fix             what you would change
```

### Plus one entry: the thing you are unsure about

```
What you noticed
The case that it is fine
The case that it is a defect
What would settle it
```

Name something specific. A blank costs more than a wrong guess.

---

## How to spend 40 minutes

- **First 5:** read `REQUIREMENTS.md` one requirement at a time. For each, find the code meant to
  meet it.
- **Next 10:** run the sign-up. Fill a small shift past the number of spots it shows. Count what the
  database ends up holding. Use the "Intake desk" shift, which has few spots.
- **Next 10:** use the "check my shifts" lookup with invented input, not your own. Try an email that
  is not a plain address. Read what comes back.
- **Next 10:** start the app with `--trace-sql`, load the home page once, and count the SQL
  statements it printed. Then save the page and run web-check.
- **Last 5:** read every function name and every comment against the code under it. Ask whether each
  one is true.

---

## Scoring

| Item | Points |
|---|---|
| Correctness finding | 1 |
| **Security finding** | **1, and missing it costs 2** |
| Readability finding | 1 |
| Performance finding | 1 |
| Requirements Fit finding | 1 |
| The unsure-about entry, with both cases | 1 |
| **Total** | **6** |

**The security defect is double-penalized.** A capstone with an injection hole fails its own
Security dimension no matter how good the rest is. Your instructor states this before you start.

**Four of six is a strong score.**

---

## One rule for today

**A finding with no file and line number is not a finding.** Every one of the five is on a line you
can point at.
