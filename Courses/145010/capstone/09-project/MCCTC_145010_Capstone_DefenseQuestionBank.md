# Defense Question Bank
## 145010 Senior Capstone · Weeks 17-18

**Why this file exists.** In Week 18 you present for about ten minutes and then take about five
minutes of questions nobody showed you in advance. Your instructor confirms the exact lengths and
who is on the panel. The questions are where the panel finds out whether you built this or
assembled it. **The only way to fail the capstone outright is to submit work you cannot explain,
and the defense is where that is decided.**

You cannot memorize answers to questions you have not seen. You can practice the shape of a strong
answer until it is a habit. That is what this bank is for.

**There is no answer key.** Every question is about your own project, and only you can answer it.
What this file gives you is what a strong answer contains and what a weak one sounds like.

**Competencies:** 1.2.2 (deliver formal and informal presentations), 1.2.5 (communicate for an
intended audience and purpose), 2.12.6 (stakeholder acceptance), 2.13.3 (final review and
approvals), 1.1.7 (problem solving and critical thinking applied to work decisions).

---

## The four kinds of question

| Kind | What the panel is really asking | Where the answer comes from |
|---|---|---|
| **Technical** | How does this actually work? | Your code, your architecture, your data dictionary |
| **Decision** | Why this and not that? | Your decision log |
| **Failure** | What happens when this breaks? | Your test plan, troubleshooting log, and thirty-day record |
| **Honest** | What does not work, and what would you change? | Your acceptance record, usability findings, and future improvements list |

**Notice the right-hand column.** Every strong answer is already written down somewhere in your
repository. Students who kept real logs find the defense the least stressful part of the
capstone. Students who did not find it the most.

---

## The shape of every strong answer

1. **Name the specific thing.** The file, the function, the table, the page, the decision number.
2. **Say what it does or why you chose it**, in one or two sentences.
3. **Give the evidence or the tradeoff.** A test, a measurement, an alternative you rejected.
4. **Stop.** A strong answer is usually under forty-five seconds.

**A weak answer describes technology in general.** "Flask handles the routing" is true of every
Flask app ever written. "The `/shifts/<id>/claim` route checks the claim inside one transaction so
two people cannot take the same shift, and test T-07 proves it" is about yours.

---

## Technical questions · how does this actually work?

### T1. "Walk me through what happens, step by step, when a user does the main task."

**Strong answer contains:** the path from the user's action to the stored result, naming each
layer: the page, the request, the handler, the check, the database or device, the response. It
mentions one validation along the way.

**Weak answer sounds like:** "They click the button and it saves." Or a tour of the screens with no
mention of what happens behind them.

### T2. "Show me where the data lives. What is in that table, and why is each field there?"

**Strong answer contains:** the actual table or file, opened. Each field with its type and the
reason it exists, from your data dictionary. For any personal field, why the job needs it.

**Weak answer sounds like:** "It is in the database." Or a field the student cannot explain.

### T3. "How does someone who is not you reach this system right now?"

**Strong answer contains:** where it runs, what the stakeholder types or opens, and what had to be
approved for that to work. The honest limits: a sleeping free tier, a lab-only network.

**Weak answer sounds like:** "It is on the internet." Or a demo that only works on the student's
laptop.

### T4. "Where are the secrets, and how did you keep them out of your repository?"

**Strong answer contains:** what the secrets are, where they are stored, how the code reads them,
and how you checked the history. If the project has no secrets, why not.

**Weak answer sounds like:** "I did not put any passwords in." With no way to show it.

### T5. "Pick one function you wrote without AI help and explain it line by line."

**Strong answer contains:** a real choice of function, and an explanation that includes why a
line is there, not only what it does.

**Weak answer sounds like:** reading the code aloud. Or choosing a function and then discovering
you are not sure about part of it.

---

## Decision questions · why this and not that?

### D1. "Why this track and this stack, for this problem?"

**Strong answer contains:** the problem's shape first, then the choice. One alternative you
seriously considered and why it lost. A decision log entry number.

**Weak answer sounds like:** "It is what I know." That can be a legitimate reason, and if it is
yours, say what it cost you.

### D2. "What did you cut, and how did you decide?"

**Strong answer contains:** a named cut, the week it happened, the change request, what the
stakeholder said, and why the remaining scope still solved their problem.

**Weak answer sounds like:** "I did not have time for some features." With no record of choosing.

### D3. "What did you reject that you still think was a good idea?"

**Strong answer contains:** a real idea, why it was good, and the specific reason it lost: time,
risk, data, safety, or the stakeholder's priorities. Where it lives now: the future improvements
list.

**Weak answer sounds like:** "Nothing, I am happy with everything." The panel hears that you did
not consider alternatives.

### D4. "How did AI tools shape this project, and where did you overrule them?"

**Strong answer contains:** two or three entries from your AI usage log, one where you changed or
rejected the output, and how you verified what you kept.

**Weak answer sounds like:** "I only used it a little." With a log that says otherwise, or no log.

---

## Failure questions · what happens when this breaks?

### F1. "Unplug it, stop it, or take the database away. What does the user see?"

**Strong answer contains:** exactly what the user sees, because you tested it. The test case
number. What the system logs. For a model project, what the fallback says and how it is labelled.

**Weak answer sounds like:** "It should show an error." "Should" is the word that loses this
question. What does it show?

### F2. "Tell me about the worst bug you found."

**Strong answer contains:** the symptom, the troubleshooting method you chose (top down, bottom
up, follow the path, spot the differences), what you gathered, the fix, how you tested the fix,
and the troubleshooting log entry.

**Weak answer sounds like:** "There were a lot of little bugs." Or a bug someone else found and
fixed.

### F3. "Did it survive thirty days? Show me."

**Strong answer contains:** the thirty-day record, the health log, the longest unbroken run, and
every reset with its cause. If it did not make thirty, the honest number and what you changed.

**Weak answer sounds like:** "I think it stayed up." With no log.

### F4. "Your stakeholder calls a month after you graduate and says it stopped. What happens?"

**Strong answer contains:** what the handoff documents tell them to do, who the support contact
is, what the contingency plan says, and what you agreed about your own availability.

**Weak answer sounds like:** "They can text me." That is not a support plan, and it breaks a
program rule during the capstone.

---

## Honest questions · what does not work, and what would you change?

### H1. "What does not work right now?"

**Strong answer contains:** a specific thing, the acceptance record entry or usability finding
that shows it, and what you agreed with the stakeholder about it.

**Weak answer sounds like:** "Everything works." **Every real project has a known issue.** A
student who names none has either not looked or is not saying.

### H2. "What did your usability testing find that surprised you?"

**Strong answer contains:** a finding stated as a count out of the people you watched, what they
did rather than what they said, and what you changed or deliberately did not.

**Weak answer sounds like:** "People liked it." Or a percentage from five people.

### H3. "If you started again on Monday, what would you do differently?"

**Strong answer contains:** one specific change to process, not only to code, and the evidence
that made you think so. "I would deploy in Week 10, because my host's database setup cost me most
of Sprint 1, decision 14."

**Weak answer sounds like:** "Start earlier." True of every project and tells the panel nothing.

---

## The three questions your project is most vulnerable to

**Write these yourself in Week 17.** Every project has a weak side, and you know where yours is
better than anyone. Answer each in `presentation/outline.md` using the four-step shape.

To find them, look for:

1. **The part you understand least.** Usually a library, a framework feature, or code an AI tool
   wrote that you accepted.
2. **The acceptance criterion that passed most narrowly**, or did not pass.
3. **The decision you would be least comfortable defending to your stakeholder.**

Each track guide lists five questions its track is most vulnerable to. Start there.

---

## How to say "I do not know" well

**This is a real professional skill, and pretending is worse.** A panel member who asks something
you cannot answer is often checking whether you will bluff. Bluffing is the answer that fails.

**The shape:**

1. **Say it plainly.** "I do not know."
2. **Say what you do know that is nearby.** "I know the host restarts the service when it crashes.
   I do not know how many times it will try."
3. **Say how you would find out.** "I would check the host's documentation for restart policy, and
   I would test it by making the service crash on purpose."
4. **Stop.**

**What not to do:** guess and present the guess as fact, talk until the question goes away, or
apologize repeatedly. One "I do not know" handled well raises a defense score. A confident wrong
answer the panel can see is wrong lowers it.

**The line you cannot cross.** "I do not know" is fine for an edge of the system. It is not fine
for the central parts you submitted. If you cannot explain how your own main feature works, that
is the rule above the rubric, and no phrasing fixes it.

---

## How to practice

1. **In Week 17**, write your three most vulnerable questions and draft answers.
2. **Pair with a classmate on another track.** They ask ten questions from this bank, in random
   order, without warning. You answer out loud. They time each answer and note any answer that was
   general where it could have been specific.
3. **Swap.**
4. **Record one improvement per answer** in your outline. Not a script. A note.
5. **On rehearsal day in Week 18**, do it again with a different partner.
