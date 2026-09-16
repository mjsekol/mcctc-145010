# Clinic · Paper Wireframes
## 145010 Senior Capstone · Week 10, Monday · 15 minutes · Analyze

**Slides for this clinic:** This clinic has no slide outline. It runs at the board.

**When this clinic runs.** Week 10, Monday, or any week the room shows this signal: students
opening a design tool and choosing colors first.
**If you missed it,** you can learn the skill from this file alone.
**Competencies:** 2.9.4 (develop a conceptual model and design brief), 6.1.2 (plan a web page
considering devices, audience, layout, links, and ADA requirements), 6.5.2 (plan a website's
structure for navigation and usability), 2.7.2 (ways to present data), 2.7.4 (how browsers and
devices affect a page)

---

## Why this exists

You worked in Figma in junior year. So the first thing many of you will do today is open a design
tool and pick a palette. **That is the most expensive way to design.**

A polished mockup takes an hour. If it shows the wrong screen, or the right screen in the wrong
order, the hour is gone, and you will be reluctant to throw it away because it looks good. A paper
sketch takes three minutes. You throw it away without a second thought.

The question today is not "what does it look like?" It is **"what is on each screen, and how does a
person get from one to the next?"** Boxes and words answer that. Color does not.

## The skill in plain language

1. **List every main screen.** Take them from your requirements. Every screen serves at least one
   requirement. A screen that serves none is out of scope.
2. **Draw the screen flow first.** One box per screen, arrows for how a person moves between them.
3. **Sketch each screen as boxes and words.** Real labels in the stakeholder's words. No color, no
   fonts, no icons you would have to draw well.
4. **Draw web screens twice:** phone width and desktop width. Industrial track: the panel at its
   real screen size.
5. **Write accessibility notes on the sketch.** The heading, the label of every input, the Tab
   order, where an error message appears, and what a screen reader says first.
6. **Photograph it, name the file, commit it.** A sketch on your desk is not evidence.

Paper is the default. A design tool your instructor has approved is allowed, with the same rule:
boxes and words, gray only.

## Worked example 1 · the screen flow

*Composite, not a real organization.* The Parts Bin Board has four main screens and one
confirmation.

```
  [ Report a low bin ]  --Mark low-->  [ Thanks, B-03 marked low ]
          |                                     |
          |                            "Report another bin" link
          |                                     |
          +<------------------------------------+

  [ Coordinator sign-in ]  --signed in-->  [ Low list ]  --"Counts" link-->  [ Board opens by day ]
                                               |
                                    "Restocked" on a row
                                               |
                                    [ Low list, row removed ]
```

Longest path to the main task: open the link, choose the bin, press Mark low. Three steps. The design brief
template asks you to question anything longer than three.

## Worked example 2 · the report screen, phone and desktop

*Composite.* Drawn on paper, written here as text. Photographed files:
`wireframes/01-report-phone.jpg` and `wireframes/02-report-desktop.jpg`.

```
PHONE, 360 wide                     NOTES (written beside the sketch)
+----------------------------+
| Parts Bin Board            |      h1 = "Report a low bin"
|----------------------------|
| Report a low bin     (h1)  |      Tab order: 1 Bin, 2 Note,
|                            |      3 Mark low
| Bin                        |
| [ B-03  Tubes, 26 in.  v ] |      Label "Bin" is a real label on the
| Match the code on the      |      drop-down, not placeholder text
| bin label.                 |
|                            |      An error appears NEXT TO the field
| Note (optional, 120 max)   |      with the problem, and Narrator
| [                    ]     |      reads it
| [                    ]     |      Narrator should say first:
|                            |      "Report a low bin, heading level 1"
| [ Mark low ]               |
|                            |      No name field. On purpose.
+----------------------------+

DESKTOP, 1280 wide (the co-op desktop by the door)
+------------------------------------------------------------------+
| Parts Bin Board                                                  |
|------------------------------------------------------------------|
|  Report a low bin (h1)              | How this works             |
|                                     | 1. Find the code on the    |
|  Bin   [ B-03  Tubes, 26 in.  v ]   |    bin label.              |
|  Note  [                        ]   | 2. Mark it low.            |
|                                     | 3. The coordinator sees it |
|  [ Mark low ]                       |                            |
+------------------------------------------------------------------+
```

Notice what is not there: a color, a logo, a font choice. Notice what is: the exact label words,
the order, and where the error goes.

## Worked example 3 · the low list

*Composite.* `wireframes/03-low-list-desktop.jpg`.

```
+----------------------------------------------------------------------+
| Parts Bin Board                        Signed in as coordinator      |
|                                                      [ Sign out ]    |
|----------------------------------------------------------------------|
| Low bins (h1)                          3 bins low                    |
| [ Print this list ]    Counts (link)                                 |
|                                                                      |
| Bin    Part            Note                Marked     Action         |
| ----   -------------   -----------------   --------   ------------   |
| B-03   Tubes, 26 in.   last two gone       7:42 pm    [ Restocked ]  |
| B-11   Brake pads      -                   6:15 pm    [ Restocked ]  |
| B-07   Chains          ask about 9 speed   last Tue   [ Restocked ]  |
+----------------------------------------------------------------------+
NOTES: a real table with column headers, so Narrator reads "Bin, B-03".
Each button's accessible name includes the bin: "Restocked, B-03".
Low state is shown in words ("3 bins low"), never by color alone.
Newest first, as R2 says. The printed list must fit one page (AC-2).
```

The note in the last line comes straight from NF3. Writing it on the sketch now means you build
it right the first time.

## The wrong version, and what it costs

*Composite.* A student opens a design tool at the start of the period. By the end they have one
screen: a dark theme, a custom font, a bike icon, rounded cards, and a "Volunteer profile" panel.

What that costs:

1. **One screen of four.** The design brief needs every main screen by the end of today.
2. **A screen for something not in scope.** "Volunteer profile" traces to no requirement. The
   signed scope says volunteers report with no name.
3. **No accessibility notes,** because the tool invited styling, not planning.
4. **Sunk-cost attachment.** When the stakeholder says "the volunteers will never find that
   button," a student with an hour in the mockup argues instead of listening.

## Why the wrong version is tempting

A styled mockup looks like progress, and it is fun. Paper feels childish for a senior. But the
people who design for a living sketch first for exactly this reason: it is cheap to be wrong on
paper. **Color comes last, after the boxes are right.** The design brief has a section for it,
section 8, and it comes after section 6.

## Do this today

1. On one sheet, draw your screen flow. Check each screen against your requirements.
2. Sketch every main screen. Web projects: phone and desktop. Write labels, Tab order, error
   position, and the first thing a screen reader says.
3. Photograph each sheet in good light, flat, with no people in the photo.
4. Save them in `docs/measure-analyze/wireframes/` with names like `01-report-phone.jpg`.
5. Fill in sections 5, 6, and 7 of the
   [Design Brief template](../05-labs/MCCTC_145010_Template_DesignBrief.md) in
   `docs/measure-analyze/design-brief.md`. Section 6's table points to each file.
6. Commit the photos and the brief.

## If you are ahead, if you are behind

**Ahead.** Write section 2, the conceptual model: the handful of things in your system and how they
relate, in words your stakeholder would recognize. For the co-op: "A bin holds one kind of part. A
bin can be reported low many times. A report is cleared when the bin is restocked."

**Behind.** Draw the flow and the one screen for your most important requirement. Commit those.
Finish the rest in Period 8 today, and say so at standup tomorrow, because
the architecture is due tomorrow too.

## Words the WebXam uses

| Exam word | What it means here |
|---|---|
| **Wireframe** | A layout sketch with no styling. |
| **Site structure, navigation** | Your screen flow. 6.5.2. |
| **Conceptual model** | The main things in your system and how they relate. 2.9.4. |
| **Design brief** | The document that tells a builder what to make, for whom, and why. 2.9.4. |
| **Responsive design** | The same content arranged for a phone and a desktop. |
| **Ways to present data** | Web page, web application, desktop application, mobile view. 2.7.2. |
| **Screen reader** | Software that reads the page aloud, like Windows Narrator. 2.7.4. |

## Self-check

**1.** A classmate's wireframe for the low list shows low bins in red and restocked bins in green,
with no other difference. What is the problem, and what is the fix?

**2.** Why draw the screen flow before the screens?

**3.** Name two things that belong on a wireframe and two that do not.

### Answers

**1.** Meaning is carried by color alone, which a person who cannot tell red from green, or a
screen reader user, will miss. The fix is words: a "Low" or "Restocked" label, or restocked bins
removed from the list.

**2.** Because the flow shows which screens exist and how a person reaches each one. A screen that
no arrow reaches, or a task that takes five steps, shows up on the flow before you spend time
sketching it.

**3.** Belong: real label text, the order of elements, where an error appears, Tab order notes.
Do not belong: colors, fonts, final icons, a logo treatment.
