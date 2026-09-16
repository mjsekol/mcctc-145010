# Clinic · Running a Usability Session
## 145010 Senior Capstone · Clinic · Week 15, Monday

**The signal:** first sessions are tomorrow. Anyone who has not piloted their tasks today needs this
before the build period starts.

**Slides:** [outline](../04-slides/MCCTC_145010_Slides_W15_RunningAUsabilitySession.md). No
exported deck yet. To generate it when Gamma credits are available, from the repository root:
`node tools/gamma.js Courses/145010/capstone/04-slides/MCCTC_145010_Slides_W15_RunningAUsabilitySession.md --export pptx`

**If you missed it,** you can learn the skill from this file alone. You ran a study in 145130. This
one is on a finished product for a real stakeholder, and the rules are the same.

**Competencies:** 6.5.10 (develop and execute usability tests on a completed website, checking
accessibility, ease of use, and navigation), 2.12.4 (develop, perform, and document usability
testing), 1.10.2 (determine the customer's needs), 1.10.5 (determine satisfaction by using
measurement tools)

**Every session below is a composite**, written for this note. The Northside Community Garden is an
invented organization, and P2 is not a real person.

---

## The idea in plain language

**You set up a starting state, read a goal out loud, and then stay quiet while a stranger tries it.
You write down what they do, with times.** That is the whole method. The difficulty is entirely in
the staying quiet.

## Why it exists

You know where everything is because you put it there, and you cannot un-know it. The only way to
find out what a stranger does not know is to watch one try.

**What they did is the data. Your reasons are not.** When a participant struggles, you will want to
explain. The moment you explain, you have stopped measuring whether they would have found it.

### The rules, which are conditions and not advice

From the [Usability Test Protocol](../05-labs/MCCTC_145010_Template_UsabilityTestProtocol.md).
Breaking one stops the session.

1. **They say yes out loud** after you read the consent script as written.
2. **No recording of any kind.** No video, audio, screen capture, or photographs. You write on paper.
3. **Participants are P1 to P5.** No names, ages, or job titles anywhere.
4. **No classmates in the formal five.** Today's pilot is the classmate session.
5. **Nothing from a session goes into an AI tool.** Not the notes, not a summary.
6. **Never alone with an adult you do not know.**
7. **You thank every participant in writing** before the last day of the course.

---

## Worked example 1 · the first ninety seconds

```
FACILITATOR  (reads the consent script word for word)
             I am testing a project I built, and I am not testing you. Anything
             that goes wrong is information I need. I am going to ask you to do a
             few things and then stay quiet while you do them, and that is on
             purpose, not rude. I am not recording anything and I am not writing
             down your name. You can stop at any point, for any reason, and you do
             not have to tell me why. Is that okay?
P2           Sure, yes.
FACILITATOR  If you get stuck, stay stuck for a bit. That is the part I most
             need to see.
FACILITATOR  (reads Task 1) You can help at the garden this Saturday morning.
             Sign yourself up for a bed that still needs someone.
             (starts the clock, puts hands in lap)
```

**The result:** a spoken yes, which you tick on the sheet. The consent script is read exactly as
written, because the sentences people drop when they paraphrase are the recording one and the
stopping one. A nod is not a yes.

## Worked example 2 · a task written as a goal

```
INSTRUCTION (do not use)   Click the Saturday tab and press Claim on bed 4.
GOAL (use)                 You can help at the garden this Saturday morning.
                           Sign yourself up for a bed that still needs someone.
Starting state             Week of the session selected; beds 1-3 taken, 4-6 open
Completed when             one open Saturday bed shows the participant's first name
Expected time              under 60 seconds
Tests requirement          R3
```

**The instruction version tests whether P2 can follow directions.** The goal version tests whether
your page shows them where Saturday is and which beds are open, which is what R3 needs. Monday's
pilot checks that the goal does not give the answer away and that the task is possible at all.

## Worked example 3 · the moment it goes wrong, and the sheet it produces

```
0:00  scrolls the page top to bottom
0:18  clicks "Sunday"
0:24  scrolls again, pauses
0:31  P2: "Where are the Saturday ones?"
      FACILITATOR: "What are you trying to do right now?"
0:35  P2: "Find Saturday."   (facilitator says nothing else)
0:52  hovers over the week arrows, back and forth
1:04  clicks the right arrow, sees next week's Saturday, clicks back
1:20  clicks "Saturday", clicks Claim on bed 4
1:26  sees "Bed 4 is yours"
1:30  P2: "Oh, that was fine."
```

The same session on the [Observation Sheet](../05-labs/MCCTC_145010_Template_UsabilityObservationSheet.md):

```
TIME   WHAT THEY DID                                WHAT THEY SAID
0:00   scrolled whole page
0:18   clicked Sunday (wrong attempt 1)
0:24   scrolled, H 7s                               "Where are the Saturday ones?"
0:52   H 12s over week arrows
1:04   moved to next week and back (wrong 2)
1:20   Saturday, Claim bed 4
1:26   success message                              "Oh, that was fine."

Task 1   Completed: yes   Time: 1:26   Wrong attempts: 2   First look: Sunday   H: 2
Rule-break box: [x] I did not break any of them
```

**Read the two columns together.** The right column says "fine." The left column says 86 seconds
against an expected 60, two wrong attempts, and two hesitations. **The left column wins.** And notice
what the facilitator said: one allowed question, then nothing.

---

## What you may say, and what you may not

```
MAY NOT                                    MAY
the name of a control ("click Save")       nothing, which is usually right
"you can..."                               "What are you trying to do right now?"
"did that work?"                           "What did you expect to happen?"
the answer, including with your face       "Take your time."
```

**"Am I doing this right?"** gets: "There is no right way. I want to see what you would actually do."
**Stuck for three minutes?** Say "Let us move to the next one," and write where they were stuck.
**Fifteen minutes?** Stop, even mid-task.

---

## The wrong version, and what it produces

```
0:31  P2: "Where are the Saturday ones?"
      FACILITATOR: "Oh, you can use the tabs at the top. I put them there because
      the coordinator wanted days first. See, Saturday. Then press Claim."
0:40  clicks Saturday, Claim
0:42  success
```

**What it produces:** a sheet that says Task 1 was completed in 42 seconds with no problems. It is
false. The finding, that people do not see the day tabs, is gone, and the facilitator's explanation
became the design. Five sessions like this produce a findings table with nothing in it. The rule-break
box must now be ticked for "named a control" and "explained or defended the design," and the Task 1
result carries that caveat.

## Why the wrong version is tempting

Watching someone struggle with your work is uncomfortable. Helping feels kind. Explaining feels like
setting the record straight. **Silence is the kind thing here**, because the next person to struggle
will be a real volunteer on a Saturday morning, with nobody there to explain.

If you catch yourself mid-explanation, say: "Sorry, ignore me. Please carry on the way you were."

---

## What to do in your project today

1. Finish `docs/control/usability/protocol.md` from the protocol template: four to six goal tasks,
   each with a starting state, completed-when, expected time, and requirement.
2. Include at least one task on navigation or accessibility: several steps deep, on a phone, or with
   the keyboard alone.
3. Pilot with a classmate. Label it a pilot. Fix every task the pilot broke, and record what it found.
4. Confirm five sessions and a backup, with times.
5. Print one observation sheet per participant, plus spares.
6. Practice the consent script out loud twice. Commit.

---

## Vocabulary

| Term | Meaning |
|---|---|
| **Usability session** | Watching one person try goal tasks on your project while you stay quiet |
| **Goal task** | What the person wants to do, without saying how |
| **Starting state** | What is on screen and in the data before the task begins |
| **Hesitation (H)** | A pause, hover, or back-and-forth, written with its length |
| **Wrong attempt** | A separate try before the right one |
| **Pilot** | A practice session with a classmate to fix the tasks |

---

## Check yourself

1. A participant finishes a task and says, "That was confusing." Your sheet shows 20 seconds and no
   wrong attempts. Which column wins, and what do you write?
2. Rewrite as a goal: "Open the Alarms tab and acknowledge the alarm."
3. A participant asks, "Should I press the blue one?" What do you say?

---

## Check your answers

**1.** The left column, what they did, is the measurement: 20 seconds, no wrong attempts. You still
record "That was confusing" word for word in the right column, labelled as their opinion. If you
want to know more, ask in the debrief: "Was there a moment you were not sure what would happen
next?"

**2.** "The panel says something is wrong. Deal with it the way you would on a real shift." It names
the situation and the goal, and it does not name the tab or the button.

**3.** "There is no right way. I want to see what you would actually do." Then stay quiet. Do not say
yes, no, or "you are doing fine."
