# Lecture Notes: Accessibility Is a Requirement, and WCAG Is How You Test It
## 145010 Web Design & Senior Capstone · Week 3 · Monday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W03_AccessibilityIsARequirement.md).
There is no exported deck yet. To generate one, from the repository root:
`node tools/gamma.js Courses/145010/units/unit-3-accessibility/04-slides/MCCTC_145010_Slides_W03_AccessibilityIsARequirement.md --export pptx`

If you missed class, you can learn this concept from this file alone. You need Python and the course's
`web-check` tool to run the examples.

**Competencies:** 6.1.2 (plan a web page considering subject, devices, audience, layout, color, links,
graphics, and ADA requirements), 2.7.4 (how different browsers and devices affect the function of a
page, including ADA, text-to-speech, screen readers, mobile and desktop), 1.5.5 (how bias and
discrimination influence productivity and profitability), 1.5.6 (analyze work tasks from a different
cultural perspective).

---

## Read this first: this is not legal advice

**Your instructor is not a lawyer, and this file is not legal advice.** It explains what the law is for,
at the level of the competency, so you recognize when it applies to something you build. It
deliberately does **not** state compliance deadlines, size thresholds, penalties, or the outcome of any
court case. Those details change, some of them have already changed since the rules were written, and
a wrong detail in a lesson is worse than none.

When a real project depends on the answer, go to the source, and bring the question to someone
qualified to answer it. These are the primary sources. Each loaded when this lesson was built, and each
is marked **[VERIFY]** because government pages move:

- **ADA.gov, the U.S. Department of Justice's ADA site,** guidance on web accessibility:
  `https://www.ada.gov/resources/web-guidance/` **[VERIFY]**
- **ADA.gov, fact sheet on the web and mobile app rule for state and local governments:**
  `https://www.ada.gov/resources/2024-03-08-web-rule/` **[VERIFY]**
- **W3C, Web Content Accessibility Guidelines (WCAG) 2.2:** `https://www.w3.org/TR/WCAG22/` **[VERIFY]**
- **Section508.gov**, for the federal government's own accessibility requirements:
  `https://www.section508.gov` **[VERIFY]**

---

## Why this exists

Last week you checked your layout at three widths. You were checking that the page worked for people
whose screens are not like yours. This week you check that it works for people whose **bodies** are not
like yours.

Some people read a page with their ears, through a screen reader. Some never touch a mouse. Some zoom to
400 percent. Some cannot tell red from green. Some use voice control and say the name of the link they
want. None of them are rare, and every one of them is a customer, a volunteer, a student, or an
employee of whoever you build for.

**The syllabus says this is a legal requirement, not a courtesy.** That is the first half of today. The
second half is how you find out, with a test, whether you met it.

---

## Who navigates differently, and what they use

Competency 2.7.4 asks you to identify how devices and assistive technology change how a page works. Here
is the list to know.

| Technology | What the person does | What your page must give them |
|---|---|---|
| **Screen reader** (Windows Narrator, NVDA, JAWS, VoiceOver on Apple devices, TalkBack on Android) | Hears the page read aloud and moves by heading, landmark, link, or field | Real structure, names on everything, text for every meaningful image |
| **Text-to-speech read-aloud** (built into browsers and operating systems) | Hears a block of text read aloud, often while also looking | Text that is real text, in the right language |
| **Keyboard only** | Tab, Shift+Tab, Enter, Space, arrow keys | Every control reachable, a visible focus ring, no traps |
| **Switch access** | One or two buttons that step through controls | The same as keyboard, plus patience in the design |
| **Voice control** | Says "click Sign up" | Visible labels that match the control's name |
| **Magnification and zoom** | Sees a small part of the page at a time, very large | Zoom allowed, layout that reflows, nothing that only makes sense at a glance |
| **Captions and transcripts** | Reads what is said in audio and video | Captions on every video, from Week 2 |
| **A phone instead of a desktop** | Touch, a small screen, often a slow connection, often in sunlight | Large enough targets, strong contrast, responsive layout |

**The failure mode you are most likely to have.** You test with a mouse and your own eyes on a laptop.
That test is real, and it covers one row of that table.

---

## The law, at the level you need

**The Americans with Disabilities Act (ADA)** is a federal civil rights law that prohibits
discrimination against people with disabilities. You met its employment side in 145060. Its other
parts cover the services of **state and local governments**, which includes public schools, and of
**businesses open to the public**.

**The U.S. Department of Justice says the ADA's requirements apply to what those organizations offer on
the web.** Its guidance on web accessibility says so for both groups, and names WCAG as one of the
existing standards that help organizations know what to do.

**For state and local governments there is now a specific rule.** The Department of Justice published a
rule that names **WCAG 2.1 Level AA** as the technical standard for their web content and mobile apps,
and its fact sheet lists public schools among the organizations covered. **Its compliance dates have
already been changed since it was published.** Look them up on ADA.gov when you need them. Do not
quote a date from memory, including from this course.

**For businesses, the guidance this lesson draws on does not name a required version of WCAG.** It
still says the ADA applies to their web content. Check ADA.gov for whether that has changed. Lawsuits
about inaccessible websites happen, and their outcomes vary. This file does not summarize any of them.

**Federal agencies** follow Section 508, a different law with its own standards.

**What that means for you, practically.** Your capstone stakeholder in Week 7 may be a school, a
township, a library, or a business. Whichever it is, "we did not think about accessibility" is not a
position you want to hand them. Build to WCAG 2.2 Level AA, which is this course's standard, and you are
building to a version at least as demanding as the one the rule names, with one small exception covered
below.

---

## WCAG, the test you can pass or fail

**WCAG** is the Web Content Accessibility Guidelines, published by the **W3C**, the World Wide Web
Consortium, which also publishes CSS and many other web standards. **This course uses WCAG 2.2**, which W3C publishes as a
Recommendation. When you cite a criterion in this course, you cite it from 2.2, by number and name.

It is organized in four principles. The acronym is **POUR**:

- **Perceivable.** People can get the information through at least one sense they have.
- **Operable.** People can use every control with the input method they have.
- **Understandable.** People can understand the content and predict what the page will do.
- **Robust.** The page works with the browsers and assistive technology people really use.

Under the principles are **success criteria**. Each one is a **testable statement**. It has a number, a
name, and a level:

| Level | Meaning |
|---|---|
| **A** | The minimum. Failing one blocks some people outright |
| **AA** | The level the Department of Justice rule names, and this course's standard |
| **AAA** | The highest. W3C does not recommend requiring it for whole sites, because some content cannot meet every AAA criterion |

**WCAG 2.2 removed one criterion**, 4.1.1 Parsing. W3C's page notes that anyone whose policy still
requires an earlier version may need to keep testing it. That is the small exception mentioned above.

**The mental model to keep all week.** A success criterion is not an opinion. It is a test. "The page
is accessible" cannot be failed. "Body text has a contrast ratio of at least 4.5:1 against its
background" can.

---

## Today's two criteria: contrast and colour

### 1.4.3 Contrast (Minimum), Level AA

Text needs a **contrast ratio of at least 4.5:1** against its background. **Large text** needs at least
**3:1**. WCAG defines large text as **at least 18 point, or 14 point bold**. 18 point is 24 pixels. 14
point is about 18.7 pixels. **16-pixel bold button text is not large.**

The ratio runs from 1:1, white on white, to 21:1, black on white.

### 1.4.11 Non-text Contrast, Level AA

The parts of a control you need to see to know it is there, and graphics you need to understand, need
**3:1** against what is next to them. A text box whose border is almost the colour of the page is the
usual failure.

### 1.4.1 Use of Color, Level A

**Colour must not be the only way information is shown.** "Fields in red are required" fails. "Red bar
means urgent" fails. The fix is almost always words, and colour can stay as a second cue.

---

## Worked example 1: the contrast ratio is arithmetic

The ratio is not a judgement. It is a formula from the WCAG definitions, and you can run it.

```python
# contrast_ratio.py: the WCAG contrast formula, so the number stops being magic.
def channel(value):
    c = value / 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def luminance(hex_colour):
    hex_colour = hex_colour.lstrip("#")
    r, g, b = (int(hex_colour[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)

def ratio(text, background):
    lighter, darker = sorted([luminance(text), luminance(background)], reverse=True)
    return (lighter + 0.05) / (darker + 0.05)

for text, background in [("#a3a3a3", "#ffffff"), ("#444444", "#ffffff"), ("#ffffff", "#6cc070")]:
    r = ratio(text, background)
    verdict = "passes" if r >= 4.5 else "fails"
    print(f"{text} on {background}: {r:.2f}:1, {verdict} 4.5:1 for normal text")
```

Output:

```
#a3a3a3 on #ffffff: 2.52:1, fails 4.5:1 for normal text
#444444 on #ffffff: 9.74:1, passes 4.5:1 for normal text
#ffffff on #6cc070: 2.23:1, fails 4.5:1 for normal text
```

The first and third pairs are from the page you rebuild this week. The light grey looks elegant. White
on that green looks bold. Both fail, and the number says so without anyone's taste being involved.

In class you get the same number from Chrome's colour picker in DevTools. The script exists so you know
where the number comes from.

---

## Worked example 2: the tool finds contrast for you

`web-check` runs axe, an automated accessibility checker, and axe measures contrast on every piece of
text.

```
node tools/web-check/check.js Courses/145010/units/unit-3-accessibility/05-labs/lab-w03-01-files/index.html --widths 360
```

Part of the output:

```
  axe at 360px: 7 violation(s)
    color-contrast (serious, 3 node(s))  Elements must meet minimum color contrast ratio thresholds  e.g. .intro | .note | .btn
```

Three elements, one rule. The rule name is `color-contrast`. The criterion it tests is 1.4.3.

---

## Worked example 3: the tool does not know what colour means

The rebuild page's shift table says "Green shifts have open spots. Red shifts are full," and colours
each row. A screen reader receives the text and never the colour. This is a faithful model of what gets
read out:

```python
# What a screen reader receives from the Lantern Street shift table: the text, never the colour.
rows = [
    ("Tuesday", "3:30 to 5:15", "Sorting", "open"),
    ("Tuesday", "5:15 to 7:00", "Distribution", "full"),
]
for day, time, job, css_class in rows:
    print(f"Heard: {day}, {time}, {job}")
```

Output:

```
Heard: Tuesday, 3:30 to 5:15, Sorting
Heard: Tuesday, 5:15 to 7:00, Distribution
```

One of those shifts is full. Nobody listening can tell which. **web-check reported nothing about this
table's colours.** A tool cannot know that a background colour carries meaning.

There is one colour case the tool does catch: a link inside a paragraph that is distinguished only by
colour, with no underline, when the link colour is too close to the text colour. On a test page with a
link styled `color: #333333; text-decoration: none` inside `#222222` text, web-check reported:

```
    link-in-text-block (serious, 1 node(s))  Links must be distinguishable without relying on color  e.g. #x
```

**The rule to take away:** tools catch colour problems they can measure. They cannot catch colour
problems that need to know what the colour means.

---

## The wrong version: fixing contrast by eye

A student sees the red note, "Fields in red are required," decides the red looks strong enough, and
moves on. The checker disagrees:

```
    color-contrast (serious, 3 node(s))  Elements must meet minimum color contrast ratio thresholds  e.g. .intro | .note | .btn
```

`.note` is `#d9534f` on white at 0.9rem. That is **3.96:1**. It looks red and readable to a person with
typical vision on a good screen, indoors. It fails.

And fixing the contrast would not fix the sentence. It still tells the reader to look for a colour.
That is 1.4.1, and it is a Level A failure, one level more basic than the contrast problem.

---

## Why the wrong version is tempting

**Your eyes are the test you always have with you.** They are also the test least like the people this
week is about.

**Colour is fast.** A red border says "required" to you in a tenth of a second. Words take space and
feel cluttered. The design pressure is real, which is why the rule is written down.

**The tool passes the colour-only table.** If you trust the tool as the definition of done, the most
basic failure on the page ships.

---

## Who the product serves: bias in design decisions

Competency 1.5.5 asks how bias and discrimination influence productivity and profitability. Competency
1.5.6 asks you to look at work from a different cultural perspective. On a web page those are not
abstract. They are decisions you make in the markup.

**Bias here is rarely hostile. It is usually a default nobody questioned.**

| The default | Who it quietly leaves out |
|---|---|
| "Everyone uses a mouse" | Keyboard, switch, and voice users |
| "Everyone can see colour the way I do" | People with colour vision deficiency, and everyone using a screen reader |
| "Everyone reads English" | The Spanish-speaking family the pantry page is trying to reach |
| "Everyone has a new phone and fast data" | Students on an old phone and the guest wireless |
| "Names look like my name" | Anyone whose name has an accent, a hyphen, or a second family name, when a form rejects it |
| "Everyone reads the icon the same way" | People for whom a check mark, a thumbs-up, or a colour carries a different meaning |

**The business cost, without inventing a statistic.** A page that some people cannot use loses those
people: a volunteer who could not sign up, a customer who could not order, an applicant who could not
apply. It adds support calls. It adds legal risk. And the team that built it usually never finds out,
because the people it failed are not in the room.

**The cultural perspective, in one line of HTML.** The pantry page has a Spanish sentence. Without
`lang="es"` on it, a screen reader reads it with English pronunciation. The sentence was written for a
Spanish-speaking family and delivered in a form that family cannot understand. **A team where somebody
reads Spanish catches that in seconds. A team where nobody does ships it.** That is the productivity
argument for a team with different perspectives, stated as a bug.

**The strongest case on the other side.** Designing for everyone costs time, and a small organization's
volunteer builder has limited time. The honest answer is not that the cost is zero. It is that most of
this week's fixes are free when you do them from the start, and expensive when you do them after a
complaint.

---

## Planning a page for all of its users (6.1.2)

Before you build a page, answer these on paper. The Week 3 project's access plan asks exactly these.

1. **Who uses it?** Name at least one person who does not navigate the way you do.
2. **On what?** Phone, desktop, assistive technology.
3. **Layout.** What is the heading outline? What are the landmarks?
4. **Colour.** What are your text and background pairs, and their ratios? Is any meaning carried by
   colour alone?
5. **Links.** Does every link make sense read alone?
6. **Graphics.** Which images carry information, and what is their text alternative? Which are
   decorative?
7. **Standard.** Which WCAG version and level are you building to? In this course, 2.2 AA.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Accessibility** | Whether people with disabilities can perceive, operate, and understand a page with the tools they use |
| **Assistive technology** | Software or hardware a person uses to access a computer: screen readers, switches, magnifiers, voice control |
| **Screen reader** | Software that reads the page aloud and lets the user move by structure |
| **ADA** | The Americans with Disabilities Act, a federal civil rights law protecting people with disabilities |
| **WCAG** | Web Content Accessibility Guidelines, published by W3C. This course uses version 2.2 |
| **W3C** | The World Wide Web Consortium, which publishes web standards including CSS and WCAG |
| **POUR** | Perceivable, Operable, Understandable, Robust: the four WCAG principles |
| **Success criterion** | A testable WCAG requirement with a number, a name, and a level |
| **Conformance level** | A, AA, or AAA |
| **Contrast ratio** | A number from 1:1 to 21:1 comparing the luminance of two colours |
| **Large text** | At least 18 point, or 14 point bold, under WCAG |
| **Section 508** | The federal law covering accessibility of federal agencies' technology |

---

## Self-check

**Question 1.** A designer picks `#ffffff` text on a `#6cc070` button and says the text is bold, so 3:1
is enough. Give the ratio, say whether it passes, and explain the designer's mistake.

**Question 2.** Rewrite "Swaps in red are urgent" so it passes 1.4.1, and name the level of 1.4.1.

**Question 3.** Your capstone stakeholder is the township library. They ask, "Do we legally have to make
this accessible, and by when?" Write the two or three sentences you would say, as a student developer
who is not a lawyer.

---

### Answers

**1.** 2.23:1. It fails. WCAG's large text is at least 18 point, or 14 point **bold**. A typical 16-pixel
bold button label is 12 point bold, which is not large, so the requirement is 4.5:1. Even the large text
threshold of 3:1 would not be met at 2.23:1.

**2.** Many answers work. For example: each swap carries the word "Urgent" or "Not urgent" in text, and
the sentence becomes "Each swap says how soon the shift starts." 1.4.1 Use of Color is Level A.

**3.** A strong answer: "The Department of Justice says the ADA applies to what state and local
governments offer on the web, and a township library is usually part of local government, which you can
confirm. The Department has published a rule naming WCAG 2.1 Level AA as the technical standard for
those governments. The compliance dates have changed since it was published, so I would check the
current dates on ADA.gov and ask your legal counsel rather than give you a date myself. I am building to
WCAG 2.2 Level AA, which covers what that standard asks for." Full credit needs three things: the purpose
of the law, a primary source, and no invented date or promise of legal compliance.
