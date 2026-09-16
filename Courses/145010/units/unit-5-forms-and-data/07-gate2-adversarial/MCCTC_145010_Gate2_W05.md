# Gate 2: Adversarial Review · Week 5
## 145010 Web Design & Senior Capstone · Unit 5 · Week 5, Friday

**40 minutes.** Individual. You should run the app and send it requests. You may not ask a model
whether it is correct, because a model's work is what is being reviewed.

The app is in `gate2-w05-files/`: `app.py` and three templates. Copy the folder, and in it:

```
python app.py --port 8415
```

Open `http://127.0.0.1:8415/`. It creates `carwash.db` with three invented volunteers the first time
it runs. **Stop the server with Ctrl+C when you finish**, and delete `carwash.db` if you want to start
again from the three volunteers.

---

## What you are looking at

A robotics club asked an AI assistant for a sign-up app for its car wash fundraiser, using the
requirements in Part A. The assistant produced a tidy Flask app. It uses placeholders in its INSERT,
escapes its templates, checks every field on the server, refuses a busy port, and passes `web-check`
with zero errors and zero violations on every page.

**Five defects, one in each category:** Correctness, Security, Readability, Performance,
Requirements Fit.

**At least one is a judgement call.** If you think a finding is arguable, say so and argue it.

---

## PART A: The requirements

> Build a volunteer sign-up for the car wash. It must:
>
> 1. Ask for the volunteer's **name** (required, up to 50 characters), **grade** (9 to 12), and
>    **shift** (9:00 am, 11:00 am, or 1:00 pm).
> 2. Allow **4 volunteers per shift**. Show how many spots each shift has left, and refuse a full
>    shift.
> 3. **Check every field on the server.** The browser's checks are a convenience.
> 4. When something is wrong, use the course's **accessible error pattern**: errors tied to their
>    fields, a summary people can navigate, and the volunteer's answers kept.
> 5. After signing up, give the volunteer a **confirmation code**. The lookup page shows **only the
>    sign-up that matches the code** someone enters.
> 6. Store everything in SQLite.

---

## PART B: What to try

- Load the form and read the spots left for each shift. Then sign up for the 1:00 pm shift, which
  has nobody in it, and read the spots again. Then try to sign up a second person for 1:00 pm.
- Look up the code `a1b2c3`. Then think about what the lookup page does with what you type.
- Submit the form with a name and a grade but no shift, with the browser's checks removed. Look at
  what comes back, with the keyboard and with dev tools.
- Read `app.py` against Part A, one requirement at a time. Read every function name and docstring
  and ask whether it is true.
- Count how much work the app does to show the form once.

You may send requests however you like: the browser, dev tools, or a short Python script using
`urllib`, like `send_raw.py` from the lab. Any lookup code you try should be typed into the lookup
page's box or into the address after `?code=`.

---

## What to submit

For each defect:

1. **File and line number**
2. **Dimension**
3. **What goes wrong for a real person**, a volunteer or the club
4. **How you showed it**: what you sent and what came back
5. **The fix**, in code or in one precise sentence

Then one final entry: **what I was unsure about**, naming something specific. It is scored, and a
blank costs more than a wrong guess.

### How to spend 40 minutes

- **First 5:** start it, use it once as a volunteer would.
- **Next 15:** the five things to try above. Write down every surprise.
- **Next 10:** read `app.py` and `templates/volunteer.html` against Part A.
- **Last 10:** write up. Stop the server.

---

## Scoring

Five defects, one point each, plus one for the unsure-about entry. **Your instructor states the
security weighting before you start.**

**Four of five is a strong score.**
