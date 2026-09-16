# Gate 2: Adversarial Review · Week 3
## 145010 Web Design & Senior Capstone · Week 3, Friday, Build 1

**40 minutes.** Individual and silent. You may and should open the page, use the keyboard, open
DevTools, and run web-check. You may not ask a model whether the page is correct, because a model wrote
it.

The page is `gate2-w03-files/club-fair.html`. Copy the whole folder and open the page in Chrome.

---

## What you are looking at

A student activities office asked an AI assistant for a club fair sign-up page and pasted in the
requirements below. The assistant produced `club-fair.html` and a comment at the top of it that says:

> Accessibility statement: this page meets WCAG 2.2 Level AA. It passes automated accessibility checks
> with zero violations.

**Half of that statement is true.** Run web-check and you will see which half.

**Five defects, one in each category:** Correctness, Security, Readability, Performance, Requirements
Fit. **web-check reports none of them.** Every one is findable by a person in 40 minutes with the
tools you used this week.

**One of the five is genuinely arguable.** You will be scored on your reasoning for that one, not only
on whether you found it.

---

## PART A: The requirements

> Build a one-page sign-up for the club fair. It must:
>
> 1. Show every club at the fair with when and where it meets, in a table.
> 2. Tell students they may pick up to three clubs, and let them pick.
> 3. Collect **only** the student's first name and school email. Nothing else.
> 4. Meet WCAG 2.2 Level AA, including full keyboard use and a working skip link.
> 5. Load quickly on a phone on the school's guest wireless, and use the banner art the office supplied:
>    the wide version on large screens and the narrow version on phones.
> 6. Match the Student Activities look: navy, light blue, white.

---

## PART B: What the AI produced

`gate2-w03-files/`:

| File | What it is |
|---|---|
| `club-fair.html` | The page under review |
| `received.html` | Where the form goes. It saves nothing |
| `banner-wide.svg`, `banner-narrow.svg` | The office's banner art |

Start here:

```
node tools/web-check/check.js <path to your copy>/gate2-w03-files/club-fair.html
```

A real run of that command, on the build machine:

```
PASS  Courses/145010/units/unit-3-accessibility/07-gate2-adversarial/gate2-w03-files/club-fair.html
  validation: 0 error(s), 0 warning(s)
  axe at 360px: 0 violation(s)
  axe at 768px: 0 violation(s)
  axe at 1280px: 0 violation(s)
```

**That is the trap.** It passes. Now find out what it passes while being wrong.

---

## What to submit

For each defect: **line number**, **dimension**, **what goes wrong for a real person**, **how you
proved it** (what you pressed, clicked, or read, and what you saw), and **the fix**.

Then one final entry: **what I was unsure about**, naming something specific. That entry is scored, and a
blank costs more than a wrong guess.

### How to spend 40 minutes

- **First 5:** read Part A one requirement at a time. For each, point at the line meant to meet it.
- **Next 10:** mouse out of reach. Reload. Tab once, press Enter, Tab again. Where are you? Then fill in
  the form with invented values, **not your own**, and submit it. Read the address bar.
- **Next 10:** open DevTools, Network panel, and reload at phone width and at desktop width. Count what
  loads.
- **Next 10:** read every `id`, every `for`, and every comment. Ask whether each one is true.
- **Last 5:** watch the table for ten seconds without scrolling. Decide what you think, and write down
  why.

---

## Scoring

Five defects, one point each, plus one for the unsure-about entry. **The security defect counts double:
missing it costs 2 points.** Your instructor states this before you start.

**Four of five is a strong score.**
