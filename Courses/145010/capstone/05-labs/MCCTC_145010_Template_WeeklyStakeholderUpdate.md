# Template · Weekly Stakeholder Update
## 145010 Senior Capstone · every Friday, Weeks 8-17

**Commit as:** `docs/communication/updates/week-<nn>.md`, the exact text you sent.
**Send:** every Friday from your school account, with your instructor copied. Short form in Weeks
8-10. Full form in Weeks 11-17.

**Competencies this evidences:** 1.2.5 (communicate information for an intended audience and
purpose), 1.2.11 (professional correspondence), 1.2.13 (solicit stakeholders' opinions), 1.4.8
(electronic media and network etiquette), 2.13.2 (communicate plans to key stakeholders in a
timely manner).

---

## Why this exists

**Your stakeholder is not in this room.** The update is the only picture they have of the project.
If the picture is accurate every week, there are no surprises in Week 16. If it is optimistic every
week, Week 16 is one large surprise.

**The update is not a diary.** "I worked on the database" tells them nothing. "You can now create
next week's shifts yourself at the link below" tells them what changed for them.

**The failure to avoid is hiding bad news.** Every student is tempted to write "going well" in the
week things went badly, planning to catch up first. The update that hides a problem is the one your
stakeholder remembers when the problem arrives anyway. **Bad news goes in the week it happens, and
it goes near the top.** The [Stakeholder Communication Guide](MCCTC_145010_Guide_StakeholderCommunication.md#3-bad-news-we-are-behind)
shows how.

---

## Short form · Weeks 8-10

```markdown
Subject: <project name>: week <n> status

Hello <title and last name>,

This week: <one or two sentences on what was finished>.
Next week: <one sentence>.
What I need from you: <a question with a date, or "nothing this week">.

Thank you,
<first name>
```

---

## Full form · Weeks 11-17

```markdown
Subject: <project name>: week <n> update, <on track / at risk / behind>

Hello <title and last name>,

**Status: <on track / at risk / behind>.** <One sentence saying why.>

**What you can see or try this week**
- <What changed for you, in your terms. A link or where to find it, if there is one.>

**Progress against what we agreed**
| Acceptance criterion | Status |
|---|---|
| AC-1 <short name> | <working / in progress / not started / cut by agreement> |
| AC-2 | |

**Problems, and what I am doing about them**
- <The problem in one sentence. What it affects. What you are doing. When you will know more.>
- <Or "none this week.">

**What I need from you, and by when**
- <A decision or answer, with a date. Or "nothing this week.">

**Next week**
- <One to three things you will finish.>

**Scope**
<"No changes." Or the change request, and that it needs their agreement in writing.>

Thank you,
<first name>
Senior, AI Automation and Software Development
```

**From Week 12 on, add one line:** "The system has run for <n> days without manual intervention."
If it reset, say so and why.

---

## Choosing the status honestly

| Status | Use it when |
|---|---|
| **On track** | Everything planned for this sprint is done, and nothing you know of threatens the next one. |
| **At risk** | Something could cause a missed criterion, and you have a plan. Most honest weeks in a real project are this one. |
| **Behind** | A planned item is not done, or a criterion will not be met without a change. Say what you propose. |

**"At risk" is not a failure.** It is the status that lets your stakeholder help you while there is
still time.

---

## The same week, written two ways

**This is a composite example.** The hosting database for a shift sign-up app stopped accepting
connections on Wednesday, and two days went into fixing it.

**What a student instinctively writes:**

> Hi, things are going really well this week. I made a lot of progress on the backend and learned
> a lot about databases. Next week I will keep working on the shift page. Let me know if you have
> any questions.

It says nothing false. It also hides that the shift page is two days late, and it gives the
coordinator no reason to plan around it.

**What the stakeholder needs:**

> Status: at risk. The database connection failed on Wednesday and fixing it took two days, so
> the coordinator page is not ready yet.
>
> What you can see: the shared sign-up link now shows next week's shifts, read only.
>
> Problem: the coordinator page, where you create shifts, will be ready Wednesday of next week
> instead of today. I have already cut the printable view from this sprint so the page still
> lands next week. The fix and the reason for the failure are written up in my project log.
>
> What I need: nothing this week.

---

## Before you send · self-check

- [ ] The status in the subject line matches the body.
- [ ] Any problem is in the problems section, not softened elsewhere.
- [ ] Every "what I need" has a date.
- [ ] No technical word without its meaning in the same sentence.
- [ ] No personal data about anyone.
- [ ] Your instructor is copied.
- [ ] The exact text is committed.
