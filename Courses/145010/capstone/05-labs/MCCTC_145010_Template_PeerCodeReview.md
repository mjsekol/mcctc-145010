# Template · Peer Code Review
## 145010 Senior Capstone · Review 1 Week 13, Wednesday · Review 2 Week 14, Tuesday

**Commit as:** `docs/improve/peer-review-1.md` and `docs/improve/peer-review-2.md`, in the
repository of the project **being reviewed**. The reviewer writes sections 1 to 5. The author
writes section 7.
**Due:** the review at the end of the build period on review day. The author response by Friday of
the same week.

**Competencies this evidences:** 1.1.9 (give and receive constructive feedback to improve work
habits), 1.1.7 (problem-solving and critical thinking on work-related issues), 1.2.5
(communicate for an intended audience), 2.11.3 (investigate symptoms using a chosen
methodology), 2.12.3 (compare with expected performance).

---

## Why this exists

**You cannot see your own blind spots, by definition.** A reader who did not write the code finds
the assumption you did not know you made. That is worth more in Week 13, when you can still fix it,
than a panel finding it in Week 18.

**The same standard scores your final project.** Technical Execution is scored on the
Five-Dimension Code Review. Two peer reviews are two rehearsals of the score that counts.

**The failure to avoid, as a reviewer:** "Looks good." A review with no findings means the reviewer
did not look hard, not that the code is perfect.

**The failure to avoid, as an author:** defending every finding. You are allowed to reject a
finding. You have to say why, in writing, and a finding you rejected without a reason is scored as
ignored.

---

## How it runs · 60 minutes

| Minutes | What happens |
|---|---|
| **Before** | The author commits, writes the commit hash below, and gives the reviewer the requirements, the test plan, and a list of the three to five files that matter most. |
| **0-10** | The author walks through the main task, file by file. The reviewer listens and takes notes. No defending, no fixing. |
| **10-45** | The reviewer reads alone, with the checklist below, and fills in the findings table. The author works on something else. |
| **45-55** | The reviewer explains each finding. The author asks questions. **The author does not argue yet.** |
| **55-60** | Scores. Commit the review to the author's repository. |

**Pair with someone who reads your language.** A C# panel reviewed by a Python-only reader is
still useful for Readability and Requirements Fit and weaker for the rest. Your instructor sets the
pairs. **Review 2 uses a different reviewer from Review 1.**

**Review the code, never the coder.** "This function does not check for an empty list" is a
finding. "You forgot again" is not.

---

## The checklist, by dimension

**Correctness**
- Does the main task do what the requirement says, for normal input?
- What happens at the edges: empty, zero, the largest value, the same action twice?
- Do the tests the author ran actually test the requirement?

**Security**
- Any secret in the code, a config file, or the history?
- Does anything change data without checking who is asking?
- Does any input reach a database query, a file path, or a command without being handled safely?
- Does any response or log contain personal data or internal error detail?

**Readability**
- Could you explain each function after reading it once?
- Do names say what things are? Do comments agree with the code?
- Is anything repeated that should be one function?

**Performance**
- Is anything done inside a loop that could be done once?
- Is data read or requested more often than it needs to be?
- Does anything grow without limit: logs, tables, memory?

**Requirements Fit**
- Is every in-scope requirement present?
- Is anything present that no requirement asked for? After Week 12, that is scope creep.
- Does the failure behavior match the requirements' "what happens when things go wrong" section?

---

```markdown
# Peer Code Review · Review <1 or 2>

Project reviewed: <name>                 Author: <first name>
Reviewer: <first name>                   Week <n>, <day>
Commit reviewed: <hash>
Files read: <list>

## 1. What the author walked through
<Two or three sentences in your own words. If you cannot write this, ask before you score.>

## 2. What I ran
| Command or check | Result |
|---|---|
| <the project's tests> | <passed n, failed n> |
| <the validator or checker, for web pages> | <errors n> |
| <the app itself, main task> | <what happened> |

## 3. Findings
| # | Where (file, function, line) | Dimension | What happens because of it | Suggested fix | Severity |
|---|---|---|---|---|---|
| 1 | | | | | must fix / should fix / consider |
| 2 | | | | | |

**Severity:** **must fix** means a requirement fails, data is exposed, or it breaks for a real user.
**Should fix** means it will cause trouble later. **Consider** means it would be better another way.

## 4. One thing this code does well
<Specific. Name the file or function and say why it works.>

## 5. Scores · Five-Dimension Code Review
| Dimension | Score (0-20) | Evidence: finding numbers or a short reason |
|---|---|---|
| Correctness | | |
| Security | | |
| Readability | | |
| Performance | | |
| Requirements Fit | | |
| **Total** | **/100** | |

## 6. Review 2 only
- Must-fix findings from Review 1, and whether each is fixed: <list with evidence>
- What changed since Review 1: <files and features>
- Anything added that no requirement asked for: <list, or "none found">
- Security, looked at again from scratch: <findings or "none found">

## 7. Author response · written by the author by Friday
| Finding # | Accepted / rejected / deferred | What I did, or why not | Commit |
|---|---|---|---|
| | | | |
```

---

## Scoring guide

Score what you found evidence for, not a general impression. A score with no evidence in column
three is not a score.

| Score | Meaning, for any dimension |
|---|---|
| **18-20** | No finding above **consider**. You looked hard, and you can say where. |
| **14-17** | One **should fix**, or several **consider** findings. |
| **10-13** | One **must fix**, or several **should fix** findings. |
| **0-9** | More than one **must fix**, or the dimension could not be checked because the code does not run. |

**A must-fix security finding caps Security at 9.** Unchecked input and exposed secrets are how
small programs cause real damage.

**Requirements Fit needs the requirements.** If the author cannot produce
`docs/measure-analyze/requirements.md`, this row scores 0-9, because nothing can be checked against
nothing.

---

## Before you commit · self-check

- [ ] At least three findings, or a written reason why you found fewer after looking hard.
- [ ] Every finding says where, what happens, and a fix.
- [ ] Every score has evidence.
- [ ] Section 4 is specific.
- [ ] Nothing in the review is about the person.
