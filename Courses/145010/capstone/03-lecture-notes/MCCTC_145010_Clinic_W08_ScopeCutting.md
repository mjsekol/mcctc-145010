# Clinic · Cutting Scope
## 145010 Senior Capstone · Week 8, Tuesday · 15 minutes · Define

**Slides for this clinic:** This clinic has no slide outline. It runs at the board.

**When this clinic runs.** Week 8, Tuesday, or any week the room shows this signal: any "no" from
Monday evening's reading of the drafts. There always is one.

**If you missed it,** you can learn the skill from this file alone.

**Competencies:** 2.9.2 (determine the scope and purpose of the project), 1.1.7 (problem-solving and
critical thinking when making decisions), 1.2.7 (problem-solving and consensus-building to determine
next steps), 1.1.9 (give and receive constructive feedback), 2.9.5 (task breakdown and
deliverables).

---

## Why this exists

**Today your instructor tells you whether your proposal will finish.** For some of you the answer is
no. That is the most useful thing anyone will say to you this semester, because Week 8 is the
cheapest week to cut. Tomorrow the proposal goes to your stakeholder. After that, every cut is a
conversation with an adult who has already read your promise.

The [scope rule](../09-project/MCCTC_145010_Capstone_Specification.md#the-scope-rule) exists
because oversized scope is the most common way a capstone fails, and it is only fixable early.

**Hearing "no" is hard. Cutting well is a skill.** A student who cuts badly keeps every feature at
half size and finishes none of them. This clinic is how to cut so that what is left is finished.

---

## The skill in plain language

**1 · Write down what your instructor says, word for word.** Yes or no. The three tasks that will
take four times longer. What to cut. Do not argue in the conference. Ask questions if something is
unclear.

**2 · Reopen your needs-discovery meeting record.** Read the "What they said" section. The thing
your stakeholder named is the thing that stays.

**3 · Sort every in-scope item into one of three piles.**

| Pile | Test | What happens to it |
|---|---|---|
| **Named** | The stakeholder said it, and the meeting record shows it | Stays in scope |
| **Needed** | A named item cannot work without it: sign-in to protect a page, a health check | Stays in scope |
| **Not named** | Everything else, however good | Goes to the stretch list or out of scope |

**4 · Cut whole features, not slices of every feature.** Five finished things beat eight things at
sixty percent.

**5 · Know the difference between a stretch goal and a line.** A stretch goal is a good idea that
waits. It starts only when every acceptance criterion already passes. A line is something this
program does not do at all: switching real equipment, taking payments, storing personal data the
job does not need, or putting anyone's personal data into an AI tool. Lines go in out of scope with
the reason.

**6 · Write the minimum viable version in two or three sentences.** The smallest thing your
stakeholder would actually use.

**7 · Record every cut as a decision** in `decision-log.md`, with the reason.

**8 · Re-add the hours.** The Improve total must be 50 or fewer. Bring it back to your instructor
before the proposal goes out.

---

## Worked example 1 · The Parts Bin Board, before and after the cut

*Composite, not a real organization or person.* A volunteer-run community bike repair co-op.
Repairs stall because a parts bin is empty and nobody told the shop coordinator. The coordinator
said, "I do not need anything fancy." Some volunteers have no smartphone and use the donated desktop
by the door.

**The draft's Improve tasks, already estimated with the four-times rule:**

| Task | Hours | Pile | Decision |
|---|---|---|---|
| Anyone with the shop link marks a bin low | 4 | Named | Keep |
| Optional note, 120 characters at most, no name | 2 | Named | Keep |
| Coordinator sign-in | 8 | Needed | Keep. It protects the low list |
| Coordinator sees the low list and marks items restocked | 4 | Named | Keep |
| Health endpoint that checks the database | 4 | Needed | Keep. The thirty-day record depends on it |
| First-party page-view counter, no cookies | 2 | Needed | Keep. It measures use |
| Deploy to the approved host, with a local fallback | 6 | Needed | Keep |
| Accessibility and validation fixes | 4 | Needed | Keep |
| Tests for mark-low and restock | 4 | Needed | Keep |
| Fixing what sprint demos turn up | 4 | Needed | Keep |
| Volunteer accounts with hours tracking | 16 | Not named | Cut to out of scope |
| Barcode scanning with a phone camera | 16 | Not named | Cut to the stretch list |
| Automatic ordering from a supplier | 12 | Not named, and a line | Out of scope. It spends money |
| Photo of the empty bin | 8 | Not named | Cut to the stretch list |
| **Improve total** | **94** | | |

**The arithmetic.** The kept rows are 4 + 2 + 8 + 4 + 4 + 2 + 6 + 4 + 4 + 4 = 42. The cut rows are
16 + 16 + 12 + 8 = 52. 42 + 52 = 94, which matches the draft total. **After the cut, the Improve total
is 42, which is under 50 with 8 hours of margin.**

**Notice barcode scanning.** It is a good idea. It also needs a phone, and the volunteers who use
the desktop by the door would be left out. It waits on the stretch list, and if it is ever built, the
desktop path still has to work.

---

## Worked example 2 · Two cuts, recorded

The shape comes from the [Decision Log template](../05-labs/MCCTC_145010_Template_DecisionLog.md).

```markdown
## D-3 · Volunteer accounts cut from scope
**Week 8, Tuesday**   Phase: Define

**The situation:** The scope check said the draft will not finish. Volunteer accounts were 16 of 94 hours.

**Options considered:**
1. Keep accounts · each report is tied to a person · 16 hours, and names and passwords stored for every volunteer
2. No volunteer sign-in; anyone with the shop link marks a bin low · almost no personal data · a false report is possible

**Chosen:** 2

**Why:** The coordinator named empty bins, not who reported them. Option 2 stores no volunteer data.

**What it costs:** A report cannot be traced to a person. The coordinator can clear any report.

**Evidence:** Scope check, Week 8, Tuesday. Needs-discovery record, Week 7, Friday.

**Revisit if:** The coordinator reports false reports during usability testing.
```

```markdown
## D-4 · Automatic supplier ordering is out of scope
**Week 8, Tuesday**   Phase: Define

**The situation:** The draft had the board place orders when a bin was marked low.

**Options considered:**
1. Automatic ordering · saves the coordinator a step · spends the co-op's money without a person deciding, and needs payment details
2. The board shows the low list; the coordinator decides what to order · the coordinator keeps control

**Chosen:** 2

**Why:** No money changes hands and no payment details are entered anywhere in this program. A person should decide what to buy.

**What it costs:** The coordinator still places orders by hand.

**Evidence:** Capstone Specification, non-negotiable 9.

**Revisit if:** Never within this capstone. Listed as a future improvement for someone else to weigh.
```

---

## Worked example 3 · The proposal's scope section, after

```markdown
### In scope
- Anyone with the shop link can mark a bin low by bin code, with an optional note of up to
  120 characters. No name is asked for.
- The coordinator signs in, sees every bin marked low, and marks items restocked.
- A health endpoint that checks the database, and a first-party page-view counter.
- Runs on the host my instructor approves, with a local fallback on the shop desktop.

### Out of scope
- Volunteer accounts. Reports are not tied to a person.
- Ordering parts or spending money of any kind.
- Any customer information. None leaves the building.

### Stretch goals
*Started only when every acceptance criterion already passes.*
1. A photo of the empty bin, optional.
2. Barcode scanning, with the desktop path still working.
```

**The minimum viable version, in two sentences:** a volunteer at the desktop by the door can tell
the coordinator a bin is empty without finding them. The coordinator can see every empty bin in one
list and clear it when restocked.

---

## The wrong version, and what it costs

The student hears "this will not finish" and keeps all fourteen tasks, each "a simpler version." The
total drops on paper from 94 to 60 because every estimate was shaved, not because anything was cut.
The unknown tasks still take four times the guess. By Week 14, the sign-in works, the low list half
works, and scanning and photos are each started. Nothing on the acceptance list passes cleanly.

The other wrong version is the argument. "I can do it, I will work Period 8 every day." The
arithmetic already counted Period 8.

---

## Why the wrong version is tempting

The features you are cutting are often the ones you were most excited about. A cut feels like
admitting the proposal was wrong. Shaving every estimate feels like a compromise that keeps
everyone happy.

A cut is not a loss. It is on your stretch list, in writing, and you start it the day every criterion
passes. **A student who cuts to a small finished project has succeeded at what the capstone is
teaching.**

---

## Do this today

1. At your scope check, write down your instructor's words in your decision log's notes.
2. Sort your in-scope list into named, needed, and not named.
3. Cut. Update section 7 (in scope, out of scope, stretch) and section 11 (hours) of
   `docs/define/concept-proposal.md`.
4. Write one decision log entry per cut.
5. Re-add the Improve total. Show your instructor before the end of the build period.
6. Commit. Tomorrow the proposal goes to your stakeholder.

---

## If you are ahead, if you are behind

**Ahead.** Your scope check said yes. Start drafting the
[Acceptance Agreement](../05-labs/MCCTC_145010_Template_AcceptanceAgreement.md) criteria from your
in-scope list. Tomorrow's clinic is about exactly that.

**Behind.** If your scope check ran long, your instructor may move your send day to Thursday. Finish
the cut first, then the rest of the proposal.

---

## Words the WebXam uses

| Exam word | What it means in this skill |
|---|---|
| **Scope** | What the project will and will not do |
| **Deliverables** | What you hand over. A cut changes this list |
| **Objectives** | The measurable results the project aims for. Cuts must protect them |
| **Constructive feedback** | Criticism meant to improve the work. The scope check is one |
| **Consensus-building** | Reaching agreement on next steps. Your cuts become the proposal your stakeholder agrees to |
| **Decision** | A choice between real options, recorded with the reason |

---

## Self-check

**1.** A student cuts nothing but lowers every estimate by a third. Why does the scope check still
say no?

**2.** Sort this item for the co-op: "Coordinator sign-in." Named, needed, or not named? Why?

**3.** What is the difference between moving a feature to the stretch list and moving it to out of
scope?

### Answers

**1.** Lowering estimates does not remove any work. The unknown tasks still take about four times the
first guess, so the real total is unchanged and still over fifty.

**2.** Needed. The coordinator did not ask for a sign-in, but the low list and the restock button
must be protected, so a named feature cannot work safely without it.

**3.** A stretch goal is a good idea that waits and is started only when every acceptance criterion
already passes. Out of scope means the project will not do it, often because it crosses a line such
as money, equipment control, or personal data.
