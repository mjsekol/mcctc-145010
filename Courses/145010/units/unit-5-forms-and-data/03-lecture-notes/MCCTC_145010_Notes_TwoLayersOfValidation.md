# Lecture Notes: Two Layers of Validation
## 145010 Web Design & Senior Capstone · Unit 5 · Week 5, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W05_TwoLayers.md).
There is no exported deck yet. To generate one, from the repository root:
`node tools/gamma.js Courses/145010/units/unit-5-forms-and-data/04-slides/MCCTC_145010_Slides_W05_TwoLayers.md --export pptx`

If you missed class, you can learn this concept from this file alone, with the lab app running on
port 8405 and a second terminal open in the same folder.

**Competencies:** 6.4.7 code scripting to interact with data sources · 1.4.6 use an electronic
database to create business and technical information · 6.4.3 the attributes that make inputs check
themselves.

---

## Why this exists

This is the most important sentence of the week, and possibly of the course's web half:

> **Client-side validation is a convenience. Server-side validation is the defence.**

Everything the browser checks runs on a computer the person controls. That is fine for helping
honest people. It protects nothing. A database full of empty names, impossible numbers, and
over-booked slots is what you get when a server believes the page.

---

## The concept in plain language

**The browser's checks are attributes.** You have seen them:

| Attribute | What the browser does |
|---|---|
| `required` | Refuses to send if empty |
| `type="email"` | Refuses text without an `@` and a sensible shape |
| `min`, `max`, `step` on a number | Refuses numbers out of range |
| `minlength`, `maxlength` | Refuses text that is too short, and stops typing past the maximum |
| `pattern` | Refuses text that does not match a regular expression |

When one fails, the browser shows its own message. Verified in Chrome 153:

```
Please fill out this field.
Please include an '@' in the email address. 'casey' is missing an '@'.
Value must be less than or equal to 8.
```

**Every one of them can be skipped.** Four ways, all used in the lab:

1. Delete the attribute in the Elements panel, then submit.
2. Call `form.submit()` in the Console. It sends the form without running any checks or any submit
   listener.
3. Turn JavaScript off, if the checks are written in JavaScript.
4. Send the request from a program. `send_raw.py` does this in six lines of standard library.

**So the server checks every rule, again, on every request.** It checks what the form promised:
lengths, formats, allowed choices. It also checks what only the server knows: whether the slot still
has room, whether the choice exists in the database. When anything fails, it stores nothing and
answers **400**, with messages a person can act on.

**A database constraint is a third layer, not a replacement.** A `CHECK` or foreign key refuses bad
data at the last moment, but it refuses by raising an error, which the person sees as a crash page.

---

## Worked example 1: the server that believes the page

The lab app ships a route that stores whatever arrives, labelled DO NOT COPY:

```python
@app.post("/naive/signup")
def naive_signup():
    with open_db() as db:
        db.execute(
            "INSERT INTO signups (performer_name, email, act_type, slot_id, minutes, needs, source) "
            "VALUES (?, ?, ?, ?, ?, ?, 'naive')",
            (request.form.get("performer_name", ""), request.form.get("email", ""),
             request.form.get("act_type", ""), request.form.get("slot", "1"),
             request.form.get("minutes", ""), ",".join(request.form.getlist("needs"))),
        )
    return redirect(url_for("list_signups"), code=303)
```

Send it garbage, from a second terminal:

```
python send_raw.py --port 8405 naive
```

```
POST /naive/signup
body: performer_name=&email=not-an-email&act_type=fire-juggling&slot=1&minutes=banana&needs=fog+machine
status: 303
redirected to: /signups
```

`/signups` now has a row with no stage name, act `fire-juggling`, and minutes `banana`, in slot 1,
which was already full. The placeholders did their job: nothing was injected. The data is still
wrong.

---

## Worked example 2: the server's rules

```python
def validate_signup(form, open_slots):
    errors = {}
    clean = {}

    name = (form.get("performer_name") or "").strip()
    if not (2 <= len(name) <= 40):
        errors["performer_name"] = "Enter a stage name between 2 and 40 characters."
    clean["performer_name"] = name

    act = form.get("act_type") or ""
    if act not in {"music", "comedy", "poetry", "other"}:
        errors["act_type"] = "Choose the kind of act: music, comedy, poetry, or other."
    clean["act_type"] = act

    slot_text = form.get("slot") or ""
    try:
        slot_id = int(slot_text)
    except ValueError:
        slot_id = None
    if slot_id not in open_slots:
        errors["slot"] = "Choose a time slot from the list."
    elif open_slots[slot_id] <= 0:
        errors["slot"] = "That slot is now full. Choose another time."
    clean["slot"] = slot_id

    # ... email, minutes, needs, agree in the same shape ...
    return clean, errors
```

Three habits in it. **Trim before measuring**, so `"   "` counts as empty. **Check against a list of
allowed values**, never against "looks reasonable". **Report every problem at once**, so the person
fixes them in one pass.

The route uses it before it stores anything:

```python
open_slots = {row["id"]: row["places_left"] for row in slot_rows(db)}
clean, errors = validate_signup(request.form, open_slots)
if errors:
    ...  # store nothing, answer 400
```

---

## Worked example 3: the same garbage, to the defended route

```
python send_raw.py --port 8405 garbage
```

Verified output:

```
POST /signup
body: performer_name=&email=not-an-email&act_type=fire-juggling&slot=1&minutes=banana&needs=fog+machine
status: 400
  server said: Enter a stage name between 2 and 40 characters.
  server said: Enter an email address in the form name@example.com.
  server said: Choose the kind of act: music, comedy, poetry, or other.
  server said: That slot is now full. Choose another time.
  server said: Enter how long your act is, a whole number from 1 to 8 minutes.
  server said: Choose only from the equipment listed.
  server said: Tick the box to agree to the house rules.
```

Seven problems, seven sentences, nothing stored. And a correct request still works:

```
python send_raw.py --port 8405 good
```

```
status: 303
redirected to: /signups?added=5
```

The number is 5 because the naive row from example 1 took number 4 on a freshly reset database.

---

## The wrong version, and what it produces

The wrong version is example 1, and its output is a database with rows no form could have made.
There is a second wrong version worth knowing, the one that relies on the database alone:

```
python send_raw.py --port 8405 badslot
```

```
POST /naive/signup
body: performer_name=&email=not-an-email&act_type=fire-juggling&slot=99&minutes=banana&needs=fog+machine
status: 500
  the server failed while handling this request
```

The foreign key refused slot 99, so nothing was stored. The person got a crash page, and every other
bad value would have been stored if the slot had been real.

---

## Why the wrong version is tempting

You test your form by using it, and when you use it, the browser checks everything. The server code
never sees a bad request on your machine, so it never looks unfinished. And "I already checked that
in the HTML" sounds like a finished thought.

The habit that prevents it: **for every rule in your form, point at the line in the server that
checks it again.** If you cannot, the rule is decoration.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Client-side validation** | Checks the browser runs before sending. A convenience. |
| **Server-side validation** | Checks the server runs on what arrived. The defence. |
| **Constraint validation** | The browser's built-in checks from `required`, `type`, `min`, `max`, `pattern` |
| **`form.submit()`** | Sends a form with no checks and no submit event |
| **Allow list** | The set of values that are accepted. Anything else is refused. |
| **400 Bad Request** | The server's answer when it refuses what was sent |
| **Database constraint** | A rule in the database itself, such as a foreign key or CHECK |

---

## Self-check

**Question 1.** Name four ways to get a form's data to the server without the browser's
`required` check stopping it.

**Question 2.** Why does `validate_signup` need `open_slots`, when the form's own select only offers
real slots?

**Question 3.** A route uses `?` placeholders for every value. A teammate says that makes validation
unnecessary. What is right and wrong in that?

---

### Answers

**1.** Delete `required` in the Elements panel; call `form.submit()`; turn off the script if the
check is in JavaScript; send the request from a program such as `send_raw.py`. Accept `curl` or any
HTTP tool for the last one.

**2.** Because a request does not have to come from the select. `slot=99` or `slot=3am` can be sent
directly, and a real slot can fill up between loading the page and submitting it. Only the database
knows how many places are left.

**3.** Right: placeholders stop the values from changing the SQL, so they prevent injection. Wrong:
they store whatever arrives, exactly as sent, so an empty name, `banana` minutes, and an over-booked
slot all go in. Safe to store and valid to store are different questions.
