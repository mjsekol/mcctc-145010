# Clinic · Writing for the User
## 145010 Senior Capstone · Clinic · Week 17, Wednesday

**The signal:** user guide drafts with developer steps in them: "restart the service," "check the
logs," "run the migration." The user guide is delivered today.

**Slides:** This clinic has no slide outline. It runs from the board.

**If you missed it,** you can learn the skill from this file alone. The small script in example 3 was
run on the build machine with Python 3.13, and the output is pasted exactly.

**Competencies:** 2.13.6 (deliver support and training materials), 6.1.4 (use writing process
techniques: drafting, revising, editing, and proofreading), 1.2.5 (communicate directions for an
intended audience and purpose), 1.2.12 (technical writing), 1.10.3 (communicate features, benefits,
and warranties to the customer)

**Every example below is a composite.** The Northside Community Garden is an invented organization.

---

## The idea in plain language

**Your README is for developers. Your user guide is for the people who use the project.** It is
written in their words, one task per section, with numbered steps and the exact text they will see
on screen. It is written in four separate passes: draft, revise, edit, proofread. The template is the
[User Guide](../05-labs/MCCTC_145010_Template_UserGuide.md).

## Why it exists

Your stakeholder has never seen your code and never will. After Week 18, this document is the only
version of you they have. **The test of a user guide is simple to state:** your stakeholder does the
main task using only this document while you sit on your hands.

**The four passes are graded, not only the result.** Competency 6.1.4 names the writing process.
Record each pass in your decision log with the week and day.

**This is harder than it sounds.** You cannot unknow how your project works, the same problem you
met in usability testing. The revise pass, where you watch someone use the guide, is how you get
around it.

---

## Worked example 1 · developer sentences, turned into user sentences

```
DEVELOPER                                        USER
Navigate to the root route.                      Open the sign-up page: <address>.
The free tier may need to spin up.               The first time each day, the page can take
                                                 up to a minute to open. Wait, then reload.
The POST writes to the signups table.            Press **Claim**. You should see
                                                 **Bed 4 is yours**.
If you get a 503, check the logs.                If the page says **Sign-up is down, try
                                                 again in a few minutes**, wait five minutes
                                                 and reload. If it still says that, use the
                                                 paper sheet by the shed and tell the
                                                 coordinator.
Restart the service.                             (Not in the user guide. A person restarting
                                                 the system is a manual intervention. It
                                                 belongs in the rollout plan's contingency
                                                 section, with who does it.)
```

**Three rules are visible.** Say what the person does and what they will see. Put screen text in
bold, exactly as it appears. Give every failure a next step a non-developer can take.

## Worked example 2 · one task section, finished

```markdown
## Sign up for a bed

You can do this on a phone or a computer. It takes about a minute.

1. Open the sign-up page: <address>.
   You should see **Northside Garden · This week's beds**.
2. Choose the day you can help, for example **Saturday**.
   Open beds show a **Claim** button. Taken beds show a first name.
3. Press **Claim** next to an open bed.
4. Type your first name and press **Sign me up**.
   You should see **Bed 4 is yours**.

*Screenshot: signup-step-4.png, with invented names.*

If you see **This bed is already taken**, someone signed up a moment before you.
Choose another open bed.
```

**Notice what is missing:** no technology, no reasons, and no words like `simply`. Every step is one action followed
by what should happen, so the reader knows at once if something went wrong. The button name matches
the usability finding that changed it.

## Worked example 3 · the four passes, on the same guide

```
Pass 1, draft      Week 17 Wed, period 1   every task written, badly if necessary
Pass 2, revise     Week 17 Wed, period 2   a building adult did "Sign up for a bed"
                                           with only the guide; stopped at step 2
                                           ("which day is this week?"); step 2 rewritten
Pass 3, edit       Week 17 Wed, period 3   long sentences split; "navigate" and
                                           "route" removed; every bold screen text
                                           checked against the live page
Pass 4, proofread  Week 17 Wed, Period 8   read aloud; step numbers, links, spelling
```

For the edit pass, a ten-line script can find long sentences. This one flags any sentence over 20
words:

```python
import re
import sys

LIMIT = 20
text = open(sys.argv[1], encoding="utf-8").read()
for number, line in enumerate(text.splitlines(), 1):
    for sentence in re.split(r"(?<=[.?])\s+", line):
        words = len(sentence.split())
        if words > LIMIT:
            print(f"line {number}: {words} words: {sentence[:50]}...")
```

Run on the developer-voice draft of this section:

```
line 2: 36 words: To sign up you need to navigate to the root route ...
line 4: 22 words: Click on the Claim button next to an open bed and ...
```

**A script helps the edit pass. It cannot do the revise pass.** Only a person using the guide shows
you where it fails. Keep your guide out of AI tools if it contains anything from your stakeholder
that is not public, and record any AI help in your AI usage log either way.

---

## The sections people forget

- **What it does not do.** People trust a tool more when they know its limits.
- **What the messages mean.** A table: exact message, what it means, what to do.
- **Privacy.** What is stored, why, who can see it, how long, and how to ask for removal.
- **Accessibility.** Keyboard use, zoom, and who to tell if something is hard to use.
- **Support and warranty (1.10.3).** What will be fixed, by whom, until when. It must match your
  acceptance agreement. For most capstones: until the end of Week 18, and after that only what is
  agreed in writing through the school.

---

## The wrong version, and what it produces

```markdown
# User Guide
Clone the repo and run `pip install -r requirements.txt`, then `flask run`.
Go to localhost:5000. Sign up for shifts. If it breaks, restart it or text me.
Should be pretty self-explanatory.
```

**What it produces:** a coordinator who stops at the first line, because none of it is something they
do. `localhost` is the student's own machine, so the address does not work for anyone else. "Sign up
for shifts" has no steps or screen text. "Restart it" asks for a manual intervention. "Text me" breaks
the school-channel rule and ends when you graduate. "Self-explanatory" is the phrase that tells a
reader they should already understand, and they will stop asking. The handoff part of the rubric
looks for a guide the stakeholder worked through, and this one cannot be worked through.

## Why the wrong version is tempting

It is accurate, for you. You wrote the README first, and the user guide feels like the same
information. It also feels respectful not to over-explain to an adult. **Clear steps are not
talking down. They are what lets a busy adult use your project on a Friday night with nobody to ask.**

---

## What to do in your project today

1. Copy the [User Guide template](../05-labs/MCCTC_145010_Template_UserGuide.md) to `user-guide.md`.
2. Pass 1: one section per task, named as a goal. Get every task down.
3. Pass 2: watch one person, the stakeholder or someone like them, do the main task using only the
   guide. Rewrite where they stopped.
4. Pass 3: shorten, replace technical words, and check every bold screen text against the live page.
5. Pass 4: read it aloud. Check numbering, links, and spelling.
6. Record all four passes in your decision log with week and day.
7. Screenshots use invented data only. Check the support section against your acceptance agreement.
8. Deliver it to the stakeholder, log it in the contact log, and commit.

---

## Vocabulary

| Term | Meaning |
|---|---|
| **User guide** | The stakeholder-facing document for using, trusting, and recovering the project |
| **Draft** | Pass 1: get everything written |
| **Revise** | Pass 2: change content and order after watching someone use it |
| **Edit** | Pass 3: change sentences and words |
| **Proofread** | Pass 4: find errors in spelling, punctuation, numbering, and links |
| **Warranty** | What you promise to fix, and until when |

---

## Check yourself

1. Which pass would catch a step that is missing entirely? Which would catch "teh"?
2. Rewrite as a user step: "Hit the endpoint to export the CSV."
3. Your guide says, "I will fix any problem you find." Why is that a problem, and what do you write
   instead?

---

## Check your answers

**1.** A missing step is caught in the revise pass, when a person using the guide gets stuck where
the step should be. "teh" is caught in the proofread pass.

**2.** Something like: "Press **Download this week**. A file named **garden-week.csv** is saved to
your Downloads folder. You can open it in a spreadsheet." Use your real button text and file name.

**3.** It promises support with no end date and no channel, which you cannot give after Week 18. Write
what will be fixed, by whom, and until when, matching the acceptance agreement: for example, "The
student will fix problems reported through the school until the end of Week 18. After that, no
support is promised unless agreed in writing through the school."
