# Template · Written Test Plan and Acceptance Procedure
## 145010 Senior Capstone · Week 10, Wednesday, and used through Week 17

**Commit as:** `docs/measure-analyze/test-plan.md`
**Due:** Week 10, Wednesday. Acceptance procedure (section 7) sent to the stakeholder Week 10,
Thursday, and agreed by Week 11, Friday. Results added every sprint and after every correction.

**Competencies this evidences:** 2.12.1 (a written procedure agreed by stakeholders and the team
for determining acceptability), 2.12.2 (a test system that accurately mimics external interfaces),
2.12.3 (test cases that are realistic, compare with expected performance, and include targeted
platforms and device types), 2.12.4 (develop, perform, and document usability and testing
integration), 2.12.5 (make corrections indicated by test results), 2.13.5 (test the delivered
application), 2.7.4 (how browsers and devices affect a page, including screen readers), 6.5.11
(cross-platform and cross-browser compatibility and validation), 2.11.6 (test a solution).

---

## Why this exists

**A test plan is a list of ways your project could be wrong, written before you know whether it
is.** Writing it in Week 10 means you test what the stakeholder needs. Writing it in Week 15 means
you test what you happened to build.

**The failure to avoid is a test that cannot fail.** "The app works correctly" passes every time
because nobody can disagree with it. A real test case has a starting state, an action, and an
expected result specific enough that it could come out wrong.

**The second failure is testing only on your own machine.** Your requirements name devices and
browsers. Every one of them gets cases.

---

## What a realistic test case looks like

| Weak | Strong |
|---|---|
| Test that shifts can be claimed. | **T-07.** Starting state: shift S3 is open, two browsers are signed out. Action: both open S3 and press Claim within ten seconds of each other. Expected: the first claim succeeds; the second browser shows "This shift was already taken" and S3 lists one volunteer. Platform: Chrome desktop and a phone browser. |
| Test the alarm. | **T-12.** Starting state: test mode replaying the recorded hot afternoon. Action: let the replay pass the 35 degree threshold. Expected: the panel shows the alarm banner within one reading interval, the alarm history gains one row, and the dashboard shows the alarm state on refresh. |
| Test that the AI handles bad input. | **T-19.** Starting state: stub model server running in "malformed" mode on the test port. Action: ask evaluation question Q4. Expected: the answer is labelled as the fallback, shows a manual and page from keyword search, and the service log records a parse failure with no question text in it. |

**These come from composite projects.** Write your own.

---

```markdown
# Test Plan · <project name>
Version <1.0>   Written: Week 10, <day>   Supports: Requirements version <n>

## 1. What this plan covers
- **Requirements covered:** R1 to R<n>, E1 to E<n>, NF1 to NF<n>
- **Not tested, and why:** <for example: load from hundreds of users, because the stakeholder's
  group has twenty people>

## 2. Targeted platforms and devices
*From the requirements. Every row here gets cases.*

| ID | Platform | Device or screen | Why it is targeted |
|---|---|---|---|
| P1 | <browser, current version on lab machines> | desktop, 1280 wide | <stakeholder's office machine> |
| P2 | <phone browser> | phone, 360 wide | <volunteers use phones> |
| P3 | <keyboard only> | desktop | NF3 |
| P4 | <screen reader: Windows Narrator, or another your instructor approves> | desktop | NF3 |
| P5 | <operator panel monitor / lab machine running the model> | | |

## 3. The test setup
*2.12.2. Copied from the architecture's section 9, with the exact commands.*

| Stand-in | Start command | Modes it simulates |
|---|---|---|
| | | |

## 4. Test cases

| ID | Req | Platform | Starting state | Action | Expected result |
|---|---|---|---|---|---|
| T-01 | R1 | P1 | | | |
| T-02 | R1 | P2 | | | |
| T-03 | E1 | P1 | | | |

**Include at least:**
- one case for every functional requirement, on every targeted platform it applies to
- one case for every failure in the requirements' section 2
- one security case and one privacy case
- validation: every page through the HTML validator, zero errors (NF5)
- accessibility: every page through the automated checker, zero violations; a keyboard-only
  walkthrough of every main task; a screen reader walkthrough of the main page (NF3)
- one performance case with a measured number (NF1)
- one integration case that runs a whole task through every component, on the deployed system
- one case that proves the thirty-day health log is being written (NF2)

## 5. What automated tools cannot tell you
*The accessibility checker finds some problems and misses others. List what your human checks
cover that the tool does not: whether alternative text is meaningful, whether the focus order makes
sense, whether a screen reader user can finish the task, whether link text makes sense on its own.*

- <...>

## 6. Results
*Add a block every time you run the plan. Never delete an old block.*

### Run <n> · Week <n>, <day> · commit <hash> · <sprint review / release candidate / after corrections / delivered system>
| ID | Result | What you actually saw |
|---|---|---|
| T-01 | PASS / FAIL / NOT RUN | <an exit code, a message, a count, a screenshot file name> |

Totals: PASS <n>  FAIL <n>  NOT RUN <n>
Corrections made because of this run: <list, each with the case, the change, and the re-run>

**After any correction, re-run the whole plan, not only the failed case.**

## 7. Acceptance procedure
*2.12.1. The cases you and the stakeholder run together in Week 16. One row per acceptance
criterion in the signed agreement. Written for the stakeholder to follow.*

- **Agreement version:** <n>
- **Sent to stakeholder:** Week 10, <day>   **Agreed:** Week <n>, <day>, <in writing / in a meeting>
- **What they changed when they read it:** <or "nothing," recorded honestly>
- **Where it will be run:** <the deployed system, on <devices>>
- **Stakeholder role running it:** <role>

**Read this to the stakeholder before starting:**
> Some of these cases test what happens when something goes wrong, so a message on screen may be
> the right result. If something fails that we did not expect, I will write it down and fix it
> afterward rather than fix it in front of you. If any step does not make sense, tell me, because
> that is something I need to fix in the writing.

| AC | Starting state | What to do | What you should see | Result | Evidence |
|---|---|---|---|---|---|
| AC-1 | | | | | |
| AC-2 | | | | | |

**Verdicts:** PASS (you saw the expected result), FAIL (you did not), NOT RUN (it could not be run,
with the reason). NOT RUN is never a pass.

**The rule:** a case is never changed because it is about to fail. A case that turns out to be
wrong is recorded as NOT RUN, and any change is agreed in writing by both of you.
```

---

## Before you commit · self-check

- [ ] Every case has a starting state and an expected result that could fail.
- [ ] Every targeted platform has cases.
- [ ] Every stand-in in section 3 starts with an explicit port.
- [ ] Section 5 names at least three things the automated checker cannot tell you.
- [ ] Section 7 has one row per signed acceptance criterion and nothing else.
