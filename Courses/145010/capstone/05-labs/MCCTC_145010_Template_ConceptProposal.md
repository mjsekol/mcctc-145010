# Template · Concept Proposal
## 145010 Senior Capstone · Weeks 7-8

**Commit as:** `docs/define/concept-proposal.md`
**Due:** sections 1-4 started Week 7, Thursday. Full draft Week 8, Monday. Final version, after
the scope reality check, sent to the stakeholder Week 8, Wednesday. Presented Week 8, Thursday.

**Competencies this evidences:** 2.9.1 (scope and purpose of branding), 2.9.2 (scope and purpose
of the project), 2.9.3 (target audience, client needs, expected outcomes, objectives, budget),
2.9.5 (timeline, communication plan, task breakdown, costs, deliverables, responsibilities), 2.9.6
(develop and present a comprehensive proposal to stakeholders), 1.6.1 (business opportunities),
1.6.5 (organizational structure and chain of command), 1.6.8 (features and benefits that make a
product competitive), 1.6.11 (activities within a budget), 1.6.12 (classifications of employee
benefits, deductions, and compensation), 1.9.1 (create and interpret a budget), 1.9.8 (income
sources and expenditures), 1.10.2 (customer needs), 1.10.3 (features, benefits, and warranties),
1.3.5 (safety compliance measures), 1.3.7 (labor laws, including minor labor laws), 1.3.8 and
1.7.13 (intellectual property), 1.4.7 (productivity tools for tasks and timelines), 1.2.1 (cite
sources of information).

---

## Why this exists

**A proposal is a promise you can keep.** It is where you and your stakeholder agree what you
will build, what you will not, and how both of you will know it worked. Everything after Week 8
is measured against it: your requirements trace to it, your acceptance criteria come from it, and
your Requirements Fit score is judged against what grew out of it.

**The proposal is also where scope gets killed.** Your instructor reads it on Tuesday of Week 8
and tells you whether it will finish. A long, impressive proposal is not a good one. A good one is
specific enough that a stranger could tell whether you delivered it.

**The failure to avoid.** Writing the proposal about the software. Write it about the problem.
The software is section 9, and it is short.

---

## How to use this template

- Copy everything inside the fence into `docs/define/concept-proposal.md`.
- Replace every line in angle brackets. Delete the lines in italics once you have read them.
- **Every section is required.** If a section does not apply, write why in one sentence.
- Refer to your stakeholder by role, not by name, unless they have told you in writing that you
  may use their name.
- Write for your stakeholder. They are not a programmer. If a sentence needs a technical word,
  explain it in the same sentence.
- Label the version. Every time it changes after the stakeholder has seen it, the version goes up
  and the decision log says why.

---

```markdown
# Concept Proposal · <project name>
Version <1.0>   Written: Week <n>, <day>   Track: <Industrial / HMI | Full-Stack | AI-Integrated>
Prepared by: <your first name and last initial>   For: <stakeholder role>, <organization>

## 1. The problem and the purpose of this project
*2.9.2. One paragraph. Who has the problem, what goes wrong, how often, and what it costs them in
time, errors, or stress. Then one sentence: the purpose of this project.*

<paragraph>

**Purpose:** <one sentence, beginning "This project exists so that...">

## 2. The stakeholder and their organization
*1.6.5. Who is who. You need this to know who can approve the work and who will support it after
you leave.*

| Role | What they do here | Their part in this project |
|---|---|---|
| <stakeholder role> | <one line> | Main contact. Approves the proposal and acceptance |
| <who they report to> | | <approves, or needs to know> |
| <backup contact role> | | Acts for the stakeholder if they are unavailable |
| <who will use it day to day> | | Users |
| <who will look after it after handoff> | | Support |

**Who has final approval for this project in their organization:** <role>
**What their organization needs before it accepts something new:** <their words, from the
needs-discovery conversation>

## 3. Target audience
*2.9.3. The people who will use it. Not "everyone."*

- **Primary users:** <who, roughly how many, how often they would use it>
- **Devices and places they would use it on:** <phone at a counter, desktop in an office, panel
  on a shop floor>
- **What they already know:** <comfort with technology, vocabulary they use>
- **Accessibility needs you know of or should plan for:** <and how you found out>
- **Anyone under 18 among the users?** <yes / no. If yes, your instructor approves exactly what is
  stored about them.>

## 4. Client needs
*1.10.2. What the stakeholder told you, in their words where possible. Cite the meeting record.*

| # | Need | Where it came from |
|---|---|---|
| N1 | <the stakeholder needs to be able to...> | Meeting record, Week <n> <day> |
| N2 | | |
| N3 | | |

## 5. The opportunity, and features and benefits
*1.6.1, 1.6.8, 1.10.3. What they do about the problem now, what exists already, and why your
project is worth their time. A feature is what it does. A benefit is what that means for them.*

**What they do now:** <the current workaround>
**What already exists, and why it does not fit:** <one or two options you looked at, with the
reason, and a citation for anything you read>

| Feature | Benefit to the stakeholder |
|---|---|
| <what it does> | <what changes for them> |
| | |
| | |

## 6. Expected outcomes and objectives
*2.9.3. Objectives are specific and measurable. At least one is measured before and after, in
Week 9 and again in Week 17.*

- **Expected outcome:** <what is different for the stakeholder when this works>
- **Objective 1:** <measurable, for example: the number of unfilled shifts in a month>
- **Objective 2:**
- **The baseline question you will measure in Week 9:** <one question, and how you will measure it>

## 7. Scope
*2.9.2. The most important section. Be concrete. Your instructor's scope check reads this first.*

### In scope
- <a thing the finished project will do, specific enough to test>
- <...>

### Out of scope
*Say plainly what you will not do, so nobody expects it.*
- <...>

### Stretch goals
*Started only when every acceptance criterion already passes.*
- <...>

### Scope changes after Week 12
Scope is locked at the end of Week 12. After that, scope may be reduced by agreement and is never
expanded. New ideas go on a future improvements list delivered at handoff.

## 8. Branding
*2.9.1. The scope and purpose of branding for this project: whose identity the product carries,
and why that matters to the people who use it.*

- **Whose brand:** <the stakeholder's organization / a simple identity you create / none needed,
  because...>
- **Permission:** <the stakeholder's permission to use their name, logo, or colors, and where it
  is recorded. Do not use a logo without it.>
- **Why it matters here:** <for example: staff trust a tool that looks like it belongs to their
  organization>
- **Tone of the words in the product:** <formal, plain, friendly, and why>
- **Accessibility limits on branding:** <brand colors still meet contrast requirements, or how you
  will adjust them>

## 9. The approach
*Short. Which track, the main pieces, and where it will run. The detail belongs in the
architecture in Week 10.*

<three to five sentences>

**Where it will run and who will reach it:** <your plan, marked "to be confirmed with my
instructor in Week 10">

## 10. Deliverables
*2.9.5. The things you hand over.*

| # | Deliverable | Delivered in |
|---|---|---|
| D1 | The deployed <system>, reachable by <who> | Week 11 first version, Week 16 accepted |
| D2 | User guide | Week 17 |
| D3 | Training session or training materials | Week 17 |
| D4 | Rollout plan | Week 17 |
| D5 | Handoff package: access, documentation, future improvements list | Week 17 |

## 11. Task breakdown
*2.9.5, 1.4.7. Every task with an hour estimate. Keep the list in a task tracker too, and say
which one. Build tasks are Weeks 11-14 and have about fifty hours in total.*

Tracked in: <GitHub Projects board / other approved tool>

| # | Task | Phase | Hours | Depends on |
|---|---|---|---|---|
| T1 | | Define | | |
| T2 | | Measure & Analyze | | |
| T3 | | Improve | | |
| ... | | | | |
| | **Improve total** | | **<n>** | |
| | **All phases total** | | **<n>** | |

**If the Improve total is over 50, cut before the scope check, not after it.**

## 12. Timeline
*2.9.5. By week. The fixed milestones cannot move.*

| Week | Phase | What is finished by Friday |
|---|---|---|
| 7 | Define | Stakeholder named |
| 8 | Define | Proposal presented, agreement signed |
| 9 | Measure | Baseline, requirements version 1 |
| 10 | Analyze | Design brief, architecture, test plan |
| 11 | Improve | <sprint goal>, walking skeleton deployed |
| 12 | Improve | <sprint goal>, scope locked |
| 13 | Improve | <sprint goal> |
| 14 | Improve | <sprint goal>, release candidate |
| 15 | Control | Usability testing with five users |
| 16 | Control | Corrections, acceptance run |
| 17 | Control | Rollout, training, handoff |
| 18 | Control | Final presentation |

## 13. Responsibilities
*2.9.5. Who does what. Include the stakeholder's part, because acceptance needs it.*

| Who | Responsible for |
|---|---|
| Me | <building, testing, documentation, weekly updates, ...> |
| <stakeholder role> | <answering questions within an agreed time, reviewing requirements, the acceptance run, final approval> |
| <backup contact role> | <acting for the stakeholder if they are unavailable> |
| My instructor | Supervising the project and all contact, approving where it runs |

## 14. Communication plan
*2.9.5. How and when you and the stakeholder talk.*

- **Channel:** my school email account, with my instructor copied. Meetings at school, on an
  approved call, or on a school-arranged visit.
- **Weekly update:** every Friday, by <time of day>.
- **Response time I ask for:** <for example: two school days for a question>
- **Meetings planned:** proposal presentation Week 8; requirements review Week 10; acceptance run
  Week 16; training Week 17.
- **If I cannot reach the stakeholder:** after two contacts over five school days, my instructor
  contacts them, then the backup contact.

## 15. Budget and costs
*2.9.3, 2.9.5, 1.6.11, 1.9.1, 1.9.8. Every cost, including the ones nobody pays. Cite every
price or rate you use. Nobody in this project spends money and no payment details are entered
anywhere.*

### Equipment and services

| Item | Source | Cost to the stakeholder | Value | Where the value comes from |
|---|---|---|---|---|
| <Raspberry Pi and sensor / hosting free tier / lab computer> | <lab inventory / host> | $0 | <$ amount> | <cited source> |
| | | | | |

### Labor

*A developer's time has a value even when nobody is paid for it. Estimate it so the stakeholder
understands what they are receiving.*

| Work | Hours (from section 11) | Rate | Value |
|---|---|---|---|
| All phases | <n> | <$ per hour, from a cited source> | <hours x rate> |

**Rate source:** <cite it. For example, an occupational wage table from a government source. Do
not make up a rate.>

**Labor cost is more than a wage.** *1.6.12. An employer's cost for a worker includes more than
the hourly pay. In two or three sentences, name the classifications: benefits (such as health
coverage, retirement contributions, and paid leave), deductions taken from a paycheck (such as
taxes withheld), and costs an employer pays on top of wages. Cite your source. Do not invent a
percentage.*

<two or three sentences>

### Income sources and expenditures

*1.9.8. Who provides what, and what it costs after you leave.*

| | During the project | After handoff |
|---|---|---|
| **Provided by the school** | <lab hardware, software, supervision> | <nothing / the device stays in the lab> |
| **Provided by the stakeholder** | <their time, their documents, access> | <their time to maintain it> |
| **Ongoing costs** | $0 | <for example: $0 on a free tier, and what happens if the free tier changes> |

**Total cost to the stakeholder:** $0. **Total value delivered:** <equipment value + labor
value>.

## 16. Workplace rules that affect this project
*1.3.5, 1.3.7. Ask your stakeholder. Record what they said.*

- **Safety rules where the project will be used:** <their rules, posted procedures, and any safety
  data sheets for the area. Or "none apply, because...">
- **Who may go where:** <areas you may not enter, supervision needed>
- **This project is unpaid school work, not a job.** If anyone offers to pay you, stop and tell your
  instructor.
- **If it were a job:** minor labor laws limit the work people under 18 do for pay. From an official
  government source, name one kind of rule that would apply to you in this workplace, and cite the
  source. <one or two sentences, with citation>

## 17. Intellectual property
*1.3.8, 1.7.13. Who owns what. Your instructor reviews this section before it is sent.*

- **Your code:** <for example: I keep the copyright and release the code under <license>, which
  lets the stakeholder use, copy, and change it. Or: I keep the copyright and give the stakeholder
  written permission to use and modify it for their organization.>
- **The stakeholder's materials:** <documents, logos, data I will use, with their permission>
- **Third-party code, assets, and models:** listed in LICENSING.md, each with its license.
- **Do not agree to hand over ownership of your work** without your instructor and your parent or
  guardian involved.

## 18. Data and privacy
- **Data the project will hold:** <what, and whose>
- **Personal data:** <none / only what the job needs, and why each piece>
- **No personal data enters any AI tool**, including the stakeholder's documents if they contain any.

## 19. Risks
*The three things most likely to stop this project, and what you do about each.*

| Risk | How likely | What I will do | What I cut first if it happens |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

## 20. Presented and approved
*2.9.6. Filled in after you present.*

- **Presented:** Week 8, <day>, <in person at school / on an approved call / in writing>
- **Questions the stakeholder asked:** <list>
- **What changed because of the presentation:** <list, and the new version number>
- **Stakeholder response:** <approved / approved with changes / not approved, and why>
- **Acceptance agreement version this proposal supports:** <version>
```

---

## Before you send it · self-check

- [ ] Section 1 describes the problem without describing the software.
- [ ] Every in-scope item in section 7 could be tested by someone who is not you.
- [ ] The Improve hours in section 11 add up to 50 or fewer.
- [ ] Every price and rate in section 15 has a citation.
- [ ] Section 17 was read by your instructor.
- [ ] No names except your own, unless the stakeholder agreed in writing.
- [ ] You read it aloud once. Anything you stumbled on, you rewrote.
