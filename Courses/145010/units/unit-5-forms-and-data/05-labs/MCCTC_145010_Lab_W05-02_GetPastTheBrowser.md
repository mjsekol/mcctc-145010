# Lab W05-02 · Get Past the Browser
## 145010 Web Design & Senior Capstone · Unit 5 · Week 5, Wednesday and Thursday

**Competencies:** 6.4.7 code scripting to interact with data sources · 1.4.6 use an electronic
database · 6.4.6 format a form with tabindex · 6.4.2 add a form to a page · 6.4.3 form inputs and
their attributes

**Time:** Wednesday Build 1 and the first 25 minutes of Build 2, Thursday Build 1 and the first 25
minutes of Build 2. **Due 25 minutes into Thursday Build 2.**

---

## The situation

The open mic sign-up from Lab W05-01 works when people use it the way you did. The shop's owner
heard that a regular typed "a lot" into the minutes box and the host read out a 90-minute slot. She
wants to know how that could happen when the box only takes numbers, and she wants it to never
happen again, without making the form harder for anyone to use.

*The Bean Counter is invented for this lab. Every value you send must be invented.*

**What you will build:** server-side rules that refuse anything wrong no matter how it was sent,
and an error page that tells every person, including keyboard and screen reader users, exactly what
to fix.

---

## Before you start

Keep working in `labs/w05/` from Lab W05-01. Your form posts to `/signup` and your route stores what
arrives. **This lab starts by attacking that route.**

Open two terminals in `labs/w05/`: one for the server, one for `send_raw.py`.

Read `03-lecture-notes/MCCTC_145010_Notes_TwoLayersOfValidation.md` before Part A and
`03-lecture-notes/MCCTC_145010_Notes_AccessibleErrors.md` before Part B if you missed either day.

**Rules.** Gate 3 conditions, AI use logged. **Steps 2, 3, and 16 are done by you, by hand,**
because seeing the failure is the point.

---

## Part A · Wednesday · The server is the defence

**Step 1. Start fresh.**

```
python app.py --port 8405 --reset
```

*You should see:* `Database rebuilt: openmic.db` and the address line.

**Step 2. Go around the page, twice.** In the second terminal:

```
python send_raw.py --port 8405 naive
```

Open `http://127.0.0.1:8405/signups`. Then, in the browser, open the form, press F12, delete the
`required` attribute from the stage name in the **Elements** panel, leave the name empty, fill the
rest, and press Sign up.

*You should see:* a 303 from `send_raw.py`, a row on `/signups` with no name, act `fire-juggling`,
and minutes `banana`, and your own empty-name sign-up stored too. **Record** both, and one sentence on
why the form's `required` did not stop either.

**Step 3. Attack your own route.**

```
python send_raw.py --port 8405 garbage
```

*You should see:* `status: 303`. Your Tuesday route stored it. **Record** the output.

**Step 4. Write the rules.** Open `validation.py`. Write `validate_signup` so it follows the rules in
its docstring and uses **exactly** these messages:

| Field | When | Message |
|---|---|---|
| `performer_name` | not 2 to 40 characters after trimming | `Enter a stage name between 2 and 40 characters.` |
| `email` | empty after trimming | `Enter an email address so we can confirm your slot.` |
| `email` | over 254 characters, or no match for `EMAIL_PATTERN` | `Enter an email address in the form name@example.com.` |
| `act_type` | not in `ACT_TYPES` | `Choose the kind of act: music, comedy, poetry, or other.` |
| `slot` | not a whole number, or not a key in `open_slots` | `Choose a time slot from the list.` |
| `slot` | a real slot with 0 places left | `That slot is now full. Choose another time.` |
| `minutes` | not one or two digits, or not 1 to 8 | `Enter how long your act is, a whole number from 1 to 8 minutes.` |
| `needs` | any value not in `NEEDS`, or any value twice | `Choose only from the equipment listed.` |
| `agree` | not exactly `yes` | `Tick the box to agree to the house rules.` |

Put the trimmed, typed values in `clean`: the name and email as trimmed text, the slot as an `int`,
the minutes as an `int` when valid, and the needs as a sorted list.

Turning `slot` into a number can fail. Use `try` and `except ValueError`, as you did in 145060.

**Step 5. Run the tests after every field.**

```
python test_validation.py
```

*You should see,* at the start, `FAILED (failures=16, errors=3)`. At the end:

```
Ran 15 tests in 0.00?s

OK
```

Do not change the test file. **Record** the final output.

**Step 6. Use it.** In `app.py`, change `/signup` as the Wednesday TODO describes. Build
`open_slots`, call `validate_signup`, and **store nothing if there are errors**. Store the `clean`
values, not the raw ones. For today, when there are errors, return this, which Thursday replaces:

```python
return "Refused: " + " ".join(errors.values()), 400
```

Restart the server.

**Step 7. Attack it again.**

```
python send_raw.py --port 8405 garbage
python send_raw.py --port 8405 full
python send_raw.py --port 8405 good
```

*You should see:* `status: 400`, `status: 400`, and `status: 303` with a `redirected to` line.
Reload `/signups`: the good sign-up is there and nothing new from the other two. **Record** all
three outputs.

**Step 8. The Elements trick again.** Delete `required` from the stage name in the browser, leave it
empty, and submit.

*You should see:* a plain page that begins `Refused: Enter a stage name between 2 and 40
characters.` The browser was fooled. The server was not. **Record** it.

---

## Part B · Thursday · Errors people can find

**Step 9. The title and the summary.** In `templates/signup.html`:

1. Make the `<title>` start with `Error: ` when there are errors: `{% if errors %}Error: {% endif %}`.
2. At the top of `<main>`, add the summary, only when there are errors:

```html
{% if errors %}
<div class="error-summary" id="error-summary" tabindex="-1" aria-labelledby="error-summary-title">
  <h2 id="error-summary-title">There {{ "is a problem" if errors | length == 1 else "are " ~ (errors | length) ~ " problems" }} with your sign-up</h2>
  <ul>
    {% for field, message in errors.items() %}
    <li><a href="#{{ field_ids[field] }}">{{ message }}</a></li>
    {% endfor %}
  </ul>
</div>
{% endif %}
```

*You should see:* nothing yet. The route still returns the plain text from step 6.

**Step 10. Tie each message to its field.** For every field, use the two macros at the top of the
template:

- `{{- error_for("email") }}` on the line **before** the input, after its hint
- `{{ described("email", "email-hint") }}` **inside** the input's opening tag, after the last
  attribute, replacing any `aria-describedby` you wrote on Monday

For the two groups, give the fieldsets `id="act-fieldset"` and `id="needs-fieldset"`, put
`{{ described("act_type") }}` or `{{ described("needs") }}` inside the fieldset tag, and put the
`error_for` line straight after the legend. For the agreement, put `{{- error_for("agree") }}` before
its `<div class="choice">`.

Then keep the answers. Add `value="{{ values.get('performer_name', '') }}"` to the text inputs, the
same for email and minutes, `checked` to the chosen radio and ticked boxes, and `selected` to the
chosen slot. If you wrote each radio out by hand on Monday, compare with its own value, such as
`values.get('act_type') == 'music'`. The pattern, written as a loop, is:

```html
<input type="radio" id="act-{{ value }}" name="act_type" value="{{ value }}" required
       {%- if values.get('act_type') == value %} checked{% endif %}>
```

**Step 11. Send the page back.** In `/signup`, replace the step 6 line with a real page:

```python
values = {name: request.form.get(name, "") for name in FIELD_IDS}
values["needs"] = request.form.getlist("needs")
return render_template("signup.html", slots=slot_rows(db), errors=errors,
                       values=values, field_ids=FIELD_IDS), 400
```

Restart the server. With JavaScript turned off in dev tools (Ctrl+Shift+P, "Disable JavaScript"),
delete `required` from every field and submit an empty form. Turn JavaScript back on afterwards.

*You should see:* the form again, a title starting `Error:`, a summary listing the problems, a
message next to each field, and anything you had typed still in place. Then save it and check it:

```
python save_page.py --port 8405 signup saved/form-errors.html --post
node tools/web-check/check.js labs/w05/saved/form-errors.html
```

The second command runs from the repository root. *You should see:* `PASS`. **Record** it.

**Step 12. The same rules in the browser.** In `static/signup.js`, write `checkForm()`. Use
`new FormData(form)` and `data.get(...)`, apply the same rules as `validation.py` for the stage name,
email, act, slot, minutes, and agreement, and use the sentences in `MESSAGES`. For the slot, also
treat a disabled option as not chosen. Return an object like `{ email: MESSAGES.email_format }`.

*You should see:* in the Console, `checkForm()` on an empty form returns six problems.

**Step 13. Show them.** Write `showErrors(errors)` following the four numbered parts of its TODO.
Build everything with `createElement` and `textContent`. Add the message id to any
`aria-describedby` already on the element, so the hint stays.

*You should see:* `showErrors(checkForm())` in the Console draws the summary and the messages and
puts focus on the summary.

**Step 14. Take over the submit.** Set `form.noValidate = true` in the script, not in the HTML.
Listen for `submit`. When `checkForm()` finds problems, call `event.preventDefault()` and
`showErrors(...)`.

*You should see:* an empty submit draws the summary, sends nothing (the Network panel stays empty),
and a second empty submit still shows **one** summary, not two.

**Step 15. Focus on arrival.** Add one line at the end of the script: if the page arrived with an
`#error-summary`, move focus to it.

*You should see:* after step 11's bypass, focus on the summary as soon as the page loads.

**Step 16. Test it the way people use it.**

1. Hand off the mouse. Submit the empty form with Enter. **Record** where focus went.
2. Press Tab, then Enter on the first summary link. **Record** where focus went.
3. In the Console, run `document.querySelector("#agree").setAttribute("tabindex", "1")`, click the
   address bar, and press Tab four times. **Record** the order. Reload to undo it.
4. Turn on Narrator (Windows key + Ctrl + Enter). Submit the empty form, then Tab to the email field.
   **Record** what Narrator says at each point, in its words. Turn Narrator off the same way.

**Step 17. Submit.** Stop the server. Commit and push.

---

## Acceptance criteria

- [ ] Step 2 and step 3 records show garbage stored before any validation existed
- [ ] `python test_validation.py` prints `OK`, and `test_validation.py` is unchanged
- [ ] `/signup` stores only `clean` values and stores nothing when there are errors
- [ ] `garbage` and `full` get 400, `good` gets 303
- [ ] The server's error page has all six parts: title, summary with links, focus, messages tied with
      `aria-describedby`, `aria-invalid`, kept answers
- [ ] `web-check` reports PASS on the saved error page
- [ ] An empty submit with script on sends nothing and moves focus to one summary
- [ ] No `innerHTML` anywhere in `signup.js`
- [ ] No positive `tabindex` anywhere
- [ ] The step 16 records, including Narrator's words

---

## If it breaks

| What you see | What it means |
|---|---|
| `AttributeError: 'NoneType' object has no attribute 'strip'` | A field that was not sent came back as `None` from `form.get(...)`. Write `(form.get("performer_name") or "").strip()`. |
| `TypeError: cannot unpack non-iterable NoneType object` | `validate_signup` does not end with `return clean, errors`. |
| `ValueError: invalid literal for int() with base 10: '3am'` in the terminal, and an error page | The slot conversion is not inside `try`. |
| A test says `expected only slot, got ['slot', 'minutes']` | One field's rule is too strict, or two rules share a field name. Read which field the test changed. |
| `jinja2.exceptions.UndefinedError: 'values' is undefined` | A `render_template` call does not pass `values`. The GET route already passes `values={}`. |
| Two summaries appear after two submits | `showErrors` does not call `clearErrors()` first. |
| The browser's own bubble appears instead of your summary | `form.noValidate = true` is missing, or the script failed to load. Check the Console. |
| Focus does not move to the summary | The summary has no `tabindex="-1"`, so it cannot take focus. |

---

## Stretch goal

Add one more server rule that only the database can check: the same stage name cannot sign up twice
on the same night. Choose the message yourself, add a test for it to a **new** test file, and explain
in `lab-notes.md` why this rule cannot live in the browser at all.

---

## Submission checklist

- [ ] `validation.py`, `app.py`, `templates/signup.html`, `static/signup.js`
- [ ] `saved/form-errors.html` and its checker output
- [ ] `lab-notes.md` with every record item from steps 2 to 16
- [ ] Every server stopped
- [ ] AI usage log entry for any AI use
- [ ] Committed and pushed 25 minutes into Thursday Build 2

---

## Extended options

All four assess the same competencies and are graded on the same scale.

### Three observable signals for choosing

| What you see by the middle of Wednesday Build 1 | Give them |
|---|---|
| Tests still show more than 10 failures after 20 minutes | SCAFFOLDED |
| Tests passing field by field, records complete | STANDARD |
| Tests passing early, asking whether the database could enforce this | EXTENDED |
| Asking what any of this has to do with their own project | APPLIED |

### SCAFFOLDED

Your instructor gives you `validation.py` with the name, email, and act rules already written. You
write the slot, minutes, needs, and agree rules. On Thursday your instructor gives you a finished
`showErrors`; you write `checkForm`, the submit listener, and the focus line. Check in after step 5
and after step 11.

### STANDARD

The lab as written.

### EXTENDED

Everything in STANDARD, plus a **third layer**. Add `CHECK` constraints to `schema.sql` so the
database itself refuses a minutes value outside 1 to 8 and an act type outside the four allowed.
Rebuild with `--reset`, run `python send_raw.py --port 8405 naive`, and explain in writing what the
person sees, why, and why the constraints are still worth having.

*Hint, not the answer:* the SQLite documentation's page on `CREATE TABLE` has a section on CHECK
constraints. Remember that the minutes column is stored as text in this schema.

### APPLIED

Take the form you designed for Lab W05-01 APPLIED, or specify one now for something in your life.
Write its server rules, with a test file of at least ten tests, and give it the full six-part error
pattern. Then run `send_raw.py`-style requests against it by copying `send_raw.py` and changing the
fields.
