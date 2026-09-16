# Clinic · The Needs-Discovery Conversation
## 145010 Senior Capstone · Week 7, Thursday · 15 minutes · Define

**Slides for this clinic:** This clinic has no slide outline. It runs at the board.

**When this clinic runs.** Week 7, Thursday, or any week the room shows this signal: stakeholders
replying yes and students with no question list.

**If you missed it,** you can learn the skill from this file alone.

**Competencies:** 1.2.13 (identify stakeholders and solicit their opinions), 1.10.2 (determine the
customer's needs and identify solutions), 1.2.12 (technical writing to complete forms and reports),
1.6.5 (organizational structure and chain of command), 1.3.5 (safety compliance measures).

---

## Why this exists

**Your stakeholder said yes. Now you have about twenty minutes to learn their problem.** Most of what
you write for the next eleven weeks is built from this conversation: your proposal's client needs,
your acceptance criteria, your baseline question, and half your defense answers.

The conversation usually goes wrong in one of two ways. The student arrives with no questions and
fills the silence by describing the app they want to build. Or the student asks questions that can
only be answered yes, like "Would you use an app that tracks parts?" Almost everyone says yes to be
polite. You leave with a yes and no information.

**The meeting record matters as much as the meeting.** Two people leave the same conversation
remembering different things. A record written the same day, with their words in quotation marks,
turns a conversation into something both of you can check.

---

## The skill in plain language

**Before.** Pick eight to ten questions from the
[needs-discovery questions](../05-labs/MCCTC_145010_Template_MeetingRecord.md#needs-discovery-questions).
Put them in order: the problem, the people, the limits, the measuring. Print them or have them open.
Confirm the meeting is at school or on an approved call, with your instructor present or aware.

**During.**

- **Open with "walk me through the last time."** A specific recent event gives you steps, people,
  and costs. "How does it usually go?" gives you a summary with the details sanded off.
- **Follow the answer, not your list.** "What happened next?" and "How did you find out?" are the
  two most useful follow-ups you have.
- **Let silence sit.** Count to five in your head. People often add the most useful thing after a
  pause.
- **Do not pitch.** If they ask what you will build, say: "I do not know yet. I want to understand
  the problem first. I will bring you a written proposal next week."
- **Write their words.** Exact phrases in quotation marks. Your own interpretations go in a separate
  column later.
- **Ask for a record you can count, with no names in it.** That becomes your Week 9 baseline.
- **Close with the promise.** "Thank you. I will send you a short summary today so you can correct
  anything I got wrong."

**After, the same day.** Write the meeting record. Send the short summary from your school account
with your instructor copied. Add a line to the contact log. Commit.

---

## Worked example 1 · The question list, rewritten

*Composite, not a real organization or person.* A volunteer-run community bike repair co-op.
Volunteers fix donated bikes on open-shop nights. The stakeholder is the co-op's shop coordinator.

**Before:**

```
1. Would you use an app that tracks your parts?
2. Do you have trouble with inventory?
3. Would notifications be helpful?
4. Is your current system bad?
5. What features do you want?
```

Every question is closed, leading, or about a product. Question 5 hands the design job to someone
who is not a developer.

**After:**

```
1. Walk me through the last open-shop night when a repair stopped
   because a part was missing.
2. How did you find out the bin was empty?
3. How often does that happen? Is there a record I could count, with
   no names in it?
4. What does it cost when it happens: time, a customer waiting, a
   volunteer leaving?
5. What have you already tried?
6. Who else deals with this? Who would need to approve something new?
7. What devices are in the shop, and who uses them?
8. Is there anything I must not see, touch, or store?
9. How would you know, a month from now, that this was fixed?
```

---

## Worked example 2 · Following the answer

*Composite.* A short stretch of the conversation. **C** is the coordinator. **S** is the student.

```
S: Walk me through the last night a repair stopped because a part was
   missing.
C: Tuesday. A volunteer had a kid's bike up on the stand, went for a
   tube, and the bin was empty.
S: What happened next?
C: She came and found me. I walked the shelves, found two other bins
   empty, and texted myself a list so I would remember to order.
S: How did you find out the other two were empty?
C: I didn't until I looked. Nobody tells me. They grab the last one and
   move on.
S: (waits)
C: Honestly, some of the volunteers are retirees who don't carry a
   smartphone. There's a desktop by the door, and that's it.
S: How often does a repair stop like that?
C: A few times a night. It's in the repair log, "waiting on part."
C: So what are you going to build, an app?
S: I don't know yet. I want to understand the problem first. I'll send
   you a written proposal next week.
C: Good. I don't need anything fancy.
```

**Look at what the pause produced.** The fact about the retirees and the desktop by the door came
after the student said nothing. It changes the whole design: anything that needs a phone would
exclude some of the volunteers.

**Look at the pitch that did not happen.** The coordinator asked. The student declined. The
coordinator's reply, "I don't need anything fancy," is now in the record, and it will matter at
the scope check.

---

## Worked example 3 · The same-day record and the follow-up

The record follows the [Meeting Record template](../05-labs/MCCTC_145010_Template_MeetingRecord.md).
Here are its two most important sections, from the conversation above.

```markdown
## What they said
- The last stalled repair was a Tuesday: a tube bin was empty.
- The coordinator walks the shelves and "texted myself a list."
- "Nobody tells me. They grab the last one and move on."
- "Some of the volunteers are retirees who don't carry a smartphone."
- There is one desktop, by the door.
- Stalled repairs are written in the paper repair log as "waiting on part."
- "I don't need anything fancy."

## What I understood
*My interpretation.*
- The real gap is the moment a volunteer takes the last item. Nobody records it.
- Anything I propose must work on the desktop by the door, not only on phones.
- The repair log could give a baseline count of stalled repairs, with no names, if the
  coordinator counts the entries.
```

The follow-up message, sent the same day:

```
Subject: Summary of our conversation about empty parts bins

Dear <title and last name>,

Thank you for your time today. Here is what I understood. Please
correct anything I got wrong.

- Repairs stall when a bin is empty and nobody has told you.
- Some volunteers use the desktop by the door because they do not
  carry a smartphone.
- The repair log records stalled repairs as "waiting on part."

One question: could you count the "waiting on part" entries for the
last six open-shop nights, without any names, and send me the numbers?
A reply by next Wednesday would let me plan my measurement.

Thank you,
<first name>
```

---

## The wrong version, and what it costs

The student arrives with a mockup and walks the coordinator through five screens. The coordinator
says "Sure, looks great." The meeting record lists the student's features and no needs.

In Week 8 the proposal's client needs section has nothing to cite, so the student cites their own
mockup. The acceptance criteria describe the student's idea, and the coordinator signs them to be
polite. In Week 15, usability testing shows the retirees at the desktop by the door cannot use a
phone-first design. Nobody asked who uses the shop computer, because the meeting was a
demonstration.

---

## Why the wrong version is tempting

Silence in a conversation with an adult feels like failing. Showing a mockup feels like proof that
you are capable. And a yes feels like progress, because you walked in hoping for one.

A needs-discovery conversation is the one meeting in the capstone where you are not supposed to
have answers. Your job is to leave knowing more than you arrived with.

---

## Do this today

1. Build your question list: eight to ten questions, in order, from the template list.
2. Save it as `docs/communication/meetings/week-07-fri-needs-discovery.md`, under a heading
   "Questions I plan to ask". After the conversation, the rest of the record goes in the same file.
3. Confirm the time and place with your stakeholder and your instructor.
4. Practice the pitch refusal aloud once: "I do not know yet. I want to understand the problem first."
5. Commit.

---

## If you are ahead, if you are behind

**Ahead.** Start section 4 of your concept proposal, client needs, with placeholders that say
"from the needs-discovery meeting, Week 7, Friday." Tomorrow you fill them from the record.

**Behind.** **No reply to your first contact yet?** Today is the day to send one polite follow-up
and tell your instructor at this standup, not at the end of the day. The follow-up draft is in the
[Stakeholder Communication Guide](../05-labs/MCCTC_145010_Guide_StakeholderCommunication.md#8-when-your-stakeholder-goes-quiet).

---

## Words the WebXam uses

| Exam word | What it means in this conversation |
|---|---|
| **Client needs** | What the stakeholder must be able to do. You find them by asking about the last time, not by pitching |
| **Solicit opinions** | Ask for the stakeholder's view and record it in their words |
| **Stakeholder** | Anyone affected by the project or with authority over it. Ask who else deals with the problem |
| **Chain of command** | Who approves what in their organization. Ask who would need to approve something new |
| **Safety compliance** | The workplace's safety rules. Ask whether any apply where the project would be used |
| **Report** | A written record for others to use. The meeting record is one |

---

## Self-check

**1.** Rewrite this question so it cannot be answered with a polite yes: "Would a website that shows
empty bins help you?"

**2.** Your stakeholder asks, halfway through, "So what are you going to make?" What do you say, and
why?

**3.** In your notes you wrote "the coordinator is frustrated with the volunteers." Which section of
the meeting record does that belong in, and why?

### Answers

**1.** Something like: "Walk me through the last time you found an empty bin. How did you find out?"
It asks about a real event, so the answer contains steps and facts instead of a courtesy.

**2.** "I do not know yet. I want to understand the problem first, and I will bring you a written
proposal next week." Describing a solution makes them react to your idea instead of telling you
about their problem.

**3.** "What I understood." It is your interpretation, not their words. If the coordinator said
something you can quote, that quotation goes under "What they said," and the interpretation stays
labelled as yours.
