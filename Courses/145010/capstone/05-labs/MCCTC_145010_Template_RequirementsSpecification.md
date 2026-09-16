# Template · Requirements Specification
## 145010 Senior Capstone · Weeks 9-10

**Commit as:** `docs/measure-analyze/requirements.md`
**Due:** version 1 Week 9, Wednesday, sent to the stakeholder Thursday. Reviewed by the stakeholder
by Week 10, Friday.

**Competencies this evidences:** 1.10.2 (determine the customer's needs and identify solutions),
2.12.1 (a written procedure for determining acceptability, which starts here), 1.2.12 (technical
writing), 2.7.4 (how browsers and devices affect a page), 2.7.5 (data volume, bandwidth, and
latency), 6.1.2 (plan for devices, audience, and ADA requirements), 6.5.11 (cross-platform and
cross-browser compatibility), 1.4.6 (electronic databases for business information).

---

## Why this exists

The proposal says what you will build in the stakeholder's words. The requirements say it in words
precise enough to build and test. **Your Requirements Fit score is judged against this document**,
so a vague requirement is a risk to you, not only to the stakeholder.

**The failure to avoid.** A requirement that is really a design: "a blue button on the top right."
A requirement says what must be possible, not how it looks. The design brief decides how it looks.

**The second failure.** Requirements that grow. Every requirement traces to a proposal item. A
requirement that traces to nothing is a scope change and needs a change request.

---

## How to write one

- **Numbered, and never renumbered.** A removed requirement is marked removed, not deleted, so old
  references still make sense.
- **Each functional requirement has at least one acceptance criterion** in Given, When, Then form.
- **Each one traces** to a need (N-number) and a scope item in the proposal.
- **Use "must" for required and "should" for wanted.** A "should" is not tested in acceptance.
- **Non-functional requirements have numbers.** "Fast" is not a requirement. "The main page loads
  in under 3 seconds on the lab network, measured with the browser's developer tools" is.

---

```markdown
# Requirements Specification · <project name>
Version <1.0>   Written: Week 9, <day>   Supports: Concept Proposal version <n>,
Acceptance Agreement version <n>

## 1. Functional requirements

### R1 · <short name>
The system must <what must be possible, in the stakeholder's terms>.
Traces to: need N<n>, proposal scope item "<item>".

- AC-1.1 Given <...>, when <...>, then <...>.
- AC-1.2 Given <...>, when <...>, then <...>.

### R2 · <short name>
...

## 2. What happens when things go wrong
*Every failure your system can meet, and what the user sees. Each gets a criterion.*

| ID | Situation | What the user sees | Criterion |
|---|---|---|---|
| E1 | <database, sensor, host, or model unavailable> | <exact behavior> | AC-E1 |
| E2 | <input that is blank, too long, or the wrong type> | | AC-E2 |
| E3 | <someone not signed in tries to change data> | | AC-E3 |

## 3. Non-functional requirements

| ID | Kind | Requirement | How it is measured |
|---|---|---|---|
| NF1 | Performance | <main task completes in under n seconds on <network or hardware>> | <tool and method> |
| NF2 | Availability | Runs 30 consecutive days without manual intervention | Thirty-day survival record |
| NF3 | Accessibility | Zero automated accessibility violations at WCAG 2 A and AA on every page; every task possible by keyboard alone; headings, labels, and alternative text that make sense in a screen reader | Automated check, keyboard walkthrough, screen reader walkthrough |
| NF4 | Devices and browsers | <the list, from the proposal's audience section> | Test plan platform cases |
| NF5 | Validity | Zero HTML validation errors on every page | Validator run |
| NF6 | Security | <who can do what; secrets never in the repository> | Test cases and review |
| NF7 | Privacy | Stores only the data in the data dictionary; no personal data in any AI tool or log | Data dictionary review, log search |
| NF8 | Data size and speed | <how much data moves per request, and the response time on the slowest target connection> | <measurement> |
| NF9 | Retention | <how long data is kept, and what removes it> | |

*Industrial track: include reading interval, stale-data threshold, and storage growth per day.
AI-Integrated track: include the measured model response time and the fallback behavior.
Full-Stack track: include the host's measured wake-up time if the free tier sleeps.*

## 4. Data requirements
*What the system stores. The full detail goes in the data dictionary in Week 10.*

| Data | Why it is needed | Personal? | Kept for |
|---|---|---|---|
| | | | |

## 5. Constraints
*Things you cannot change.*

- Models, if any, run locally on approved hardware. No commercial AI developer account.
- Free tiers only. No payment details entered anywhere.
- All stakeholder contact through school channels.
- <hardware, network, or site constraints>

## 6. Out of scope
*Copied from the proposal, plus anything the requirements review ruled out.*
- <...>

## 7. Traceability
| Need | Proposal scope item | Requirements | Acceptance criteria |
|---|---|---|---|
| N1 | | R1 | AC-1.1, AC-1.2 |
| N2 | | | |

## 8. Review and sign-off
- **Sent to stakeholder:** Week 9, <day>
- **Their questions and changes:** <list, with the meeting record or message it came from>
- **Version after review:** <n>
- **Stakeholder response:** <reviewed and agreed / agreed with changes>, Week 10, <day>

## 9. Change history
| Version | Week and day | What changed | Why | Change request |
|---|---|---|---|---|
| 1.0 | Week 9, <day> | First version | | |
```

---

## Before you send it · self-check

- [ ] Every functional requirement traces to the proposal.
- [ ] Every functional requirement has a criterion that could fail.
- [ ] Every non-functional requirement has a number and a way to measure it.
- [ ] Section 2 covers at least three failures.
- [ ] Nothing here describes colors, positions, or fonts. That is the design brief.
- [ ] A stranger could tell, from section 1 alone, what the system does.
