# Additional Resources · Week 1
## 145010 Web Design & Senior Capstone · Unit 1 · Semantic HTML & the Browser
### Topics: how a document becomes a page, landmarks and headings, links and paths, data tables

Every link below is marked **Confident** or **[VERIFY]**. **Confident** means the address
returned HTTP 200 to a request from the build machine while this file was written. That proves
the page existed then, not that it still says the same thing. A **[VERIFY]** link has not been
confirmed. Click it before you rely on it, and tell your instructor if it has moved.

**Nothing here asks you to create an account, install anything, or use an AI service.** If a
resource asks for any of those, skip it.

In-repository links are relative to this file and they all resolve.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | MDN Learn: Structuring content with HTML | All week | On-level | 30 min per section |
| 2 | web.dev Learn HTML: semantic HTML, links, tables | Tue, Wed, Thu | On-level | 20 min each |
| 3 | MDN: How the web works, and What is a web server | Mon | Remediation | 15 min each |
| 4 | The HTML standard: the parsing chapter | Mon | Extension | 30 min |
| 5 | MDN element reference | Any | On-level | as needed |
| 6 | W3C WAI tutorials: page structure, and tables | Tue, Thu | On-level | 25 min each |
| 7 | Chrome DevTools: accessibility features reference | Tue, Thu | On-level | 15 min |
| 8 | Interactive practice: the W3C validator, and this week's two checkers | Any | On-level | 20 min |
| 9 | A free video under 20 minutes | Any | Remediation | under 20 min |
| 10 | Industry connection: the WebAIM Million | Tue | Extension | 20 min |
| 11 | This week's four lecture notes | Any | Review | 20 min each |
| 12 | Side quests SQ-21 and SQ-22 | Fri | Extension | 1 to 2 blocks |

---

## 1. Primary reading

**MDN Learn web development, Structuring content with HTML** ·
`https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content` ·
**Confident.**

**What it is.** Mozilla's free, maintained course on HTML. It starts from zero, so skim what you
already know. **Why this one.** It is current, it is free with no account, and its sections map onto
this week one to one. Read the section for the day you are on, not the whole module.

| Day | Section | Address | Status |
|---|---|---|---|
| Tue | Headings and paragraphs | `.../Structuring_content/Headings_and_paragraphs` | Confident |
| Tue | Lists | `.../Structuring_content/Lists` | Confident |
| Tue | Structuring documents | `.../Structuring_content/Structuring_documents` | Confident |
| Wed | Creating links | `.../Structuring_content/Creating_links` | Confident |
| Thu | HTML table basics | `.../Structuring_content/HTML_table_basics` | Confident |

**Read it with one question in your hand:** on Wednesday, find where the page explains what a
path starting with `..` means, and check it against Worked example 1 in the Links and Paths notes.

**Time.** About 30 minutes per section. **Level.** On-level.

---

## 2. A second explanation of the same ideas

**web.dev, Learn HTML** · Google's free HTML course. **Confident** for all three pages:

- Semantic HTML: `https://web.dev/learn/html/semantic-html`
- Links: `https://web.dev/learn/html/links`
- Tables: `https://web.dev/learn/html/tables`

**Why this one.** A different author explaining the same element choices. If MDN's version did not
land, this one often does. Read the semantic HTML page on Tuesday with the div soup example from
the notes open beside it.

**Time.** 20 minutes each. **Level.** On-level.

---

## 3. Where a page comes from

**MDN, How the web works** ·
`https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works`
· **Confident.**

**MDN, What is a web server?** ·
`https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server`
· **Confident.**

**Why these.** Monday's second half, static and dynamic sites, in plain language. The web server
page describes the difference between a server that sends stored files and one that builds pages.

**Assign a question, not the page:** *In your own words, what does a dynamic server do that a
static one does not, and what does that cost?* Then compare your answer with Monday's self-check
question 3.

**Time.** 15 minutes each. **Level.** Remediation.

---

## 4. The rules the browser follows

**The WHATWG HTML Living Standard, parsing HTML documents** ·
`https://html.spec.whatwg.org/multipage/parsing.html` · **Confident.**

**Why this one.** This is the actual rulebook for Monday's lesson: exactly what a browser builds
from broken markup. It is long and precise, and nobody reads it front to back. It is the page to
open for Lab W01-01's EXTENDED option: search it for the algorithm that handles misnested
formatting elements.

**Time.** 30 minutes, searching, not reading. **Level.** Extension.

---

## 5. The element reference

**MDN, HTML elements reference** ·
`https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements` · **Confident.**

Two pages you will open this week, both **Confident**:

- The `a` element: `https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a`, for
  `href`, `download`, and `mailto:`
- The `th` element: `https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th`,
  for `scope` and `headers`

**Why this one.** When you are not sure whether an element or attribute exists, this is where you
check, instead of asking a model that may invent one.

**Time.** As needed. **Level.** On-level.

---

## 6. Structure for people who do not see the page

**W3C Web Accessibility Initiative, Page Structure tutorial** ·
`https://www.w3.org/WAI/tutorials/page-structure/` · **Confident.**

**W3C Web Accessibility Initiative, Tables tutorial** ·
`https://www.w3.org/WAI/tutorials/tables/` · **Confident.** Its page on tables with multi-level
headers, `https://www.w3.org/WAI/tutorials/tables/multi-level/`, is also **Confident** and is the
one Lab W01-02's EXTENDED option needs.

**Why these.** They come from the group that writes the accessibility guidelines, and they show
the markup and explain who it helps. Week 3 leans on the same site.

**Time.** 25 minutes each. **Level.** On-level.

---

## 7. The Accessibility tab in Chrome

**Chrome DevTools, Accessibility features reference** ·
`https://developer.chrome.com/docs/devtools/accessibility/reference` · **Confident.**

**Why this one.** It documents the Accessibility tab in the Elements panel and the
**Show accessibility tree** toggle that Lab W01-01 step 17 uses. Read the section on the
Accessibility tab, then select a table in your own lab and read its role.

**Time.** 15 minutes. **Level.** On-level.

---

## 8. Interactive practice

**The W3C Nu HTML Checker** · `https://validator.w3.org/nu/` · **Confident.** Paste a page, get a
list of problems. It is a different validator from the one inside `web-check`, so expect different
wording, and possibly different findings. When they disagree, write down both messages and ask. **Do
not paste anything with personal information into any online tool.**

**This week's own checkers**, which need no internet:

- [structure_check.py](../05-labs/structure-check/structure_check.py), for headings, landmarks,
  generic boxes, dead links, and tables
- `tools/web-check/check.js`, from the repository root, for validation, the accessibility audit,
  and overflow at three widths. Setup and options are in
  [tools/web-check/README.md](../../../../../tools/web-check/README.md).

**The practice that teaches the most:** break a working page on purpose, one mistake at a time,
and predict what each checker will say before you run it. A heading skip, a fragment typo, a `td`
where a `th` belongs. Keep a list of which checker caught which mistake.

**Time.** 20 minutes. **Level.** On-level.

---

## 9. A free video

**[VERIFY].** No specific video is named here, because a title and a channel that turn out to be
wrong cost more than no link at all.

**What to search for, and how to pick one.** Search for a video under 20 minutes on **semantic
HTML** or **HTML landmarks and headings**. Watch the first two minutes before you assign it, and
use three tests:

1. It writes real markup on screen, not only slides
2. It shows the result in a browser's developer tools or with a screen reader
3. It does not ask you to install anything, sign up, or buy a course

The **Chrome for Developers** channel, `https://www.youtube.com/@ChromeDevs`, returned HTTP 200
from the build machine and publishes free DevTools material. Search its uploads for accessibility
tree videos, and check the runtime before you assign one. **[VERIFY]** any specific video.

**Time.** Under 20 minutes. **Level.** Remediation.

---

## 10. Industry connection

**WebAIM, The WebAIM Million** · `https://webaim.org/projects/million/` · **Confident.**

**What it is.** WebAIM, an accessibility organization, runs an automated check across a very
large set of popular home pages and publishes what it finds. **Why this one.** It is the
closest thing to a census of whether real, professionally built pages do what you practiced this
week. Read the list of the most common problems and count how many of them this week's checkers
would catch.

**Read the numbers in the current report yourself.** This file quotes none of them, because the
report is updated and any number copied here would go stale.

**The argument to be able to make both ways.** One side: automated checks miss so much that a
report built on them understates the problem. The other: a problem an automated check can find
in seconds, left on a professional home page, says something about how pages get built. Both are
real positions. Write down which one the report persuaded you of, and why.

**Also useful:** WebAIM's article on semantic structure,
`https://webaim.org/techniques/semanticstructure/` · **Confident.**

**Time.** 20 minutes. **Level.** Extension.

---

## 11. This week's lecture notes

| Day | Notes |
|---|---|
| Monday | [How a document becomes a page](../03-lecture-notes/MCCTC_145010_Notes_HowADocumentBecomesAPage.md) |
| Tuesday | [Landmarks, headings, and lists](../03-lecture-notes/MCCTC_145010_Notes_LandmarksHeadingsAndLists.md) |
| Wednesday | [Links and paths](../03-lecture-notes/MCCTC_145010_Notes_LinksAndPaths.md) |
| Thursday | [Data tables, and choosing how to present data](../03-lecture-notes/MCCTC_145010_Notes_DataTablesAndPresentation.md) |

**You should be able to answer all twelve self-check questions without reading the answers.** The
two that matter most for the project are Wednesday's question 1, relative paths from a nested
folder, and Tuesday's question 1, why `web-check` passes a page with no headings.

**Time.** 20 minutes each. **Level.** Review.

---

## 12. Side quests

From the [Side Quest Catalog](../../../../Misc/MCCTC_Side_Quest_Catalog_2026-2027.md), graded under
BPA / Credential / Capstone:

**SQ-21 · The Accessibility Pass** · one to two blocks · ★★. Take a page you built in an earlier
course, navigate it with only the keyboard, then with a screen reader and your eyes closed. This
week's structure work is what makes that possible. Windows Narrator is built into the lab
machines.

**SQ-22 · Make It Load in Under a Second** · one block · ★★. Measure a page's load time, then cut it
without removing features. Gate 2 W01's oversized banner is the kind of thing you will find.

---

## For the student who is behind

1. The Monday lecture notes, worked example 1, with the file open in Chrome and Elements beside it
2. MDN's Headings and paragraphs, then Lists
3. `structure_check` on your own lab page after every single change, reading only the line that
   changed
4. The web.dev Links page, with the folder tree from Gate 1 Rep 02 drawn on paper

## For the student who is ahead

- The parsing chapter of the HTML standard, and Lab W01-01 EXTENDED
- The W3C multi-level tables tutorial, and Lab W01-02 EXTENDED
- The WebAIM Million, and a decision log entry taking a position on what automated checks miss
- SQ-21 on your Flask CRUD app from 145065
