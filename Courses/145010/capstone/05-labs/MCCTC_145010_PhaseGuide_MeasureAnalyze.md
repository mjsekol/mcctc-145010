# Phase Guide · Measure & Analyze
## 145010 Senior Capstone · Weeks 9-10

**Why this phase exists.** You are about to spend four weeks building. Every hour of that is
cheaper if you know three things first: how bad the problem is today, exactly what "done" means,
and how the pieces fit. Students who skip this phase build the wrong thing quickly. It feels like
progress until Week 15.

**The other reason.** In Week 16 your stakeholder decides whether to accept your work. In Week 18
you report what changed. **Both depend on a number you can only take now, before anything you
build exists.** Once your project is in use, the "before" is gone.

**What you are producing.** A baseline measurement, a requirements specification, a design brief
with a conceptual model and wireframes, an architecture with a data dictionary, and a written
test plan that includes the acceptance procedure.

**Competencies this phase evidences:** 2.9.4 (conceptual model and design brief), 2.12.1 (a
written acceptance procedure agreed by stakeholders and team), 2.12.2 (a test system that mimics
external interfaces), 2.12.3 (realistic test cases across targeted platforms and devices), 1.10.2
(customer needs), 1.10.5 (measurement tools), 6.1.2 (plan a page for audience, devices, layout,
color, and ADA), 6.5.2 (plan a site's structure for navigation and usability), 2.7.2 (ways to
present data), 2.7.4 (how browsers and devices affect a page), 2.7.5 (data volume, bandwidth, and
latency), 1.4.4 (hardware to support software), 1.4.6 (a database for business information),
1.2.12 (technical writing), 2.11.4 (gather and analyze data about a problem).

---

## What done looks like

At the end of Week 10:

- [ ] `docs/measure-analyze/baseline.md`: the current process measured, with the method written
      so you can repeat it exactly after handoff.
- [ ] `docs/measure-analyze/requirements.md`: every requirement traceable to the proposal, every
      requirement with at least one acceptance criterion someone else could run, **reviewed by the
      stakeholder**.
- [ ] `docs/measure-analyze/design-brief.md` and `wireframes/`: audience, conceptual model, site or
      screen structure, wireframes for every main screen, accessibility plan, branding.
- [ ] `docs/measure-analyze/architecture.md`: the components, where each runs, how they talk, the
      data dictionary, and the hosting or device decision **made with your instructor**.
- [ ] `docs/measure-analyze/test-plan.md`: test cases across your targeted platforms and devices,
      the test setup that stands in for the real external pieces, and the acceptance procedure
      **sent to the stakeholder**.
- [ ] Your milestone review in Week 10 is complete and its actions are in your decision log.
- [ ] Status notes on Fridays of Weeks 9 and 10.
- [ ] AI-Integrated track: the "why a model" comparison in your decision log, and the ethics and
      licensing analysis finished.

---

## Week 9 · Measure

**The goal of the week:** a number for "how it is now" and a first list of "what it must do."

**Grading Period 3 closes at the end of this week.** Commit every period. See
[what Grading Period 3 sees](MCCTC_145010_PhaseGuide_Define.md#what-grading-period-3-sees).

### Monday · plan the baseline

- [ ] Open your needs-discovery meeting record. Find the sentence where the stakeholder said what
      hurts.
- [ ] Turn it into one measurable question. Use the
      [Baseline Measurement template](MCCTC_145010_Template_BaselineMeasurement.md).
- [ ] Decide the method: timing a task, counting errors in existing records, counting occurrences
      in a period. **Write the method precisely enough that you could repeat it in Week 17.**
- [ ] Ask the stakeholder for what you need. Through school channels, today.

### Tuesday · collect it

- [ ] Take the measurement, or collect the records you will count.
- [ ] **No personal data in your baseline.** Count things. Do not copy names.
- [ ] If the stakeholder cannot give you data this week, write down what you asked for, when, and
      what you will use instead. A smaller honest baseline beats a guessed one.

### Wednesday · requirements, version 1

- [ ] [Requirements Specification](MCCTC_145010_Template_RequirementsSpecification.md): every
      requirement from the proposal, each with at least one acceptance criterion.
- [ ] Non-functional requirements: how fast, on which devices, how accessible, how long it must
      run unattended.
- [ ] AI-Integrated track: write the "why a model" comparison in your decision log. What would a
      version with no model do, and what does the model add?

### Thursday · finish the baseline, send the requirements

- [ ] Baseline record complete, with the limits of the measurement stated.
- [ ] Requirements version 1 sent to the stakeholder for review, with a specific question: "Is
      anything here not what you meant, and is anything missing?"

### Friday · stakeholder day

- [ ] Status note, short form.
- [ ] Record any requirement feedback in a meeting record.
- [ ] Commit. **Grading Period 3 closes.**

---

## Week 10 · Analyze

**The goal of the week:** a design you could hand to another developer, and a test plan your
stakeholder has seen.

**Milestone Review 1 happens this week.** Your instructor looks at your commit history, your
committed documents, and your contact log. What you say in the review matters less than what is
in the repository.

### Monday · design brief and wireframes

- [ ] [Design Brief](MCCTC_145010_Template_DesignBrief.md): audience, conceptual model, site or
      screen structure, and how the product presents its data.
- [ ] Wireframes for every main screen. Paper photographed, or a design tool your instructor has
      approved. Boxes and words, not colors.
- [ ] Accessibility plan: keyboard, contrast, headings, labels, and what a screen reader user hears.

### Tuesday · architecture and data dictionary

- [ ] [Architecture and Data Dictionary](MCCTC_145010_Template_ArchitectureAndDataDictionary.md):
      every component, where it runs, and how it talks to the others.
- [ ] **Where it runs is decided with your instructor**, in conference, and written with the
      reason. For the Industrial and AI tracks this includes which network.
- [ ] Every stored field in the data dictionary, with its type and the reason it exists.
- [ ] Full-Stack track: read your host's current free tier terms and record what they say about
      sleeping, storage, and expiry.
- [ ] AI-Integrated track: measure the model's response time on the target hardware for a
      realistic request. Record it.

### Wednesday · the written test plan

- [ ] [Test Plan](MCCTC_145010_Template_TestPlan.md): test cases for every requirement, on every
      platform and device your requirements name.
- [ ] The test setup: what stands in for the sensor, the host, the database, or the model while you
      test. **This is 2.12.2**, and it is also what lets you work when the real thing is not
      available.
- [ ] The acceptance procedure: the cases you and the stakeholder will run together in Week 16.

### Thursday · send the acceptance procedure

- [ ] Send the acceptance procedure to the stakeholder with one sentence: "These are the tests we
      will run together in Week 16. Please tell me if any of them is not what you meant."
- [ ] Ask for agreement by Week 11, Friday.

### Friday · stakeholder day

- [ ] Requirements signed off by the stakeholder, or their changes recorded and version 2 sent.
- [ ] Status note, short form.
- [ ] Milestone review actions in your decision log.
- [ ] Sprint 1 plan drafted, ready for Monday.

---

## The two failures to catch this phase

**Scope creeping back.** The earliest signal is a requirements specification longer than the
proposal's in-scope list. Every requirement should trace to a proposal item. A requirement that
does not is a scope change and needs a change request.

**The stakeholder going quiet.** The earliest signal is requirements sent Thursday with no reply by
the following Wednesday. Follow the steps in the
[Stakeholder Communication Guide](MCCTC_145010_Guide_StakeholderCommunication.md#8-when-your-stakeholder-goes-quiet).
Do not wait for the milestone review to mention it.

---

## The evidence this phase produces, and where it is scored

| Evidence | Rubric part |
|---|---|
| Baseline record | 1A · **3C measured change**, which is impossible without it |
| Requirements specification, stakeholder-reviewed | 1A · **2A Requirements Fit** is scored against it |
| Design brief and wireframes | 1A · 2A Readability and Correctness of the interface |
| Architecture and data dictionary | 1A · 2A Security (what is stored and why) · 4C technical questions |
| Test plan and acceptance procedure | 1A · **3A acceptance** runs these cases |
| Milestone review actions | 1B decision log |
| Status notes and meeting records | 1D |

---

## Words the WebXam uses for what you did this phase

| Exam word | In your project |
|---|---|
| **Baseline** | The measurement of the current process before your project exists. |
| **Conceptual model** | The main things in your system and how they relate, before any code. |
| **Design brief** | The short document that tells a designer what to make, for whom, and why. |
| **Wireframe** | A layout sketch with no styling. |
| **Site structure, navigation** | Your site map or screen flow. 6.5.2. |
| **Test case** | A starting state, an action, and an expected result that could fail. |
| **Targeted platforms, device types** | The browsers, screen sizes, and devices your requirements name. |
| **Test system that mimics external interfaces** | Your stand-in for the sensor, host, database, or model. |
| **Acceptance procedure** | The written tests that decide whether the stakeholder accepts the work. 2.12.1. |
| **Bandwidth, latency** | How much data moves and how long it takes. Your measured response times. 2.7.5. |
