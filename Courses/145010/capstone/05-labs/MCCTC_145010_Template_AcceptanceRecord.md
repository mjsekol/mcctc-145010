# Template · Acceptance Record
## 145010 Senior Capstone · Week 16

**Commit as:** `docs/control/acceptance-record.md`, **unsigned**. The signed copy goes to your
instructor.
**Due:** run sheet during the acceptance run, Week 16, Wednesday or Thursday. The complete record,
with the stakeholder's decision, Week 16, Friday.

**Competencies this evidences:** 2.12.6 (seek stakeholder acceptance upon successful completion of
the test plan), 2.12.5 (make corrections indicated by test results), 2.12.3 (compare with expected
performance on targeted platforms), 2.12.1 (the agreed procedure, used as agreed), 1.2.12
(technical writing to complete forms and reports), 1.2.13 (stakeholders).

---

## Why this exists

**This is the record your Stakeholder Outcome score is built on.** It says what you and your
stakeholder agreed in Week 8, what happened when you checked it together, and what they decided.

**The one rule of the run:** you never change a case because it is about to fail. That is the whole
reason the procedure was agreed before you started building.

**The section people leave empty is section 5.** Known and not fixed. A record with something in it
is an honest record. A record with nothing in it makes a reader wonder what was left out.

---

## Before the run

- [ ] You are running the acceptance procedure **as committed** when the stakeholder agreed it.
      Write that commit hash below.
- [ ] The deployed system is the one being tested, not your local copy.
- [ ] Your instructor is present, or the call is one your instructor approved.
- [ ] You have read the pre-run script from your test plan's section 7 aloud.

---

```markdown
# Acceptance Record · <project name>
Acceptance run: Week 16, <day>

## 1. What was agreed
- **Acceptance agreement version:** <n>, signed Week 8, <day>
- **Changes agreed since, by change request:** <CR numbers, or "none">
- **Acceptance procedure:** test plan section 7, agreed Week <n>, <day>, at commit <hash>
- **What the stakeholder changed when they read the procedure:** <or "nothing," recorded honestly>

## 2. The run
- **Where:** <the deployed system, at its address or location>
- **Devices and platforms:** <list>
- **Stakeholder side present:** <roles>
- **Supervision:** <instructor present / instructor-approved call / decided in writing>
- **If the stakeholder could not attend:** <the procedure and results were sent in writing on
  Week <n>, <day>, and their written decision is recorded in section 6. The run was not recorded
  as attended.>

## 3. Results
| AC | Verdict | What was actually seen |
|---|---|---|
| AC-1 | PASS / FAIL / NOT RUN | <a message, a count, a time, a screen, not "it worked"> |
| AC-2 | | |
| AC-3 | | |
| AC-4 | | |
| AC-5 | | |
| AC-6 | | |

First run: PASS ___  FAIL ___  NOT RUN ___

**Every NOT RUN has a reason:** <...>
**What the stakeholder said during the run** (their words, labelled as their opinion): <...>
**Cases the stakeholder did not understand:** <each is a finding about the writing>

## 4. Corrections
*One entry per failed case. A correction with no re-run under it is a plan, not a correction.*

### Correction for AC-<n>
- **What failed:** <...>
- **What I changed:** <file and line, commit hash>
- **Re-run:** Week 16, <day>, <PASS / FAIL>, <what was seen>

**Whole procedure re-run after the last correction:** Week 16, <day>, commit <hash>
After corrections: PASS ___  FAIL ___  NOT RUN ___

## 5. Known and not fixed
*Anything still failing or missing, and what you and the stakeholder agreed to do about it.*
| Item | Why it is not fixed | What was agreed |
|---|---|---|
| | | <accepted as is / fixed by Week 17 Friday / moved to future improvements> |

## 6. The stakeholder's decision
- **Decision:** <accepted / accepted with agreed follow-up / not accepted>
- **In their words:** "<...>"
- **Follow-up agreed, with dates:** <...>
- **Given:** Week 16, <day>, <in person / on an approved call / in writing>

*Signed copy kept by the instructor. Do not commit signatures.*

Stakeholder:   ______________________________   Week 16, ________
Student:       ______________________________   Week 16, ________
Instructor:    ______________________________   Week 16, ________
```

---

## If the run does not go as planned

**A case turns out to be wrong, not the project.** Say so to the stakeholder before running it.
Record it NOT RUN with the reason. You and the stakeholder decide together whether to change it,
out loud, and the change is written into a change request. It never happens quietly in a text
editor.

**Everything passed.** Possible. Before you celebrate, ask which case could have failed and what
would have had to be true for it to fail. If the honest answer is none, your cases were written to
pass. Tell your instructor.

**The stakeholder says "not accepted."** Record it exactly, with the reason. Ask what would change
their decision and whether it can be done by Week 17, Friday. A clear "not accepted" with an honest
record scores better than a vague "accepted" with none.

**The stakeholder cannot be reached at all.** Follow the steps in the
[Control phase guide](MCCTC_145010_PhaseGuide_Control.md#if-your-stakeholder-disappears).
