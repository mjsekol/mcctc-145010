# Clinic · Counting Without Names
## 145010 Senior Capstone · Week 9, Tuesday · 15 minutes · Measure

**Slides for this clinic:** This clinic has no slide outline. It runs at the board.

**When this clinic runs.** Week 9, Tuesday, or any week the room shows this signal: anyone about
to copy a record with names in it.
**If you missed it,** you can learn the skill from this file alone.
**Competencies:** 1.10.5 (determine satisfaction by using measurement tools), 2.11.4 (gather and
analyze data about the problem), 1.2.1 (extract relevant, valid information and cite its source),
1.2.11 (write professional correspondence)

---

## Why this exists

Today you collect your baseline. The records that hold it almost always hold names too: customer
names on a repair log, patient names on a sign-in sheet, staff names on a schedule.

**No personal information enters your project or any AI tool. Ever.** That is non-negotiable 7
in the [Capstone Specification](../09-project/MCCTC_145010_Capstone_Specification.md#non-negotiables).
Breaking it stops the work until it is fixed. It also breaks the trust that got you the records in
the first place. A stakeholder who sees their customers' names in a student's repository does not
answer the next email.

The good news is that you never need a name to count something. You need to know that a thing
happened, and how often.

## The skill in plain language

**Count things. Do not copy people.** Three moves, in order of preference:

1. **The stakeholder counts, you record the totals.** You hand them a tally sheet. They read their
   own records and fill it in. You never see a name.
2. **The stakeholder removes names first.** They cover or cut the name and contact columns before
   you see anything. You check what you received before you store it.
3. **You count beside them, and write only totals.** At school, or on a visit the school arranged,
   with your instructor's approval. Your notebook gets numbers, never a name.

**Never do any of these:**

- Photograph a page that has names on it.
- Copy a row "for now" and plan to delete the names later.
- Paste any record into an AI tool to count it for you, even with names blurred.

**And when the data does not arrive:** write down what you asked for and when. Pick a smaller
honest fallback. Say so in the limits. **A smaller honest baseline beats a guessed one.**

## Worked example 1 · the tally sheet

*Composite, not a real organization.* The Parts Bin Board student needs stalled repairs from the
bike co-op's paper repair log. That log has each customer's name and phone number. So the student
sends the shop coordinator this sheet and never asks for the log:

```
Parts Bin Board . baseline tally sheet . for the shop coordinator
Please fill in one row per open-shop night, starting with the most recent.
Please do not write any names or phone numbers on this sheet.

Night   Repairs started   Stalled: bin was empty   Which bins ran out
-----   ---------------   ----------------------   ----------------------
1
2
3
4
5
6

"Stalled: bin was empty" means the log says "waiting on part" and the part
comes from a bin (tubes, brake pads, chains, cables).
```

Every column is a count or a part type. Nothing on the sheet can identify a person.

## Worked example 2 · the request message

*Composite.* Sent Week 9, Monday, from the student's school account with the instructor copied.

```
Subject: Parts Bin Board: one count I need from the repair log

Hello,

To show later whether the board helps, I need a "before" number now.
Could you fill in the attached tally sheet for the last six open-shop
nights? It asks only for counts: repairs started, and repairs that
stalled because a bin was empty. Please leave out all names and phone
numbers. I do not need to see the log itself.

It should take about ten minutes. If you can send it back by Thursday,
I can finish the baseline this week.

Thank you,
Jordan
Senior, AI Automation & Software Development
```

It says why before what, asks for counts only, names the time it takes, and gives a deadline. It
does not ask for the log.

## Worked example 3 · when the data does not arrive

*Composite, and a different run of the same story.* By Wednesday there is no reply. The student
does three things.

**First,** the contact log gets a line:

```
| Week 9, Wed | sent | school email, instructor copied | follow-up on tally sheet | no reply to Monday's request | |
```

**Second,** a short follow-up goes out, with the instructor copied, asking whether a smaller
version helps: "Could you count only the last three nights?"

**Third,** section 2 of the baseline record says what happened:

```
Asked for: six nights of counts, Week 9, Monday.
Received:  three nights of counts, Week 9, Thursday.
Using:     the three nights received. Week 17 will repeat with three nights,
           so the two counts compare.
```

That is honest, and it can be repeated. A number the student estimated alone would be neither.

## The wrong version, and what it costs

*Composite.* A student photographs two pages of the repair log on a phone "to count later," then
pastes the text into an AI chat and asks it to count the stalled repairs.

What that costs:

1. **Non-negotiable 7 is broken twice.** Customers' names and phone numbers are now on a personal
   phone and inside an AI tool the co-op never agreed to.
2. **The work stops.** Tell your instructor the same day. Your instructor decides with you what
   happens to the photo and how the stakeholder is told. Do not hide it. A hidden mistake found
   later is far worse.
3. **The count may be wrong anyway.** A chat tool can miscount or invent rows. You would be
   reporting a number you did not check.

## Why the wrong version is tempting

A photo takes two seconds. Counting by hand takes ten minutes. The names feel harmless because you
were not going to use them. But the rule is not about what you meant to do with the data. It is
about where the data ended up. **If you never hold a name, you can never leak one.**

## Do this today

In the build period:

1. If you have not sent your data request, send it now, with a tally sheet shaped for your
   records. Instructor copied. Log it in `docs/communication/contact-log.md`.
2. If the data arrived, check it for names before you save anything. If a name is there, stop and
   tell your instructor.
3. Fill in section 2 of `docs/measure-analyze/baseline.md`, including the line "How personal data
   was kept out."
4. Commit. Commit the tally sheet only if it has no names on it.

Use the [Baseline Measurement template](../05-labs/MCCTC_145010_Template_BaselineMeasurement.md).
The follow-up steps for a quiet stakeholder are in the
[Stakeholder Communication Guide](../05-labs/MCCTC_145010_Guide_StakeholderCommunication.md#8-when-your-stakeholder-goes-quiet).

## If you are ahead, if you are behind

**Ahead.** Write your "what I did not measure, and why" section. Then check your needs-discovery
meeting record: does it name anyone who is not the stakeholder? If so, change them to a role.

**Behind.** If you have not asked for data yet, you are one day behind and the fix is one email.
Send it before standup ends tomorrow. Ask your instructor to read it first.

## Words the WebXam uses

| Exam word | What it means here |
|---|---|
| **Valid information** | Data that measures what you claim, from a source you can name. 1.2.1. |
| **Cite the source** | Say where each number came from: which record, which period, who counted. |
| **Measurement tool** | The tally sheet, the log, the count. 1.10.5. |
| **Professional correspondence** | The request message: purpose, ask, time, deadline. 1.2.11. |
| **Personal information** | Anything that identifies a person: a name, a phone number, a photo, an address. |

## Self-check

**1.** Your stakeholder emails you a spreadsheet of last month's appointments to count. You open
it and see a column of client names. What do you do?

**2.** Why is "the stakeholder counts, you record the totals" the first choice, ahead of "the
stakeholder removes names first"?

**3.** Your stakeholder sends counts for four nights instead of six. Write the one sentence that
goes in your limits.

### Answers

**1.** Stop. Do not save it into your project and do not paste it anywhere. Tell your instructor
the same day. Then ask the stakeholder, with your instructor copied, for counts only, and offer
your tally sheet.

**2.** Because if you never receive the records, a name cannot slip through. When the stakeholder
removes names, one missed column still reaches you.

**3.** One good answer: "The baseline covers four open-shop nights, not the six planned, because
that is what the coordinator could provide; the Week 17 repeat will also use four nights."
