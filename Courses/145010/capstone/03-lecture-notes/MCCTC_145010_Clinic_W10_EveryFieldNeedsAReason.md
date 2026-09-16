# Clinic · Every Field Needs a Reason
## 145010 Senior Capstone · Week 10, Tuesday · 15 minutes · Analyze

**Slides for this clinic:** This clinic has no slide outline. It runs at the board.

**When this clinic runs.** Week 10, Tuesday, or any week the room shows this signal: data
dictionaries copied from a tutorial, or phone numbers stored in case they are useful someday.
**If you missed it,** you can learn the skill from this file alone.
**Competencies:** 1.4.6 (use an electronic database to create business and technical
information), 1.4.4 (use system hardware to support software applications), 2.7.5 (data
transmission volumes, bandwidth, and latency), 1.2.12 (technical writing)

---

## Why this exists

**The data dictionary is where privacy is decided.** Every field you store is a promise to look
after it. A field you never store can never leak, never go stale, and never become a defense
question you cannot answer.

This is the cheapest moment to delete a field. Today it costs one row in a table. In Week 14 it
costs a migration, a code change, and a change request.

It is also scored. The Capstone rubric caps Security at 9 of 20 for any must-fix finding, and it
names "personal data stored that the requirements did not need" as one. A panel member will ask
the Full-Stack defense question: "What personal data does this app hold, and why does it need each
piece?" Your data dictionary is the answer.

## The skill in plain language

For every table, write one sentence: **what does one row represent?** Then one line per field:

| Column | What you write |
|---|---|
| Field | The name in your code |
| Type | integer, text, timestamp, true or false |
| Required | yes or no |
| Example (invented) | A made-up value, never a real one |
| Personal? | Could it identify a person, alone or with other fields? |
| **Why it exists** | Which requirement needs it. **No reason, no field.** |
| Kept for | How long |
| Removed by | What deletes it |

Then write the section most students skip: **fields considered and not stored**, each with the
reason. That list proves you thought about privacy on purpose.

**Where it runs is not your decision alone.** The host, the lab machine, or the device is decided
with your instructor in conference this week, and written in section 3 of the architecture with
who approved it. Some options need approval from people outside the classroom. Do not design around
a host you have not been given.

## Worked example 1 · the Parts Bin Board dictionary

*Composite, not a real organization. Every example value is invented.*

**Table: `bins`.** One row is one physical parts bin on the co-op's shelves.

| Field | Type | Required | Example (invented) | Personal? | Why it exists | Kept for | Removed by |
|---|---|---|---|---|---|---|---|
| id | integer | yes | 3 | no | Unique key | as long as the bin exists | coordinator removes the bin |
| code | text | yes | B-03 | no | R1: volunteers choose the bin by the code on its label | same | same |
| part | text | yes | Tubes, 26 inch | no | R2: the low list says what to restock | same | same |

**Table: `low_reports`.** One row is one "this bin is low" report.

| Field | Type | Required | Example (invented) | Personal? | Why it exists | Kept for | Removed by |
|---|---|---|---|---|---|---|---|
| id | integer | yes | 118 | no | Unique key | 30 days after restock | nightly cleanup |
| bin_id | integer | yes | 3 | no | R1: which bin is low | same | same |
| note | text, 120 max | no | last two gone | could be, if someone types a name | R1: the size or detail the coordinator needs | same | same, or the coordinator deletes it |
| reported_at | timestamp | yes | 2027-03-11T18:42 | no | R1 and R2: the low list shows when each bin was marked, newest first | same | same |
| restocked_at | timestamp | no | 2027-03-12T09:05 | no | R3: clears the report from the list; kept briefly so a wrong tap can be undone | same | same |

**Table: `coordinator`.** One row is the one account that can see and clear the list.

| Field | Type | Required | Example (invented) | Personal? | Why it exists | Kept for | Removed by |
|---|---|---|---|---|---|---|---|
| id | integer | yes | 1 | no | Unique key | until handoff changes it | instructor-approved handoff step |
| username | text | yes | coordinator | no, a role name | NF6: only the coordinator signs in | same | same |
| password_hash | text | yes | (a hash from `werkzeug.security`, never a password) | no | NF6: sign-in without storing the password | same | same |

**Table: `daily_opens`.** One row is one day's count of board opens. No cookies, no addresses.

| Field | Type | Required | Example (invented) | Personal? | Why it exists | Kept for | Removed by |
|---|---|---|---|---|---|---|---|
| day | date | yes | 2027-03-11 | no | R4: counts are shown per day | until handoff | handoff checklist |
| opens | integer | yes | 14 | no | R4: the count itself | same | same |

A first draft of this table also had a `path` column for which page was opened. R4 counts board
opens only, so `path` had no reason and was cut. That is this clinic in one line.

The 30-day retention is a composite decision the coordinator agreed to. Yours comes from your own
stakeholder and goes in the retention row, NF9, of your requirements.

## Worked example 2 · fields considered and not stored

*Composite.* This list is as important as the tables.

| Field | Why it is not stored |
|---|---|
| Volunteer name on a report | The coordinator needs to know which bin, not who noticed. The signed scope says no name. |
| Volunteer phone number | Nothing in the requirements calls anyone. |
| Coordinator email | Password reset is on the stretch list. Until then, the user guide gives a manual reset done with the instructor. |
| IP address or device type | The open counter needs a count, not a visitor. NF7 says no addresses and no cookies. |
| Customer name or repair ticket number | Customer data stays in the co-op's building. No requirement needs it. |
| Photo of the empty bin | The code and the note are enough. A photo could catch a person. |

## Worked example 3 · how big does it get?

*Composite.* Section 6 of the architecture asks for storage growth with the arithmetic shown.

```
Reports per open-shop night, high estimate:   10
Open-shop nights per week (composite):         2
Reports per year:          10 x 2 x 52 = 1,040
Bytes per report, rough:   note 120 + two timestamps 38 + ids about 10 = 168
Estimate per year:         1,040 x 168 = 174,720 bytes, about 0.17 MB
```

A check on the build machine: a SQLite file with the `bins` and `low_reports` tables above, 30
bins, and 1,040 reports with every note at the full 120 characters came to **204,800 bytes**, about
0.2 MB. The estimate was close. The file is bigger because SQLite stores its own structure in
fixed-size pages. With 30-day retention the real table stays far smaller. Storage is not this
project's risk. Write that down, with the number, so nobody has to wonder.

## The wrong version, and what it costs

*Composite.* A student copies a `users` table from a web tutorial:

```
users: id, first_name, last_name, email, phone, birth_date, street_address,
       created_at, last_login_ip
```

For a board where volunteers never sign in, and one coordinator does.

What that costs:

1. **Eight fields with no reason, and seven of them personal.** Only `created_at` identifies no
   one. The requirements asked for none of them.
2. **Security capped at 9 of 20** under the rubric rule on personal data the requirements did not
   need.
3. **A defense question with no good answer.** "Why do you store volunteers' birth dates?"
4. **A privacy notice you now have to write,** explaining data you did not need.

## Why the wrong version is tempting

Tutorials include every field because they are showing you how, not deciding for you. Copying one
feels safe because it came from somewhere. And extra fields feel free: "I might need it later."
**Later never arrives, and the risk arrives now.** If a real need appears after Week 10, it comes
with a requirement, a change request, and a reason. Then it gets a row.

## Do this today

1. Book your "where it runs" conversation with your instructor if you have not had it. Write the
   decision, who approved it, and the reason in section 3 of the architecture.
2. Write "what one row represents" for every table.
3. Fill in every column for every field. Every "Why it exists" names a requirement.
4. Write at least three "fields considered and not stored."
5. Do the storage arithmetic in section 6.
6. Commit `docs/measure-analyze/architecture.md`, using the
   [Architecture and Data Dictionary template](../05-labs/MCCTC_145010_Template_ArchitectureAndDataDictionary.md).

Track notes: Industrial, the reading interval and retention decide your storage growth; read
[the Industrial / HMI guide](../09-project/MCCTC_145010_TrackGuide_IndustrialHMI.md). AI-Integrated,
decide whether questions are stored at all, and if so why; read
[the AI-Integrated guide](../09-project/MCCTC_145010_TrackGuide_AIIntegrated.md). Full-Stack, read
your host's free tier terms today; see
[the Full-Stack guide](../09-project/MCCTC_145010_TrackGuide_FullStack.md#where-it-runs-and-who-can-reach-it).

## If you are ahead, if you are behind

**Ahead.** Write the Relationships section. For the co-op: `low_reports.bin_id` refers to
`bins.id`. What happens to reports when a bin is removed? Decide, and write it down.

**Behind.** Do the dictionary before the diagram. Commit the tables with every "Why it exists"
filled in. The rest of the architecture can follow in Period 8.

## Words the WebXam uses

| Exam word | What it means here |
|---|---|
| **Electronic database** | Your tables, and what they store for the stakeholder. 1.4.6. |
| **Data dictionary** | The list of every stored field with its type and purpose. |
| **Hardware to support software** | Where it runs, and whether that machine has what the software needs. 1.4.4. |
| **Data transmission volume** | How much data moves and is stored. Your storage arithmetic. 2.7.5. |
| **Personal information** | Any field that could identify a person, alone or combined. |
| **Retention** | How long data is kept and what removes it. |

## Self-check

**1.** A classmate's dictionary has a `phone` field with the reason "in case we need to contact
them." Keep it or remove it? Why?

**2.** Why does the `note` field say "could be" in the Personal column, when the form never asks for
a name?

**3.** Who decides where your project runs, and where is that decision written?

### Answers

**1.** Remove it, and list it under "fields considered and not stored." "In case" is not a
requirement. If contacting people becomes a real need, it arrives with a requirement and a change
request.

**2.** Because a person can type anything into a free-text box, including a name. Marking it
honestly means the design handles it: a hint on the form, a length limit, a retention rule, and a
way for the coordinator to delete a note.

**3.** You and your instructor, in conference, with anyone else whose approval the option needs.
It is written in section 3 of `docs/measure-analyze/architecture.md`, with who approved it and the
reason.
