# Clinic · Writing Up a Session the Same Day
## 145010 Senior Capstone · Clinic · Week 15, Tuesday

**The signal:** yesterday's pilot write-ups with opinions and no counts, such as "they liked it" or
"seemed a little confused." Real sessions start today.

**Slides:** This clinic has no slide outline. It runs from the board.

**If you missed it,** you can learn the skill from this file alone.

**Competencies:** 2.12.4 (develop, perform, and document usability testing), 1.2.12 (technical
writing to complete forms and create reports), 1.10.5 (determine satisfaction by using measurement
tools)

**Every session record below is a composite**, written for this note. The Northside Community
Garden is an invented organization.

---

## The idea in plain language

**Before you go home, your paper sheet becomes `docs/control/usability/sessions/P<n>.md`, with
numbered lines.** Each line is one thing the participant did or said, with a time. Counts per task go
underneath. Opinions are copied word for word and labelled as opinions.

## Why it exists

**Nothing was recorded, so your sheet is the only record.** Your handwriting at 1:04 means something
today. By Thursday you have run four more sessions, and "H 12s arrows" could be anyone.

**The numbered lines are for Friday.** The findings table cites evidence as `P3 L7`. A finding with a
line number behind it is something your stakeholder, your instructor, and the panel can check.

---

## The shape of a write-up

```markdown
# Session P3
Week 15, Wednesday · Period 8 · school conference room · building adult
Project commit: 7d2e1b0 · Facilitator only, no note taker
Consent read as written: yes · Yes out loud: yes · Recorded: no · Names written: no

## What happened
L1  0:00  T1  read the page heading, scrolled down
L2  0:09  T1  clicked Saturday
...

## Per task
| Task | Completed | Time | Wrong attempts | First place they looked | Hesitations |

## Debrief, word for word (opinions)
## Accessibility and navigation notes
## Rule breaks, mine
## Moments that surprised me
```

---

## Worked example 1 · from sheet to lines

The sheet, as written during the session:

```
TIME  WHAT THEY DID                          WHAT THEY SAID
0:00  heading, scroll
0:09  Sat
0:13  Claim bed 2 - msg "already taken"      "huh"
0:20  H 6s
0:26  Claim bed 5 - ok                        
2:05  T2 Tab x9, focus lost after Claim?
2:40  mouse, "My shifts" link                 "I usually use the mouse anyway"
```

The write-up, the same afternoon:

```
L1   0:00  T1  read the page heading, scrolled to the bed list
L2   0:09  T1  clicked "Saturday"
L3   0:13  T1  pressed Claim on bed 2; message "This bed is already taken"
L4   0:13  T1  said "huh" (opinion)
L5   0:20  T1  hesitated 6 s on the bed list
L6   0:26  T1  pressed Claim on bed 5; message "Bed 5 is yours"; task complete
L7   2:05  T2  keyboard only: pressed Tab 9 times; after Claim, focus went to
               the top of the page (from memory, not certain it was 9)
L8   2:40  T2  switched to the mouse and clicked "My shifts"
L9   2:40  T2  said "I usually use the mouse anyway" (opinion)
```

**Four habits are visible.** The exact screen text replaces "msg." Shorthand becomes full words.
Anything filled in afterward is marked "from memory." Each spoken remark has its own line, labelled
as an opinion.

## Worked example 2 · the per-task counts

```
| Task | Completed           | Time | Wrong attempts | First place they looked | Hesitations |
| T1   | yes                 | 0:26 | 1 (L3)         | bed list                | 1 (L5)      |
| T2   | yes, with the mouse | 0:50 | 0              | Tab key                 | 0           |
| T3   | moved on at 3 min   | 3:00 | 2 (L12, L14)   | top menu                | 2           |
```

**T2 needs a careful word.** The task was "keyboard only." P3 finished it by switching to the mouse
after losing focus. So the honest entry is "yes, with the mouse," and L7 is the evidence of a keyboard
problem. Writing plain "yes" would hide the finding.

**T3 "moved on at 3 min"** is a result, not a failed session. It is exactly what the protocol says to
write when someone is stuck for three minutes.

## Worked example 3 · the parts people skip

```
## Debrief, word for word (opinions)
Q: If you had to do that again tomorrow, what would you do differently?
A: "I'd look for a list of my own shifts first, before signing up."
Q: What would you call the page where you see what you signed up for?
A: "My garden days."

## Rule breaks, mine
Task 3: I said "you can" at 3:40 ("you can go back"). T3 result carries this caveat.

## Moments that surprised me
- L7: focus jumped to the top after Claim. I never tested that with the keyboard.
- The name "My garden days" is better than "My shifts."
```

**The rule-break line is not a confession. It is data.** On Friday, any finding that rests on T3
from P3 carries the caveat, and your findings are more trustworthy because you said so.

---

## The wrong version, and what it produces

```markdown
# P3
Went pretty well. P3 seemed a little confused on the first one but figured it out.
Liked the design. Had some trouble with the keyboard thing. Said the colors were nice.
Overall good session, 8/10.
```

**What it produces on Friday:** nothing to count. "A little confused" is not a time or a wrong
attempt. "Some trouble with the keyboard thing" does not say where focus went, so nobody can fix it.
"Liked the design" and "colors were nice" are opinions with no label. "8/10" is a score the
participant never gave. There is no line number to cite. The findings table ends up built from
memory, which after five sessions means built from whatever you wanted to find.

## Why the wrong version is tempting

It is the end of the day, the session went fine, and a paragraph takes two minutes. Writing numbered
lines takes twenty. It also feels like you will remember. **You will not remember which of five
people lost focus after Claim.** The twenty minutes today saves an hour of guessing on Friday.

---

## Before you commit a write-up

- [ ] Every line has a time and a task number.
- [ ] Every spoken remark is word for word and labelled as an opinion.
- [ ] Every filled-in time is marked "from memory."
- [ ] The per-task table matches the lines, with line numbers in it.
- [ ] Your own rule breaks are recorded with the task.
- [ ] **Nothing identifies the person.** No name, age, job title, school, or description that
      points to one person. P-number and kind of participant only.
- [ ] **Nothing from this sheet or this file went into an AI tool.** Not to tidy it, not to
      summarize it.
- [ ] The paper sheet goes to your instructor or is kept at school, not left in a bag.

---

## What to do in your project today

1. After each session, block twenty minutes in the build period or Period 8 to write it up.
2. Use the shape above in `docs/control/usability/sessions/P<n>.md`.
3. Commit each write-up the day it happens.
4. Keep a running scratch list of "things more than one person did." Do not turn it into findings
   yet. That is Friday.
5. Follow the [Observation Sheet](../05-labs/MCCTC_145010_Template_UsabilityObservationSheet.md)
   checklist before you leave the room, and the
   [Usability Test Protocol](../05-labs/MCCTC_145010_Template_UsabilityTestProtocol.md) part 7 for the
   line numbering.

---

## Vocabulary

| Term | Meaning |
|---|---|
| **Session write-up** | The typed record of one session, `sessions/P<n>.md` |
| **Line number** | The `L7` label that lets a finding cite exact evidence |
| **Opinion** | Anything the participant said, copied word for word and labelled |
| **From memory** | A detail filled in after the session, marked so readers know |
| **Caveat** | A note that a result may be affected, for example by a facilitator slip |

---

## Check yourself

1. Rewrite as numbered lines: "P4 took forever to find Saturday, then got it."
2. A participant said "this was no problem" after two wrong attempts. How many lines is that, and what does
   each say?
3. Why can you not paste your sheet into an AI tool to clean up the handwriting, even with no names
   on it?

---

## Check your answers

**1.** Something like: "L2 0:05 T1 scrolled the bed list; L3 0:19 T1 clicked Sunday (wrong attempt);
L4 0:30 T1 hesitated 11 s at the week arrows; L5 0:48 T1 clicked Saturday." The exact times come
from your sheet. "Forever" becomes a number, and "got it" becomes the action that finished the task.

**2.** At least three: one line for each wrong attempt, with what they pressed and what the screen
said, and one line with their exact words, labelled as an opinion. The counts table then shows two
wrong attempts, whatever they said.

**3.** Rule 5 in the protocol forbids anything from a session going into an AI tool, with or without
names. The record is about a real person who agreed to be observed on paper by you, not by a service.
It also risks the tool changing what was written, and the sheet is the only record.
