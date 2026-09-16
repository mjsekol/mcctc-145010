# Clinic · Reviewing Code You Did Not Write
## 145010 Senior Capstone · Clinic · Week 13, Tuesday

**The signal:** walkthroughs in 145130 that ended with "looks good." Peer Code Review 1 is tomorrow.
This note also covers what Review 2 checks on Week 14, Tuesday, so the instructor uses it again for
that briefing.

**Slides:** This clinic has no slide outline. It runs from the board.

**If you missed it,** you can learn the skill from this file alone. The two code examples were run on
the build machine with Python 3.13, and the output is pasted exactly.

**Competencies:** 1.1.9 (give and receive constructive feedback), 1.1.7 (problem solving and critical
thinking on work-related issues), 2.11.3 (investigate symptoms based on a chosen method), 2.12.3
(compare with expected performance)

**The examples use the Northside Community Garden, an invented organization.** It is a composite.

---

## The idea in plain language

**A review is a search, not a reading.** You are not checking whether the code looks tidy. You are
hunting for the place where it does something the requirement did not ask for, with a list of
questions in your hand and the program running in front of you.

## Why it exists

You cannot see your own blind spots. That is what a blind spot is. The author tested the inputs they
thought of. You are useful because you think of different ones.

**This is also a rehearsal.** In Week 18 your instructor scores your final code on the same
Five-Dimension Code Review: Correctness, Security, Readability, Performance, Requirements Fit.
Tomorrow you practice giving that score. On Friday you practice receiving it.

**This is harder than writing code.** Reading code you did not write is slow and uncomfortable, and
most of a real software job is exactly that. Expect the first twenty minutes to feel unproductive.

---

## How to read, in order

1. **Read the requirement first**, from the author's `docs/measure-analyze/requirements.md`. You
   cannot judge Requirements Fit against nothing.
2. **Run the main task yourself.** Write down what you ran and what happened. This is section 2 of
   the review.
3. **Follow one request all the way through**, from the page to the stored result. This is the
   "follow the path" troubleshooting method, used on purpose.
4. **Then attack the edges**: empty, zero, the largest value, the same action twice, an apostrophe.
5. **Then read for the other dimensions** with the checklist in the
   [Peer Code Review template](../05-labs/MCCTC_145010_Template_PeerCodeReview.md).

---

## Worked example 1 · an edge the author never tried

The author's tool-shed tracker has this function. Their test used three wait times.

```python
def average_wait(minutes):
    """Average wait at the garden tool shed, in minutes."""
    return sum(minutes) / len(minutes)

print(average_wait([4, 6, 11]))
print(average_wait([]))
```

Output, traceback shortened, last line exact:

```
7.0
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
```

**The finding, written well:**

| # | Where | Dimension | What happens because of it | Suggested fix | Severity |
|---|---|---|---|---|---|
| 1 | `stats.py`, `average_wait`, line 3 | Correctness | On a morning before anyone has used the shed, the dashboard page crashes for the coordinator. | Return `None` for an empty list and show "No visits yet" on the page. | must fix |

**Notice the fourth column.** It names a real person and a real moment. "Divides by zero" is true,
and "the coordinator's page crashes every morning" is the reason anyone cares.

## Worked example 2 · a comment that disagrees with the code

```python
shifts = [
    {"day": "Saturday", "bed": 1, "taken_by": "Aubrey"},
    {"day": "Saturday", "bed": 2, "taken_by": None},
    {"day": "Sunday", "bed": 3, "taken_by": None},
]

def open_shifts(day):
    # returns only the shifts nobody has claimed yet
    return [s for s in shifts if s["day"] == day]

print(open_shifts("Saturday"))
```

Output:

```
[{'day': 'Saturday', 'bed': 1, 'taken_by': 'Aubrey'}, {'day': 'Saturday', 'bed': 2, 'taken_by': None}]
```

**Aubrey's claimed shift is in the "open" list.** The comment says one thing and the code does
another. A reader who trusts the comment never finds this. That is why you run code instead of
reading comments.

This is two findings, and you record both: a Correctness finding (volunteers are offered a shift
that is already taken) and a Readability finding (the comment and the name promise a filter that is
not there).

## Worked example 3 · the same finding, written three ways

```
WEAK      "Security could be better."
WEAK      "You forgot to check the login again."
STRONG    "#4 · routes.py, delete_shift, line 58 · Security · Anyone who knows the
           address /shifts/7/delete can remove a shift without signing in, so a
           volunteer could delete another person's claim. · Check the session
           before the delete and return 403 otherwise. · must fix"
```

The first is not checkable. The second is about the person, and the template says to review the
code, never the coder. The third has a location, a dimension, a consequence, a fix, and a severity,
so the author can act on it without asking you a single question.

---

## What Review 2 checks, on Week 14, Tuesday

Review 2 uses a different reviewer. It does not start over. It checks four things, in section 6 of
the template:

1. **Every must-fix finding from Review 1**, and whether it is fixed. Evidence means a commit and a
   re-run, not the author's word.
2. **What changed since Review 1**, file by file.
3. **Anything added that no requirement asked for.** After Week 12, that is scope creep, and it is
   a Requirements Fit finding.
4. **Security, looked at again from scratch.** New code brings new input paths.

---

## The wrong version, and what it produces

```
## 3. Findings
| # | Where | Dimension | What happens | Fix | Severity |
| 1 | general | Readability | some names could be clearer | rename stuff | consider |

## 5. Scores
Correctness 20 · Security 20 · Readability 19 · Performance 20 · Requirements Fit 20 · Total 99
```

**What it produces:** a review with no evidence behind any score. The template's scoring guide says
a score with no evidence is not a score. The author learns nothing, the same defects reach the
panel in Week 18, and your review earns no credit as a review.

## Why the wrong version is tempting

The author is your friend, and they are sitting right there. Finding problems feels like an
accusation. You also assume the code works because it looked fine in their demo. **A review with no
findings means you did not look hard, not that the code is perfect.** The kind thing to do is find
the crash now, in Week 13, while there is still time to fix it.

---

## What to do in your project today

1. Tonight or in Period 8, commit, and write the commit hash your reviewer will read.
2. Pick the three to five files that matter most and list them for your reviewer.
3. Make sure `docs/measure-analyze/requirements.md` and your
   [Test Plan](../05-labs/MCCTC_145010_Template_TestPlan.md) are committed and current.
4. Read the whole [Peer Code Review template](../05-labs/MCCTC_145010_Template_PeerCodeReview.md),
   including the 60-minute protocol, so tomorrow runs on time.
5. Practice on your own code for ten minutes: run your main task with an empty input.

---

## Vocabulary

| Term | Meaning |
|---|---|
| **Finding** | One specific problem, with where, what happens, a fix, and a severity |
| **Must fix / should fix / consider** | The three severities in the template |
| **Edge case** | An input at a boundary: empty, zero, largest, repeated |
| **Follow the path** | Tracing one piece of data through every step to find where it goes wrong |
| **Scope creep** | Features added that no signed requirement asked for |

---

## Check yourself

1. You run the author's main task and it works. Name three edge inputs you try next for a shift
   sign-up form.
2. Rewrite this finding so the author can act on it: "The search is kind of slow."
3. In Review 2 the author says, "I fixed all the must-fix findings." What do you ask for before you
   write that down?

---

## Check your answers

**1.** Any three of: an empty first name, a bed number of zero or a negative number, the largest bed
number plus one, the same shift claimed twice, two people claiming the same shift at once, and a name
with an apostrophe.

**2.** A strong version: "#3 · search.py, find_plots · Performance · With invented test data of 200
beds, one search sends 201 queries to the database, because the code runs one query per bed inside
the loop, so the wait grows with every bed the garden adds. · One query with a join, which sent 1
query and returned the same 200 rows. · should fix." The key parts are a location, a counted or
measured number, the consequence, and a fix. (Both counts were measured on the build machine with a
small invented script.)

**3.** The commit hash for each fix and a re-run that shows the failing case now passes. Write the
evidence in section 6, not the author's statement.
