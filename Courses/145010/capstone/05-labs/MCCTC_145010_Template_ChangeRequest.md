# Template · Change Request and Scope Lock Statement
## 145010 Senior Capstone · Weeks 9-17

**Commit as:** `docs/improve/change-requests.md`. The scope lock statement goes at the top in Week
12. Each change request is added below it.
**Due:** a change request before any change to scope or acceptance criteria takes effect. The scope
lock statement Week 12, Friday.

**Competencies this evidences:** 1.10.4 (identify procedures for initiating product and service
improvements), 1.2.11 (professional correspondence), 1.2.7 (consensus-building to determine next
steps), 2.12.1 (changes to the agreed acceptance procedure made by agreement).

---

## Why this exists

**Scope changes are normal. Unrecorded scope changes are how capstones fail.** A request that
arrives in a hallway conversation and gets built without a record is a change nobody agreed to. In
Week 16 it becomes an argument about what "done" means.

**The rule after Week 12 is simple to state and hard to follow.** Scope may be reduced. It is never
expanded. A new idea after Week 12 goes on the future improvements list, however good it is.

**Before Week 12, a change that adds work names what it replaces.** The hours in a week do not grow
because the list did.

---

## The scope lock statement · Week 12, Friday

```markdown
# Scope Lock · <project name>
Locked: Week 12, Friday   Acceptance agreement version: <n>

## In scope, final
- <every item that will be delivered>

## Moved to stretch goals
*Started only if every acceptance criterion passes.*
- <...>

## Moved to future improvements
*Delivered as a list at handoff. Not built.*
- <...>

## Sent to the stakeholder
Week 12, Friday, with the weekly update. Their reply: <...>

From this point, scope may be reduced by agreement and is never expanded.
```

---

## A change request

```markdown
## CR-<n> · <short title>
**Raised:** Week <n>, <day>   **By:** <me / stakeholder role / a user, through the stakeholder>
**Type:** <reduce scope / change a criterion / add scope, before Week 12 only>

**What is asked for:** <one or two sentences>

**Why:** <the reason, with evidence: a meeting record, a sprint review, a test result>

**What it affects**
| Affected | Change |
|---|---|
| Requirements | <R-numbers> |
| Acceptance criteria | <AC-numbers, before and after> |
| Hours | <added or saved> |
| Replaces | <before Week 12: what is removed to make room> |

**After Week 12:** <this request reduces scope / this request adds scope and goes to the future
improvements list instead>

**Decision:** <agreed / not agreed / moved to future improvements>
**Agreed by:** <stakeholder role>, Week <n>, <day>, <in writing, where recorded>
**Acceptance agreement version after this change:** <n>
**Decision log entry:** D-<n>
```

---

## Future improvements list

Keep it at the bottom of the same file. It is delivered at handoff.

```markdown
## Future improvements
| # | Idea | Who asked | Why it would help | Why it was not built |
|---|---|---|---|---|
| FI-1 | | | | <arrived after scope lock / too large / needs data we do not have> |
```

---

## How to say it to the stakeholder

When a stakeholder asks for something new after Week 12, the
[Stakeholder Communication Guide](MCCTC_145010_Guide_StakeholderCommunication.md#4-scope-change-request)
has the words. The short version:

> That is a good idea, and I have added it to the list of future improvements I will hand over with
> the project. The scope was locked in Week 12 so that what we agreed will be finished and tested
> properly.

---

## Before you commit · self-check

- [ ] Every change to an acceptance criterion has a CR with the stakeholder's written agreement.
- [ ] No change after Week 12 adds scope.
- [ ] Every agreed CR raised the agreement version.
- [ ] The future improvements list has every idea that was not built, with who asked.
