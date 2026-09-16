# Gate 2 · Week 14 · Parts Checkout List
## 145010 Web Design & Senior Capstone · Week 14, Friday, first 40 minutes of the build period

**40 minutes. Individual. Silent. No AI tool**, because a model wrote the page you are reviewing.

**You may and should open it and use it.** Files are in `W14/`. It runs from a file, with no server.

---

## Why this today

This is release-candidate week. Today your own project has to be finished, tested, and ready for
real users on Monday. A release candidate is the version you would ship. The whole point of a
release candidate is that it has been looked at hard, not that it runs.

So today you look hard at one. The robotics club got this parts-checkout page from an AI assistant.
It works. Members have been using it. The same Five-Dimension Code Review that scores this page
scores your Technical Execution in Week 18, and the defect that gets past you here is the kind that
gets past you there.

**Ridgeview Robotics Club is an invented organization, a composite of high school robotics clubs. No
real club is involved, and every name and note in the data is invented.**

---

## What you are looking at

A single page with client-side JavaScript. No framework, no network. Members type a part and a short
note, the checkout appears in the list, a filter box narrows the list as you type, and a count shows
how many parts are due back within 7 days. It was built from `W14/REQUIREMENTS.md`. Read the
requirements first. Every defect is a place where the code and the requirements disagree.

**Five defects, one in each dimension of the Five-Dimension Code Review:**

```
Correctness       an off-by-one, a wrong operator, a bad boundary
Security          input that can run as code, a missing check
Readability       a name that lies, a comment that contradicts the code under it
Performance       repeated work, something redone that did not change
Requirements Fit  something the requirements asked for that is missing or wrong
```

**One of the five is subtle.** Most of the class will read past it.

**There is also one item that is genuinely arguable**, and it is not one of the five. You are scored
on your reasoning for it, not on which side you land.

---

## How to run it

The page runs straight from the file. No server, no port.

```
Open W14/index.html in Chrome.
```

To review it the way a browser sees it, open Chrome DevTools (F12). Use the Console tab to watch for
errors and the Elements tab to read the live page.

**web-check runs on the file itself.** From the repository root:

```
node tools/web-check/check.js Courses/145010/capstone/07-gate2-adversarial/W14/index.html
```

**One safety rule for the security defect.** You are testing whether text you type can run as code.
Do not use anything that could be destructive, and never test this on a real site. A safe test note
is an image tag with a broken source and an `onerror` that sets a value you can read, not one that
pops up a box. The instructor will show a safe payload if you have not seen one.

---

## What to hand in

### Five findings, one per dimension

For each finding:

```
Dimension          which of the five
File and line      the exact file and line number
The requirement    which numbered requirement it breaks
What goes wrong     for a real person, in one sentence
How you proved it   what you typed, clicked, ran, or read, and what you saw
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
  meet it. Open `parts-data.js` and note the reference date the count is measured from.
- **Next 10:** work out by hand how many parts are due within 7 days of that reference date. Compare
  your number with the number the page shows.
- **Next 10:** type a note that tries to run code, add it, and see what happens. Watch the Console.
- **Next 10:** open the Performance or Console tab, type slowly in the filter box, and ask what the
  page redoes on each keystroke. Then run web-check on the file.
- **Last 5:** read every function name and every comment against the code under it.

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

**The security defect is double-penalized.** A page that runs whatever a user types is the failure
this week is built around. Your instructor states this before you start.

**Four of six is a strong score.**

---

## One rule for today

**A finding with no file and line number is not a finding.** Every one of the five is on a line you
can point at.
