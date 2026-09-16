# Clinic · The Update When the Week Went Badly
## 145010 Senior Capstone · Week 12, Wednesday · 15 minutes · Improve

**Slides for this clinic:** This clinic has no slide outline. It runs at the board.

**When this clinic runs.** Week 12, Wednesday, or any week the room shows this signal: Sprint 1
reviews that say "almost" and updates that say "going well."
**If you missed it,** you can learn the skill from this file alone.
**Competencies:** 1.2.5 (communicate for an intended audience and purpose), 1.2.11 (professional
correspondence), 1.4.8 (electronic communication and network etiquette), 1.2.13 (identify
stakeholders and solicit their opinions), 2.13.2 (communicate plans to key stakeholders in a timely
manner)

---

## Why this exists

**Some of you wrote "going well" last Friday in a week that did not go well.** Nobody lied on
purpose. You expected to catch up by Monday, so the problem felt temporary. Now it is Wednesday of
Week 12, the problem is still there, and Friday's update has to say so.

**This is the hardest message of the capstone to write**, because it may also have to correct the
last one. It is also the one your stakeholder will remember. A stakeholder who hears bad news early
can plan around it. A stakeholder who hears it in Week 16 stops trusting everything you sent before.

Friday is also scope lock. If this week went badly, Friday's update is where the plan changes, and
tomorrow's clinic covers the scope lock statement that goes with it. Today is the update itself.

The full guidance is in the
[Stakeholder Communication Guide, section 3](../05-labs/MCCTC_145010_Guide_StakeholderCommunication.md#3-bad-news-we-are-behind).
This clinic adapts it to Week 12. It does not replace it.

---

## The skill in plain language

A bad-week update has six moves, in this order.

1. **Choose the status honestly.** Use the table in the
   [Weekly Stakeholder Update](../05-labs/MCCTC_145010_Template_WeeklyStakeholderUpdate.md#choosing-the-status-honestly)
   template. If a planned item is not done, the status is **behind**, not "at risk."
2. **Bad news first.** In the first two sentences. Not after the good news.
3. **One apology at most**, and only if it was your doing. Then move to the plan.
4. **What you are doing**, not how you feel about it.
5. **A choice for the stakeholder**, when there is one. People would rather decide than be told.
6. **When they will hear from you next**, as a day. Then keep it.

**If last week's update was wrong, say so once, plainly.** "Last Friday I wrote that the project was
on track. It was not." Then move on. That sentence costs you less than the stakeholder finding out
on their own.

**Never write a calendar date you have not checked.** "Monday" or "next Friday" is enough.

---

## Worked example 1 · the week, in facts

**This is a composite, not a real organization, and not the Parts Bin Board.** An Industrial/HMI
student is building "Cooler Watch" for a volunteer food pantry. A sensor reads the walk-in cooler's
temperature. A panel shows it. A web dashboard lets the pantry's operations lead check it from their
office. The system monitors only. It never switches anything.

The Sprint 1 review, Week 11 Friday, in the student's own file:

```
Goal met? partly
Sensor reading reaches the panel: yes, on the lab bench
Dashboard reachable by the operations lead: no
  The connection out of the lab network needs authorization.
  I asked on Thursday. It had not been decided by Friday.
Hours planned: 10   Hours spent: 11   Tasks finished: 3 of 5
Also: 5 hours went into a trend chart that was not in the plan.
Thirty-day clock: not started
```

Update 1, sent that same Friday, said "Status: on track. Everything is going well."

Two things are wrong with that. The review says "partly," and the student knew it when they sent
the update. And the chart that ate five hours was never in the plan, which is scope creeping in
before scope lock.

---

## Worked example 2 · what a student instinctively writes on Friday of Week 12

```
Subject: Cooler Watch: week 12 update

Hi, sorry for the late update and sorry again about last week, I know you
are really busy and I really appreciate your patience. Things are mostly
going well! I added a really cool trend chart that I think you will like.
There have been a few small delays with the network but I am working on it
and it should be fine soon. Let me know if you have any questions!
```

Read it the way the operations lead will.

- **Three apologies** and no plan. The reader ends up reassuring the student.
- **"Mostly going well."** The dashboard they need still does not reach them.
- **Good news first**, and it is the chart nobody asked for.
- **"A few small delays."** Buried, vague, with no effect named.
- **"Should be fine soon."** No day, no choice, nothing to plan around.
- Two exclamation points in a message about a problem.

---

## Worked example 3 · the same week, written honestly

```
Subject: Cooler Watch: week 12 update, behind

Hello <title and last name>,

Status: behind. The dashboard is not yet reachable from your office,
which means you cannot yet check the cooler from your desk.

Last Friday I wrote that the project was on track. It was not, and I
should have said so then. I am sorry about that.

What works: the sensor reading reaches the panel on our lab bench, every
minute, and the panel shows how old the last reading is.

The problem: the dashboard needs permission to connect from the school's
lab network to outside it. My instructor is asking district IT, and I
expect an answer by Tuesday.

If the answer is yes, you can check the dashboard from your office by
the end of next week. If it is no, there are two ways forward, and I
would like you to choose:
  1. The panel goes on a screen at the pantry, next to the cooler, and
     you check the reading there.
  2. The device connects through the pantry's own network, so the
     dashboard reaches your office. This needs approval from whoever
     looks after that network.
Which would you prefer? A reply by Tuesday lets me plan the next sprint
either way.

The thirty-day unattended run has not started yet, because the system
is not yet where it will finally run. It starts the day it is.

Scope: I built a trend chart this sprint that was not in our agreement.
I have moved it to the list of future improvements, and it will not take
time from what we agreed.

I will write to you on Tuesday when I hear from district IT, and send the
full update on Friday as usual.

Thank you,
<first name>
```

What changed, move by move:

| Move | Where it is |
|---|---|
| Status honestly chosen | "Behind," in the subject and the first word of the body |
| Bad news first | The dashboard, in the first sentence, in the reader's terms: "check the cooler from your desk" |
| One apology | Once, for the wrong update, with no extra words |
| What you are doing | The instructor's request to district IT, with a day |
| A choice | Two options for the likely problem, and a question with a reply-by day |
| Next update | Tuesday, and Friday |

It also records the out-of-plan chart as a scope decision instead of presenting it as a gift, and
it includes the Week 12 line about the thirty-day run, even though the news is bad. A clock that is
not running by Week 12, Friday is also a conversation with your instructor at standup, before the
update is sent.
**On Friday, the partner who reads it before it is sent checks each move.**

---

## The wrong version, and what it costs

The wrong version is example 2, sent. **What it costs:** the operations lead plans as if the
dashboard is coming. In Week 15 the usability sessions need a dashboard the pantry can reach, and it
still cannot. By then there is no time to set up the panel option instead. The record also shows two
updates in a row that softened a problem, which is scored under the stakeholder communication record
in your rubric.

---

## Why the wrong version is tempting

**You expect to fix it before anyone notices.** Sometimes you do. The week you do not, the update
that hid it is the one they reread.

**Admitting last week was wrong feels like admitting you are bad at this.** It is the opposite. A
professional who corrects the record is one a stakeholder keeps trusting.

**Apologizing feels polite.** Once is polite. Three times hands your feelings to the reader to
manage.

---

## Do this today

1. Open your Sprint 1 review and your Update 1 side by side. Do they agree?
2. Draft Friday's update in `docs/communication/updates/week-12.md` from the
   [template](../05-labs/MCCTC_145010_Template_WeeklyStakeholderUpdate.md). Write the status line
   first.
3. Check it against the six moves. Count your apologies.
4. If Update 1 was wrong, write the one correcting sentence.
5. If something is blocked by a decision someone else makes, tell your instructor at standup
   tomorrow, so the update can name a real day.
6. **Commit the draft.** It is sent Friday, after a partner reads it, with your instructor copied.

---

## If you are ahead, if you are behind

**If you are ahead:** your week went well. Write the update anyway and check it against the same
moves. "On track" is a claim, so the "What you can see" section has to prove it.

**If you are behind:** you have not sent Update 1 at all. Send it today, short and honest, and tell
your instructor. Then write Friday's update on time.

---

## Words the WebXam uses

| Exam word | What it means here |
|---|---|
| **Professional correspondence** | The update, written for a client, not a friend (1.2.11) |
| **Intended audience and purpose** | The operations lead, who needs to plan, not to hear how hard you worked (1.2.5) |
| **Network etiquette** | School account, instructor copied, a clear subject, no slang or exclamation points (1.4.8) |
| **Solicit stakeholders' opinions** | The choice you offer, with a reply-by day (1.2.13) |
| **Timely communication** | Bad news the week it happens, and the next update on the day you said (2.13.2) |

---

## Self-check

**1.** Your sprint plan had four tasks. Three are done. The one not done is the page your
stakeholder asked for most. On track, at risk, or behind?

**2.** Rewrite this opening so the bad news comes first: "Hope you had a good week. I made good
progress on the styling, and the sign-in page is almost ready, though the saving is not working
yet."

**3.** Why offer the stakeholder a choice instead of telling them your plan?

### Answers

**1.** Behind. A planned item is not done, and it is the one that matters most to the stakeholder.
"At risk" is for something that could go wrong and has a plan. This already went wrong.

**2.** One good version: "Status: behind. Saving does not work yet, so the sign-in page cannot be
used this week. I expect a fix by Wednesday and will tell you Wednesday either way." The styling can
go under "what you can see," or be left out.

**3.** Because it is their problem you are solving, and they know things you do not, such as which
option fits how their organization works. A choice also turns bad news into a decision they help
make, which keeps them involved and keeps the relationship working.
