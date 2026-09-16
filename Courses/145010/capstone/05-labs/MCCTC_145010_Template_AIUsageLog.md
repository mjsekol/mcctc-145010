# Template · AI Usage Log
## 145010 Senior Capstone · Weeks 7-18, written as you work

**Commit as:** `ai-usage-log.md` at the top of your repository.
**Due:** continuously, from the first AI interaction that affects anything you submit.

**Competencies this evidences:** 1.3.8 (verify compliance with computer and intellectual property
laws and regulations), 1.2.1 (extract relevant, valid information and cite sources), 1.1.7
(critical thinking when making decisions).

---

## Why this exists

You have kept one of these since Week 1 of junior year. In the capstone it matters more, for three
reasons.

1. **A stakeholder may ask how something was built.** "I do not remember" is not an answer you
   want to give to someone outside this building.
2. **The only way to fail outright is submitting work you cannot explain.** Writing down what you
   changed and how you verified it is how you make sure you can.
3. **The panel will ask.** "Where did you overrule an AI tool?" is a defense question. The answer
   is in this file or nowhere.

**The failure to avoid is a log written at the end from memory.** It reads like a guess because it
is one.

---

## The rules

1. **Every AI interaction that changed something you submitted gets an entry.** Code, documents,
   messages to your stakeholder, test cases, commit messages.
2. **Only tools your instructor has approved.** Any model your project calls runs locally. No
   commercial AI developer account is used for any part of the capstone.
3. **No personal information goes into any AI tool.** Not yours, not your stakeholder's, not their
   staff's or customers'. No names, no records, no photographs, no database rows with real data in
   them. Use invented examples.
4. **No stakeholder material goes into an AI tool without their written permission**, even if it
   has no personal data in it.
5. **Nothing from a usability session goes into an AI tool.** Not the notes, not a summary.
6. **Gate 1 reps never appear here.** Gate 1 is closed.
7. **"I used it and changed nothing" is a legitimate entry**, and it is the one you will be asked
   about. Accepting output is a decision you own.

---

```markdown
# AI Usage Log · <project name>

## Entry <n> · Week <n>, <day> · <what this affected>

**Tool:** <the approved tool or local model, and version if known>

**Personal data check:** I confirmed the prompt contained no personal information and no
stakeholder material without permission. <yes>

**What I asked:**
> <the prompt, exactly as sent>

**What came back, in summary:**
<two or three sentences>

**Evaluation**
| Parameter | What I found |
|---|---|
| Validity | <is it correct? how do I know?> |
| Relevance | <does it fit my project, or is it generic?> |
| Authenticity | <can I trace where any facts, code patterns, or citations came from?> |
| Potential Bias | <does it assume a kind of user, language, or situation that does not fit?> |
| Hallucinations | <anything invented: a function, a setting, a citation, a statistic?> |

**What I kept:**

**What I changed, and why:**

**How I verified it:** <ran it, tested it, checked the official documentation, compared with my
requirements>

**Licensing or ownership note:** <anything that affects LICENSING.md, or "none">
```

**The last four fields are the graded ones.** The first four are record keeping.

---

## A worked example

**Composite example.** Write your own.

```markdown
## Entry 9 · Week 12, Tuesday · src/health.py

**Tool:** the local model on lab machine 4

**Personal data check:** yes. The prompt described the route in general terms only.

**What I asked:**
> Write a Flask route at /health that returns JSON with the app version and whether the
> database connection works. Use SQLAlchemy.

**What came back, in summary:**
A route that ran a SELECT 1 query inside a try block, returned status 200 with "db": "ok" on
success, and returned status 200 with "db": "error" and the exception message on failure.

**Evaluation**
| Parameter | What I found |
|---|---|
| Validity | Ran it. The success path worked. |
| Relevance | My project does not use SQLAlchemy. It uses sqlite3 directly. |
| Authenticity | The pattern matches the Flask documentation's JSON responses. |
| Potential Bias | None I could see. |
| Hallucinations | None, but it returned the raw exception text, which my requirements forbid. |

**What I kept:** the idea of a trivial query to test the connection, and the JSON shape.

**What I changed, and why:** rewrote it for sqlite3. Changed the failure status to 503 so my
scheduled health check counts it as a failure. Removed the exception text from the response,
because NF7 says no internal detail reaches a response, and logged it on the server instead.

**How I verified it:** test T-22 with the database file renamed. The check logged
status=503 db=down and the response body had no exception text.

**Licensing or ownership note:** none.
```

---

## Before you commit · self-check

- [ ] Every entry was written the same day.
- [ ] Every prompt is pasted exactly, and none contains personal data.
- [ ] "What I changed" and "How I verified" have real content in most entries.
- [ ] The log agrees with your commits. A file that is plainly AI-assisted has an entry.
