# Template · Conceptual Model and Design Brief
## 145010 Senior Capstone · Week 10, Monday

**Commit as:** `docs/measure-analyze/design-brief.md`, with wireframes in
`docs/measure-analyze/wireframes/`
**Due:** Week 10, Monday, end of the build period.

**Competencies this evidences:** 2.9.4 (develop a conceptual model and design brief), 6.1.2 (plan
a web page considering subject, devices, audience, layout, color, links, graphics, and ADA
requirements), 6.5.2 (plan a website's structure for navigation and usability), 2.7.2 (ways to
present data), 2.9.1 (branding), 6.5.14 (search engine optimization, for public pages), 1.5.6
(reading work from a different cultural perspective).

---

## Why this exists

**A design brief is what you would hand another developer so they could build the right thing
without asking you.** Writing it forces decisions you would otherwise make by accident at eleven at
night: what the main screen is for, what a user sees first, what happens on a phone.

**The conceptual model is the part people skip.** It is the handful of things your system is about
and how they relate, in words your stakeholder would recognize. If you cannot write it in half a
page, you do not yet understand the problem well enough to build it.

**The failure to avoid.** Polished mockups. A wireframe is boxes and words. Color and fonts come
last, and a beautiful mockup of the wrong screen costs more than a sketch of the right one.

---

```markdown
# Design Brief · <project name>
Version <1.0>   Written: Week 10, <day>   Supports: Requirements version <n>

## 1. The brief in one paragraph
*What you are designing, for whom, to do what, and the one thing it must get right.*

## 2. The conceptual model
*The main things in this system and how they relate, in the stakeholder's words. No code, no
tables yet.*

**The things:**
- <Shift: a time slot at the stand that one volunteer can claim>
- <Volunteer: ...>
- <...>

**How they relate:**
- <A week has many shifts. A shift has at most one volunteer.>
- <...>

**A diagram** (boxes and lines, drawn by hand and photographed, or written as text):

    <thing> 1 ---- many <thing>
    <thing> many ---- 1 <thing>

**What the user thinks is happening**, in one sentence. If this differs from what the system
really does, say how the design keeps them from being surprised.

## 3. Audience and context
*From the proposal. Add what you learned since.*

| Question | Answer |
|---|---|
| Who uses it | |
| Where they are when they use it | <standing at a counter, on a shop floor, at home in the evening> |
| What device | |
| How much time they have | |
| What they already call things | <use their words for labels> |
| Accessibility needs to plan for | |
| Reading level and language | <plain language; any users who read another language first> |

**Read it from another perspective.** *1.5.6. Name one assumption your design makes that someone
from a different background, age, or culture might not share: a date format, an icon, a word, a
color meaning. Say what you will do about it.*

## 4. How the product presents its data
*2.7.2. Which presentation fits: responsive web page, web application, desktop application,
operator panel, mobile view. Why this one for this audience.*

## 5. Structure and navigation
*6.5.2. Every page or screen, and how a user gets between them.*

    Home
      Week view
        Shift detail
      Sign in
        Coordinator view
          Create shifts
          Print schedule

**Main task path**, step by step, for the requirement that matters most:
1. <...>
2. <...>

**Longest path to any main task:** <number of steps. More than three is worth questioning.>

## 6. Wireframes
*One per main screen, in `wireframes/`. Paper photographed, or a design tool your instructor has
approved. Boxes and words. At phone width and desktop width for web projects. Operator panel at its
real screen size for the Industrial track.*

| Screen | File | Requirement it serves | What the user must see first |
|---|---|---|---|
| | `wireframes/<file>` | R<n> | |

## 7. Accessibility plan
*6.1.2. This is a legal requirement, not a courtesy.*

- **Headings:** <the outline of the main page>
- **Keyboard:** <every task by keyboard, focus visible, no traps; the order a Tab key follows>
- **Labels and alternative text:** <every input labelled; what the images are for>
- **Color and contrast:** <contrast meets the automated check; meaning never by color alone>
- **Screen reader:** <what the main page sounds like, in order>
- **Motion and time:** <nothing flashes; nothing times out without warning>

## 8. Visual design and branding
*2.9.1. From the proposal. Colors and type chosen after the wireframes work.*

- **Colors:** <with the contrast check result for text on each background>
- **Type:** <readable sizes; what an operator can read at distance, for the Industrial track>
- **Logo and name:** <used with permission, recorded where>
- **Voice of the words on screen:** <plain, short, the stakeholder's vocabulary>

## 9. Content plan
- **Who writes the words on each page:** <you, from the stakeholder's material>
- **Proofreading:** every page drafted, revised, edited, and proofread before release (6.1.4)
- **Media:** <any images, audio, or video; source and license; captions for video>

## 10. Search and sharing
*6.5.14. Public pages only. Write "not public" if the whole product is private.*

- **Page titles and descriptions:** <one per public page>
- **What a search for the stakeholder's organization should find:** <if anything>
- **What must never be found by search:** <private pages, and how they are kept out>

## 11. Decisions and open questions
| Decision or question | Options considered | Chosen, or who will answer | Decision log entry |
|---|---|---|---|
| | | | |
```

---

## Before you commit · self-check

- [ ] Your stakeholder would recognize every word in section 2.
- [ ] Every main screen has a wireframe, and every wireframe serves a requirement.
- [ ] The main task takes three steps or fewer, or you wrote why not.
- [ ] Section 7 is specific to your screens, not a general list.
- [ ] No color decision depends on color alone to carry meaning.
