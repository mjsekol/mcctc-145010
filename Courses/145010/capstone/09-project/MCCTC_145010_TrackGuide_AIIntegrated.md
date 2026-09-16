# Track Guide · AI-Integrated
## 145010 Senior Capstone · Read before Week 8

**Why this track exists.** In 145130 you wrapped a locally hosted model in a service, called it
from a C# application, handled every way it can fail, and studied the law and ethics around it.
This track does that for a real person whose problem is worth a model.

**What makes it hard.** Two things. The model is the least reliable part of your system and the
part your stakeholder will trust most. And "worth a model" is a claim you have to defend: a
problem that a search box or a sorted list would solve is not an AI problem, and the panel will
ask.

**Competencies this track evidences most heavily:** 1.3.8 (compliance with computer and
intellectual property laws), 1.7.13 (protecting intellectual property), 1.5.5 (how bias
influences a product), 2.12.2 (a test system that mimics external interfaces), 2.12.3 (realistic
test cases compared with expected performance), 2.11.4 (gather and analyze data about a problem).

---

## The rule that shapes this track

**Models run locally, on hardware your instructor approves.** No part of any capstone requires a
commercial AI developer account or key. Commercial developer APIs require their users to be 18 or
older, and nothing in this program asks you to work around that.

Only models your instructor has approved are downloaded or installed, under the Lab Acceptable
Use and Safety Agreement.

---

## The typical shape

```
front end (C# or web)
    |
    v
your service  --> input check (refuse early, cost nothing)
    |         --> retrieval or rules, if any
    |         --> local model server  (lab hardware, explicit port)
    |         --> output check (parse, validate, label the source)
    |         --> fallback when the model cannot be used
    +--> health endpoint and health log
```

**One envelope for every answer**, with a field saying where the answer came from: the model,
the fallback, or a refusal. You built this in 145130. Build it again for your own problem.

---

## A composite example

**This is a composite, not a real organization.** The service counter at a small equipment
repair shop answers the same questions every day from a stack of printed service manuals. Staff
spend minutes finding the right page while a customer waits.

It is a reasonable AI problem because the answers live in long documents written in ordinary
language, and a person still makes the final call. It is the example in
[Scope Calibration](MCCTC_145010_Capstone_ScopeCalibration.md#example-3--ai-integrated).

---

## The minimum viable version

- **One task**, for staff, not the public. The model helps a person. The person decides.
- **A service** wrapping a local model, with an input check, an output check, and a fallback
  that still does something useful when the model is not available.
- **Every answer shows where it came from.** For a document task, the source document and page.
  For a classification, the label and whether the model or the fallback produced it.
- **"I could not find that" is a valid answer**, and the service gives it rather than inventing
  one.
- **A stand-in model server** so the whole project runs and is testable on a machine with no
  model on it. That is your 2.12.2 evidence.
- **An evaluation set** of at least 20 realistic, invented or non-personal cases with the answer
  a person would expect, run against the real model, with the results recorded. That is your
  2.12.3 evidence.
- **The written ethics and licensing analysis.** Required, not optional. See below.
- **A health endpoint and a health log.**

## What a stretch looks like

- A second document set or a second task.
- A comparison of two approved local models on your evaluation set, with the tradeoff written up.
- A feedback button staff use to mark an answer wrong, stored with no personal data.
- A report of the questions the service could not answer, for the stakeholder to act on.

**Not stretch goals, because they change the risk:** a public-facing chatbot, anything that
answers customers without a person in between, fine-tuning a model, and any feature that needs
personal data to work.

---

## The written ethics and licensing analysis

**Required for this track, and scored in Process & Documentation and in the defense.** Commit it
as `docs/define/ethics-and-licensing.md`, start it in Week 8, and finish it by Week 10. It
extends your [Licensing Statement](../05-labs/MCCTC_145010_Template_LicensingStatement.md). It
does not replace it.

**Use your own reading, not a summary.** You practiced this in 145130 with the licensing audit
and the privacy impact assessment. Open the actual license files and quote them.

### Part 1 · The model's license

- The exact model, version, and where it was downloaded from.
- The license file that shipped with it, by name.
- **Quoted:** what it permits, what it requires, what it forbids, and what triggers the
  requirements. The four questions from 145130.
- Whether your stakeholder's use is permitted, with the clause that says so.
- Any use-restriction clause, quoted, and why your project does or does not fall under it.
- **What you could not determine**, stated plainly, and who could answer it.

### Part 2 · The data's license and ownership

- Where every document or record the system reads came from, and who owns it.
- The stakeholder's written permission to use it, and where that permission is recorded.
- Confirmation that it contains no personal data, and how you checked.

### Part 3 · Who owns the output

What your stakeholder receives, who owns the code you wrote (see the acceptance agreement), and
what is honestly uncertain about ownership of model output. **Present the strongest case on each
side** where the question is open. Do not pretend it is settled.

### Part 4 · Harm and bias

- **Who could be harmed by a wrong answer**, and how badly. A wrong page number costs a minute. A
  wrong safety instruction could hurt someone.
- **What your design does about each**: the source shown, the person in the loop, the refusal.
- **Where bias could enter**: the documents chosen, the language the model handles well or
  badly, who the evaluation cases represent. Tie it to 1.5.5: how that bias would affect the
  stakeholder's work and the people they serve.
- **What you measured and what you did not.** An evaluation set of twenty cases shows how the
  system did on twenty cases. It does not show how it does in general.

### Part 5 · The decision

One paragraph: given everything above, is this an appropriate use of a model for this
stakeholder? If the honest answer has conditions, state them. Those conditions go in the user
guide.

**This is not legal advice, and your analysis should say so.** It is a documented, careful reading
by someone who is not a lawyer, which is what 1.3.8 asks you to be able to produce.

---

## The technical risks that sink this track

**1. The model is not available.** The lab machine is off, the model server is busy, a download
was not approved. **Fix it with the stand-in server and the fallback from Week 11.** A project
that can only be demonstrated when the model is up cannot be tested, and a panel will not wait.

**2. Answers that sound right and are wrong.** A model does not fail loudly. **Fix it with the
evaluation set and the source line on every answer.** Count wrong answers, not only crashes.

**3. Slow answers.** Local models on lab hardware can take many seconds. **Measure it in Week 10**
and write the measured time into the requirements. Your client's timeout is longer than your
service's worst case, with the arithmetic in a comment. You did this in 145130.

**4. Reachability.** A model on lab hardware is on the lab network. **How the stakeholder reaches
the system is decided with your instructor in Week 10**, and nothing is exposed to the internet by
a student. Two shapes usually work: the stakeholder uses it on a lab machine, or it is installed
on a machine the stakeholder's organization owns and approves, running an approved local model
there. [VERIFY with your instructor and, where a school network is involved, district IT]

**5. The wrong server answers.** A client pointed at the wrong port does not fail. It gets an
answer from something else. **Every service and every recorded command takes an explicit port.**
Do not use a model server's default port for anything of yours.

**6. The "why AI" question.** If a keyword search would do the job, the panel will say so. **Write
the comparison in Week 9**: what the baseline process is, what a non-AI version would do, and what
the model adds that the simpler version cannot.

---

## Surviving thirty days, on this track

**What "manual intervention" looks like here:** restarting the model server by hand, restarting
your service because it stopped answering, clearing a stuck queue, re-downloading a model.

**How you prove it did not happen:**

1. **A health endpoint** that reports whether your service is up, whether the model server
   answered a trivial request, and which model and version is loaded.
2. **A health log** your service or a scheduled check writes on a fixed interval.
3. **The fallback counts.** A day where the model was down and the fallback answered, labelled
   correctly, is a day the system survived. A day where the system gave a model-labelled answer
   while the model was down is a failure, even though nothing crashed.
4. **Your services start at boot and restart on their own** on the machine they run on. [VERIFY
   on that machine]

A health log line might look like this. It is program data, so the timestamp belongs there:

```
2027-04-23T14:15:00  result=ok  service=ok  model=down  answered_by=fallback
```

---

## Where Strand 6 lives in this track

If your front end is on the web, it carries the same standard as the instruction phase: valid,
accessible, responsive. If your front end is C#, **your user guide and a small status page are
still web pages**, and the Gate 1 reps are how you keep Strand 6 current for Week 16.

---

## Defense questions this track is most vulnerable to

1. "Why does this need a model? What would a search box get wrong?"
2. "Your model is down right now. What does the user see?"
3. "Quote me the clause in the model's license that allows this use."
4. "Out of your twenty evaluation cases, how many were wrong, and what did the wrong ones have in
   common?"
5. "Who could be hurt by a wrong answer, and what stops that?"

The full bank is in [Defense Question Bank](MCCTC_145010_Capstone_DefenseQuestionBank.md).
