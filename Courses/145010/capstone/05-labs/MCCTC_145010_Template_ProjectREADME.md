# Template · Project README
## 145010 Senior Capstone · started Week 7, finished Week 17

**Commit as:** `README.md` at the top of your repository.
**Due:** a first version in Week 7, with the project name and the stakeholder role. Updated every
sprint. Complete for the release candidate in Week 14 and final in Week 17.

**Competencies this evidences:** 1.2.12 (technical writing), 1.2.5 (communicate for an intended
audience), 6.5.5 (the tools used to build it), 2.13.6 (support materials, for the next developer).

---

## Why this exists

**The README is for the next developer.** That might be a future student, someone your stakeholder
hires, or you in a year. The user guide is for the people who use the project. This file is for the
people who have to run it, fix it, or change it.

**The test of a README:** someone who has never seen your project follows it on a clean machine and
gets it running without asking you anything. Before Week 17, ask a classmate to try. Fix every place
they stopped.

**The failure to avoid is hiding what is not finished.** A README that says everything works, on a
project with a known issue, is the first thing a panel member will test.

---

```markdown
# <Project name>

<One sentence: what it does, for whom.>

**Capstone project, 145010 Web Design & Senior Capstone.** Built for <stakeholder role> at <kind of
organization>. Track: <Industrial / HMI | Full-Stack | AI-Integrated>.

## Status
<Release candidate / accepted / handed over.> Last updated Week <n>, <day>.

## What it does
- <the main task>
- <...>

## What is not finished
- <known issues, from the acceptance record>
- <anything cut, from the scope lock statement>

## How it is put together
<Three or four sentences, and a link to docs/measure-analyze/architecture.md.>

## Running it locally
*Every command. Every port explicit. Tested on a clean machine, Week <n>, <day>.*

1. Requirements: <language versions, tools>
2. Get the code: <...>
3. Install: <...>
4. Settings: <which environment variables, where their values come from. Never the values.>
5. Start the stand-ins, if needed: <command with explicit port>
6. Start it: <command with explicit port>
7. Open: <address>

## Running the tests
<command, and what a passing run prints>

## Deploying
<Link to the deployment steps in the architecture document. Every release is recorded in the
events log.>

## Where things are
| Folder or file | What it holds |
|---|---|
| `src/` | |
| `docs/define/` | Proposal and agreement |
| `docs/measure-analyze/` | Baseline, requirements, design, architecture, test plan |
| `docs/improve/` | Sprints, reviews, change requests |
| `docs/control/` | Usability, acceptance, rollout, handoff, thirty-day record |
| `docs/communication/` | Contact log, weekly updates, meeting records |
| `decision-log.md` | Every decision and why |
| `ai-usage-log.md` | Every AI interaction that changed something submitted |
| `troubleshooting-log.md` | Every real problem and its verified fix |
| `LICENSING.md` | Licenses for everything used |
| `user-guide.md` | For the people who use it |

## Tools
<Editor or IDE, and why. Anything else a developer needs.>

## Licensing
See `LICENSING.md`. This project's code is released under <license>.

## Data and privacy
<What it stores, and a pointer to the data dictionary. No real data in this repository.>
```

---

## Before you commit · self-check

- [ ] A classmate followed "Running it locally" without asking you anything.
- [ ] "What is not finished" is honest and current.
- [ ] Every port is explicit.
- [ ] No secret values, and no real names.
