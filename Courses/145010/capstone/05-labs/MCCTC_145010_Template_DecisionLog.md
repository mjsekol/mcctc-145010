# Template · Decision Log
## 145010 Senior Capstone · Weeks 7-18, written on the day

**Commit as:** `decision-log.md` at the top of your repository.
**Due:** continuously. At least four entries by the end of Week 8 and at least ten by the end.

**Competencies this evidences:** 1.1.7 (apply problem-solving and critical-thinking skills when
making decisions), 1.2.7 (problem-solving and consensus-building to determine next steps), 1.2.12
(technical writing).

---

## Why this exists

**The capstone is Gate 3 work, and Gate 3 requires a decision log.** It is the record of every
choice that shaped the project, written when you made it, with the options you did not take.

**It is where your defense answers live.** "Why this and not that?" is a whole category of defense
question. A student with a real log opens it and reads the reason. A student without one tries to
remember, in front of a panel, why they chose something in Week 9.

**The failure to avoid is a diary.** "Worked on the login page today" is not a decision. "Used the
framework's built-in sign-in instead of writing my own, because..." is.

---

## What counts as a decision

Write an entry whenever you choose between real options, including:

- the problem, the stakeholder, and the track
- anything cut, moved to stretch, or deferred
- a library, framework, host, database, model, or tool
- a data field kept or not kept
- a change to requirements or acceptance criteria
- an action from a milestone review, scope check, or peer review
- a usability finding you acted on, and one you chose not to act on
- how you fixed a problem, when there was more than one way

---

```markdown
# Decision Log · <project name>

## D-<n> · <short title>
**Week <n>, <day>**   Phase: <Define / Measure & Analyze / Improve / Control>

**The situation:** <one or two sentences. What forced a choice.>

**Options considered:**
1. <option> · <what is good about it> · <what is bad about it>
2. <option> · <...> · <...>
3. <optional third option>

**Chosen:** <option n>

**Why:** <the reason, tied to the stakeholder's needs, the requirements, time, safety, or evidence>

**What it costs:** <the tradeoff you accepted>

**Evidence:** <a measurement, a test result, a meeting record, a review finding, or "judgment,
not yet tested">

**Revisit if:** <the condition that would make you choose differently>

**Related:** <requirement, change request, troubleshooting entry, AI usage log entry>
```

---

## Two example entries

**Composite examples, from a shift sign-up project.** Write your own.

```markdown
## D-6 · Sign-in only for the coordinator
**Week 9, Wednesday**   Phase: Measure & Analyze

**The situation:** Volunteers need to claim shifts. Accounts for every family would mean storing
emails and passwords for about 40 adults.

**Options considered:**
1. Accounts for everyone · each claim is tied to a login · 40 sets of personal data, password
   resets, and three extra sprints of work
2. Coordinator signs in, volunteers use a shared link and a first name and last initial ·
   almost no personal data · a volunteer could claim a shift under someone else's name
3. No sign-in at all · simplest · anyone with the link could delete shifts

**Chosen:** 2

**Why:** The coordinator said in the needs-discovery meeting that the families trust each other and
the real problem is double-booking, not impersonation. Option 2 stores the least personal data.

**What it costs:** A false claim is possible. The coordinator can release any claim, which is
requirement R4.

**Evidence:** Meeting record, Week 7, Friday, lines 4-6.

**Revisit if:** The coordinator reports a false claim during usability testing.

**Related:** R2, R4, data dictionary "claims" table.
```

```markdown
## D-14 · Printable view cut from Sprint 3
**Week 13, Monday**   Phase: Improve

**The situation:** The database failure in Week 12 cost two days. Sprint 3 cannot fit both the
coordinator page and the printable view.

**Options considered:**
1. Keep both, work Period 8 every day · risks both being half done
2. Cut the printable view to the stretch list · the coordinator page lands on time

**Chosen:** 2

**Why:** The coordinator page is AC-3 in the signed agreement. The printable view is a stretch goal.

**What it costs:** The coordinator keeps writing the stand's paper schedule by hand for now.

**Evidence:** Sprint 2 review, hours remaining 11 against 19 needed.

**Revisit if:** Every acceptance criterion passes before Week 15.

**Related:** Change request CR-2, weekly update Week 12.
```

---

## Before you commit · self-check

- [ ] Every entry has at least two real options.
- [ ] Every "why" names something outside your own preference, or says honestly that it is a
      preference.
- [ ] The week and day are the day you decided, not the day you wrote it up. If you are writing it
      late, say so in the entry.
