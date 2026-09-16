# Lecture Notes: What Tools Cannot See, and Testing With People
## 145010 Web Design & Senior Capstone · Week 3 · Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W03_TestingWithPeople.md).
There is no exported deck yet. To generate one, from the repository root:
`node tools/gamma.js Courses/145010/units/unit-3-accessibility/04-slides/MCCTC_145010_Slides_W03_TestingWithPeople.md --export pptx`

If you missed class, you can learn this concept from this file alone. You need Chrome, `web-check`,
headphones, and a partner for the last part.

**Competencies:** 6.5.10 (develop and execute usability tests checking information accessibility, ease
of use, and navigation), 2.7.4 (how text-to-speech and screen readers change a page), 1.5.5 and 1.5.6
(bias and cultural perspective in who a product is tested with), 1.3.2 (protocols for a clean, safe,
and healthy work environment).

---

## Why this exists

By now you have seen the pattern three days running. On the Lantern Street page, web-check fully
reported **six** of twenty-four planted problems. On the swap board, **two** of eight.

That is not a flaw in web-check. Automated checkers are built to report what they can prove from the
page at rest, and they are good at it. **They cannot use the page.** They cannot press Tab and notice
they are stuck. They cannot listen to alt text and decide it is useless. They cannot tell that a colour
means "full."

So a page is not tested until a person has used it the way the people it serves will use it. Today is
how to do that on purpose, and how to write down what you found so someone else can check it.

---

## The concept in plain language

**Accessibility testing has three layers, and you need all three.**

| Layer | What it is | What it catches | What it costs |
|---|---|---|---|
| **1. Automated** | `web-check`: a validator and axe | Missing attributes, missing names, measurable contrast, invalid markup | Seconds. Run it every time you save |
| **2. Expert walkthrough** | You, with a checklist, using only a keyboard and then a screen reader | Traps, focus order, invisible focus, meaningless names, heading outline, colour meaning | Twenty minutes per page |
| **3. Usability test** | Someone who did not build it tries real tasks while you watch and stay quiet | Everything you are too close to see: confusing labels, a link nobody finds, a step nobody expects | An hour, and a person's time |

**Layer 1 without layers 2 and 3 is how "passes automated checks" turns into "fully accessible" in a
statement nobody verified.**

---

## Layer 2: the screen reader walkthrough

**Windows Narrator** is built into Windows. **NVDA** is a free screen reader for Windows that many
testers use; it is not installed on the machine these notes were written on, so every NVDA step is
marked **[VERIFY]**.

**Starting and stopping Narrator:** Ctrl + Windows key + Enter. Do that once before you start, and once
when you finish, and confirm it has stopped.

**The Narrator key** is Caps Lock or Insert by default. Microsoft's "Complete guide to Narrator" lists
the start keys, Narrator + Space bar for scan mode, Ctrl to stop reading, and the three list commands
below. The single-letter keys for headings and landmarks were not confirmed from that guide when these
notes were written. Your instructor confirms everything marked **[VERIFY]** on a lab machine:

| Action | Narrator | NVDA **[VERIFY]** |
|---|---|---|
| Turn on or off | Ctrl + Windows key + Enter | Ctrl + Alt + N, if the desktop shortcut was set up at install |
| Stop speaking | Ctrl | Ctrl |
| Switch to moving through the page by element | Narrator + Space bar toggles scan mode **[VERIFY]** | Browse mode is on by default in web pages |
| Next heading | H, in scan mode **[VERIFY]** | H |
| Next landmark | D, in scan mode **[VERIFY]** | D |
| Next form field | F, in scan mode **[VERIFY]** | F |
| List of links, headings, landmarks | Narrator + F7 links, Narrator + F6 headings, Narrator + F5 landmarks **[VERIFY]** | Insert + F7 |

**The walkthrough is a checklist, not a tour.** `lab-w03-01-files/walkthrough-checklist.md` has ten
checks, S1 to S10. For each, you write what you **heard**, not what you expected.

**The failure mode that wastes the period.** Using the mouse while the screen reader talks. Clicking moves
the screen reader to wherever you clicked, so you skip exactly the navigation you were supposed to test,
and you learn nothing about how a screen reader user moves. Hands on the keyboard only.

---

## Layer 3: a usability test in fifteen minutes

Competency 6.5.10 asks you to **develop and execute** usability tests on accessibility, ease of use, and
navigation. You ran usability studies in an earlier course. The accessibility version adds one rule:
**the participant uses the input method you are testing,** keyboard only today.

1. **Write the tasks before the session.** A task is a goal, not an instruction. "Find out whether the
   Thursday afternoon sorting shift still has space" is a task. "Tab to the table" is an instruction and
   tests nothing.
2. **Read each task once.** Then be quiet.
3. **Do not help.** If they are stuck for sixty seconds, say "let's move on" and write down where they
   stopped. The place they got stuck is the finding.
4. **Record three things per task:** finished or not, time, and where they hesitated.
5. **Make one change** because of what you saw, and say which observation caused it.

**Who you test with matters, and this is where bias lives.** If you only ever test with classmates who
think like you, use the same devices, and read the same language, your test will confirm your page works
for people like you. For 1.5.5 and 1.5.6, ask: who is missing from this test? A classmate doing a
keyboard-only test is a useful stand-in. **It is not the same as testing with a person who uses a
keyboard or a screen reader every day**, and your write-up should say so. In the capstone, when you test
with real users in Weeks 15 and 16, that difference is the one to close.

**Never treat a person with a disability as a test prop.** A real participant is recruited, agrees, can
stop at any time, and is thanked. The capstone usability protocol covers that properly.

---

## Worked example 1: the automated layer passes a page with a trap in it

Take the rebuilt Lantern Street page and add back a small script that "tidies" the phone number when
Tab is pressed, cancelling the Tab key. web-check on that page, path shortened to the file name:

```
PASS  h_trap_back.html
  validation: 0 error(s), 0 warning(s)
  axe at 360px: 0 violation(s)
  axe at 768px: 0 violation(s)
  axe at 1280px: 0 violation(s)
```

A keyboard walk of the same page:

```
   9  <input#volunteer-email> textbox "Email"  focus ring: visible
  10  <input#volunteer-phone> textbox "Phone (optional)"  focus ring: visible
  11  <input#volunteer-phone> textbox "Phone (optional)"  focus ring: visible  <- did not move
  12  <input#volunteer-phone> textbox "Phone (optional)"  focus ring: visible  <- did not move
  TRAP: Tab pressed three times and focus did not move.
```

**Every automated check passed and no keyboard user can finish the form.** That is 2.1.2 No Keyboard
Trap (A), and only layer 2 found it.

---

## Worked example 2: what a screen reader navigates by

A screen reader user skims by heading and landmark. Here is what the browser's accessibility tree offers
for each version of the Lantern Street page, read with a script on the build machine.

Before the rebuild:

```
HEADINGS   h1 Volunteer with us / h4 How it works
LANDMARKS  form
LINKS      "Shifts" / "Sign up" / "Visit" / (no name) / "Read more" / "Read more" / "click here"
```

After:

```
HEADINGS   h1 Volunteer with us / h2 How it works / h2 Pantry hours / h2 This week's shifts / h2 Sign up for a shift / h2 Finding the side door / h3 What to wear on a shift / h3 Getting your service hour form signed
LANDMARKS  banner / navigation Main / main / region How it works / region Pantry hours / region This week's shifts / region Sign up for a shift / form / region Finding the side door / contentinfo
LINKS      "Skip to main content" / "Shifts" / "Sign up" / "Finding us" / "Add shifts to your calendar" / "What to wear on a shift" / "Getting your service hour form signed" / "Directions to the side door"
```

Read the "before" block as a screen reader user would. Two headings on a page with five sections. No
main landmark. A link list with a nameless link and three links that say nothing alone. **web-check
passed every one of those problems except the nameless link.** The screen reader walkthrough, checks
S2, S3, and S10, is where you hear them.

---

## Worked example 3: a usability test record

This record is **invented for these notes** to show the format. It is not a real session.

```
Page: week3-rebuild/index.html        Method: keyboard only, no mouse
Tester: Dana (partner)                Author: Jordan

T1  "Find out whether the Thursday afternoon sorting shift still has space."
    Finished: yes   Time: 0:48
    Hesitated: tabbed through the whole header and both help links first;
    did not know the table was not focusable and kept pressing Tab past it.

T2  "Sign up for the Saturday shift. Use the name Test Volunteer and the
     email volunteer@example.com."
    Finished: yes   Time: 1:35
    Hesitated: pressed Tab from Yes expecting No; used arrow keys after 10 s.

T3  "Find out which door to use when you arrive."
    Finished: yes   Time: 0:22
    Hesitated: none. Used "Finding us" in the nav.

Change made: T1 showed the skip link was missed because it only appears on
focus and the tester was already past it. Added a visible "Jump to this
week's shifts" link at the top of main. Rerun of web-check: PASS.
```

What makes this a good record: every task is a goal, every hesitation is an observation and not an
opinion, and the change names the observation that caused it.

**What is honest about it:** T1's hesitation is partly a keyboard-only artifact. A sighted keyboard user
reads a table with their eyes and does not need to focus it. A screen reader user would move into the
table with the screen reader's own table keys. The record should note that a keyboard-only test is not a
screen reader test.

---

## The wrong version: declaring it done at layer 1

```
node tools/web-check/check.js week3-rebuild/index.html
PASS
```

and a commit message that says `Page is fully accessible`.

That sentence is a claim about every person who will use the page. The evidence behind it is a program
that never pressed a key, never heard a word, and never tried to sign up. Worked example 1 is a page that
earns exactly that PASS and traps every keyboard user.

**The honest commit message** says what was checked: `web-check passes at 360/768/1280; keyboard walk
K1-K10 pass; Narrator walkthrough S1-S10, S4 not testable (no Spanish voice installed)`.

---

## Why the wrong version is tempting

**A green PASS feels like a finish line.** It is a starting line.

**Human testing is slow and awkward.** Watching a partner struggle with your page and saying nothing is
uncomfortable. That discomfort is where the findings are.

**You already know how the page works.** That is exactly why you cannot test it by yourself.

---

## A clean, safe, and healthy test station (1.3.2)

Competency 1.3.2 is about following protocols that keep a workplace clean, safe, and healthy. A room
running screen reader tests is a small workplace, and it has real protocols:

- **Headphones on, volume low.** Thirty screen readers on speakers make every test in the room useless,
  and listening at high volume for a whole period is bad for your hearing.
- **Clean shared headphones** before and after you use them, or use your own earbuds.
- **Cables and chairs.** Partner testing means moving to another station. Keep headphone and charger
  cables off the floor where people walk.
- **Breaks.** A long keyboard-only session is a repetitive strain session. Stand up at the reset.
- **Turn the screen reader off** before you leave the machine, and check that it is off.

**And the design version of the same competency.** What you put on a page can affect a user's health.
WCAG 2.3.1 Three Flashes or Below Threshold (A) exists because flashing content can trigger seizures.
Motion that starts on its own can make some people dizzy or sick, which is why browsers let people ask
for reduced motion and why a page should respect it. A pulsing badge, an auto-playing carousel, and a
parallax background are design decisions with a health dimension. Those are not the same thing as a
clean workplace, and the competency is about the workplace, but a developer who thinks about one tends
to think about the other.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Automated test** | A program that checks a page without a person, such as web-check |
| **Expert walkthrough** | A trained person working through a checklist on the page |
| **Usability test** | A person who did not build the page tries real tasks while an observer records |
| **Task** | A goal a participant is asked to reach, written without naming controls |
| **Facilitator** | The person who reads tasks and stays quiet |
| **Finding** | An observation from a test that points to a change |
| **Screen reader walkthrough** | Navigating the page by keyboard with a screen reader running, recording what is heard |
| **Scan mode** | Narrator's mode for moving through a web page by headings, landmarks, and other elements |
| **Browse mode** | NVDA's equivalent mode in web pages |
| **Listening log** | A timestamped written record of what a screen reader said, used when recording is not possible |

---

## Self-check

**Question 1.** Name one problem from the Lantern Street page that belongs to each testing layer, the
layer that first catches it: automated, walkthrough, usability test.

**Question 2.** Your partner is stuck on T2 for forty seconds and asks, "Do I press Tab or the arrow key
here?" What do you say, and what do you write down?

**Question 3.** A classmate's walkthrough record says S4, the Spanish sentence, failed. You check the page
and `lang="es"` is on the paragraph. Give two possible explanations and what you would check for each.

---

### Answers

**1.** Many answers work. Automated: the logo with no `alt`, or the phone field with no label. Walkthrough:
the keyboard trap, the invisible focus, the file-name alt text, the missing Spanish `lang`. Usability test:
anything a person hesitates over that a checklist does not name, such as not realizing the radio group
takes arrow keys, or not finding the directions.

**2.** Nothing that answers the question. A neutral reply such as "What would you try?" or silence. Write
down: "T2, 0:40, stuck at the Yes/No choice, unsure whether Tab or arrows move between options." That
hesitation is the finding. If the sixty seconds run out, say "let's move on."

**3.** First, the machine may have no Spanish voice installed, so Narrator cannot switch pronunciation
even when the markup is right. Check the installed voices, and record S4 as not testable on that machine.
Second, the `lang` attribute may be on a different element from the one being read. Check the element in
DevTools. A misspelled code such as `lang="sp"` is less likely to be the cause, because web-check catches
it: on a test page with that code it reported `valid-lang (serious, 1 node(s))  lang attribute must have a
valid value`. Run web-check and confirm the code is `es`.
