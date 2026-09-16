# Guide · The Proofreading Pass
## 145010 Web Design & Senior Capstone · Week 1, Friday · Competency 6.1.4

**Why this exists.** A page is read by strangers who cannot ask you what you meant. A wrong
kickoff time on a league page sends a family to an empty field. A typo in a heading makes the
whole page look careless. The checkers you ran this week cannot catch either one. `web-check`
does not know when a game starts. You do, or you know who to ask.

You already know the writing process from English class: drafting, revising, editing,
proofreading. This guide applies it to a web page, where each pass looks for something
different. **Do the passes separately.** Reading once for everything finds the typos and
misses the wrong fact every time.

---

## Pass 1 · Draft

**What you are doing:** getting every piece of content onto the page in roughly the right
place.

**What to record in your log:** anything you left out on purpose, and anything you were unsure
of. "Round 3 kickoff, notes say 9:00 and also maybe 9:30, asked Dana" is a draft note.

**The failure mode:** polishing sentences in the draft pass. You will rewrite half of them
anyway.

---

## Pass 2 · Revise

**What you are looking at:** structure and content, not sentences.

Ask these, and write down what each answer changed:

1. Does every one of the client's questions have a section that answers it?
2. Is anything said in two places? If so, say it once and link to it.
3. Is every heading a true label for what is under it?
4. Is anything a list that should be a table, or a table that should be a list?
5. Did you trust a note that another note contradicts? Which one wins, and why?

**The failure mode:** keeping something because you already wrote it.

---

## Pass 3 · Edit

**What you are looking at:** sentences and links.

1. Read every sentence out loud. Cut any sentence that does not help a parent on game day.
2. Read every link's text on its own, with nothing around it. "Click here" fails. "Medical
   release form (PDF, 1 page, 2 KB)" passes.
3. Check every number against the source: times, sizes, counts, the address.
4. Check every name against the source: team names, the park, the league.
5. Run `structure_check`. It lists every link and every heading in one place, which is the
   fastest way to read them all together.

**The failure mode:** checking a number against your own draft instead of against the notes.

---

## Pass 4 · Proofread

**What you are looking at:** the surface. Spelling, capitalization, punctuation, spacing.

1. Read the page in the browser, not in the editor. You see what a visitor sees.
2. Read it backwards, section by section, from the footer up. Your brain stops predicting the
   next sentence and starts reading the words.
3. Open View Source and read the comments. Anything you would not want a stranger to read,
   delete.
4. Run both checkers one last time and save the output to `evidence/`.

**The failure mode:** proofreading in the editor with syntax colors on. The colors make wrong
words look right.

---

## What your log looks like

This example is from a different invented page, a band car wash fundraiser, so it shows the
shape without doing your project for you.

```markdown
# Proofreading log

## Draft
- Left out the note about who is bringing the hoses. It is for volunteers, not customers.
- Start time unclear: the flyer says 9:00, the group chat says "maybe 10". Asked the
  booster president.

## Revise
- Prices appeared in two sections. Kept them under Prices only and linked to it.
- The flyer says trucks are 12 dollars and the price sheet says 10. Used 10, because the price
  sheet is newer. Confirmed with the booster president.

## Edit
- Start time: used 10:00 (the booster president's answer).
- Link text "here" rewritten to say what the file is and how big it is.

## Proofread
- "Fundriaser" corrected to "Fundraiser" in the h1.
- "Satruday" corrected to "Saturday" in the footer.
```

**Every correction in your log must be visible in your page.** A log that claims a fix the page
does not have scores zero for that line.
