# Template · Architecture and Data Dictionary
## 145010 Senior Capstone · Week 10, Tuesday

**Commit as:** `docs/measure-analyze/architecture.md`
**Due:** Week 10, Tuesday, end of the build period. The "where it runs" decision is made in
conference with your instructor this week.

**Competencies this evidences:** 1.4.4 (use system hardware to support software applications),
1.4.6 (an electronic database for business and technical information), 2.7.5 (data transmission
volumes, bandwidth, and latency), 2.7.8 (static versus dynamic sites and the reasons for each),
6.5.5 (select an integrated development environment), 6.4.7 (scripting that interacts with data
sources), 6.5.12 (publish to a web server), 2.12.2 (a test system that mimics external interfaces).

---

## Why this exists

**Architecture is the map of your system.** When something breaks in Week 13, this is the page
that tells you where to look. When a panel member asks "how does someone reach this," this is the
page your answer comes from.

**The data dictionary is where privacy is decided.** Every field you store is written here with
the reason it exists. A field with no reason gets deleted before it is built, which is the cheapest
moment to delete it.

**The failure to avoid.** Designing around a host, a network, or a device you have not been given.
Where your system runs is decided with your instructor, and some options need approval from people
outside the classroom. Write down what was actually approved.

---

```markdown
# Architecture · <project name>
Version <1.0>   Written: Week 10, <day>   Supports: Requirements version <n>

## 1. The picture
*Every component and every connection. Text diagram, or a drawing committed as an image with the
same content written below it.*

    browser  --HTTPS-->  web app (host)  --->  database (host)
                              |
                              +--> /health

## 2. Components
| Component | What it does | Language or product | Runs on | Port or address |
|---|---|---|---|---|
| | | | | |

*Every port is explicit. Never rely on a default. Never use a port another service in the lab
already uses.*

## 3. Where it runs, and who can reach it
- **Decision:** <host, lab machine, device, stakeholder's machine>
- **Approved by:** <instructor, and anyone else whose approval was needed>, Week 10, <day>
- **Who can reach it, and how:** <the stakeholder opens a link / uses the lab machine / ...>
- **What it needs that you do not control:** <a network, a host's free tier, a device>
- **Free tier or site terms read and recorded:** <what they say about sleeping, storage, expiry,
  and where you read it> [VERIFY terms are current]
- **Static or dynamic, and why:** *2.7.8.* <one or two sentences>

## 4. Hardware
*1.4.4. What the software needs from the hardware, and what the hardware actually has.*

| Component | Needs | Has | Checked how |
|---|---|---|---|
| <model server> | <memory, storage> | <lab machine spec> | <command or setting you looked at> |
| <Pi logger> | <storage growth per day> | <card size> | |

## 5. How the pieces talk
*6.4.7. Every request between components.*

| From | To | Request | Sends | Receives | Fails how |
|---|---|---|---|---|---|
| browser | web app | `POST /shifts/<id>/claim` | first name, last initial | updated shift | shift already taken, not found, database down |
| | | | | | |

## 6. Data volume and speed
*2.7.5. Estimate, then measure in Sprint 1.*

- **Largest thing sent in one request:** <size, estimated>
- **Requests per day, expected:** <number, and where the estimate comes from>
- **Slowest connection or hardware a user will have:** <what it is>
- **Response time measured:** <number, tool, Week and day> *Filled in once measured.*
- **Storage growth per day and per year:** <arithmetic shown>

## 7. Configuration and secrets
- **Settings that change between your machine and the deployed system:** <list>
- **Where secrets live:** <host environment settings, a local file listed in .gitignore>
- **How the code reads them:** <the variable names, never the values>
- **Checked the repository history for secrets:** <how, Week and day>

## 8. Logging and health
- **What is logged:** <events, never personal data, never secrets>
- **The health check:** <address, what it reports>
- **The health log for the thirty-day record:** <what writes it, how often, where it lives>

## 9. The test setup
*2.12.2. What stands in for each piece you do not control, so you can test without it.*

| Real piece | Stand-in | How to start it | What it can simulate |
|---|---|---|---|
| <sensor> | <replay file of recorded readings> | <command with explicit port> | <normal, hot afternoon, sensor silent> |
| <model server> | <stub server> | | <slow, down, malformed answer> |
| <hosted database> | <local database with invented data> | | <empty, full, unavailable> |

## 10. Deployment steps
*Written so someone else could follow them. These are also what make a release "planned" for the
thirty-day rule.*

1. <...>
2. <...>

## 11. Tools
*6.5.5. The editor or IDE you chose and why, and every other tool the project needs.*

| Tool | Version | Why this one |
|---|---|---|
| | | |

## 12. Dependencies
Every library, framework, model, and asset, with its license, is listed in `LICENSING.md`.

---

# Data Dictionary

*One row per stored field. Examples are invented, never real.*

## Table or collection: <name>
*What one row represents:* <one sentence>

| Field | Type | Required | Example (invented) | Personal? | Why it exists | Kept for | Removed by |
|---|---|---|---|---|---|---|---|
| id | integer | yes | 42 | no | Unique key | as long as the row | row delete |
| | | | | | | | |

## Table or collection: <name>
...

## Relationships
- <table>.<field> refers to <table>.<field>. <What happens when the referenced row is removed.>

## Fields considered and not stored
| Field | Why it is not stored |
|---|---|
| <phone number> | <the job does not need it> |
```

---

## Before you commit · self-check

- [ ] Your instructor approved section 3, and the approval is written down.
- [ ] Every port is explicit.
- [ ] Every personal field has a reason and a removal rule, or it is in "not stored."
- [ ] Section 9 lets you test every component without the real external piece.
- [ ] No secret values appear anywhere in this file.
