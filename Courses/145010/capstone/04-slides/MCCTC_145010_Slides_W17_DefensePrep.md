# Five Minutes Nobody Scripted
---
## Slide 1: A panel member asks what you never practiced
- You present for about ten minutes
- Then about five minutes of unscripted questions
- Nobody shows you the questions first
- This is where "cannot explain" is decided
Speaker notes: Next week you present for about ten minutes, and then a panel asks you questions for about five. I confirm the exact lengths and who is on the panel. You will not see those questions in advance. Here is why that matters. The only way to fail the capstone outright is to submit work you cannot explain, and the defense is where that gets decided. The good news is that you cannot memorize answers, but you can practice a shape until it is a habit. That is today.
Image: A student at a podium facing a three-person panel, one panelist raising a hand, deep navy and accent blue.
---
## Slide 2: Four kinds of question
```
TECHNICAL   How does this actually work?       code, architecture, data dictionary
DECISION    Why this and not that?             decision log
FAILURE     What happens when this breaks?     test plan, troubleshooting log, 30-day record
HONEST      What does not work? What next?     acceptance record, findings, future list
```
Speaker notes: Every question the panel asks falls into one of four kinds. Look at the right-hand column. Every strong answer is already written down somewhere in your repository. Students who kept real logs find the defense the least stressful part of the capstone, because they are reading from their own records. The defense question bank in the project folder has sixteen examples across these four kinds.
Image: None. This slide is code.
---
## Slide 3: The shape of every strong answer
- Name the specific thing
- Say what it does, or why you chose it
- Give the evidence or the tradeoff
- Stop. Usually under forty-five seconds
Speaker notes: Four steps. Name the specific thing: the file, the function, the table, the page, the decision number. Say what it does or why you chose it, in a sentence or two. Give the evidence: a test, a measurement, an alternative you rejected. Then stop. The stop is the step people skip, and the longer you talk after the evidence, the more likely you are to say something you cannot back up.
Image: Four numbered stepping stones crossing a stream, the last one labelled stop.
---
## Slide 4: The wrong way, and why it fails
```
PANEL    If the database is unavailable, what does a volunteer see?

WEAK     It should show an error. Flask handles errors, so it would
         catch it and show a message or something.

         No file named. No test cited. "Should" instead of "does."
         Rubric 4C: general where a specific answer existed.
```
Speaker notes: Here is a composite weak answer to a failure question. It names no file. It cites no test. And it uses the word should. Should is the word that loses a failure question, because the panel is asking what the system does, not what it ought to do. The rubric describes answers like this as describing the technology in general rather than your project in particular, and that is the three to four band out of eight.
Image: None. This slide is code.
---
## Slide 5: The same question, answered
```
STRONG   The database_down handler in app.py returns "Sign-up is down,
         try again in a few minutes" with status 503. That was AC-4. It
         failed in the acceptance run, I added the handler, and the re-run
         passed on Thursday of Week 16. The log line holds no volunteer data.
```
Speaker notes: Same question. Named thing: the database down handler in the app file. What it does: returns that exact message with a 503. Evidence: acceptance criterion four, including the fact that it failed first and was fixed. Then stop. Notice that the failure makes this answer stronger, not weaker. It proves the student tested it.
Image: None. This slide is code.
---
## Slide 6: Your three most vulnerable questions
- The part you understand least
- The criterion that passed narrowly, or failed
- The decision hardest to defend to your stakeholder
- Write answer notes for each, not scripts
- Start from your track guide's list
Speaker notes: Every project has a weak side, and you know where yours is better than anyone. Look in three places. The part you understand least, which is usually a library, a framework feature, or code an AI tool wrote that you accepted. The acceptance criterion that passed most narrowly or did not pass. And the decision you would be least comfortable defending to your stakeholder. Write those three questions in your presentation outline, with notes in the four-step shape. Each track guide lists five questions its track is most vulnerable to. Start there.
Image: A shield with three small cracks, each labelled with a sticky note.
---
## Slide 7: Saying I do not know, well
```
PANEL     How many times will the host restart your app before it gives up?

STUDENT   I do not know. I know it restarted on its own once, in my
          self-recovery test, thirty-day record section 2. I would find
          the limit in the host's documentation on restart policy, and
          test it by crashing the app on purpose more than once.
```
Speaker notes: This is a real professional skill, and bluffing is the answer that fails. The shape is say it plainly, say what you do know nearby, say how you would find out, and stop. One I do not know handled like this raises a defense score. A confident wrong answer the panel can see is wrong lowers it. There is one line you cannot cross. I do not know is fine for an edge of the system. It is not fine for how your own main feature works.
Image: None. This slide is code.
---
## Slide 8: The rehearsal protocol
- Today: three vulnerable questions, answer notes drafted
- Pair with a classmate on another track
- Ten bank questions, random order, answered aloud
- Partner times each answer, marks general ones
- Swap, then repeat Monday with a new partner
Speaker notes: Here is how you practice, from the question bank. Today you write your three vulnerable questions and draft notes. Then pair with someone on a different track, because they will ask the questions an outsider asks. They pick ten questions from the bank in random order, without warning, and you answer out loud. They time each answer and mark any answer that was general where it could have been specific. Swap. Write one improvement per answer in your outline. On Monday, rehearsal day, do it again with a different partner.
Image: Two students facing each other, one holding a stopwatch and a printed question list.
---
## Slide 9: What you are about to build
- Presentation outline drafted, eight sections, time budget
- Three vulnerable questions with four-step notes
- One timed rehearsal with a partner today
- Rehearsal record filled in and committed
- Read rubric part 4 before you leave
Speaker notes: Here is your build period. Copy the final presentation outline template into your presentation folder and draft all eight sections with the time budget. Write your three vulnerable questions with answer notes. Run one rehearsal with a partner from another track, today or in Period 8, and fill in the rehearsal record with what you changed. Read part 4 of the capstone rubric so you know exactly what the panel scores. The full clinic note has every example from today. Commit before you leave.
Image: An outline document with eight numbered sections and a stopwatch icon beside it, accent blue highlights.
---
