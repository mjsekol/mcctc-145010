# The Browser Forgives. The Standard Does Not.
---
## Slide 1: What is wrong with this page
- A header, a list, two cards, a picture
- It opens in Chrome
- Most people call it finished
- It has nine errors
Speaker notes: I am going to open a page and I want you to tell me what is wrong with it. Take a good look. Most rooms say nothing, and one person notices that the middle card looks a bit off. Hold onto whatever you think. In two minutes a checker is going to tell us this page has nine errors in it, and the browser has not mentioned a single one.
Image: A screenshot of a tidy robotics club page with a header, a list, two cards, and a floor plan.
---
## Slide 2: Browsers repair instead of refusing
- A compiler stops at your first mistake
- A browser shows whatever it is given
- It repairs broken markup silently
- The repair is not always what you meant
Speaker notes: You have used compilers for two years. They stop at your first mistake. A browser does the opposite. It was built to show anything, because a browser that refused a slightly broken page would lose its users. So it repairs your markup and draws the repair, and it never tells you. Most of the time the repair is close enough. Today we look at the times it is not.
Image: A mechanic quietly patching a car while the driver looks at the road, no warning lights on the dashboard.
---
## Slide 3: The checker's answer
```
FAIL  looks-fine/club.html
  validation: 9 error(s), 0 warning(s)
    line 12:6  deprecated  <center> is deprecated: use CSS instead
    line 16:6  no-implicit-close  Element <p> is implicitly closed by adjacent <ul>
    line 22:6  close-order  Stray end tag '</p>'
    line 28:52  element-permitted-content  <a> element is not permitted as a descendant of <a>
    line 36:13  no-dup-id  Duplicate ID "roles"
    line 38:43  attr-quotes  Attribute "href" using unquoted value
```
Speaker notes: This is part of the real output from web-check on that page. Nine validation errors, plus a missing alt text that the accessibility audit also caught. A list inside a paragraph. A stray closing tag. A link inside a link. The same id twice. An address with no quotes around it. None of that showed up as a message in the browser.
Image: None. This slide is code.
---
## Slide 4: What Chrome built instead
- The list moved out, an empty paragraph added
- The linked card split into three pieces
- href="shop map.html" became href="shop"
- #roles jumps to the wrong heading
Speaker notes: Open the Elements panel and compare. The browser closed the paragraph before the list and added an empty one after it. The card that was a link with another link inside it got split into three siblings, which is the broken card some of you spotted. The shop map link now goes to a page called shop, because an unquoted value stops at the first space. Four repairs, zero messages.
Image: Side by side, the source file and the Elements panel, with the differences circled in Launch Blue.
---
## Slide 5: Two engines, one repair
```
chrome   Chrome/153.0.8010.48    360px  overflow 0px  elements 35  dom 025f9ff189
firefox  firefox/156.0           360px  overflow 0px  elements 35  dom 025f9ff189
Same dom fingerprint in both engines means both rebuilt the page into the same tree.
It does not mean the tree is the one you meant. Validate the source.
```
Speaker notes: Here is the same page in Chrome and in Firefox, two different engines. Same number of elements, same fingerprint of the tree. They agree completely. The HTML standard describes how to repair broken markup, and both follow it. So they agree with each other, and neither of them agrees with what the author meant. Agreement is not correctness.
Image: None. This slide is code.
---
## Slide 6: The wrong way to validate
- Copy the page from the Elements panel
- Paste it into the validator
- Nine errors become six
- Two of the six are not even in your file
Speaker notes: Here is a mistake that feels clever. You copy the page out of DevTools and validate that. On the build machine that reported six errors instead of nine. The list in the paragraph, both stray tags, the nested link, and the unquoted address all vanished, because the browser had already repaired them. And two new whitespace complaints showed up that are not in your file at all. Validate the file you wrote, not the page the browser built.
Image: Two validator reports, nine lines and six lines, with the missing five lines ghosted in Launch Red.
---
## Slide 7: An engine is not a logo
- Chrome, Edge, Opera, Brave: Blink
- Firefox: Gecko
- Safari: WebKit, and not on Windows
- Chrome plus Edge is one engine tested twice
Speaker notes: Cross-browser testing is about engines. Chrome and Edge look different and they draw pages with the same engine, Blink. Firefox uses Gecko. Safari uses WebKit, which does not run on Windows, so you cannot test it in this lab. If your matrix says tested in Chrome and Edge, it says one engine. Say how many engines you really tested, and name the one you could not.
Image: Three engine names in columns with browser names listed under each.
---
## Slide 8: What a cross-browser test checks
- Layout at 360, 768, and 1280
- Keyboard only, focus always visible
- Video plays, captions toggle
- Forms and your feedback question work
Speaker notes: Engines agree on parsing much more than on everything else. So your matrix checks the rest. Layout at three widths. The whole site with the keyboard only. Media playing with captions. Form controls, which really do look and act differently between engines. Every row says what you checked and what you saw, in words. Looks good is not a row.
Image: A filled-in test matrix with browser, width, page, check, and result columns.
---
## Slide 9: Your editor is a checker too
- Problems panel: Ctrl+Shift+M
- Format Document: Shift+Alt+F
- A validator extension, if the lab allows one
- Pick the tool that catches today's mistakes
Speaker notes: Choosing an IDE is an exam competency and a real decision. You already use VS Code. Turn on the Problems panel. Format the document, because re-indenting makes a misplaced closing tag jump out. If the lab allows a validation extension, use it. The reason to choose an editor for a job is simple: it should catch this week's mistakes while you type, before a checker or a visitor does.
Image: A VS Code window with the Problems panel open under an HTML file.
---
## Slide 10: What you are about to build
- Lab W06-03 Part A: club.html to zero errors
- Then every page of your own site
- Part B: the cross-browser matrix, by hand
- Fix in content and template, never in site
Speaker notes: Build one is part A. Take the club page to zero errors, and change as little as you can while you do it. Then run web-check on your own site and fix everything it finds, in your content files and your template, never in the site folder. Build two is part B, the matrix. Visible browser windows, at least eight rows, both keyboard rows, and an honest count of engines. Safari goes in the could not test section.
Image: A checklist with part A and part B, and a web-check PASS line underneath.
