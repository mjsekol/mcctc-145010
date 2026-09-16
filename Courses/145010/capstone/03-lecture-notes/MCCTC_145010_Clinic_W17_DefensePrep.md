# Clinic · Defense Prep
## 145010 Senior Capstone · Clinic · Week 17, Thursday

**The signal:** presentation outlines that are feature tours: slide after slide of screens, with no
problem, no stakeholder, no numbers, and no known issue. The outline is drafted tomorrow and rehearsed
Monday.

**Slides:** [outline](../04-slides/MCCTC_145010_Slides_W17_DefensePrep.md). No exported deck yet. To
generate it when Gamma credits are available, from the repository root:
`node tools/gamma.js Courses/145010/capstone/04-slides/MCCTC_145010_Slides_W17_DefensePrep.md --export pptx`

**If you missed it,** you can learn the skill from this file alone. Read it with the
[Defense Question Bank](../09-project/MCCTC_145010_Capstone_DefenseQuestionBank.md) open beside it.

**Competencies:** 1.2.2 (deliver formal and informal presentations), 1.2.5 (communicate for an
intended audience and purpose), 1.1.7 (problem solving and critical thinking on work-related
decisions), 2.12.6 (stakeholder acceptance), 2.13.3 (final review and approvals)

**Every exchange below is a composite.** The Northside Community Garden is an invented organization.

---

## The idea in plain language

**You cannot memorize answers to questions you have not seen. You can practice the shape of a strong
answer until it is a habit.** Next week a panel asks you about five minutes of unscripted questions.
They come in four kinds, and every strong answer is already written down somewhere in your
repository.

## Why it exists

**The only way to fail the capstone outright is to submit work you cannot explain, and the defense is
where that is decided.** The defense is also 8 of the 20 Presentation & Defense points. The panel is
finding out whether you built this or assembled it.

**This is the part students fear most.** The students who kept real logs usually find it the least
stressful part of the capstone, because they are reading from their own records.

---

## The four kinds of question

| Kind | What the panel is really asking | Where your answer lives |
|---|---|---|
| **Technical** | How does this actually work? | Your code, architecture, and data dictionary |
| **Decision** | Why this and not that? | Your decision log |
| **Failure** | What happens when this breaks? | Your test plan, troubleshooting log, thirty-day record |
| **Honest** | What does not work, and what would you change? | Your acceptance record, usability findings, future improvements |

## The four-step answer shape

1. **Name the specific thing.** The file, the function, the table, the page, the decision number.
2. **Say what it does or why you chose it**, in one or two sentences.
3. **Give the evidence or the tradeoff.** A test, a measurement, an alternative you rejected.
4. **Stop.** A strong answer is usually under forty-five seconds.

---

## Worked example 1 · a failure question, weak and strong

```
PANEL    If the database is unavailable, what does a volunteer see?

WEAK     It should show an error. Flask handles errors, so it would just
         catch it and show a message or something.

STRONG   The route in app.py raises an OperationalError, and the
         database_down handler returns "Sign-up is down, try again in a few
         minutes" with status 503. That was AC-4. It failed in the acceptance
         run with an Internal Server Error, I added the handler, and the
         re-run passed on Thursday of Week 16. The log line records the error
         without any volunteer data.
```

**Count the steps in the strong answer.** Named thing: the handler in `app.py`. What it does: returns
the message with 503. Evidence: AC-4, the failure, the re-run. Stop. **"Should" is the word that
loses a failure question.** The panel wants what it does, not what it ought to do.

## Worked example 2 · your three most vulnerable questions

The bank tells you where to look: **the part you understand least**, **the acceptance criterion that
passed most narrowly or did not pass**, and **the decision you would be least comfortable defending
to your stakeholder.** A student's notes in `presentation/outline.md`:

```
1. Q: Your sessions use Flask-Login. How does it know who is signed in?
   Answer notes: a signed session cookie; the secret key signs it; where my key
   lives (environment variable, not the repository); what I do not know: the
   exact signing algorithm. Say so, and say where I would look.

2. Q: AC-6 is "accepted with follow-up." Why did it not pass?
   Answer notes: export format needed a library not approved for lab
   machines; found Week 16 Thu; agreed plain table export; FI-7.

3. Q: Why did you store first names at all?
   Answer notes: R2; the coordinator needs to see who is coming; D-8 considered
   bed numbers only; rejected because the coordinator calls out names at the
   gate; nothing else stored; retention rule removes last season.
```

**Notes, not a script.** Each one names the evidence you will point to.

## Worked example 3 · saying "I do not know" well

```
PANEL    If the host restarts your app after a crash, how many times will it
         try before giving up?

STUDENT  I do not know. I know the host restarted it on its own once, in the
         self-recovery test in my thirty-day record, section 2. I do not know
         the limit. I would find it in the host's documentation on restart
         policy, and I would test it by making the app crash on purpose more
         than once.
```

**The shape:** say it plainly, say what you do know that is nearby, say how you would find out, stop.
One "I do not know" handled like this raises a defense score. A confident wrong answer the panel can
see is wrong lowers it.

**The line you cannot cross.** "I do not know" is fine for an edge of the system. It is not fine for
the central parts you submitted. If you cannot explain how your own main feature works, no phrasing
fixes it.

---

## The rehearsal protocol

From the Defense Question Bank, "How to practice":

1. **Today, Week 17:** write your three most vulnerable questions and draft answer notes.
2. **Pair with a classmate on another track.** They ask ten questions from the bank, in random order,
   without warning. You answer out loud. They time each answer and mark any answer that was general
   where it could have been specific.
3. **Swap.**
4. **Record one improvement per answer** in your outline. A note, not a script.
5. **Week 18, Monday, rehearsal day:** do it again with a different partner.

```
## Rehearsal record
| Week and day   | With whom        | Time taken       | What I changed afterward                      |
| Week 17, Thu   | Hana (Full-Stack)| 11:40 + 6 Q      | cut screen tour; 3 answers said "should"; reread TS-4 |
| Week 18, Mon   | Luis (HMI)       | 9:55 + 10 Q      | D2 answer now names CR-3                       |
```

---

## The wrong version, and what it produces

```
presentation/outline.md
Slide 1: Title
Slide 2: Home page
Slide 3: Sign-up page
Slide 4: Coordinator page
Slide 5: Settings page
Slide 6: Thank you, questions?

Vulnerable questions: none, it all works.
Rehearsal: will practice the night before.
```

**What it produces:** a presentation the rubric describes as "a tour of features rather than an
account of a problem solved," the 3-4 band of 8. No problem, stakeholder, acceptance result,
usability count, or baseline number. "It all works" invites the honest question, "What does not
work?", with nothing prepared. Practicing alone the night before tests nothing, because nobody asks a
question you did not expect.

## Why the wrong version is tempting

Screens are what you spent the most hours on, and showing them feels like proof. Naming weak spots
feels like handing the panel ammunition. **The panel finds the weak spots either way.** The only
choice is whether you have thought about them first.

---

## What to do in your project today

1. Copy the [Final Presentation Outline template](../05-labs/MCCTC_145010_Template_FinalPresentationOutline.md)
   to `presentation/outline.md`. Draft the eight sections with their time budget.
2. Write your three most vulnerable questions, using the three places to look above, and the track
   guide's list for your track.
3. Draft answer notes for each, in the four-step shape, with the evidence named.
4. Rehearse with a partner from another track today or in Period 8. Fill in the rehearsal record.
5. Read the [Capstone Rubric, part 4](../09-project/MCCTC_145010_Capstone_Rubric.md#4-presentation--defense--20-points).
   Commit.

---

## Vocabulary

| Term | Meaning |
|---|---|
| **Defense** | The unscripted questions after your presentation |
| **Technical / decision / failure / honest** | The four kinds of defense question |
| **Four-step answer** | Name it, say what or why, give evidence, stop |
| **Vulnerable question** | A question aimed at the weakest part of your project |
| **Rehearsal record** | The table of practice runs and what you changed after each |

---

## Check yourself

1. Which kind of question is "Why SQLite and not a hosted database?", and where does your answer come
   from?
2. A panel member asks, "What happens if two people claim the same bed at once?" You tested it. Give
   the four steps in order, with what goes in each.
3. You are asked how your authentication library stores sessions and you are not sure. What are the
   four parts of your answer?

---

## Check your answers

**1.** A decision question. The answer comes from your decision log: the entry where you chose, the
alternative you considered, and why it lost.

**2.** Name it: the claim route and its check, for example the single transaction in the claim
function. Say what it does: only the first claim is saved and the second browser sees "This bed is
already taken." Evidence: test case T-07 and acceptance criterion AC-2, both passed. Stop.

**3.** Say plainly that you do not know. Say what you do know nearby, such as where the secret key
lives and that the cookie is signed. Say how you would find out: the library's documentation and a
test. Stop. If sessions are central to your project, study this before Monday.
