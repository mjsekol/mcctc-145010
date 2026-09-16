# The AI's draft · Concept Proposal sections
## Gate 2 · Week 8 · folder file 3 of 3

**Everything in this folder is invented and composite.** The co-op, the coordinator, and the
student are not real.

**What this file is.** The draft the lab's assistant returned from `student-prompt.md`, unedited.
It uses the section numbers of the Concept Proposal template, so the numbers skip. Items inside
each section are numbered (1.1, 3.2, 7.4) and table rows have IDs (N2, T11) so you can cite them.

---

# Concept Proposal · Parts Bin Board
Version 0.9 draft   Written: Week 8, Monday   Track: Full-Stack
Prepared by: [your first name and last initial]   For: Shop coordinator, community bike repair
co-op

## 1. The problem and the purpose of this project

**1.1** On open-shop nights, volunteers at the co-op repair donated bikes. When a volunteer reaches
for a part and the bin is empty, the repair stops, and the bike waits on the stand until the next
open-shop night or longer. Nobody reports the empty bin. The shop coordinator finds out on Sunday
by walking the shelves and texting a list, so the parts order is always a week behind the problem.
Some nights two or three repairs stall this way.

**1.2 Purpose:** This project exists so that the coordinator knows which parts bins are empty
before Sunday, and fewer bikes wait on a part the co-op could have restocked.

## 3. Target audience

**3.1 Primary users:** volunteers on open-shop nights, who report empty bins, and the shop
coordinator, who reviews the list and restocks.

**3.2 Devices and places they would use it on:** Because all volunteers carry smartphones, the
Parts Bin Board is designed mobile-first as an installable app that volunteers download to their
phones. The shared desktop by the door is not a target device.

**3.3 What they already know:** volunteers know the bin labels on the shelves, such as B-01 for
26-inch tubes. The coordinator is not a programmer and will look after the system after handoff.

**3.4 Accessibility needs you know of or should plan for:** none were raised in the meeting. The
student will ask at the proposal presentation.

**3.5 Anyone under 18 among the users?** Yes. Some volunteers are high school students. No
information about any volunteer is stored.

## 4. Client needs

| # | Need | Where it came from |
|---|---|---|
| N1 | The coordinator needs to know which bins are empty before Sunday. | Meeting record, Week 7, Friday |
| N2 | The coordinator asked for "a mobile app our volunteers can download" so volunteers can report an empty bin from the shop floor. | Meeting record, Week 7, Friday |
| N3 | Customer information stays inside the co-op. | Meeting record, Week 7, Friday |
| N4 | Volunteers should not need an account or a password. | Meeting record, Week 7, Friday |

## 5. The opportunity, and features and benefits

**5.1 What they do now:** the coordinator walks the shelves on Sunday and texts a list of empty
bins, then orders from that list.

**5.2 What already exists, and why it does not fit:** a paper sheet by the bins was considered. It
does not reach the coordinator before Sunday, which is the whole problem.

| Feature | Benefit to the stakeholder |
|---|---|
| F1. A volunteer marks a bin low with its bin code and an optional note | The coordinator hears about an empty bin the night it happens |
| F2. The coordinator signs in and sees the low list, and marks items restocked | One list to order from, and no Sunday shelf walk |
| F3. Customer sign-up with accounts and full repair history | Customers can log in from home and check their bike's repair status |
| F4. Donor tracking with monthly donor reports | The co-op can thank donors and forecast next month's donations |
| F5. An installable mobile app | Volunteers report from the shop floor without walking to a computer |

## 7. Scope

### In scope

**7.1** A volunteer marks a bin low: bin code and an optional note of up to 120 characters. No
name is asked for.

**7.2** No sign-in for volunteers; anyone with the shop link can mark a bin low.

**7.3** The coordinator signs in, sees the low list, and marks items restocked.

**7.4** Customer sign-up: each customer creates an account and sees the full repair history of
their bikes.

**7.5** Donor tracking: every donor and every donated part is recorded, with a monthly donor
report for the volunteer board.

**7.6** The volunteer app, installable on phones.

**7.7** A health endpoint and a first-party page-view counter that stores no cookies and no IP
addresses.

### Out of scope

**7.8** Payments of any kind.

**7.9** Ordering parts automatically from a supplier.

### Stretch goals

**7.10** A printable low list for the wall by the bins.

### Scope changes after Week 12

**7.11** Scope is locked at the end of Week 12. After that, scope may be reduced by agreement and
is never expanded. New ideas go on a future improvements list delivered at handoff.

## 11. Task breakdown

Tracked in: GitHub Projects board

| # | Task | Phase | Hours | Depends on |
|---|---|---|---|---|
| T1 | Needs discovery, concept proposal, presentation | Define | 6 | |
| T2 | Acceptance agreement | Define | 2 | T1 |
| T3 | Baseline count from the paper repair log, names covered | Measure & Analyze | 3 | T2 |
| T4 | Paste the co-op's customer repair spreadsheet into an AI assistant to find patterns in which parts run out, and use them to pre-fill the parts list | Measure & Analyze | 2 | T2 |
| T5 | Requirements, design brief, wireframes, architecture, test plan | Measure & Analyze | 10 | T3, T4 |
| T6 | Walking skeleton: Flask and SQLite deployed, health endpoint | Improve | 6 | T5 |
| T7 | Mark-a-bin-low page with bin code and note | Improve | 5 | T6 |
| T8 | Coordinator sign-in | Improve | 6 | T6 |
| T9 | Low list and mark restocked | Improve | 5 | T8 |
| T10 | First-party page-view counter | Improve | 3 | T6 |
| T11 | Customer sign-up, accounts, and repair history | Improve | 20 | T8 |
| T12 | Donor tracking and monthly donor reports | Improve | 14 | T8 |
| T13 | Installable mobile app for volunteer phones | Improve | 12 | T7 |
| T14 | Accessibility and device testing | Improve | 5 | T7, T9 |
| T15 | Bug fixing and polish | Improve | 10 | T14 |
| | **Improve total** | | **48** | |
| T16 | Usability sessions with five users | Control | 6 | T15 |
| T17 | Acceptance run and corrections | Control | 6 | T16 |
| T18 | User guide, training, rollout plan, handoff | Control | 6 | T17 |
| T19 | Final presentation | Control | 4 | T18 |
| | **All phases total** | | **93** | |

**11.1** The Improve total of 48 hours is within the 50-hour build budget, so the scope is
finishable in four sprints.

## 15. Budget and costs

### Equipment and services

| Item | Source | Cost to the stakeholder | Value | Where the value comes from |
|---|---|---|---|---|
| E1. Lab computer for development | School lab inventory | $0 | Not priced | Provided by the school during the project |
| E2. Hosting on an approved free tier | The host's published free tier | $0 | $0 | The host's free tier terms, to be confirmed in Week 10 |
| E3. The donated desktop by the door | The co-op | $0 | Already owned | No purchase needed |

### Labor

| Work | Hours (from section 11) | Rate | Value |
|---|---|---|---|
| C1. All phases | 93 | $41.27 per hour | $3,838.11 |

**15.1 Rate source:** $41.27 per hour is the Ohio median for entry-level web developers, from the
Ohio Tech Workforce Report.

**15.2 Labor cost is more than a wage.** An employer pays for more than the hourly wage. Benefits
such as health coverage, retirement contributions, and paid leave are part of compensation.
Deductions, such as taxes withheld, are taken out of each paycheck. Some costs are paid by the
employer on top of wages. This project pays no wage, so none of these costs apply, but they are
part of what a developer's time is worth.

### Income sources and expenditures

| | During the project | After handoff |
|---|---|---|
| **Provided by the school** | Lab hardware, software, and supervision | Nothing |
| **Provided by the stakeholder** | The coordinator's time and the bin labels | The coordinator's time to maintain it |
| **Ongoing costs** | $0 | $0 on a free tier. If the free tier changes, the local fallback on the co-op desktop keeps the board running |

**15.3 Total cost to the stakeholder:** $0. **Total value delivered:** $3,838.11.
