# Resources · Week 3 · Accessibility & Compliance
## 145010 Web Design & Senior Capstone

**How to read the status column.** **Loaded** means the page was fetched when this file was built and its
title matched. **[VERIFY]** means check it before you assign it, because it was not fetched, or because it
is a government or legal page that moves. Every legal source is marked [VERIFY] regardless.

**Not legal advice.** The legal sources below are where the rules are published. Reading them is not the
same as knowing whether a particular organization complies, and nothing in this course tells you that.

---

## 1. Primary reading · on-level

**W3C, "Web Content Accessibility Guidelines (WCAG) 2.2."**
`https://www.w3.org/TR/WCAG22/` · **Loaded** · [VERIFY] before class, as with every standard.

**What it is.** The standard this course cites. **Why this one.** Every audit row this week cites a
criterion from it, by number and name. **Time.** 30 minutes for the principles and the criteria this week
uses: 1.1.1, 1.3.1, 1.4.1, 1.4.3, 1.4.11, 2.1.1, 2.1.2, 2.4.3, 2.4.4, 2.4.7, 3.1.1, 3.1.2, 3.3.2, 4.1.2.
Read the criterion text, not the whole document.

**W3C WAI, "Understanding WCAG 2.2"** pages, one per criterion. Reached from each criterion in the
standard. The page for 3.1.2 was loaded when this file was built:
`https://www.w3.org/WAI/WCAG22/Understanding/language-of-parts.html` · **Loaded**

**Why these.** The standard says what. The Understanding pages say why and give examples, including the
"in context" rule for 2.4.4 that the Lab W03-01 key argues about.

---

## 2. Video · not linked

**No video is linked in this file.** None was verified on the build machine. If you assign one, check
that it is under 20 minutes, free, and demonstrates a real screen reader on a real page. Record where and
when you checked it in your own planning notes, and add only the title and link to this file.

---

## 3. Interactive practice · on-level and remediation

**W3C WAI, `Easy Checks: A First Review of Web Accessibility`** (the page title, quoted exactly)
`https://www.w3.org/WAI/test-evaluate/easy-checks/` · **Loaded**

**What it is.** A short set of checks a person can do without special software, such as the page title,
image text alternatives, and keyboard access. **Why this one.** It is the same kind of check you give the
coordinator in your client note. **Time.** 20 minutes. **Remediation** for a student whose audit had fewer
than six `me` rows.

**web.dev, "Learn Accessibility."**
`https://web.dev/learn/accessibility` · **Loaded**

**What it is.** A free course in modules, including ARIA and HTML, content structure, and keyboard focus,
with a quiz. **Why this one.** Short modules that match Tuesday and Wednesday. **Time.** 15 minutes per
module. **On-level.**

---

## 4. Official documentation

**MDN Web Docs, "Accessibility."**
`https://developer.mozilla.org/en-US/docs/Web/Accessibility` · **Loaded**

**Why this one.** The reference for HTML elements and ARIA attributes, and the page the Lab W03-01 and
W03-02 EXTENDED hints point toward. **On-level and extension.**

**Chrome DevTools, "Accessibility features reference."**
`https://developer.chrome.com/docs/devtools/accessibility/reference` · **Loaded**

**Why this one.** How to open the Accessibility tab and the full-page accessibility tree you use on
Tuesday. **Time.** 10 minutes. **On-level.**

**Microsoft Support, "Complete guide to Narrator."**
`https://support.microsoft.com/en-us/windows/complete-guide-to-narrator-e4397a0d-ef4f-b386-d8ae-c172f109bdb1`
· **Loaded** · [VERIFY], because support URLs change.

**Why this one.** The source for the Narrator keys in this week's checklist. Its keyboard appendix lists
the commands for lists of links, headings, and landmarks. **Time.** Use it as a reference, not a reading.

**NV Access, the makers of NVDA.** `https://www.nvaccess.org/` · **Loaded**

**What it is.** A free screen reader for Windows. **Not installed on the build machine.** Any NVDA step in
this unit is [VERIFY].

---

## 5. Legal and policy sources · read the purpose, not the fine print

All **[VERIFY]**. Each loaded when this file was built. Government pages move and rules change.

- **ADA.gov, "Guidance on Web Accessibility and the ADA."**
  `https://www.ada.gov/resources/web-guidance/` · Says the ADA applies to the web content of state and
  local governments and of businesses open to the public, and names WCAG among the existing standards.
  The page itself notes that it does not reflect the later rule for state and local governments.
- **ADA.gov, fact sheet on the web content and mobile app rule for state and local governments.**
  `https://www.ada.gov/resources/2024-03-08-web-rule/` · Names WCAG 2.1 Level AA as the technical standard
  and lists public schools among the entities covered. **Its compliance dates had already been changed
  when this file was built. Read the current ones there. Do not copy them into a lesson.**
- **Section508.gov.** `https://www.section508.gov` · The federal government's own accessibility program.
  Not fetched. [VERIFY].

**Why these.** When a capstone stakeholder asks "do we have to," these are where the answer starts, and the
answer to give is "here is where it is published, and here is what I checked," not a legal opinion.

---

## 6. Industry connection · extension

**WebAIM Contrast Checker.** `https://webaim.org/resources/contrastchecker/` · **Loaded**

**What it is.** A free, browser-based contrast checker from WebAIM, a web accessibility organization. **Why this one.** It does
in a browser what Monday's Python function does, and designers you work with in the capstone may already
use it. Compare its answer for `#767676` on white with the 4.54:1 you calculated.

**axe-core on GitHub.** `https://github.com/dequelabs/axe-core` · Not fetched. [VERIFY].

**What it is.** The open-source engine inside `web-check`. **Why this one.** Its rule descriptions say which
rules are WCAG-tagged and which are best practice, which is exactly why web-check did not report skipped
heading levels this week. **Extension.**

**No news article is linked.** A current article about web accessibility in industry was not verified on
the build machine. If you add one, prefer a primary source, and say whether it is reporting or opinion.

---

## 7. Side quest · extension

**Build an accessibility checklist page, and audit it with itself.**

Write a single HTML page that is the three client checks from your note, expanded to ten, each with a
"how to check" line and a WCAG criterion number and name. Then make that page pass web-check, walk it with a
keyboard, and listen to it with Narrator. Commit it to your portfolio repository.

**Stretch.** Add a section on the one criterion you found hardest to test by hand, and describe what a
person would need to do to test it. Look at 1.4.10 Reflow and 1.4.12 Text Spacing on the W3C site.

**Connects to:** the capstone, where your stakeholder will need exactly this kind of page, and the BPA 365
and 455 team events. Confirm this year's event guidelines for what each one judges.

---

## Exit criteria for Week 3

You can check yourself against these. They are the syllabus's words for this week.

- [ ] I can plan a web page considering audience, layout, colour, links, graphics, and ADA requirements.
- [ ] I can identify how different browsers and devices, including text-to-speech and screen readers,
      affect how a page works.
- [ ] I can develop and run a usability test that checks accessibility, ease of use, and navigation.
- [ ] I can recognize ways bias may influence how a product serves different users.
- [ ] I rebuilt a supplied inaccessible page to pass an automated check with zero errors.
- [ ] I demonstrated keyboard-only navigation end to end.
- [ ] I recorded a screen reader walkthrough, or a partner wrote a listening log where recording was not
      possible.
