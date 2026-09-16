# Template · User Guide
## 145010 Senior Capstone · Week 17

**Commit as:** `user-guide.md` at the top of your repository. If you also publish it as a web page,
that page meets the same standard as your project: zero validation errors, zero automated
accessibility violations, readable on a phone.
**Due:** Week 17, Wednesday, proofread and delivered to the stakeholder.

**Competencies this evidences:** 2.13.6 (deliver support and training materials), 1.10.3
(communicate features, benefits, and warranties to the customer), 6.1.4 (drafting, revising,
editing, and proofreading), 1.2.5 (communicate directions for an intended audience), 1.2.12
(technical writing).

---

## Why this exists

**Your README is for developers. This is for the people who use the project.** Your stakeholder
has never seen your code and never will. Everything they need to use, trust, and recover the
project goes here, in their words.

**The failure to avoid is writing for yourself.** "Run the migration, then restart the service" is
a developer sentence. "If the page says Something went wrong, wait one minute and reload it. If it
still says that, call <role>" is a user sentence.

**The test of a user guide:** your stakeholder does the main task using only this document, while
you sit on your hands. Whatever they get stuck on, you rewrite.

---

## How to write it

- **One task per section.** The title is what the person wants to do: "Sign up for a shift."
- **Numbered steps, one action each**, each followed by what they should see.
- **Use the exact words on the screen**, in bold, so they can match them.
- **Screenshots use invented data only.** No real names, no real records.
- **Plain language.** Short sentences. No technical word without an explanation beside it.
- **Draft, revise, edit, proofread.** Four passes, not one. Read it aloud on the last pass.

---

```markdown
# <Project name> · User Guide
For: <stakeholder organization and the users>   Version <n>   Week 17

## What this is for
<Two or three sentences. The problem it solves, in the stakeholder's words.>

## What it does, and what that means for you
*1.10.3. Features and benefits.*
| It can | Which means |
|---|---|
| | |

## What it does not do
- <Be clear. People trust a tool more when they know its limits.>

## Before you start
- **Where to find it:** <address or location>
- **What you need:** <device, browser, account>
- **Who has an account:** <roles>

## <Task 1: the main task, named as a goal>
1. <One action.> You should see **<exact screen text>**.
2. <...>
3. <...>

*Screenshot: <file>, with invented data.*

## <Task 2>
...

## What the messages mean
| On screen | What it means | What to do |
|---|---|---|
| **<exact message>** | | |

## When something goes wrong
| What you notice | Try this first | If that does not work |
|---|---|---|
| The page does not load | <wait one minute and reload, because the free host may be waking up> | <contact role> |
| | | |

## Privacy
<One paragraph. What the project stores, why, who can see it, how long it is kept, and how to ask
for something to be removed.>

## Accessibility
<Keyboard use, screen reader notes, zoom, and who to tell if something is hard to use.>

## Support and warranty
<Plain words, matching the acceptance agreement. What will be fixed, by whom, until when. What is
not promised.>

## Asking for a change
<How to request an improvement, from the rollout plan section 10.>

## Words used in this guide
| Word | Meaning |
|---|---|
| | |
```

---

## The proofreading pass · 6.1.4

Do these in order, on four separate passes. Record each pass in your decision log with the week and
day, because 6.1.4 is evidenced by the process, not only the result.

1. **Draft.** Get every task written, badly if necessary.
2. **Revise.** Read it as the stakeholder. Reorder, cut, add missing steps. Watch someone use it
   for the main task and fix where they stopped.
3. **Edit.** Shorten sentences. Replace technical words. Check every screen text matches the
   product exactly.
4. **Proofread.** Spelling, punctuation, numbering, links. Read it aloud.

## Before you deliver · self-check

- [ ] Your stakeholder, or someone like them, did the main task using only this guide.
- [ ] Every screen text in bold matches the product.
- [ ] Every screenshot uses invented data.
- [ ] The support section promises nothing you cannot give.
- [ ] All four passes are recorded.
