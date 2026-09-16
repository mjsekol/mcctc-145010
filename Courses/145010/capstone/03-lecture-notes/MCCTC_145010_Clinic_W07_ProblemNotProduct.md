# Clinic · The Problem, Not the Product
## 145010 Senior Capstone · Week 7, Wednesday · 15 minutes · Define

**Slides for this clinic:** This clinic has no slide outline. It runs at the board.

**When this clinic runs.** Week 7, Wednesday, or any week the room shows this signal: worksheets
that name a category ("small businesses") or describe an app.

**If you missed it,** you can learn the skill from this file alone.

**Competencies:** 1.10.2 (determine the customer's needs and identify solutions), 2.9.2 (determine
the scope and purpose of the project), 1.6.1 (identify business opportunities), 1.2.13 (identify
stakeholders and solicit their opinions), 1.1.7 (problem-solving and critical thinking when making
decisions).

---

## Why this exists

**A stakeholder does not want an app. They want a problem to stop.** When you describe software
first, you have picked the answer before you understand the question. Everything after that is you
defending a guess.

Your idea conference is today or tomorrow. Your instructor asks six questions. The second one is
"What happens today, step by step, when the problem occurs?" A student who answers it by describing
an app has told the instructor, in one sentence, that they do not understand the problem yet.

The other warning sign is a category. "Small businesses." "Students." "Gamers." A category cannot
reply to an email, cannot tell you what is wrong, and cannot sign an agreement. A person can.

---

## The skill in plain language

A problem statement has four parts. Each one is about the world, not about software.

| Part | The question | A weak answer | A strong answer |
|---|---|---|---|
| **Who** | Which one person, by role? | "Teachers" | "The media specialist at the career center" |
| **What happens today** | Step by step, the last time it happened? | "They have trouble tracking things" | "A teacher asks if a tripod is free. The specialist pages through a paper binder." |
| **How often** | How many times, in what period, and how do you know? | "All the time" | "The specialist estimates ten loans a week and could count a week of entries." |
| **What it costs** | Time, mistakes, money, or stress? | "It is inefficient" | "A camera was listed as returned when it was not, and nobody knew for a week." |

**The no-software test.** Read your problem statement and ask: could every sentence be true in a
world with no computers? If a sentence contains app, website, dashboard, database, platform, AI,
login, or notification, it describes a product. Move that sentence to section 9 of the proposal,
where the approach goes, and write the problem again.

**Then pick the track that fits the problem.** The track follows the problem. It never leads.

| If the problem is about... | The track that usually fits |
|---|---|
| A physical condition someone needs to watch: heat, level, a machine state | Industrial / HMI |
| People coordinating, recording, or finding shared information | Full-Stack Application |
| Finding answers inside a body of text the stakeholder owns and has permitted | AI-Integrated |

---

## Worked example 1 · A worksheet entry, rewritten

*Composite, not a real organization or person.*

**Before:**

```
PROBLEM:   Small businesses need a better way to manage inventory.
WHO:       Small business owners
HOW OFTEN: Every day
My idea:   An AI-powered inventory app with barcode scanning and a dashboard.
```

Three failures in four lines. The who is a category. The how often has no source. The last line is
a product, and it arrived before the problem.

**After:**

```
PROBLEM:   Staff borrow cameras, tripods, and laptops from the media center.
           Every loan is written in a paper binder. When a teacher asks
           whether something is free, the specialist pages through the
           binder while the teacher waits. A camera was once marked
           returned when it was not, and nobody knew for a week.
WHO:       The media specialist at the career center. I have spoken to
           them twice while returning equipment for another class.
HOW OFTEN: About ten loans a week, by the specialist's estimate. The
           specialist could count a week of binder entries and give me
           the number, so no names leave the office.
```

Every sentence passes the no-software test. Notice that the after version already hints at the
baseline question for Week 9: how long it takes to answer "is it free?"

---

## Worked example 2 · The six idea-conference questions

*Composite: the service counter lead at a small equipment repair shop.*

| # | Question | Weak answer | Strong answer |
|---|---|---|---|
| 1 | Who has this problem, and have you talked to them? | "Repair shops. Not yet." | "The service counter lead. We spoke Monday. They replied yes to a conversation Friday." |
| 2 | What happens today, step by step? | "I will build an AI chatbot." | "A customer asks a question. Staff pull a printed manual, look for the page, and the customer waits." |
| 3 | How often, and how do you know? | "Constantly." | "The lead says several times a shift. I will ask whether they would tally it for a week." |
| 4 | What can they do afterward that they cannot now? | "Use AI." | "Find the right manual page while the customer is still at the counter." |
| 5 | The smallest thing they would actually use? | "The full assistant, with voice." | "A staff-only lookup that shows the manual and page it came from." |
| 6 | What do you not yet know how to build? | "Nothing, I have used AI before." | "Retrieving passages from their manuals. I will try it on one manual by Week 9." |

**Look at answer 2 again.** The weak answer is not wrong about the track. It is wrong about the
question. The question asked about today, and the answer described the future.

**Look at answer 6.** "Nothing" is the answer your instructor worries about most. Every capstone
has an unknown part. Naming it now is how you plan for it.

---

## Worked example 3 · Picking the track, with the trap

*Composite.* The media center problem from worked example 1 sounds like it could be an AI project.
"The AI could predict which equipment will be late."

Run the problem through the track table. The pain is finding out whether a tripod is free and who
has the camera. That is people recording and finding shared information. **Full-Stack fits.** A
prediction needs months of late-return records that do not exist, and it would not answer the
question the specialist asked.

Record it in your decision log. The shape comes from the
[Decision Log template](../05-labs/MCCTC_145010_Template_DecisionLog.md):

```markdown
## D-2 · Track: Full-Stack Application
**Week 7, Wednesday**   Phase: Define

**The situation:** The media center problem could be framed as an AI project or a web application.

**Options considered:**
1. AI-Integrated · predict late returns · no history exists to learn from, and it does not answer "is it free?"
2. Full-Stack · a shared loan list the specialist and staff can check · answers the question they asked

**Chosen:** 2

**Why:** The pain named is finding current loan status, which is a record, not a prediction.

**What it costs:** No AI component. The AI-Integrated track guide is not my guide.

**Evidence:** Conversation with the media specialist while returning equipment. Needs discovery is Friday.

**Revisit if:** The needs-discovery conversation shows the real pain is something else.
```

---

## The wrong version, and what it costs

"My project is an AI-powered app for students."

The idea conference stops at question 1, because "students" is not a person you can reach. Nobody
can sign the Week 8 agreement for a category. If you keep going anyway, every requirement in Week 9
is a guess, and in Week 16 there is no one to run the acceptance check. The
[Capstone Specification](../09-project/MCCTC_145010_Capstone_Specification.md#non-negotiables) is
blunt about it: no stakeholder, no project.

---

## Why the wrong version is tempting

For two years, you have been asked to build things. A product is concrete. You can picture its
screens. A problem feels vague until you have asked someone about it, and you have not asked yet.

The track also pulls. AI-Integrated sounds impressive in an interview. But the panel in Week 18 asks
why you chose it, and "it sounded good" is the answer that gets a project taken apart. Pick the
track your problem needs.

---

## Do this today

1. Rewrite your top candidate's entry in `docs/define/stakeholder-finding.md` so it passes the
   no-software test.
2. Say your answers to the six questions aloud to yourself, without notes. The questions are in the
   [Define phase guide](../05-labs/MCCTC_145010_PhaseGuide_Define.md#wednesday-and-thursday--the-idea-conference).
   Any you cannot answer is the next thing to find out.
3. Come to your idea conference with that answer ready. It is Wednesday or Thursday.
4. Choose your track. Write the decision and the alternative in `decision-log.md`.
5. Read your track guide from the
   [track table](../09-project/MCCTC_145010_Capstone_Specification.md#the-three-tracks) and all
   three examples in [Scope Calibration](../09-project/MCCTC_145010_Capstone_ScopeCalibration.md).
6. Commit.

---

## If you are ahead, if you are behind

**Ahead.** Start `docs/define/concept-proposal.md`, section 1, from the
[Concept Proposal template](../05-labs/MCCTC_145010_Template_ConceptProposal.md). Your rewritten
entry is most of the paragraph. Section 1 is due started by Thursday.

**Behind.** If your entry still names a category, pick the one person in that category you can
reach through school channels. If there is nobody, tell your instructor today.

---

## Words the WebXam uses

| Exam word | What it means in this skill |
|---|---|
| **Purpose (of the project)** | Why the project exists. Your problem statement, not your feature list |
| **Scope (of the project)** | What the project will and will not do. It comes after the problem, not before |
| **Client needs** | What the stakeholder must be able to do. Found by asking, not by imagining |
| **Target audience** | The specific people who will use it. Not "everyone" |
| **Business opportunity** | A real problem that is worth someone's time to solve |
| **Identify solutions** | Choosing an answer after the need is known. The order matters |

---

## Self-check

**1.** "Coaches need an app to track practice attendance." Name the two failures in that sentence.

**2.** Apply the no-software test to this sentence: "The front office loses track of which visitor
badges are checked out." Does it pass? Why?

**3.** A student's problem is that the robotics team's parts shelf is never labelled, so members
waste time searching. They choose AI-Integrated because a model could "recognize parts from a
photo." What question would you ask them?

### Answers

**1.** "Coaches" is a category, not one reachable person by role. "An app to track" is a product,
not a description of what happens today or what it costs.

**2.** It passes. Every word could be true with no computers: an office, badges, and losing track of
them. It still needs how often and what it costs before it is a full problem statement.

**3.** Something like: "What is the pain the team lead named, and does a model answer it?" The pain
is finding parts on a shelf. A labelled, searchable parts list answers that. A photo recognizer needs
training images that do not exist and does not fix the missing labels. The track should follow the
problem.
