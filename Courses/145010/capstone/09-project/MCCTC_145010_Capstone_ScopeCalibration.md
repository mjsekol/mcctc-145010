# Scope Calibration · Three Worked Examples
## 145010 Senior Capstone · Read before you write your proposal

**Why this file exists.** Every student who fails the capstone on scope believed, in Week 8,
that their scope was fine. The oversized versions below are not silly. They are what a capable,
motivated senior writes on a first draft. That is what makes them dangerous.

**Every organization and person below is a composite.** None is a real client.

**What "finishable" means here.** You have about twelve hours of class time a week plus Period 8.
From Week 11 to Week 14 that is four build sprints, roughly fifty hours of building. Weeks 15-18
are testing, corrections, acceptance, handoff, and the presentation. They are not build weeks, and
a plan that needs them for building has already failed.

**How to use this file.** Read all three, including the tracks you are not on. Then hold your own
draft proposal next to the oversized versions and look for the same patterns.

---

## Example 1 · Industrial / HMI

**The composite stakeholder.** The maintenance lead at a small fabrication shop. The air
compressor room overheats on hot afternoons, the compressor shuts itself down, and nobody knows
until air tools stop working on the floor.

### The oversized version

> A complete facility monitoring platform. Six sensors in the compressor room: temperature,
> humidity, vibration, current draw, air pressure, and noise. A Raspberry Pi cluster with
> redundancy. A WPF operator panel with live trend charts for all six, predictive failure
> warnings from a machine learning model trained on the readings, and text message alerts to
> the maintenance team. A web dashboard with logins for every employee, a mobile app, and a
> connection to the compressor's controller so the panel can start a cooling fan automatically.

### The finishable version

> One temperature and humidity sensor on a Raspberry Pi, read every minute by a service that
> starts at boot. Readings stored locally. A WPF operator panel showing the current reading, how
> old it is, and one high-temperature alarm at a threshold the maintenance lead picks, with
> acknowledge and history. A read-only web dashboard with the current reading and the last 24
> hours, valid and readable on a phone. A test mode that replays a recorded hot afternoon so the
> alarm can be tested without heating a room.
>
> **Stretch, named now:** a daily high-and-low summary page, and a CSV export.

### Why

| Cut | Reason |
|---|---|
| Five of the six sensors | Each sensor is its own wiring, calibration, threshold, and failure mode. The stakeholder's pain is heat. One sensor answers it. |
| Pi cluster with redundancy | A research project on its own. Thirty days of a single Pi with a health log is stronger evidence than a cluster that never finished. |
| Predictive failure model | Needs months of labelled failure data that does not exist. Four sprints cannot produce it. |
| Text message alerts | Needs an account, often a paid service, and a credential. Not used in this program. |
| Logins for every employee, mobile app | The dashboard is read-only. Nobody needs to sign in to read a temperature. |
| **Connection to the compressor controller** | **Monitor, do not control.** Switching real equipment is a safety matter and not a student project. This is not a scope cut. It is a line. |

**The three tasks that would have taken four times longer than planned:** calibrating six
sensors, the predictive model, and getting permission to touch the compressor's controller.

**What the stakeholder actually cares about:** knowing it is getting hot before the air tools
stop. The finishable version does exactly that.

---

## Example 2 · Full-Stack Application

**The composite stakeholder.** The volunteer coordinator for a youth recreation league. Shifts at
the concession stand are arranged by group text. Every week a shift is double-filled or empty,
and the coordinator spends Sunday evening fixing it.

### The oversized version

> A complete league management platform. Player registration with online payment. Game
> schedules with automatic referee assignment. Volunteer shifts. A team chat. Parent and player
> accounts with profiles and photos. Push notifications. A native mobile app for both phone
> platforms. An administrator dashboard with financial reports.

### The finishable version

> A shift sign-up web application. The coordinator signs in and creates the week's shifts.
> Families open a shared link, see open shifts, and claim one with a first name and last
> initial. A shift cannot be claimed twice. The coordinator sees the week at a glance, can
> release a claim, and can print the schedule. A health endpoint, a first-party page-view counter
> with no cookies or IP addresses, and a privacy paragraph in the user guide.
>
> **Stretch, named now:** a printable weekly view for the stand's wall, and a spreadsheet export.

### Why

| Cut | Reason |
|---|---|
| Registration with online payment | No payments in this program, and handling card data is a regulated job for specialists. |
| Game schedules, referee assignment | A second and third product. The pain the coordinator named is shifts. |
| Team chat, push notifications | Messaging features that hold conversations about and with minors. Not a student project. |
| Parent and player accounts with profiles and photos | Personal data, including about minors, that the job does not need. The finishable version stores a first name and a last initial. |
| Native mobile apps | A responsive web page works on every phone and is what this course taught. |
| Financial reports | No financial data exists in the finishable version, which is the point. |

**The three tasks that would have taken four times longer than planned:** payments,
authentication for several roles, and the mobile apps.

**What the stakeholder actually cares about:** no empty shifts and no Sunday evenings. The
finishable version measures exactly that: the count of unfilled and double-filled shifts, before
and after.

---

## Example 3 · AI-Integrated

**The composite stakeholder.** The service counter lead at a small equipment repair shop. Staff
answer the same questions every day by hunting through printed service manuals while a customer
waits.

### The oversized version

> A customer-facing AI assistant on the shop's public website, available all day and night,
> answering any question about any product the shop services. Voice input and output. Answers
> in five languages. A model fine-tuned on the shop's repair history. Automatic appointment
> booking and parts ordering from the conversation.

### The finishable version

> A staff-only lookup tool on an approved machine. A staff member types a question. The service
> retrieves the most relevant passages from the shop's own service manuals, which the shop has
> given written permission to use and which contain no personal data. A local model writes a
> short answer that **always shows the manual and page it came from**, and says "I could not find
> that" when retrieval finds nothing useful. When the model is unavailable, a keyword search
> answers instead and is labelled as the fallback. An evaluation set of 25 realistic questions
> with expected answers, run and recorded. The written ethics and licensing analysis.
>
> **Stretch, named now:** a "this answer was wrong" button that records the question, not the
> person, and a weekly list of unanswered questions for the counter lead.

### Why

| Cut | Reason |
|---|---|
| Customer-facing, public website | A wrong answer to a customer is the shop's liability. A person in between catches it. It would also need the system exposed to the internet, which a student does not do. |
| Any product the shop services | The manuals the shop owns and has permitted are the whole world of the tool. Anything else is a guess. |
| Voice and five languages | Each is a project. The pain the counter lead named is finding the page. Record language limits honestly in the bias section instead. |
| Fine-tuning on repair history | Repair history contains customer information. It is also far beyond four sprints. |
| Appointment booking and parts ordering | Actions with money and customers attached. The tool helps a person find information. It does not act. |

**The three tasks that would have taken four times longer than planned:** fine-tuning, voice, and
making public answers safe enough to publish.

**What the stakeholder actually cares about:** finding the right page faster. The finishable
version measures exactly that: time to answer a set of real counter questions, before and after.

---

## The patterns, so you can find them in your own draft

| Pattern | What it looks like in a proposal | The question to ask |
|---|---|---|
| **Platform instead of problem** | "A complete system for..." | Which one pain did the stakeholder actually name? |
| **One more of everything** | Six sensors, four roles, five languages | Would one of them solve the named problem? |
| **Data that does not exist** | "Predictive", "learns from", "trained on" | Where is that data right now, and who owns it? |
| **Accounts, messages, payments** | Profiles, chat, notifications, checkout | Does the job need them, and are they allowed here? |
| **Action instead of information** | Starts the fan, books the appointment, orders the part | Should a person make that decision? |
| **Two platforms** | "A web app and a mobile app" | Does a responsive page already do it? |

**If your draft has two of these patterns, expect your instructor to say it will not finish.**
That is not a judgment on you. It is arithmetic about fifty hours.

---

## Is my scope too small?

It happens, less often. **Your scope is too small if** the minimum viable version is finished by
the end of Sprint 2 with no stretch goals named, or if the stakeholder would not notice whether
it existed.

**The fix is never a new feature after Week 12.** It is naming stretch goals in Week 8, and
choosing a problem in Week 7 that a real person would miss if it were gone.
