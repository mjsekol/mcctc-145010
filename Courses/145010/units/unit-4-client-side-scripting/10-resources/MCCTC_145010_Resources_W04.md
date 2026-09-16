# Additional Resources · Week 4
## 145010 Web Design & Senior Capstone · Unit 4 · Week 4
### Topics: where script lives and plug-ins, events, state and safe text, volume, bandwidth, and latency

Every link below is marked **Confident** or **[VERIFY]**. A [VERIFY] link has not been confirmed
live from the build machine. Click it before you rely on it, and tell your instructor if it has
moved. MDN reorganised some of its sections recently, so an MDN path marked [VERIFY] may redirect.

**Nothing here requires an account or an AI service.** If a resource asks you to sign up, skip it.

The in-repository links are relative to this file and they resolve. Reach for those first.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | This week's four lecture notes and their self-checks | Any day | Review | 20 min each |
| 2 | The Modern JavaScript Tutorial, the browser events chapters | Tue, Wed | On-level | 40 min |
| 3 | MDN: `addEventListener` | Tue | On-level | 15 min |
| 4 | MDN: `textContent`, and the security section of `innerHTML` | Wed | On-level | 15 min |
| 5 | MDN: the `<script>` element, `defer` and `async` | Mon | On-level | 15 min |
| 6 | WAI-ARIA Authoring Practices: the button and disclosure patterns | Tue, Wed | On-level | 20 min |
| 7 | OWASP Cross Site Scripting Prevention Cheat Sheet | Wed | Extension | 25 min |
| 8 | Chrome DevTools: the Network panel | Thu | On-level | 20 min |
| 9 | Interactive practice: the tasks at the end of each javascript.info chapter | Tue, Wed | On-level | 30 min |
| 10 | A free video under 20 minutes on the Network panel | Thu | Remediation | under 20 min |
| 11 | Industry connection: why page speed matters to real businesses | Thu | Extension | 15 min |
| 12 | Plug-in history: Adobe's Flash Player end-of-life page | Mon | On-level | 10 min |
| 13 | Side quest: the same component, with a framework | Fri | Extension | 1 period |

---

## 1. This week's notes

- [Where Script Lives](../03-lecture-notes/MCCTC_145010_Notes_WhereScriptLives.md)
- [The Page Waits for You](../03-lecture-notes/MCCTC_145010_Notes_ThePageWaitsForYou.md)
- [State, Render, and Comments](../03-lecture-notes/MCCTC_145010_Notes_StateRenderAndComments.md)
- [What a Page Costs to Deliver](../03-lecture-notes/MCCTC_145010_Notes_VolumeBandwidthLatency.md)

**Why these first.** They use the exact pages and numbers you work with in the labs. **Level.**
Review. **If you were at BPA,** the [catch-up guide](MCCTC_145010_CatchUp_W04.md) tells you which to
read for each day you missed.

---

## 2. Primary reading: The Modern JavaScript Tutorial

`https://javascript.info/` · **Confident** for the site. **[VERIFY]** the chapter
`https://javascript.info/introduction-browser-events` before you assign it.

**What it is.** A free, well-maintained online book on JavaScript. Part 2, "Browser: Document,
Events, Interfaces", covers the DOM and events in the order this week teaches them.

**Why this one.** It assumes you can already program, which you can, and it goes straight to what is
different in the browser. **Read with one question in hand:** what is the difference between an
`onclick` attribute and `addEventListener`, and why does this course use the second?

**Skip for now:** anything about frameworks and the chapters on custom elements.

**Time.** 40 minutes. **Level.** On-level.

---

## 3. MDN: `addEventListener`

`https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener` · **Confident.**

**Assign a question, not the page:** *What does the function you pass receive as its first
argument, and what is `event.target`?*

**Time.** 15 minutes. **Level.** On-level.

---

## 4. MDN: `textContent` and `innerHTML`

`https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent` · **Confident.**
`https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML` · **Confident.**

**Why these.** The `innerHTML` page has a security section that says, in MDN's own words, why
inserting text you do not control is dangerous. Read that section, then read the "Differences from
innerHTML" part of the `textContent` page.

**Time.** 15 minutes. **Level.** On-level.

---

## 5. MDN: the `<script>` element

`https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script` · **[VERIFY]**, because MDN has
been moving its HTML reference pages and this path may redirect.

**Assign a question:** *What happens to `defer` on a script with no `src`?* The answer is on the
page, and it is why this course puts script in files.

**Time.** 15 minutes. **Level.** On-level.

---

## 6. WAI-ARIA Authoring Practices: button and disclosure

`https://www.w3.org/WAI/ARIA/apg/patterns/button/` · **Confident.**
`https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/` · **Confident.**

**What it is.** The W3C's guide to building accessible widgets. The button pattern explains
`aria-pressed` and why a toggle button's label should not change. The disclosure pattern is the rules
toggle in Lab W04-01.

**Read the "Keyboard Interaction" section of each.** It is short and it is the checklist for your
project.

**Time.** 20 minutes. **Level.** On-level.

---

## 7. OWASP Cross Site Scripting Prevention Cheat Sheet

`https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html` ·
**Confident.**

**What it is.** The security industry's standard reference on XSS. It is dense. Read the
introduction and the section on safe sinks, which is the formal name for "use `textContent`".

**Why it matters next week.** Week 5 moves text to a server and back. The same rule applies on the
way out of the server.

**Time.** 25 minutes. **Level.** Extension.

---

## 8. Chrome DevTools: the Network panel

`https://developer.chrome.com/docs/devtools/network` · **Confident.**
`https://developer.chrome.com/docs/devtools/network/reference` · **[VERIFY]**, the reference page
with the throttling and timing sections.

**Why this one.** It is Google's own documentation for the tool you used on Thursday. Read the part
on throttling, and find the preset names your Chrome shows.

**Time.** 20 minutes. **Level.** On-level.

---

## 9. Interactive practice

The tasks at the end of each chapter on `javascript.info` are free, need no account, and have
solutions you open after trying. **Confident** for the site. Do the tasks for the events chapter and
the chapter on modifying the document.

**Also:** the three demo-style pages in Lab W04-01's extended options, which you can build as
practice with the same acceptance criteria.

**Time.** 30 minutes. **Level.** On-level.

---

## 10. A free video under 20 minutes

**[VERIFY]** The Chrome for Developers channel on YouTube, `https://www.youtube.com/@ChromeDevs`,
publishes short videos on DevTools. Your instructor picks one under 20 minutes that shows the Network
panel and throttling, and checks it before sharing. No specific video is linked here, because none was
confirmed from the build machine.

**Time.** Under 20 minutes. **Level.** Remediation, for anyone who missed Thursday.

---

## 11. Industry connection: why speed matters

`https://web.dev/articles/why-speed-matters` · **[VERIFY]**

**What it is.** Google's web.dev article on how page speed affects the people using a site. It cites
case studies from real companies. **Read the case studies critically:** each one is a company
reporting its own results. Ask what else changed at the same time.

**Connect it to Thursday.** For each case study, decide whether the problem was mostly bandwidth or
mostly latency, if the article says enough to tell.

**Time.** 15 minutes. **Level.** Extension.

---

## 12. Plug-in history

`https://www.adobe.com/products/flashplayer/end-of-life.html` · **[VERIFY]**

**What it is.** Adobe's own page about the end of Flash Player. It is the primary source for the date
in Monday's notes. If it has moved, a search for "Adobe Flash Player end of life" finds Adobe's
current page. Use Adobe's page, not a summary of it, as your plug-in note's source.

**Time.** 10 minutes. **Level.** On-level.

---

## 13. Side quest: the same component with a framework

**After** your vanilla component is submitted, rebuild it with a framework of your choice, following
that framework's official getting-started guide. Then write half a page:

- What did the framework do for you that you wrote by hand?
- How many kB does the framework version transfer under Slow 4G, against yours?
- Which would you hand to the league volunteer to maintain, and why?

This is side quest material only. The Ohio standards for this course are vanilla, and nothing
framework-based is graded in the instruction phase.

**Time.** One Period 8, or two. **Level.** Extension.
