# Additional Resources · Week 6
## 145010 Web Design & Senior Capstone · Unit 6 · Publishing, Standards & Measurement
### Topics: templates and content management, site structure, privacy-respecting measurement, web standards and validation, cross-browser testing, publishing, search fundamentals, your editor

Every link below is marked **Confident** or **[VERIFY]**. A **[VERIFY]** link has not been confirmed
live, or its exact path may have moved. Click it before you rely on it, and tell your instructor if
it has moved.

**Nothing here requires a commercial AI API, an AI account, or a key.** Every tool you need this week
runs on the lab machine. If a resource tells you to sign up for something to follow along, stop and
ask your instructor first.

**No framework this week.** The Ohio standards for this course are plain HTML, CSS, and client-side
script. React and Vue are side-quest material only. If a tutorial starts with `npm create`, it is
teaching a different course.

**About third-party analytics.** Your counter stores a page address, a day, and a yes or a no. Many
third-party analytics services collect more than that. What any one service collects, what it costs,
and who it allows to sign up change over time, and none of it was checked for this course. **Any
third-party analytics option is verified by your instructor before anyone uses it.** Do not add a
tracking snippet to your site on your own.

**About hosting services.** The same rule applies to Cloudflare Pages and Render. Their sign-up
terms, age rules, payment requirements, and limits were not verified for this course. Your
instructor checks them before this week and tells you which route you use. The lab route on your own
machine needs none of that.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | The in-repository tools, first stop | Every day | On-level | 10 min |
| 2 | This week's four lecture notes | Every day | Review | 20 min each |
| 3 | Primary reading: MDN's guide to publishing a site, and its cross-browser testing module | Wed, Thu | On-level | 45 min |
| 4 | Official: the WHATWG HTML Living Standard, parsing section | Wed | Extension | 30 min |
| 5 | Interactive practice: the W3C Markup Validation Service | Wed | On-level | 25 min |
| 6 | Official: Python `http.server` | Tue, Thu | On-level | 20 min |
| 7 | Official: the sitemap protocol and the robots.txt standard | Thu | On-level | 25 min |
| 8 | Official: search engine guidance on titles, descriptions, and robots.txt | Thu | On-level | 30 min |
| 9 | Official: VS Code documentation | Wed | Remediation | 20 min |
| 10 | Official: MDN on the `<title>` and `<meta>` elements | Mon, Thu | Remediation | 15 min |
| 11 | A free video under 20 minutes | Any | Remediation | under 20 min |
| 12 | Industry connection: measurement without tracking | Tue, Fri | Extension | 25 min |
| 13 | Side quest: map every repair the browser made | Any | Extension | 1 block |

---

## 1. The in-repository tools, first stop

**Reach for these before any website.** They describe the exact system you are building, and every
one of them runs on the lab machine with nothing installed beyond Python and Node.

| Tool | Where | What it tells you |
|---|---|---|
| `build.py` | [lab-w06-01-files/sitekit/build.py](../05-labs/lab-w06-01-files/sitekit/build.py) | joins the template and your content into `site/`, and warns about anything missing |
| `serve.py` | [lab-w06-02-files/serve.py](../05-labs/lab-w06-02-files/serve.py) | serves your site on the port you give it and counts page loads without recording who loaded them |
| `report.py` | [lab-w06-02-files/report.py](../05-labs/lab-w06-02-files/report.py) | turns the counts into a traffic report, and says what the numbers cannot tell you |
| `test_counter.py` | [lab-w06-02-files/test_counter.py](../05-labs/lab-w06-02-files/test_counter.py) | tests the counter with the standard library, so it needs nothing installed |
| `check_site.py` | [lab-w06-03-files/check_site.py](../05-labs/lab-w06-03-files/check_site.py) | requests every address the way a visitor and a crawler would, and prints `PROBLEM` lines |
| web-check | `node tools/web-check/check.js <page.html>`, run from the repository root | validates the HTML and runs an automated accessibility audit at several widths |

**Why first.** A tutorial describes somebody else's setup. These tools describe yours. When the
checker and a tutorial disagree, the checker is the one your grade is measured against.

**One thing web-check does not do.** It checks the file you wrote in one browser engine. It does not
tell you what Firefox or Safari does with it. That is why Wednesday's matrix is done by hand.

**Time.** 10 minutes to read the top of each file. **Level.** On-level.

---

## 2. This week's lecture notes

| Day | Notes |
|---|---|
| Week 6 Mon | [One Template, Many Pages](../03-lecture-notes/MCCTC_145010_Notes_OneTemplateManyPages.md) |
| Week 6 Tue | [Measure a Question, Not a Person](../03-lecture-notes/MCCTC_145010_Notes_MeasureAQuestionNotAPerson.md) |
| Week 6 Wed | [The Browser Forgives](../03-lecture-notes/MCCTC_145010_Notes_TheBrowserForgives.md) |
| Week 6 Thu | [Live and Findable](../03-lecture-notes/MCCTC_145010_Notes_LiveAndFindable.md) |

**Why these.** Friday's exam covers Weeks 1 through 6, and Strand 6 is more than half of the WebXam
in Week 16. Each note ends with self-check questions. Answer them on paper before you read the
answers. Agreeing with an answer you already read teaches you almost nothing.

**Time.** 20 minutes each. **Level.** Review.

---

## 3. Primary reading

**MDN Web Docs, Learn web development** · `https://developer.mozilla.org/en-US/docs/Learn_web_development`
· **Confident** for MDN itself at `https://developer.mozilla.org/`. **[VERIFY]** the exact path of the
Learn area, because pages in it have moved before.

Read two parts of it:

- **The page on publishing your website**, in the getting-started section · **[VERIFY]** the path.
  It walks through what it means to put files at a public address and names several ways to do it.
- **The cross-browser testing module** · **[VERIFY]** the path. Read the introduction and the part on
  testing strategies. Skip anything about automated testing services that need an account.

**Why this one.** MDN is free, maintained by Mozilla with community contributors, and this part
of it has no framework in it. The cross-browser module says in plain words what Wednesday's lesson is about: you
cannot test in every browser, so you choose which ones on purpose and you write down what you did
not test.

**Read it with one question in your hand:** which of the browsers on this lab machine share an
engine? Two browsers on the same engine are one test, not two.

**Time.** 45 minutes. **Level.** On-level.

---

## 4. The HTML standard, parsing section

**WHATWG HTML Living Standard** · `https://html.spec.whatwg.org/` · **Confident.**
The parsing section · `https://html.spec.whatwg.org/multipage/parsing.html` · **Confident.**

**Why this one.** Wednesday's lesson says the standard describes how a browser repairs broken markup.
This is the section where it does that. It is long and dense, and you do not read all of it. You read
enough to see that "the browser fixed it" is not luck. It is a written rule, which is why Chrome and
Firefox built the same tree from `club.html`.

**What to look for.** Search the page for "parse error". Notice how often the standard says what to
do next after one. That is the forgiving part.

**Time.** 30 minutes, skimming. **Level.** Extension.

---

## 5. Interactive practice: the validator

**W3C Markup Validation Service** · `https://validator.w3.org/` · **Confident.**
The Nu HTML Checker behind it · `https://validator.w3.org/nu/` · **Confident.**
The CSS validator · `https://jigsaw.w3.org/css-validator/` · **Confident.**

**Why this one.** It is run by the W3C, which publishes many web standards. It needs no account,
and you can paste markup straight into it. Use it to compare against web-check. When both report the same
error in different words, you have learned the error twice.

**The practice that teaches the most.** Take a copy of
[club.html](../05-labs/lab-w06-03-files/looks-fine/club.html) and paste it in by text input. Before
you press the button, write down how many errors you expect. Then compare. Then open the same page in
Chrome, open DevTools, and find each error's repair in the Elements panel.

**Paste only markup you wrote or were given for class.** Never paste a page that contains anyone's
personal details.

**Time.** 25 minutes. **Level.** On-level.

---

## 6. Python's `http.server`

`https://docs.python.org/3/library/http.server.html` · **Confident.**

**Why this one.** Tuesday's server is built on this module. Two things on this page matter this
week. First, find the method that writes the log line, and read what it records. That is the line
you replace in step 2 of Lab W06-02. Second, read the warning near the top of the page about using
this module in production.

**Assign yourself a question:** *which method would you override to change what the server writes
about each request?* Then check your answer against your own `serve.py`.

**Time.** 20 minutes. **Level.** On-level.

---

## 7. The two files at the root of your site

**The sitemap protocol** · `https://www.sitemaps.org/protocol.html` · **Confident.**
**RFC 9309, the Robots Exclusion Protocol** · `https://www.rfc-editor.org/rfc/rfc9309` · **Confident.**

**Why these.** They are the actual definitions of `sitemap.xml` and `robots.txt`, and both are
short. The sitemap page shows every tag and which ones are required. The RFC says how a crawler reads
`Allow` and `Disallow` lines. Find how its grammar treats text after a `#`. That is Thursday's
deliberate failure.

**Assign yourself a question:** *a sitemap lists addresses on a different site from the one it lives
on. Does the protocol page say anything about that?* Thursday's exit ticket asks the same thing.

**Time.** 25 minutes. **Level.** On-level.

---

## 8. What a search engine says about titles, descriptions, and robots.txt

**Google Search Central documentation** · `https://developers.google.com/search/docs` · **[VERIFY]**
the path.

Two pages to look for inside it:

- **The SEO starter guide** · `https://developers.google.com/search/docs/fundamentals/seo-starter-guide`
  · **[VERIFY]**
- **The introduction to robots.txt** · `https://developers.google.com/search/docs/crawling-indexing/robots/intro`
  · **[VERIFY]**

**Why this one.** It is one search company describing its own crawler, which makes it a primary
source for that crawler and nothing more. Read what it says about page titles, meta descriptions,
headings, and link text. Then compare it with what Thursday's note says: each address describes
itself honestly, and nobody can promise a ranking.

**Read it critically.** Other search engines publish their own guidance, and a claim about one
crawler is not a claim about all of them. If a page on any site promises a ranking, treat that as a
red flag.

**Time.** 30 minutes. **Level.** On-level.

---

## 9. Your editor

**VS Code documentation** · `https://code.visualstudio.com/docs` · **Confident.**

**Why this one.** Wednesday spends five minutes on the editor: the Problems panel, format on save, and
a validator in the editor. The documentation has a page for each. Search the docs for "Problems
panel" and for "format on save".

**Before you install an extension**, check with your instructor. Some extensions send data off the
machine, and an extension that adds AI completion is not allowed during a Gate 1 rep.

**Time.** 20 minutes. **Level.** Remediation.

---

## 10. The elements that describe a page

**MDN reference for `<title>`** and **for `<meta>`** · both under
`https://developer.mozilla.org/en-US/docs/Web/HTML/` · **[VERIFY]** the exact paths. Search MDN for
"title element" and "meta element".

**Why these.** Monday's template puts `{{title}}` and `{{description}}` into these two elements on
every page. Thursday explains why a person reading a list of search results sees them first. If you
are unsure which attribute of `<meta>` holds the description, these two pages settle it.

**Time.** 15 minutes. **Level.** Remediation.

---

## 11. A free video

**[VERIFY].** No specific video is named here, because a title and a channel that are wrong cost
more than no link at all.

**What to search for.** A video under 20 minutes on one of these: **"how browsers parse HTML"**,
**"HTML validation"**, or **"what is a static site generator"**. Watch the first two minutes before
you rely on it, and use three tests:

1. It shows real markup or a real terminal on screen, not only slides
2. It uses no framework, and it does not start by installing one
3. It does not ask you to sign up for anything or add a tracking script

**Time.** Under 20 minutes. **Level.** Remediation.

---

## 12. Industry connection: measurement without tracking

**[VERIFY].** No article is linked here. This topic changes fast, and a named article would be out of
date or wrong about a vendor by the time you read it.

**What to look for.** Search for current writing on **privacy-friendly analytics**, **cookieless
analytics**, or **first-party analytics**. Look for a piece written by a team that describes what it
chose to collect and what it chose not to collect, and why. Check the date on the piece and who
published it before you trust it.

**Read it against what you built.** Your counter stores a page, a day, and a yes or a no. For any
service the article describes, write down three things: what it collects, what question that answers,
and whether your counter already answers the same question with less. **Do not take a vendor's
description of its own product as fact.** Write "the vendor says" in your notes.

**The argument to be able to make both ways.** One side: collecting more lets a team answer questions
it did not think of in advance, and sometimes those questions matter. The other side: data you do
not collect cannot leak, cannot be misused, and never has to be explained to a visitor, and your
visitors this week are your classmates. Both are real positions. Your `measurement-plan.md` should
say which one you took and why.

**Time.** 25 minutes. **Level.** Extension.

---

## 13. Side quest: map every repair the browser made

**Why it fits this week.** Wednesday shows that Chrome and Firefox rebuilt `club.html` into the same
tree. This quest asks why, in the standard's own words.

**What you do.**

1. Open [club.html](../05-labs/lab-w06-03-files/looks-fine/club.html) in Chrome with DevTools open.
2. For every validation error web-check reports, find what the browser built in the Elements panel.
3. For each one, find the part of the parsing section in resource 4 that describes that repair.
   Write the section heading next to it.
4. Write a table with four columns: the error, what you wrote, what the browser built, and the
   standard's section.
5. End with one paragraph: which repair would you most likely miss by looking at the page, and why.

**Done looks like:** one row per reported error, every row with a section heading, and the paragraph.
Commit it as `browser-repairs.md`.

**If you want more after that:** add a `lastmod` date for each page to your sitemap, generated by
`build.py` rather than typed by hand, and check it against the sitemap protocol page in resource 7.

**About frameworks.** A student who wants to see how React or Vue handles a template may explore it
in Period 8 as a side quest, after the week's work is committed. Nothing in this course's labs or
exam uses one.

**Time.** One block. **Level.** Extension.

---

## For the student who is behind

1. Your lecture notes, with the self-check questions answered on paper
2. The top of each in-repository tool in section 1, to see what each one expects
3. MDN on `<title>` and `<meta>`, section 10
4. VS Code's Problems panel, section 9, so errors show while you type

## For the student who is ahead

- The HTML standard's parsing section, and the side quest in section 13
- RFC 9309, and Thursday's deliberate failure explained in its own words
- The industry connection in section 12, and a position written into `measurement-plan.md`
- The generated `lastmod` extension in section 13
