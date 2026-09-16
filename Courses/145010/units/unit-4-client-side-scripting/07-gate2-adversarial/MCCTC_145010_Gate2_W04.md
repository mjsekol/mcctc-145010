# Gate 2: Adversarial Review · Week 4
## 145010 Web Design & Senior Capstone · Unit 4 · Week 4, Friday

**40 minutes.** Individual. You may and should open the page and use it. You may not ask a model
whether it is correct, because a model's work is what is being reviewed.

The files are in `gate2-w04-files/`: `shoutouts.html`, `shoutouts.css`, and `shoutouts.js`. Copy
the folder and open `shoutouts.html` in Chrome with dev tools open. No server is needed.

---

## What you are looking at

A robotics club asked an AI assistant for a shout-out wall, using the requirements in Part A. The
assistant produced the three files. The page looks finished. The code is tidy, commented, and uses
event delegation, which is a technique people reach for when they know what they are doing.

**Five defects, one in each category:** Correctness, Security, Readability, Performance,
Requirements Fit.

**One more thing you should know before you start.** The page passes `web-check` with zero errors
and zero violations. That is a fact, not a hint that nothing is wrong.

**At least one of the five is a judgement call.** If you think a finding is arguable, say so and
argue it. Reasoning is scored.

---

## PART A: The requirements

> Build a shout-out wall for the robotics club page. It must:
>
> 1. Let a member write a shout-out of **up to 120 characters** and see a live preview of it.
> 2. Show how many characters are left, and announce the count politely to screen readers.
> 3. Add the shout-out to the wall with an **Add** button, and let **any member remove any
>    shout-out, by mouse or by keyboard**.
> 4. Let a member type in a filter box to show only shout-outs containing that text.
> 5. **Always show what a member typed as text.** Never let typed text change the page's structure
>    or run anything.
> 6. Use an external script file, loaded so it never runs before the page exists, and comment it.

---

## PART B: What the AI produced

Open the page. Try it the way a club member would, then the way a careful tester would.

Things worth trying, in no particular order:

- Write a shout-out that is exactly 120 characters. (A block of 12 characters repeated ten times is
  quick to paste: `0123456789` plus two letters, ten times.)
- Filter for `gg`, then for `GG`.
- Remove a shout-out, first with the mouse, then with only the keyboard.
- Type something that contains angle brackets into the shout-out box.
- Type a long sentence into the shout-out box with the Elements panel open on the wall list, and
  watch the list.

**Read the code with the requirements beside it**, one requirement at a time, and point at the line
that meets it. Then read every comment and ask whether it is true.

---

## What to submit

For each defect:

1. **File and line number**
2. **Dimension:** Correctness, Security, Readability, Performance, or Requirements Fit
3. **What goes wrong for a real person** using the page
4. **How you showed it:** what you typed or pressed and what happened
5. **The fix**, in code or in one precise sentence

Then one final entry: **what I was unsure about**, naming something specific. That entry is scored,
and a blank costs more than a wrong guess.

### How to spend 40 minutes

- **First 5:** use the page like a club member. Add one, remove one, filter.
- **Next 10:** try each item in the list above and write down anything surprising.
- **Next 15:** read `shoutouts.js` against Part A, one requirement at a time.
- **Last 10:** read every comment against the code under it. Write up.

---

## Scoring

Five defects, one point each, plus one for the unsure-about entry. **Your instructor states the
security weighting before you start.**

**Four of five is a strong score.**
