# Additional Resources · Weeks 13-18
## 145010 Web Design & Senior Capstone · Improve into Control

**How to read the link labels.** **Confirmed** means the page was fetched and read on the build
machine while this file was written. **[VERIFY]** means it was not confirmed there: open it before you
rely on it, and tell your instructor if it has moved. Pages change, so even a confirmed link can move
later.

**Nothing here asks you to create an account, pay for anything, or use a commercial AI service.** If a
resource asks for any of those, skip that part. Models in this program run on lab hardware.

**In-repository links come first**, because they describe exactly what you are building and they all
resolve from this file.

**Levels.** **Remediation** is for when you are behind or the idea has not clicked. **On-level** is
what the week expects. **Extension** is for when your week's work is committed and passing.

---

## WebXam review, Weeks 13-16

The WebXam 145010 post-test is in Week 16, and Strand 6 (web development) is more than half of it.
**Your instructor runs short review reps in standup**, a few minutes a day, on paper, with no AI and
no autocomplete:

| Week | What the standup reps cover |
|---|---|
| 13 | Section 6.3, scripting |
| 14 | Section 6.4, web forms |
| 15 | Section 6.5, websites, then a 40-minute practice test on Thursday, then Strand 1 and 2 vocabulary on Friday |
| 16 | Strand 1 and 2 vocabulary on Monday, a reteach clinic on the items the room missed, and the post-test on Tuesday. Confirm this year's test window with your instructor |

**The rep bank is instructor-only.** Do the reps when they are handed out. The "Words the WebXam uses"
tables at the end of the [Improve](../05-labs/MCCTC_145010_PhaseGuide_Improve.md) and
[Control](../05-labs/MCCTC_145010_PhaseGuide_Control.md) phase guides connect exam words to your own
project. Read them the week before the post-test.

---

## Week 13 · Sprint 3 and Peer Code Review 1

**This week's clinics:**
[Parameterized Queries](../03-lecture-notes/MCCTC_145010_Clinic_W13_ParameterizedQueries.md) ·
[Reviewing Code You Did Not Write](../03-lecture-notes/MCCTC_145010_Clinic_W13_ReviewingCodeYouDidNotWrite.md) ·
[Responding to a Review](../03-lecture-notes/MCCTC_145010_Clinic_W13_RespondingToAReview.md).
Template: [Peer Code Review](../05-labs/MCCTC_145010_Template_PeerCodeReview.md).

### Primary reading · OWASP SQL Injection Prevention Cheat Sheet
`https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html` · **Confirmed**

**What it is.** The industry's standard short reference on stopping SQL injection, from the Open
Worldwide Application Security Project. **Read:** the introduction, "Primary Defenses," and "Defense
Option 1: Prepared Statements (with Parameterized Queries)." **Why this one.** It says plainly that you
should stop building queries with string concatenation, and it names allow-list validation for the
cases a placeholder cannot cover, which is the column-name problem in Monday's clinic. **Time.** 25
minutes. **Level.** On-level.

### Video · a short SQL injection explainer · [VERIFY]
No specific video is named here, because a wrong title or channel costs more than no link. **Search
for:** "SQL injection" on the OWASP Foundation's official video channel, or "SQL injection
parameterized queries" from a university or a major browser or cloud company's official developer
channel. **Pick one that** is under 20 minutes, shows code being run, and does not ask you to attack a
site you do not own. **Time.** Under 20 minutes. **Level.** Remediation.

### Interactive practice · attack your own copy
**What it is.** The four small programs in the Monday clinic note. Copy them into a scratch folder
outside your repository, run them, and try your own inputs: an empty string, an apostrophe, `%`, and
`x' OR '1'='1`. **Why this one.** You see the failure and the fix on your own machine, with no account
and no risk to anyone else's system. **Never test injection against a site you do not own.** That rule
is in the Lab Acceptable Use and Safety Agreement. **Time.** 30 minutes. **Level.** On-level.

### Official documentation · Python `sqlite3`, placeholders
`https://docs.python.org/3/library/sqlite3.html` · **Confirmed**

**Read:** the how-to section titled "How to use placeholders to bind values in SQL queries." **Why
this one.** It shows both placeholder styles you saw on Monday, `?` and `:name`, and warns against
string formatting in its own words. If you use Flask, also read **Using SQLite 3 with Flask**,
`https://flask.palletsprojects.com/en/stable/patterns/sqlite3/` · **Confirmed**, which passes values
as arguments to a query helper. **Time.** 20 minutes. **Level.** On-level.

### Industry connection · how Google engineers review code
`https://google.github.io/eng-practices/review/` · **Confirmed**

**What it is.** Google's published guide to code review, with one section for reviewers and one for
authors. **Read:** "How to write code review comments,"
`https://google.github.io/eng-practices/review/reviewer/comments.html` · **Confirmed**, before
Wednesday, and "How to handle reviewer comments,"
`https://google.github.io/eng-practices/review/developer/handling-comments.html` · **Confirmed**,
before Friday. **Why this one.** It is how a large engineering organization describes the same two
jobs you do this week: commenting on the code and not the person, labelling how serious a comment is,
and answering a comment by improving the code. **Argue both sides.** The guide expects reviewers to
be fast and authors to fix most things. Your template allows a rejected finding with a reason. Which
fits a one-person capstone better, and why? **Time.** 30 minutes. **Level.** Extension.

### Side quest · SQ-05 Bug Hunt
[SQ-05 Bug Hunt](../../../Misc/side-quests/SQ-05-Bug-Hunt/README.md) · **Confirmed**, in this
repository.

**What it is.** A short program with planted defects and a test suite. You find them, document each,
and fix them without rewriting the program. **Why this one.** It is Wednesday's skill, reading code you
did not write, with a test suite that tells you when you are right. **Also in the program's side quest
catalog:** SQ-23, The Form That Fights Back, where you attack your own form with long input, script
tags, and SQL-shaped strings. Ask your instructor for it. **Time.** One block. **Level.** Extension.

---

## Week 14 · Sprint 4, Peer Code Review 2, release candidate

**This week's clinics:**
[Feature Freeze and the Release Candidate](../03-lecture-notes/MCCTC_145010_Clinic_W14_FeatureFreezeAndTheReleaseCandidate.md) ·
[Recruiting Five Real Users](../03-lecture-notes/MCCTC_145010_Clinic_W14_RecruitingFiveRealUsers.md) ·
[Testing on the Devices They Use](../03-lecture-notes/MCCTC_145010_Clinic_W14_TestingOnTheDevicesTheyUse.md).
If you need a refresher on the report itself:
[Reading a Web-Check Report](../03-lecture-notes/MCCTC_145010_Clinic_W12_ReadingAWebCheckReport.md).
BPA Nationals usually falls this week; confirm this year's date.

### Primary reading · MDN, Accessibility tooling and assistive technology
`https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/Tooling` · **Confirmed**

**What it is.** A chapter of MDN's accessibility module on automated tools and screen readers.
**Read:** the automated tools section and the screen reader section. **Why this one.** It says in its
own words that automated tools alone cannot find every accessibility problem, which is exactly the gap
between a passing web-check report and Thursday's human checks. The screen reader list names NVDA and
JAWS, which are not on the lab machines; your test plan uses Windows Narrator unless your instructor
approves another. **Time.** 30 minutes. **Level.** On-level.

### Video · Web Accessibility Perspectives
`https://www.w3.org/WAI/perspective-videos/` · **Confirmed**

**What it is.** Ten short videos from the W3C Web Accessibility Initiative, including keyboard
compatibility, text to speech, customizable text, and clear layout. The page lists the full
compilation at 7 minutes 36 seconds. **Why this one.** Each video shows a real person using a
feature your Thursday checks test. Watch keyboard compatibility and customizable text first. **Time.**
Under 10 minutes. **Level.** Remediation.

### Interactive practice · the WAI Before and After Demonstration
`https://www.w3.org/WAI/demos/bad/` · **Confirmed**

**What it is.** An inaccessible website and its fixed version, side by side, with annotations for each
barrier. **Why this one.** Try the "before" pages with the keyboard only, and then with browser zoom at
200 percent, before reading the annotations. Then compare with what you found on your own release
candidate. **For the checker itself:** run `node tools/web-check/check.js <page>` from your repository
root on every page, at the default widths. **Time.** 30 minutes. **Level.** On-level.

### Official documentation · the W3C Markup Validation Service and the WAI forms tutorial
`https://validator.w3.org/` · **Confirmed**. It validates by address, by file upload, or by pasted
markup. Use it as a second opinion when web-check's validation message is unclear.

`https://www.w3.org/WAI/tutorials/forms/` · **Confirmed**. Labelling controls, grouping them,
instructions, validating input, and user notifications. **Why these.** Section 6.4 of the WebXam review
is forms this week, and your release candidate almost certainly has one. **Time.** 20 minutes.
**Level.** On-level.

### Industry connection · release engineering and version numbers
`https://sre.google/sre-book/release-engineering/` · **Confirmed**, and Semantic Versioning,
`https://semver.org/` · **Confirmed**.

**What they are.** A chapter of Google's Site Reliability Engineering book on how software is built and
delivered, and the widely used rule for numbering releases. **Why these.** A release candidate is a
release-engineering idea. The SRE chapter argues for defining a release process at the start of a
project rather than bolting it on later, which is why your deployment steps have been documented since
Week 10. **Also relevant this week:** the OWASP Cross Site Scripting Prevention Cheat Sheet,
`https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html` ·
**Confirmed**, because Review 2 looks at security again from scratch. **Time.** 30 minutes.
**Level.** Extension.

### Side quest · SQ-21 The Accessibility Pass, and SQ-22 Make It Load in Under a Second
Both are in the program's side quest catalog; ask your instructor. **SQ-21:** complete every task on
your page with no mouse and without looking, then list what you fixed and what you could not. **SQ-22:**
measure your page's load time, cut it in half without removing features, and record before and after
measured the same way. **Why these.** They are Thursday's human checks and your performance
requirement, taken further. **Time.** One to two blocks each. **Level.** Extension.

---

## Week 15 · usability testing

**This week's clinics:**
[Running a Usability Session](../03-lecture-notes/MCCTC_145010_Clinic_W15_RunningAUsabilitySession.md) ·
[Writing Up a Session the Same Day](../03-lecture-notes/MCCTC_145010_Clinic_W15_WritingUpASessionTheSameDay.md) ·
[Who Your Five Do Not Represent](../03-lecture-notes/MCCTC_145010_Clinic_W15_WhoYourFiveDoNotRepresent.md) ·
[From Observations to a Change List](../03-lecture-notes/MCCTC_145010_Clinic_W15_FromObservationsToAChangeList.md).
Templates: [Usability Test Protocol](../05-labs/MCCTC_145010_Template_UsabilityTestProtocol.md) ·
[Usability Observation Sheet](../05-labs/MCCTC_145010_Template_UsabilityObservationSheet.md).

### Primary reading · Nielsen Norman Group, "Thinking Aloud: The #1 Usability Tool"
`https://www.nngroup.com/articles/thinking-aloud-the-1-usability-tool/` · **Confirmed**

**What it is.** An article by Jakob Nielsen on the most common usability method: people use a system
while saying what they think. **Why this one.** It explains why a cheap, small study is still worth
doing, and it names the method's limits. **Read it against your protocol.** This course keeps you
silent and writes down behavior first, and you may ask only the few questions on your list. Where does
the article's method match that, and where would it change what you observe? **Time.** 15 minutes.
**Level.** On-level.

### Video · Involving Users in Web Accessibility
`https://www.w3.org/WAI/test-evaluate/involving-users/` · **Confirmed** for the page, which embeds a
video with a descriptive transcript. **[VERIFY]** its running time before assigning it; the page gives
a file size, not a length.

**Why this one.** It makes the case that working with people with disabilities during development finds
problems that checklists miss, which is Wednesday's question: who your five do not represent. **Time.**
Under 20 minutes, to be confirmed. **Level.** Remediation.

### Interactive practice · score a session you did not run
**What it is.** Worked example 3 in the Monday clinic note shows a session as it happened, and then as
it looks on the observation sheet. Cover the sheet version, fill in your own from the timeline, and
compare. Then do the same with the wrong version on the same note. **Why this one.** Counting wrong
attempts and hesitations from a timeline is the skill you need by Tuesday afternoon. **Time.** 20
minutes. **Level.** Remediation.

### Official documentation · digital.gov, Usability
`https://digital.gov/topics/usability/` · **Confirmed**

**What it is.** The U.S. government's hub page on usability for public websites, with guides on
conducting usability tests, participant agreements, and interview techniques. **Why this one.** It is
free, plain, and written for teams who test with real members of the public. **A note on an older
source:** many older articles point to usability.gov, a government usability site that was archived.
If you find a usability.gov link, treat it as **[VERIFY]**. **Time.** 20 minutes. **Level.**
On-level.

### Industry connection · "Why You Only Need to Test with 5 Users"
`https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/` · **Confirmed**

**What it is.** Jakob Nielsen's widely cited argument for running several small usability studies
instead of one large one. **Why this one.** It is the reason this course asks for five people. **Read
it critically, both ways.** The case for: small, repeated studies find the problems most people hit,
cheaply, and leave budget to fix them. The case against: five people who are all alike miss the
problems of the people who are not like them, which is exactly Wednesday's clinic. Notice that the
article's figures describe problems found across studies, not a share of your users, which is one more
reason your own findings use counts out of five and never percentages. **Time.** 15 minutes.
**Level.** Extension.

### Side quest · pilot for another track
**What it is.** Offer to be the Monday pilot participant for a classmate on a different track, then
write one page on what it felt like to be watched in silence, with no names. **Why this one.** Being the
participant once makes you a better facilitator for the rest of the week. You are never one of their
formal five. **Time.** 30 minutes. **Level.** Extension.

---

## Week 16 · corrections and acceptance

**This week's clinics:** the WebXam reteach on Monday, then
[Running the Acceptance Run](../03-lecture-notes/MCCTC_145010_Clinic_W16_RunningTheAcceptanceRun.md) ·
[When a Criterion Fails](../03-lecture-notes/MCCTC_145010_Clinic_W16_WhenACriterionFails.md).
Templates: [Acceptance Record](../05-labs/MCCTC_145010_Template_AcceptanceRecord.md) ·
[Change Request](../05-labs/MCCTC_145010_Template_ChangeRequest.md). The WebXam post-test is Tuesday;
confirm the window.

### Primary reading · SRE book, "Testing for Reliability"
`https://sre.google/sre-book/testing-reliability/` · **Confirmed**

**What it is.** A chapter of Google's Site Reliability Engineering book on unit, integration, system,
and production tests. **Read:** the opening and the sections on system tests and regression tests.
**Why this one.** It argues that failing tests prove a lack of reliability while passing tests do not
prove it exists, which is why your acceptance run includes cases designed to fail safely. It also
recommends turning every real bug into a regression test, which is what a correction with a re-run is.
**Time.** 30 minutes. **Level.** On-level.

### Video · acceptance testing with Given, When, Then · [VERIFY]
No specific video is named. **Search for:** "acceptance criteria given when then" on the official
channel of a software organization or a university course. **Pick one that** shows criteria being
written and then checked, is under 20 minutes, and does not sell a tool. **Time.** Under 20 minutes.
**Level.** Remediation.

### Interactive practice · re-read your own agreement
**What it is.** Open your signed acceptance agreement's criteria and your test plan section 7 side by
side. For each criterion, say out loud what result would make it fail. Then read the Agile Alliance
glossary entry on Given, When, Then, `https://www.agilealliance.org/glossary/gwt/` · **Confirmed**,
and compare its example with yours. **Why this one.** Before Wednesday, you should know which case is
most likely to fail, and why. **Time.** 20 minutes. **Level.** On-level.

### Official documentation · your own procedure
**What it is.** Section 7 of the [Test Plan](../05-labs/MCCTC_145010_Template_TestPlan.md) and the
five acceptance rules in the [Control phase guide](../05-labs/MCCTC_145010_PhaseGuide_Control.md).
**Why this one.** For this week, the official document is the one you and your stakeholder agreed.
Read the committed version, not your memory of it. **Time.** 15 minutes. **Level.** On-level.

### Industry connection · Postmortem Culture
`https://sre.google/sre-book/postmortem-culture/` · **Confirmed**

**What it is.** The SRE book's chapter on blameless postmortems: a written record of what failed, its
impact, what was done, and what will stop it recurring. **Why this one.** A failed acceptance case,
written honestly with its correction, is a small postmortem. Notice that the chapter lists manual
intervention by an engineer as a reason to write one, which is the same event that resets your
thirty-day clock. **Time.** 25 minutes. **Level.** Extension.

### Side quest · a regression test for every failure
**What it is.** For every acceptance or usability failure you corrected, add an automated test that
would have caught it, and run your whole suite. **Why this one.** It is the SRE chapter's
recommendation, applied to your own project, and it protects the correction from being undone by a
later change. **Time.** One block. **Level.** Extension.

---

## Week 17 · rollout and handoff

**This week's clinics:**
[Writing a Rollout Plan](../03-lecture-notes/MCCTC_145010_Clinic_W17_WritingARolloutPlan.md) ·
[Closing the Thirty-Day Record](../03-lecture-notes/MCCTC_145010_Clinic_W17_ClosingTheThirtyDayRecord.md) ·
[Writing for the User](../03-lecture-notes/MCCTC_145010_Clinic_W17_WritingForTheUser.md) ·
[Defense Prep](../03-lecture-notes/MCCTC_145010_Clinic_W17_DefensePrep.md).
Templates: [Rollout Plan](../05-labs/MCCTC_145010_Template_RolloutPlan.md) ·
[User Guide](../05-labs/MCCTC_145010_Template_UserGuide.md) ·
[Handoff Checklist](../05-labs/MCCTC_145010_Template_HandoffChecklist.md) ·
[Thirty-Day Survival Record](../05-labs/MCCTC_145010_Template_ThirtyDaySurvival.md) ·
[Final Presentation Outline](../05-labs/MCCTC_145010_Template_FinalPresentationOutline.md) ·
[Defense Question Bank](../09-project/MCCTC_145010_Capstone_DefenseQuestionBank.md).

### Primary reading · digital.gov, plain language guide series
`https://digital.gov/guides/plain-language` · **Confirmed**. The older address,
plainlanguage.gov, redirected there when checked.

**What it is.** The U.S. government's guidance on writing that the public can understand, in four
parts: principles, writing, design, and testing for understanding. **Why this one.** Your user guide is
read by an adult who never saw your code. "Test for understanding" is Wednesday's revise pass, watching
someone use the guide. **Time.** 30 minutes. **Level.** On-level.

### Video · writing for your reader · [VERIFY]
No specific video is named. **Search for:** "plain language writing" on an official government or
university channel, or "writing user documentation" from a documentation community's official
channel. **Pick one that** is under 20 minutes and shows a before and after. **Time.** Under 20
minutes. **Level.** Remediation.

### Interactive practice · the survival report and the sentence checker
**What it is.** Run `survival_report.py` on the invented sample logs in
[`survival-files/`](../05-labs/survival-files/README.md) exactly as the Tuesday clinic note shows, and
check you get the same output. Then run it on your own logs. For the user guide, the Wednesday note
has a ten-line script that flags long sentences; run it on your draft. **Why this one.** Both give you
a real result to act on, on your own machine. **Time.** 30 minutes. **Level.** On-level.

### Official documentation · Google developer documentation style guide, procedures
`https://developers.google.com/style/procedures` · **Confirmed**, from the style guide at
`https://developers.google.com/style` · **Confirmed**.

**What it is.** How one large organization writes numbered steps: one action per step, the location
before the action, and one clear way to do a task. **Why this one.** Your user guide is mostly
procedures. **Also useful:** the W3C WAI writing tips, `https://www.w3.org/WAI/tips/writing/` ·
**Confirmed**, for link text, headings, and clear instructions, and Write the Docs,
`https://www.writethedocs.org/guide/` · **Confirmed**, a documentation community's free guide.
**Time.** 20 minutes. **Level.** On-level.

### Industry connection · Managing Incidents, and canary releases
`https://sre.google/sre-book/managing-incidents/` · **Confirmed**, and
`https://sre.google/workbook/canarying-releases/` · **Confirmed**.

**What they are.** How a large operations team assigns roles when something breaks, and how it releases
a change to a small share of users first. **Why these.** Your rollout plan's contingency section is a
small incident plan: who notices, who acts, who tells the stakeholder. The canary chapter is the
professional version of "the paper sheet stays up for two weeks." **Argue both sides.** A parallel
paper process is safe and slow to retire. Switching everyone at once is simple and has no fallback.
Which does your stakeholder need? **Time.** 40 minutes. **Level.** Extension.

### Side quest · SQ-20 Explain It to a Seventh Grader
[SQ-20](../../../Misc/side-quests/SQ-20-Explain-It-To-A-Seventh-Grader/README.md) · **Confirmed**, in
this repository.

**What it is.** A quest from 145130: explain a technical idea to a twelve-year-old, with a jargon checker
and comprehension questions. **Why this one.** Explain your own capstone instead. If a seventh grader
can say what it does and what to do when it breaks, your user guide and your defense are in good shape.
The quest's rules match usability testing: nothing recorded, no names, a parent in the room for family.
**Time.** One block. **Level.** Extension.

---

## Week 18 · presentation and portfolio

**This week's clinics:**
[When the Demo Breaks](../03-lecture-notes/MCCTC_145010_Clinic_W18_WhenTheDemoBreaks.md) ·
[Telling the Story of Your Project](../03-lecture-notes/MCCTC_145010_Clinic_W18_TellingTheStoryOfYourProject.md).
Templates: [Final Presentation Outline](../05-labs/MCCTC_145010_Template_FinalPresentationOutline.md) ·
[Portfolio Entry](../05-labs/MCCTC_145010_Template_PortfolioEntry.md). Rubric:
[Capstone Rubric](../09-project/MCCTC_145010_Capstone_Rubric.md), part 4.

### Primary reading · the Defense Question Bank, again
[Defense Question Bank](../09-project/MCCTC_145010_Capstone_DefenseQuestionBank.md) · **Confirmed**, in
this repository.

**What it is.** Sixteen questions across the four kinds, with strong and weak answers, and how to say
"I do not know." **Why this one.** On Monday you rehearse with a new partner. Read the failure and honest
questions again the night before, because those are the ones students under-prepare. **Time.** 25
minutes. **Level.** On-level.

### Video · presenting technical work · [VERIFY]
No specific video is named. **Search for:** "how to give a technical presentation" or "presenting a
software demo" on a university's official channel. **Pick one that** is under 20 minutes and talks
about structure and handling questions, not slide design. **Time.** Under 20 minutes. **Level.**
Remediation.

### Interactive practice · a timed mock defense
**What it is.** The rehearsal protocol in the
[Defense Prep clinic](../03-lecture-notes/MCCTC_145010_Clinic_W17_DefensePrep.md): ten random questions
from the bank, answered out loud, timed by a partner from another track. **Why this one.** It is the
only practice that includes a question you did not expect. **Time.** 30 minutes. **Level.** On-level.

### Official documentation · job requirements and professional organizations
**U.S. Bureau of Labor Statistics, Occupational Outlook Handbook, Web Developers and Digital
Designers:**
`https://www.bls.gov/ooh/computer-and-information-technology/web-developers-and-digital-designers.htm` ·
**[VERIFY]**. The site refused the build machine's automated check, so the address was not confirmed
there. The Handbook is the standard federal source for what a job asks in education, training, and
experience, which is your 1.1.2 evidence. **Also [VERIFY]:** CareerOneStop, `https://www.careeronestop.org/`,
a career exploration site sponsored by the U.S. Department of Labor, which also refused the check.

**Business Professionals of America:** `https://www.bpa.org/` · **Confirmed**. The career and technical
student organization this program competes in, and a professional organization for your 1.1.4
evidence. **Cite every fact you use**, with the page's name and address, and never copy a salary or
growth figure without its source. **Time.** 30 minutes. **Level.** On-level.

### Industry connection · the README an employer reads first
`https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes` ·
**Confirmed**

**What it is.** GitHub's documentation on README files: what a visitor sees first and what a good one
covers. **Why this one.** If your instructor and stakeholder agree your repository can be public, its
README is the first thing an interviewer opens. Compare it with your
[Project README](../05-labs/MCCTC_145010_Template_ProjectREADME.md) and your portfolio entry. The
repository link goes public only with both agreements. **Time.** 15 minutes. **Level.** Extension.

### Side quest · publish your portfolio entry as a checked page
**What it is.** Turn `presentation/portfolio-entry.md` into a single HTML page, run
`node tools/web-check/check.js <page>` until it passes at every width, and do a keyboard-only pass and a
200 percent zoom check on it. Screenshots use invented data only. Publish it only where your
instructor approves. **Why this one.** A web developer's portfolio page is itself a sample of their
work, and it is the last page you ship in this program. **Also in the side quest catalog:** SQ-24, Ship
for a Real Stakeholder, which you have now done for real. **Time.** One block. **Level.** Extension.

---

## For the student who is behind

1. The clinic note for today, read top to bottom, and its three "Check yourself" questions answered
   before you read the answers
2. The phase guide section for this week in [Improve](../05-labs/MCCTC_145010_PhaseGuide_Improve.md) or
   [Control](../05-labs/MCCTC_145010_PhaseGuide_Control.md), and its checklist
3. The template for today's deliverable, filled in badly first and improved second
4. Tell your instructor in standup what is blocking you. A blocked week said out loud on Tuesday is
   fixable. The same week said on Friday is not.

## For the student who is ahead

- The Google code review guide in Week 13, with a decision log entry taking a position on its advice
- SQ-21 and SQ-22 in Week 14
- A regression test for every correction in Week 16
- The SRE incident and canary chapters in Week 17, applied to your rollout plan
- Your portfolio entry as a checked, published page in Week 18
