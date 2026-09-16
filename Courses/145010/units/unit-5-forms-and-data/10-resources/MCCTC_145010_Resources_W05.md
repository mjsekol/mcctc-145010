# Additional Resources · Week 5
## 145010 Web Design & Senior Capstone · Unit 5 · Week 5
### Topics: named, labelled, grouped controls · the form action · two layers of validation · accessible errors and tabindex

Every link below is marked **Confident** or **[VERIFY]**. A [VERIFY] link has not been confirmed
live from the build machine. Click it before you rely on it, and tell your instructor if it has
moved. MDN has recently reorganised its "Learn" and reference paths, so its deep links are marked
[VERIFY] even where the page certainly exists somewhere on the site.

**Nothing here requires an account or an AI service.**

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | This week's four lecture notes | Any day | Review | 20 min each |
| 2 | MDN's web forms learning module | Mon, Wed | On-level | 45 min |
| 3 | W3C WAI Forms Tutorial, including notifications | Mon, Thu | On-level | 30 min |
| 4 | MDN: the `tabindex` attribute | Thu | On-level | 10 min |
| 5 | Flask documentation, the quickstart | Tue | Remediation | 20 min |
| 6 | Python's `sqlite3` documentation, placeholders | Tue | On-level | 15 min |
| 7 | OWASP Input Validation Cheat Sheet | Wed | Extension | 25 min |
| 8 | OWASP SQL Injection Prevention Cheat Sheet | Fri | Extension | 20 min |
| 9 | A published error summary pattern from a government design system | Thu | Extension | 15 min |
| 10 | Chrome DevTools: the Network panel's request details | Tue | On-level | 15 min |
| 11 | Interactive practice | Wed, Thu | On-level | 30 min |
| 12 | A free video under 20 minutes | Any | Remediation | under 20 min |
| 13 | Industry connection: the OWASP Top Ten | Fri | Extension | 20 min |
| 14 | Side quest: cross-site request forgery | Fri | Extension | 1 period |

---

## 1. This week's notes

- [A Form Is Named, Labelled, Grouped Controls](../03-lecture-notes/MCCTC_145010_Notes_NamedLabelledGrouped.md)
- [The Form Action, and Where the Data Goes](../03-lecture-notes/MCCTC_145010_Notes_TheFormAction.md)
- [Two Layers of Validation](../03-lecture-notes/MCCTC_145010_Notes_TwoLayersOfValidation.md)
- [Errors People Can Find, and tabindex](../03-lecture-notes/MCCTC_145010_Notes_AccessibleErrors.md)

**Why these first.** They use the lab app, its real output, and its real error messages. **Level.**
Review.

---

## 2. Primary reading: MDN's web forms module

`https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms` · **[VERIFY]**
the path. The module is also linked from MDN's "Learn web development" home.

**What it is.** A free, structured guide to HTML forms from the organisation that documents the web
platform. It covers form structure, every control type, sending data, and client-side validation.

**Read with one question in hand:** which of the attributes it describes stop a request from reaching
the server, and which of them could a person remove? Its own validation article says plainly that
client-side checks do not replace server-side ones. Find that sentence.

**Skip for now:** styling complex widgets and the pages on custom controls.

**Time.** 45 minutes. **Level.** On-level.

---

## 3. W3C WAI Forms Tutorial

`https://www.w3.org/WAI/tutorials/forms/` · **Confident.**
`https://www.w3.org/WAI/tutorials/forms/notifications/` · **[VERIFY]** the sub-page path.

**What it is.** The W3C Web Accessibility Initiative's tutorial on accessible forms: labelling,
grouping with fieldset and legend, instructions, validation, and user notifications.

**Why this one.** It is the standards body's own guidance, and its notifications page is the source
of most of the error pattern you built on Thursday.

**Time.** 30 minutes. **Level.** On-level.

---

## 4. MDN: `tabindex`

`https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/tabindex` · **[VERIFY]**, MDN
may have moved it under a new reference path.

**Assign a question:** *what does MDN say about positive values, and why?* The answer matches
Thursday's demonstration.

**Time.** 10 minutes. **Level.** On-level.

---

## 5. Flask documentation

`https://flask.palletsprojects.com/` · **Confident.** Look for the Quickstart in the contents.

**Why this one.** You used Flask in 145130. If `request.form`, `redirect`, or `render_template` feel
rusty, the Quickstart covers all three in its sections on the request object, redirects, and
rendering templates. It also explains that templates escape values automatically.

**Time.** 20 minutes. **Level.** Remediation.

---

## 6. Python's `sqlite3` documentation

`https://docs.python.org/3/library/sqlite3.html` · **Confident.**

**Assign a question:** find the section on using placeholders to bind values in SQL queries, and
answer: *what does the documentation say about building queries with string operations?*

**Time.** 15 minutes. **Level.** On-level.

---

## 7. OWASP Input Validation Cheat Sheet

`https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html` · **Confident.**

**What it is.** The security community's reference on validating input. Read the parts on allow
lists and on client-side validation. You will recognise the week's sentence in its own words.

**Time.** 25 minutes. **Level.** Extension.

---

## 8. OWASP SQL Injection Prevention Cheat Sheet

`https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html` ·
**Confident.**

**Why this one.** Gate 2 W05's security defect is here, with its fix named as the first defence.
Read the introduction and the section on prepared statements.

**Time.** 20 minutes. **Level.** Extension.

---

## 9. A published error summary pattern

`https://design-system.service.gov.uk/components/error-summary/` · **Confident.**

**What it is.** The UK government's public design system documents an error summary very close to
the one you built, with its research notes. It is a reference, not a client, and nothing in this
course copies its code.

**Read with one question in hand:** what does it say about where focus goes and what the page title
does? Compare with your own.

**Time.** 15 minutes. **Level.** Extension.

---

## 10. Chrome DevTools: request details

`https://developer.chrome.com/docs/devtools/network` · **Confident.**
`https://developer.chrome.com/docs/devtools/network/reference` · **[VERIFY]**

**Why this one.** Find what the reference calls the tab where a form's body appears, and the
setting that keeps requests after a redirect. Tuesday called them Payload and Preserve log.
[VERIFY] the names in your Chrome.

**Time.** 15 minutes. **Level.** On-level.

---

## 11. Interactive practice

MDN's forms module ends several articles with "Test your skills" exercises that run in the browser
with no account. **[VERIFY]** which exercises are currently linked.

**Also:** Gate 1 reps 01, 05, and 11 to 15 are good self-tests. Ask your instructor for them.

**Time.** 30 minutes. **Level.** On-level.

---

## 12. A free video under 20 minutes

**[VERIFY]** No specific video was confirmed from the build machine. Your instructor chooses one under
20 minutes on HTML form validation or on the Network panel, checks it, and shares it. Good sources to
search are the Chrome for Developers channel and MDN's own channel.

**Level.** Remediation, for anyone who missed Tuesday or Wednesday.

---

## 13. Industry connection: the OWASP Top Ten

`https://owasp.org/www-project-top-ten/` · **Confident.**

**What it is.** The most widely cited list of web application security risk categories. Find the
category that covers injection. Then write two sentences: which of this week's three failures from
the crash course's table fall under it, and which do not.

**Time.** 20 minutes. **Level.** Extension.

---

## 14. Side quest: cross-site request forgery

`https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html`
· **Confident.**

A form on another site can make a visitor's browser post to yours. Read the cheat sheet's
introduction, then add a token to the lab app's form that the server checks, and write half a page on
what attack it stops and what it does not. Commit it on a separate branch. It is not graded in the
instruction phase.

**Time.** One or two Period 8s. **Level.** Extension.
