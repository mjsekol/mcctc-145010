# Clinic · Telling the Story of Your Project
## 145010 Senior Capstone · Clinic · Week 18, Friday

**The signal:** this clinic runs for everyone, on the last Friday. Presentations are done, and the
portfolio entry, the thank-you notes, and the last commit are due today.

**Slides:** This clinic has no slide outline. It runs from the board.

**If you missed it,** you can learn the skill from this file alone.

**Competencies:** 1.1.5 (strategies for self-promotion in the hiring process: résumé writing,
interviewing skills, portfolio development), 1.1.2 (the scope of career opportunities and their
requirements for education, training, certification, licensure, and experience), 1.1.4 (professional
organizations and networking), 1.7.13 (protect intellectual property and knowledge), 1.2.11 (write
professional documents and résumés)

**Every example below is a composite.** The Northside Community Garden is an invented organization,
and every number in the examples is invented.

---

## The idea in plain language

**Twelve weeks of work become three things you will use for years:** a portfolio page, one résumé
line, and a two-minute story you can tell in an interview. Each one says what the problem was, who
had it, what you did, and what changed. **None of them leads with the technology.** The template is
the [Portfolio Entry](../05-labs/MCCTC_145010_Template_PortfolioEntry.md).

## Why it exists

An employer, a college, or an internship interviewer will ask, "Tell me about a project." The student
who answers with a real person, a real problem, and a measured result stands out from the student who
lists frameworks. You remember every detail today. In six months you will not.

**And the story is not only yours.** Your stakeholder, their volunteers, and their screens appear in
it. What you may share about them is their decision, and it is part of respecting their intellectual
property and their privacy (1.7.13).

---

## Worked example 1 · the portfolio page, first lines

```markdown
# Garden Bed Sign-Up
A sign-up tool a community garden's volunteer coordinator uses to fill weekend bed shifts.

## The problem
Volunteers signed up on a paper sheet by the tool shed. The coordinator found out about
empty beds on Saturday morning, when it was too late to ask anyone.

## What I did
- Agreed six acceptance criteria with the coordinator in writing before building.
- Built and deployed a phone-first sign-up page with a coordinator view, in Python and Flask.
- Ran five usability sessions; three of five people chose the wrong day first, so the
  page now opens on the next upcoming day.
- Kept it running for 31 days without anyone touching it, with a health log to prove it.

## The result
- Empty Saturday beds went from 3 a week to 1 a week over four weeks (the coordinator's
  count, same method both times; a short period, and spring weather also changed).
- Accepted by the coordinator with one agreed follow-up.

## What I would do differently
Deploy in Week 10 instead of Week 11. Hosting setup took most of my first sprint.

## Permission
Built for a local community garden, described by role at their request.
```

**What makes it strong.** The first sentence says what it does and for whom. "What I did" is in the
first person and names decisions, including one driven by evidence. The result has a number and its
limits. The permission line is honest.

## Worked example 2 · the résumé line

```
WEAK     Built a Flask app with SQLite, HTML, CSS, and JavaScript.

STRONG   Built and handed over a volunteer sign-up tool for a community garden
         coordinator, cutting empty Saturday beds from 3 to 1 a week; passed 5 of
         6 acceptance criteria with the sixth on an agreed plan, and ran 31 days
         without intervention.
```

**The shape, from the template:** a strong verb, what you built, for whom, and a result. Every number
must match a committed record, the acceptance record and the thirty-day record here. **An interviewer
may ask about any word on your résumé.** Write nothing you cannot defend the way you defended your
capstone.

## Worked example 3 · the interview story, out loud

```
The situation      A community garden's coordinator found out about empty beds on
                   Saturday morning, from a paper sheet by the shed.
What I had to do   Build something the volunteers would use on their phones, and that
                   kept working after I graduated. The hard part was the second half.
What I did         I got six acceptance criteria signed before writing code. I watched
                   five people use it, and three picked the wrong day, so I changed what
                   opens first. My acceptance run failed one case, an error page when
                   the database was down. I recorded it, fixed it, and re-ran it with
                   the coordinator.
The result         Empty Saturday beds dropped from about three a week to one, the
                   coordinator accepted it, and it ran for a month on its own.
```

Said at a steady pace, that is well under two minutes. **Practice it out loud three times**, once for
a friend who knows nothing about code. **The failure is the best part of the story.** Interviewers
ask what went wrong, and a real answer with a fix is rarer than you think.

---

## Where this points · 1.1.2 and 1.1.4

The template's last section asks three things. **Every career fact needs a source you cite.**

```
A job or program this points toward:  web developer, or a college computing program
What it asks for:                     <education, training, certification, experience>,
                                      from <source you read, with its name and link>
A professional organization:          <one you can join or follow, with where you found it>
A professional contact:               the garden coordinator, by role; I will send a
                                      thank-you note through the school and ask whether
                                      I may list them as a reference
```

**Good places to look for the facts:** the U.S. Bureau of Labor Statistics Occupational Outlook
Handbook for job requirements, a college's own program page, and Business Professionals of America,
which you already know through the program. The
[resources for Weeks 13-18](../10-resources/MCCTC_145010_Resources_W13-W18.md) list them with their
links. Do not copy a salary or growth number from memory, and do not write one without its source.

---

## Permission, and whose story it is · 1.7.13

- **Your stakeholder decides** whether their name, their organization's name, their logo, or their
  screens appear. Ask in writing, through the school. Record the answer in the permission section.
- **No real person's data on any screenshot.** Invented names only, as in every document you
  committed.
- **Your code's license and the libraries' licenses** go in the "Built with" line and your
  licensing statement. Do not present a library's work as yours.
- **The repository link** goes public only if your instructor and your stakeholder agree.
- **Your stakeholder's documents, photos, and internal processes** are theirs. Describe what you
  learned, not what they showed you in confidence.

---

## The wrong version, and what it produces

```markdown
# Garden App
Tech stack: Python, Flask, SQLite, Jinja, HTML5, CSS3, JavaScript, Git.
I made a full-stack app for the Northside Community Garden with a database and login.
It was a huge success and everyone loves it.
[screenshot of the coordinator page showing volunteers' names]
Live: <address>
```

**What it produces:** a page that describes a thousand student projects and none in particular. "Huge
success" and "everyone loves it" have no number and no source, and an interviewer's first follow-up
question has no answer. The organization is named with no recorded permission. The screenshot shows
real volunteers' names, which breaks the privacy rule you kept for twelve weeks. The live address is
shared without the stakeholder's agreement. Your instructor would ask you to take it down before
anyone else read it.

## Why the wrong version is tempting

The technology list feels impressive and takes a minute to write. Naming the organization feels like
proof it was real. A real screenshot is quicker than setting up invented data again. **The strongest
proof is a specific problem, a number with its limits, and a stakeholder who agreed to what you
wrote.**

---

## What to do today

1. Copy the [Portfolio Entry template](../05-labs/MCCTC_145010_Template_PortfolioEntry.md) to
   `presentation/portfolio-entry.md`, after your `capstone-final` tag.
2. Write the first sentence, the problem, and "What I did" in the first person.
3. Copy every number from your committed records. Add each number's limit.
4. Write the résumé line and the four-part interview story. Say the story out loud once.
5. Fill in "Where this points" with at least one cited source.
6. Check the permission section against what your stakeholder agreed in writing.
7. Write the thank-you notes to your stakeholder and your participants, with no names in the
   repository, using the [Stakeholder Communication Guide](../05-labs/MCCTC_145010_Guide_StakeholderCommunication.md).
8. Last commit.

---

## Vocabulary

| Term | Meaning |
|---|---|
| **Portfolio entry** | A page describing one project for an employer or college |
| **Résumé line** | One sentence: strong verb, what, for whom, result |
| **Interview story** | Situation, what you had to do, what you did, the result, in about two minutes |
| **Professional organization** | A group for people in a field, such as Business Professionals of America |
| **Networking** | Building and keeping professional relationships, appropriately and through proper channels |
| **Intellectual property** | Work and knowledge that belongs to someone, such as code, logos, documents, and processes |

---

## Check yourself

1. Rewrite as a résumé line: "Made a website for a food pantry using HTML and CSS."
2. Your stakeholder said they are happy for you to describe the project but prefer not to be named.
   What does your permission section say, and what else changes on the page?
3. Why does the interview story include something that went wrong?

---

## Check your answers

**1.** Something like: "Built and handed over a shift sign-up site for a food pantry coordinator,
<your measured result>; passed <n> of <n> acceptance criteria." Use your real numbers and your real
stakeholder's role. The technology can go in a "Built with" line, not the lead.

**2.** "Built for a local organization, described by role at their request." Nothing else on the page
names or identifies them: no logo, no address, no screenshot with their branding, and a live link
only if they agree to that separately.

**3.** Because interviewers ask about failure, and a specific failure with the fix shows how you work
when things go wrong. It also makes the rest of the story believable.
