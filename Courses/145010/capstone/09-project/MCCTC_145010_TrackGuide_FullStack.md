# Track Guide · Full-Stack Application
## 145010 Senior Capstone · Read before Week 8

**Why this track exists.** Most of the software people touch every day is a web application with
accounts and a database behind it. You deployed a database-backed app in 145065 and you spent the
first six weeks of this course on the front end. This track puts both in front of real users who
depend on it.

**What makes it hard.** Real users. The moment someone other than you signs in, you hold their
data, you are responsible for who can see it, and your free hosting tier's limits become their
problem. The code is rarely what sinks this track. Hosting, data, and scope are.

**Competencies this track evidences most heavily:** 6.5.12 (publish to a web server), 6.5.11
(cross-platform and cross-browser compatibility and validation), 6.5.13 (responsive design),
6.5.14 (SEO, for any public page), 6.4.7 (scripting that interacts with data sources), 1.4.6 (an
electronic database for business information), 1.10.5 (measurement tools for satisfaction),
2.7.8 (static versus dynamic, and why yours is dynamic).

---

## The typical shape

```
browser (HTML, CSS, script)
    |
    v
web application on a host  ---> database
    |                        \--> health endpoint
    +--> sign-in for the people who change data
    +--> first-party page-view counter (no cookies, no IP addresses)
```

---

## A composite example

**This is a composite, not a real organization.** The volunteer coordinator for a youth
recreation league schedules concession-stand shifts through a group text. Every week somebody
misses the message, two families show up for the same shift, and one shift has nobody. The
coordinator spends Sunday evenings sorting it out.

It is a good problem. A named person, a weekly pain, and a measurable result: unfilled and
double-filled shifts. It is the example in
[Scope Calibration](MCCTC_145010_Capstone_ScopeCalibration.md#example-2--full-stack-application).

---

## The minimum viable version

- **One job done well** for the stakeholder, with a clear start and end.
- **Sign-in for the people who change data.** Passwords stored only as hashes produced by a
  maintained library, such as `werkzeug.security` in Flask. Never stored or logged in plain text.
- **A database** with a schema in your architecture document and a data dictionary for every
  field.
- **Only the data the job needs.** Every personal field in your data dictionary has a reason
  next to it. If you cannot write the reason, delete the field.
- **Valid, accessible, responsive pages.** The same standard as the instruction phase: zero
  validation errors, zero automated accessibility violations, usable at phone width, operable by
  keyboard.
- **A health endpoint** that reports whether the application can reach its database and which
  version is running.
- **A first-party page-view counter** that stores no cookies, no IP addresses, and no
  identifiers. You built one in Week 6.
- **Deployed** to a free host your instructor has approved, reachable by the stakeholder.

## What a stretch looks like

- A second role, such as a volunteer who can see only their own shifts.
- An export the stakeholder can open in a spreadsheet.
- A printable view.
- A reminder page the stakeholder can share, with no personal data on it.
- SEO work on the public pages: titles, descriptions, headings, a sitemap.

**Not stretch goals, because they change the risk:** taking payments, sending email or text
messages from the app, storing anything about minors beyond what your instructor has approved,
and a native mobile app.

---

## Real users and their data

This is the part of the track most students underestimate.

- **Who are the users?** Write it in your proposal. If any user is under 18, your instructor
  approves exactly what the app stores about them, in writing, in Week 8.
- **Collect the least.** A first name and a last initial is often enough. A phone number rarely
  is. A birth date almost never is.
- **No personal data in any AI tool, ever.** That includes pasting a database row into a chat to
  ask why it failed. Use invented rows.
- **No real data in your repository.** Seed data and test fixtures are invented and labelled as
  invented.
- **Secrets live in the host's environment settings**, never in the code or the repository
  history. A secret committed once is exposed, even after you delete it.
- **Your privacy notice is part of the user guide.** One paragraph: what the app stores, why,
  who can see it, and how to ask for it to be removed.

---

## The technical risks that sink this track

**1. The free tier has limits you did not read.** Some free tiers put an idle service to sleep
and wake it on the next request, which makes the first page load slow. Some free database tiers
expire or are removed after a set period. **Before Week 10 ends, read your host's current free
tier terms and write down what they say about sleeping, storage, and expiry.** [VERIFY on the
host's own documentation. These terms change.] A database that is deleted in Week 15 ends your
thirty-day record and your stakeholder's trust.

**2. It works on your machine.** Environment variables, file paths, database drivers, and time
zones all differ on a host. **Fix it with the walking skeleton in Week 11:** deploy a page that
reads one row from the real database before you build anything else.

**3. Authentication eats the project.** Building sign-in from scratch, password reset, roles,
and sessions can consume three sprints. **Use your framework's maintained tools**, keep one role
if you can, and put password reset on the stretch list with a manual procedure in the user guide
until then.

**4. Nobody uses it.** A deployed app with no users has no usability evidence and no measured
change. **Fix it in Define:** the stakeholder names who the users are and agrees to put the app
in front of them by Week 15.

**5. Scope grows one feature at a time.** Every user who touches the app will ask for something.
After Week 12, every request goes on the future improvements list in your handoff, not into the
build.

---

## Where it runs and who can reach it

Your host is one your instructor has approved, on a free tier, with no payment details entered
anywhere. The syllabus names Cloudflare Pages for static sites and Render for full-stack
applications. [VERIFY current free tier terms with your instructor before Week 10]

If a host asks for a credit card, stop. That host is not used in this program.

**A local fallback is required.** Your README explains how to run the whole application on a lab
machine with a local database, for testing and for the day the host is down. That is also your
2.12.2 evidence when your test setup mimics the host's database and environment.

---

## Surviving thirty days, on this track

**What "manual intervention" looks like here:** restarting the service from the host's dashboard
because it hung, editing a database row by hand to fix a bad record, recreating an expired
database, re-entering a lost environment variable.

**What is not an intervention:** a deploy of a new version through your documented steps,
recorded in your release log. An idle service that sleeps and wakes on the next request **is not
a failure if it answers within the time your requirements allow.** Measure the wake-up time and
write it into the requirements as a fact, so nobody argues about it later.

**How you prove it:**

1. **A health endpoint** that returns the version and whether the database answered.
2. **A scheduled check** that calls the health endpoint on a fixed interval and appends one line
   per call to a log. Where that check runs is decided with your instructor: an approved lab
   machine running a scheduled task, or a scheduling feature of your host. [VERIFY which is
   available]
3. **The host's deploy history** exported or recorded as your release log.
4. **The page-view counter**, showing real use over the period.

A health log line might look like this. It is program data, so the timestamp belongs there:

```
2027-04-23T14:15:02  result=ok  status=200  ms=412
```

A line with `ms=9120` after a quiet night is a sleeping service waking up. It is not a failure
if your requirements say it is acceptable. It is a failure if they do not.

---

## Where Strand 6 lives in this track

Everywhere. Forms, tables, links, responsive layout, validation, publishing, and SEO are all in
your build. **The risk is the opposite of the other tracks:** if you use a framework that writes
your markup for you, you can finish twelve weeks having written very little HTML by hand. Keep the
Gate 1 reps going.

---

## Defense questions this track is most vulnerable to

1. "Show me where the passwords are stored and what is in that column."
2. "What personal data does this app hold, and why does it need each piece?"
3. "What happens to a user's data when the free database expires?"
4. "Why is this a dynamic site rather than a static one?"
5. "How do you know anybody used it, and what did your counter not collect?"

The full bank is in [Defense Question Bank](MCCTC_145010_Capstone_DefenseQuestionBank.md).
