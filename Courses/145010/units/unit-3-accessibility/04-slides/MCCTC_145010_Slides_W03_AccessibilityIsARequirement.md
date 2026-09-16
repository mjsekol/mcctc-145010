# Accessibility Is a Requirement
---
## Slide 1: She could not sign up
- A volunteer tried to join a pantry's shift list
- The page looked finished
- She uses a screen reader
- She gave up at the form
Speaker notes: This is the page you rebuild this week. The organization is invented, and the situation is one that happens constantly. Somebody built a page on a weekend, it looks clean, it works with a mouse, and a person who navigates differently hits a wall and leaves. Nobody finds out, because the person it failed does not file a bug report. They go somewhere else. This week is about finding that wall before she does.
Image: A clean volunteer sign-up page on a laptop, with a pair of headphones resting beside the keyboard, navy and light blue.
---
## Slide 2: Who navigates differently
- Screen readers: Narrator, NVDA, VoiceOver, TalkBack
- Keyboard only, switches, and voice control
- Zoom to 400 percent
- Colour vision that is not yours
- A cracked phone in sunlight
Speaker notes: Competency 2.7.4 asks you to know this list. Read it as people, not as technology. Every row is somebody who will use a page you build, as a customer, a volunteer, a student, or a coworker. The test you always run, a mouse and your own eyes on a good screen indoors, covers exactly one of these rows.
Image: Five simple icons in a row: headphones, keyboard, magnifying glass, an eye, a phone with a sun above it.
---
## Slide 3: It is a legal requirement
- ADA covers governments, schools, and businesses open to the public
- Justice Department: that includes what they offer online
- State and local rule names WCAG 2.1 Level AA
- Dates have changed. Look them up, never quote them
- Not legal advice. Know where the source is
Speaker notes: I am not a lawyer and this is not legal advice. Here is the purpose-level version. The Americans with Disabilities Act covers state and local governments, including public schools, and businesses open to the public. The Department of Justice says that includes their websites. For state and local governments it published a rule naming WCAG 2.1 Level AA as the technical standard. The compliance dates have already been changed since it came out, which is exactly why you never quote one from memory. The sources are in your notes, on ADA.gov.
Image: A simple document icon labelled ADA beside a web browser window, connected by an arrow.
---
## Slide 4: WCAG turns a value into a test
- W3C publishes it. This course uses version 2.2
- Four principles: Perceivable, Operable, Understandable, Robust
- Success criteria have a number, a name, a level
- Levels A, AA, AAA. We build to AA
Speaker notes: Accessible is a value. You cannot fail a value. WCAG turns it into testable statements, and that is why it matters to a developer. Every success criterion has a number, a name, and a level. When you write one in an audit this week, you write all three, from version 2.2, exactly as W3C publishes them. An invented criterion number is worth zero.
Image: A four-column diagram labelled P, O, U, R, each column with small numbered boxes underneath.
---
## Slide 5: A ratio you can calculate
```python
def ratio(text, background):
    lighter, darker = sorted([luminance(text), luminance(background)], reverse=True)
    return (lighter + 0.05) / (darker + 0.05)

print(f"{ratio('#a3a3a3', '#ffffff'):.2f}")   # 2.52
print(f"{ratio('#444444', '#ffffff'):.2f}")   # 9.74
```
Speaker notes: 1.4.3 Contrast Minimum asks for 4.5 to 1 for normal text and 3 to 1 for large text. That is not a matter of taste. It is arithmetic on the relative luminance of two colours, and the full function is in your notes. The light grey on the pantry page comes out at 2.52. It looks elegant. It fails.
Image: None. This slide is code.
---
## Slide 6: The tool measures it for you
```
node tools/web-check/check.js .../lab-w03-01-files/index.html --widths 360

  axe at 360px: 7 violation(s)
    color-contrast (serious, 3 node(s))  Elements must meet minimum
    color contrast ratio thresholds  e.g. .intro | .note | .btn
```
Speaker notes: Here is web-check on the page you rebuild. One rule, three elements. The grey paragraph, the red note, and the green button. Watch the red note especially. I am going to pick a red that looks strong enough to me, and we are going to find out.
Image: None. This slide is code.
---
## Slide 7: Watch me fix it by eye
- I darken the red note until it looks fine
- web-check still fails it: 3.96 to 1
- And the sentence says "fields in red are required"
- Fixing the shade fixes nothing a listener hears
Speaker notes: This is the deliberate failure. The red looks readable on this projector. The checker says 3.96 to 1, which is under 4.5. But the bigger problem is the sentence. It tells people to look for a colour. A screen reader user hears no colour at all. That is 1.4.1 Use of Color, and it is Level A, more basic than the contrast failure I was busy fixing.
Image: A red note beside a contrast readout showing 3.96:1 with a red fail marker.
---
## Slide 8: The tool cannot know what colour means
- Green rows are open, red rows are full
- A screen reader reads the words, never the colour
- web-check reported nothing about that table
- Fix it with words. Keep colour as a second cue
Speaker notes: This is the lesson you carry into every day this week. A tool can measure a contrast ratio. It cannot know that a pale green background means a shift has room. Only a person can see that the meaning lives in the colour. Put the meaning in text, a Status column that says Open or Full, and keep the colour if you like it.
Image: A shift table shown twice, in colour and in greyscale, where the greyscale version is impossible to read for status.
---
## Slide 9: Bias is usually a default
- Everyone uses a mouse
- Everyone reads English
- Everyone sees colour as I do
- Nobody questioned it, so nobody noticed
Speaker notes: Competencies 1.5.5 and 1.5.6 ask how bias affects who a product serves. On a web page it is rarely hostile. It is a default. The pantry page has a Spanish sentence for Spanish-speaking families, with no lang attribute, so a screen reader reads it with English pronunciation. A team with a Spanish reader on it catches that in seconds. The cost of missing it is a family that does not sign up, and nobody ever learns why.
Image: A Spanish sentence on a page with a speech bubble above it showing garbled English-style pronunciation.
---
## Slide 10: What you are about to build
- Build 1: swap board, Part 1, contrast and colour
- Measure every ratio before you change a colour
- Build 2: your access plan for the rebuild page
- Name one person who navigates differently from you
Speaker notes: Build 1 is the swap board lab, Part 1. Run web-check first, find the two things it reports, and then find the colour problem it does not. Every colour change comes with a measured ratio in your commit message. Build 2 is your access plan for the pantry page, the Define step of this week's project. The first line of that plan names a real kind of person who will use the page differently than you do.
Image: A split screen with a small ice cream shop page on the left and a one-page plan template on the right.
---
