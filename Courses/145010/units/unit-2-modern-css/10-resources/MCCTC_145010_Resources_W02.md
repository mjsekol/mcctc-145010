# Additional Resources · Week 2
## 145010 Web Design & Senior Capstone · Unit 2 · Modern CSS & Responsive Layout
### Topics: attaching CSS and the cascade, media in the flow, flexbox and grid, media and container queries

Every link below is marked **Confident** or **[VERIFY]**. **Confident** means the address returned
HTTP 200, with the page title you would expect, to a request from the build machine when this file
was built. That proves the page existed then. It does not prove the page still says the same thing.
A **[VERIFY]** link has not been confirmed. Click it before you rely on it, and tell your instructor
if it has moved.

**MDN moved its CSS pages.** Older addresses such as `.../docs/Web/CSS/float` now redirect to
`.../docs/Web/CSS/Reference/Properties/float`. This file lists the new addresses. If a tutorial
elsewhere gives you an old one, it will probably still land in the right place.

**Nothing here asks you to create an account, install anything, or use an AI service.** If a
resource asks for any of those, skip it and tell your instructor.

In-repository links are relative to this file and they all resolve. Reach for those first, because
they describe the exact pages you are building this week.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | MDN Learn: CSS styling basics, and CSS layout | All week | On-level | 30 min per section |
| 2 | web.dev Learn CSS: the cascade, flexbox, grid, container queries | Mon, Wed, Thu | On-level | 20 min each |
| 3 | MDN reference: the cascade, specificity, `:hover`, `:focus-visible` | Mon | On-level | 20 min |
| 4 | MDN reference: `max-width`, `float`, `display: flow-root`, `aspect-ratio` | Tue | On-level | 20 min |
| 5 | MDN reference: `video`, `track`, `audio`, `iframe`, and WebVTT | Tue | On-level | 25 min |
| 6 | MDN reference: flexbox, grid, `grid-template-areas` | Wed | On-level | 25 min |
| 7 | MDN reference: media queries, container queries, the viewport tag | Thu | On-level | 25 min |
| 8 | W3C WAI: captions, transcripts, contrast, focus, reflow | Mon, Tue, Thu | On-level | 25 min |
| 9 | Interactive practice: Flexbox Froggy and Grid Garden | Wed | Remediation | 30 min each |
| 10 | Browser support: checking it yourself | Thu | Extension | 15 min |
| 11 | Industry connection: checking a page at many widths | Thu, Fri | Extension | 20 min |
| 12 | A free video under 20 minutes | Any | Remediation | under 20 min |
| 13 | This week's four lecture notes and the demo pages | Any | Review | 20 min each |
| 14 | This week's labs, project, and checker | Any | On-level | as needed |
| 15 | Side quests SQ-21 and SQ-22 | Fri | Extension | 1 to 2 blocks |

---

## 1. Primary reading

**MDN Learn web development, CSS styling basics** ·
`https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics` · **Confident.**

**MDN Learn web development, CSS layout** ·
`https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout` · **Confident.**

**What it is.** Mozilla's free, maintained course on CSS. **Why this one.** It is current, free,
and needs no account. Its sections line up with this week one day at a time. Read the section for
the day you are on, not the whole module.

| Day | Section | Address | Status |
|---|---|---|---|
| Mon | Getting started with CSS | `.../Core/Styling_basics/Getting_started` | Confident |
| Mon | Handling conflicts | `.../Core/Styling_basics/Handling_conflicts` | Confident |
| Tue | Images, media, and form elements | `.../Core/Styling_basics/Images_media_forms` | Confident |
| Tue | HTML video and audio | `.../Core/Structuring_content/HTML_video_and_audio` | Confident |
| Tue | From object to iframe | `.../Core/Structuring_content/General_embedding_technologies` | Confident |
| Tue | Floats | `.../Core/CSS_layout/Floats` | Confident |
| Wed | Flexbox | `.../Core/CSS_layout/Flexbox` | Confident |
| Wed | Grids | `.../Core/CSS_layout/Grids` | Confident |
| Thu | Media queries | `.../Core/CSS_layout/Media_queries` | Confident |
| Thu | Responsive design | `.../Core/CSS_layout/Responsive_Design` | Confident |

Every address in the table starts with
`https://developer.mozilla.org/en-US/docs/Learn_web_development`.

**Read it with one question in your hand.** On Monday, in Handling conflicts, find the order the
browser uses to pick a winner. Then answer self-check question 1 in the Monday notes without looking
at the answer.

**Skip for now:** anything about CSS frameworks or preprocessors. This course writes plain CSS.

**Time.** About 30 minutes per section. **Level.** On-level.

---

## 2. A second explanation of the same ideas

**web.dev, Learn CSS** · Google's free CSS course · `https://web.dev/learn/css` · **Confident.**
Four modules, all **Confident**:

- The cascade: `https://web.dev/learn/css/the-cascade`
- Flexbox: `https://web.dev/learn/css/flexbox`
- Grid: `https://web.dev/learn/css/grid`
- Container queries: `https://web.dev/learn/css/container-queries`

**Why this one.** A different author explaining the same rules. If MDN's version did not land, this
one often does. The pages include small live examples you can edit in place.

**Read it with one question in your hand.** On Wednesday, in the grid module, find the part about
`auto-fit` and `minmax()`. Then do Wednesday's self-check question 2 by hand before you check it.

**Time.** 20 minutes each. **Level.** On-level.

---

## 3. Monday: which rule wins, and focus that matches hover

Why these: Monday's bug is a rule that is written correctly and still loses. These pages are the
rulebook for who wins.

- **Introduction to the CSS cascade** ·
  `https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction` · **Confident**
- **Specificity** ·
  `https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity` · **Confident**
- **`:hover`** ·
  `https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover` · **Confident**
- **`:focus-visible`** ·
  `https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-visible` · **Confident**
- **The `link` element**, for `rel="stylesheet"` and `href` ·
  `https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link` · **Confident**

**Assign a question, not the page:** *On the specificity page, how does the browser compare
`p.price` with `.price`? Which one wins, and does the order in the file matter here?*

**A second question worth five minutes:** *On the `:focus-visible` page, when does a browser show
focus for a mouse click and when does it not?* That is why Monday's hover rule and focus rule are
written together.

**Time.** 20 minutes. **Level.** On-level.

---

## 4. Tuesday: making outside things fit

Why these: Tuesday's first failure is an 800-pixel image on a 360-pixel phone. Each of these
properties is one line of the fix.

- **`max-width`** ·
  `https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width` · **Confident**
- **`float`** ·
  `https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float` · **Confident**
- **`display`**, which documents the `flow-root` value ·
  `https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display` · **Confident**
- **`aspect-ratio`** ·
  `https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio` · **Confident**

**Assign a question:** *On the `display` page, find `flow-root`. What does it make the element do
with floats inside it?* Then open the demo page and delete `flow-root` to watch the next heading
climb up beside the image.

**The failure to name before you hit it.** An iframe with a `height` attribute can ignore your
`aspect-ratio`. The `aspect-ratio` page explains when a ratio applies. Read that part before you
blame the property.

**Time.** 20 minutes. **Level.** On-level.

---

## 5. Tuesday: video, captions, audio, and embeds

Why these: a video that plays is not finished. It needs a fallback, captions, and a reason to trust
the file paths.

- **The `video` element** ·
  `https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video` · **Confident**
- **The `track` element** ·
  `https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/track` · **Confident**
- **The `audio` element** ·
  `https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio` · **Confident**
- **The `iframe` element** ·
  `https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe` · **Confident**
- **The WebVTT format** ·
  `https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API` · **Confident**

**Assign a question:** *On the `track` page, what do `kind`, `srclang`, `label`, and `default` each
do? Which one makes the captions show without the viewer turning them on?*

**On the `iframe` page,** read the `title` attribute and the `allow` attribute. Your project map has
a `title` and no `allow`, and you should be able to say why.

**Remember the trap.** Chrome on the build machine refused to load a `.vtt` file from a page opened
by double-clicking. Serve the folder with `python -m http.server 8000`, then stop the server with
Ctrl+C when you are done.

**Time.** 25 minutes. **Level.** On-level.

---

## 6. Wednesday: flexbox and grid

Why these: Wednesday's rule is that the parent decides where the children go. These pages describe
exactly what each parent can decide.

- **Basic concepts of flexbox** ·
  `https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts` ·
  **Confident**
- **Basic concepts of grid layout** ·
  `https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Basic_concepts` · **Confident**
- **`grid-template-areas`** ·
  `https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas` ·
  **Confident**

**Assign a question:** *On the flexbox page, what is the main axis and what is the cross axis? Which
one does `justify-content` work on?* Most flexbox confusion is an axis mix-up.

**On the `grid-template-areas` page,** find what happens when the area names do not form a
rectangle. That mistake makes the whole declaration invalid, and the browser drops it. Nothing
appears on the page or in the Console. Look for the struck-through declaration in the Styles pane.

**Time.** 25 minutes. **Level.** On-level.

---

## 7. Thursday: ask the screen, or ask the box

Why these: Thursday's page has to work on a phone, a tablet, and a laptop. These pages explain the
three tools that make that true.

- **Using media queries** ·
  `https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using` · **Confident**
- **CSS container queries** ·
  `https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries` ·
  **Confident**
- **The viewport meta tag** ·
  `https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport` ·
  **Confident**

**Assign a question:** *On the container queries page, what must be true of the parent before an
`@container` rule can match?* A container query with no container is Thursday's quietest bug.

**Responsive tables** have no single MDN page. The approach in Thursday's notes, a named, focusable
box that scrolls on its own, is the one to follow. The table sections of MDN Learn you read in
Week 1 still apply to the table itself.

**Time.** 25 minutes. **Level.** On-level.

---

## 8. The accessibility connection

Why these: Tuesday's uncaptioned video and Monday's missing focus style both pass `web-check`. The
W3C Web Accessibility Initiative explains who those pages fail. Week 3 starts here.

- **Making audio and video media accessible** · `https://www.w3.org/WAI/media/av/` · **Confident**
- **Captions and subtitles** · `https://www.w3.org/WAI/media/av/captions/` · **Confident**
- **Transcripts** · `https://www.w3.org/WAI/media/av/transcripts/` · **Confident**
- **Understanding Captions (Prerecorded)** ·
  `https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html` · **Confident**
- **Understanding Contrast (Minimum)** ·
  `https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html` · **Confident**
- **Understanding Focus Visible** ·
  `https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html` · **Confident**
- **Understanding Reflow** ·
  `https://www.w3.org/WAI/WCAG22/Understanding/reflow.html` · **Confident**

**Assign a question:** *On the captions page, who uses captions besides people who are deaf or hard
of hearing?* Then think about the last video you watched on a bus with the sound off.

**For contrast ratios in your comments,** the WebAIM Contrast Checker,
`https://webaim.org/resources/contrastchecker/` · **Confident**, takes two colors and gives a
ratio. Nothing you type there is personal.

**This file makes no claim about what any law requires.** These pages describe guidelines. Week 3
covers what they are used for.

**Time.** 25 minutes. **Level.** On-level.

---

## 9. Interactive practice

**Flexbox Froggy** · `https://flexboxfroggy.com/` · **Confident.**
**Grid Garden** · `https://cssgridgarden.com/` · **Confident.**

**What they are.** Two free browser games. Each level asks for one or two CSS declarations to move
things into place. **Why these.** They drill the property names until your fingers know them, which
is what a Gate 1 rep asks for. When the build machine loaded them, neither front page asked for a
sign-in. **The pages appear to carry ad code**, so expect ads. If either one ever asks you to create
an account, stop and use the no-account option below.

**The no-account option.** Open `index.html` in
[the Wednesday demo folder](../03-lecture-notes/examples/wed-layout/) and change one property at a
time in DevTools. Predict the result before you press Enter.

**Level.** Remediation for anyone who froze on Wednesday's Gate 1 rep. Stop when the levels start
feeling slow. That means you have it.

**Time.** About 30 minutes each.

---

## 10. Browser support: check it yourself

**Container queries were verified only in Chrome 153 on the build machine.** Firefox, Safari, and
older versions of Chrome were not tested. That is why every container query in this unit sits on a
base that works without it.

**Two places to check current support:**

- **Can I use, CSS Container Queries (Size)** · `https://caniuse.com/css-container-queries` ·
  **Confident** that the page loaded. **[VERIFY]** what it says today, because support tables change.
- **The Browser compatibility table** at the bottom of each MDN reference page in section 7.

**Read it with one question in your hand:** *which browser versions on this table would show your
stacked base card instead of the container query layout?* Then write one sentence about it in your
decision log. This file quotes no support numbers, because they go stale.

**Time.** 15 minutes. **Level.** Extension.

---

## 11. Industry connection: checking a page at many widths

**Chrome DevTools, Simulate mobile devices with device mode** ·
`https://developer.chrome.com/docs/devtools/device-mode` · **Confident.**

**Chrome DevTools, the grid and flexbox inspectors** · both **Confident**:

- `https://developer.chrome.com/docs/devtools/css/grid`
- `https://developer.chrome.com/docs/devtools/css/flexbox`

**What it is.** Google's documentation for the tools you used all week: the device toolbar, the
grid overlay, and the flex overlay. **Why this one.** Web teams check a page at more than one width
before they ship it. Device mode is one common way to do that. `web-check` with
`--widths 360,768,1280 --shots` is an automated way. Friday's seven-step briefing combines both.

**Read the limits section of the device mode page.** It says what emulation cannot tell you. That is
the same lesson as Thursday's viewport demo, where the build machine's emulation and a real phone
might not agree.

**The argument to be able to make both ways.** One side: automated screenshots at fixed widths catch
regressions every time and never get tired. The other: the bug is often at a width nobody picked,
like 600, and only a person dragging the edge finds it. Both are real positions. Your decision log
should say which checks you trust for your page, and why.

**Going further, [VERIFY].** Many design systems now describe components that adapt to their
container instead of the screen. Search for **design system container queries** and read one
article from a team that names its own components. Check the date on it and check that it does not
depend on a framework. No specific article is linked here.

**Time.** 20 minutes. **Level.** Extension.

---

## 12. A free video

**[VERIFY].** No specific video is named here, because a title and a channel that turn out to be
wrong cost more than no link at all.

**What to search for.** Search for a video under 20 minutes on **CSS grid template areas**,
**flexbox basics**, or **mobile first media queries**.

**How to pick one.** Watch the first two minutes before you rely on it, and check five things:

1. It is under 20 minutes.
2. It was published recently enough to use flexbox and grid for layout, not floats. A video that
   builds page columns with floats is out of date.
3. It uses plain CSS. Skip anything built on Tailwind, Bootstrap, or another framework.
4. It writes real CSS on screen and shows the result in a browser.
5. It does not ask you to install anything, sign up, or buy a course.

The **Chrome for Developers** channel, `https://www.youtube.com/@ChromeDevs`, returned HTTP 200
from the build machine and publishes free material on CSS and DevTools. Search its uploads for
container queries or the grid inspector. **[VERIFY]** any specific video before you use it.

**Time.** Under 20 minutes. **Level.** Remediation.

---

## 13. This week's lecture notes and demo pages

Four concepts, four files. Each ends with three self-check questions and worked answers.

| Day | Notes | Demo folder |
|---|---|---|
| Monday | [Attaching CSS and the cascade](../03-lecture-notes/MCCTC_145010_Notes_AttachingCSSAndTheCascade.md) | [mon-cascade](../03-lecture-notes/examples/mon-cascade/) |
| Tuesday | [Media in the flow](../03-lecture-notes/MCCTC_145010_Notes_MediaInTheFlow.md) | [tue-media](../03-lecture-notes/examples/tue-media/) |
| Wednesday | [Flexbox and grid](../03-lecture-notes/MCCTC_145010_Notes_FlexboxAndGrid.md) | [wed-layout](../03-lecture-notes/examples/wed-layout/) |
| Thursday | [Media queries and container queries](../03-lecture-notes/MCCTC_145010_Notes_MediaAndContainerQueries.md) | [thu-queries](../03-lecture-notes/examples/thu-queries/) |

All demo pages sit in [the examples folder](../03-lecture-notes/examples/). Each day's folder has a
working page and at least one broken one. **Open the broken one first and find the problem before
you read the notes.**

**You should be able to answer all twelve self-check questions without reading the answers.** The two
that matter most for the project are Tuesday's question 3, what PASS does not tell you about a
video, and Thursday's question 3, the phone that shows a tiny desktop page.

**Time.** 20 minutes each. **Level.** Review.

---

## 14. This week's labs, project, and checker

All **Confident**, all in this repository.

- [Lab W02-01, Style It From Outside](../05-labs/MCCTC_145010_Lab_W02-01_StyleItFromOutside.md),
  Monday and Tuesday
- [Lab W02-02, Three Widths](../05-labs/MCCTC_145010_Lab_W02-02_ThreeWidths.md), Wednesday and
  Thursday
- [Project, The League Goes Mobile](../09-project/MCCTC_145010_Project_W02_LeagueGoesMobile.md),
  all week, due Friday
- [The web-check README](../../../../../tools/web-check/README.md), for setup and the `--widths` and
  `--shots` options

**Why this matters.** When `web-check` fails on your machine and not your neighbor's, the README is
the first stop. It is faster than guessing.

**Time.** As needed. **Level.** On-level.

---

## 15. Side quests

From the [Side Quest Catalog](../../../../Misc/MCCTC_Side_Quest_Catalog_2026-2027.md), graded under
BPA / Credential / Capstone:

**SQ-21 · The Accessibility Pass** · one to two blocks · ★★. Take your league page and use it with
only the keyboard, then with a screen reader and your eyes closed. This week you wrote a focus style
and added captions, so this quest tests whether those work for a real user. Windows Narrator is built
into the lab machines. It also sets up Week 3.

**SQ-22 · Make It Load in Under a Second** · one block · ★★. Measure your page's load time, then
cut it without removing features. This week you added a photo, a video in two formats, and an
embedded map, so you now have real weight to measure and a reason to ask why the clip ships twice.

**Time.** One to two blocks. **Level.** Extension.

---

## For the student who is behind

1. The Monday notes, worked example 1, with `mon-cascade/index.html` open and the Styles pane beside it
2. MDN's Handling conflicts, then Flexbox
3. Flexbox Froggy, then Grid Garden, or the no-account option in section 9
4. `web-check` on your own page after every single change, reading only the line that changed

## For the student who is ahead

- The browser support check in section 10, and a decision log entry about it
- The industry connection in section 11, with a position taken on fixed-width checks
- The WAI Reflow page, then drag your page to 320 pixels and see what breaks
- SQ-21 on your league page, then SQ-22

---

## If a link is dead

Tell your instructor which link and which section of this file it was in. Then use the lecture notes
in section 13. They cover everything this week assesses, and they do not depend on any outside site.
