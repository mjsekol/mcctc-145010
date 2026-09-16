# Lab W05-01 · Open Mic Sign-Up
## 145010 Web Design & Senior Capstone · Unit 5 · Week 5, Monday and Tuesday

**Competencies:** 6.4.1 design a form from specifications · 6.4.2 add a form to a page · 6.4.3 add
text fields, radio buttons, check boxes, and drop-down menus · 6.4.4 explain a form action · 6.4.5
add working submit and reset buttons · 6.4.6 format a form with fieldset · 6.4.7 interact with a
database and a web service · 1.4.6 use an electronic database

**Time:** Monday Build 1 and Build 2, Tuesday Build 1 and Build 2. **Due at the end of Tuesday
Build 2.**

---

## The situation

A coffee shop runs a teen open mic night once a month. Performers sign up on a clipboard, and every
month two people get the same slot, somebody's email is unreadable, and nobody knows who needs a
microphone until the night. The shop wants a sign-up page that feeds a list the host can read.

*The Bean Counter is invented for this lab. Every name and address you type must be invented too,
with an address ending in `example.com`.*

**What you will build:** a form, written from a specification, that sends every answer to a real
Flask and SQLite server, which stores it and lists it.

---

## Before you start

Copy `lab-w05-files/` into your repository as `labs/w05/`. You will use this folder for this lab and
for Lab W05-02 on Wednesday and Thursday.

| File | What it is | You change it |
|---|---|---|
| `app.py` | The Flask server. Everything works except `/signup`. | Step 9 |
| `schema.sql` | The database: four slots, three invented sign-ups | No |
| `validation.py`, `test_validation.py` | Wednesday's work | Not yet |
| `send_raw.py` | Wednesday's tool | No |
| `save_page.py` | Saves a page so `web-check` can read it | No |
| `templates/signup.html` | The form page. **The form is missing.** | Steps 3 to 8 |
| `templates/echo.html`, `templates/signups.html` | The echo page and the list page | No |
| `static/signup.css` | Styles for everything | No |
| `static/signup.js` | Part 1 reads the web service. Part 2 is Thursday's. | No |

Create `labs/w05/lab-notes.md`. Every step that says **record** goes there.

**The server takes its port every time. This lab uses 8405.** Stop it with Ctrl+C at the end of every
period.

**Rules.** Gate 3 conditions: any tool, including an AI assistant, logged. The form markup in steps 3
to 6 is written by you, because writing a form from a specification is the competency.

---

## The specification

Build exactly this. The `name` values are the contract with the server. Do not change them.

| Label a person sees | Control | `name` | `id` | Values and rules |
|---|---|---|---|---|
| Stage name (required) | text | `performer_name` | `performer-name` | required, 2 to 40 characters, hint "2 to 40 characters. This is what the host reads out." |
| Email for your confirmation (required) | email | `email` | `email` | required, at most 254 characters, hint about using an example.com address |
| Kind of act (required) | radio group in a fieldset with that legend | `act_type` | `act-music`, `act-comedy`, `act-poetry`, `act-other` | values `music`, `comedy`, `poetry`, `other`, labels Music, Comedy, Poetry, Something else |
| Time slot (required) | select | `slot` | `slot` | first option "Choose a time" with an empty value, then one option per slot from the database |
| Length of your act, in minutes (required) | number | `minutes` | `minutes` | required, 1 to 8, whole numbers |
| What you need from us (optional) | checkbox group in a fieldset with that legend | `needs` | `need-mic`, `need-amp`, `need-bench` | values `mic`, `amp`, `bench`, labels A microphone, An amplifier, A piano bench |
| I agree to the house rules (required) | checkbox | `agree` | `agree` | value `yes`, required |
| Sign up | submit button | | | |
| Reset the form | reset button | | | |

Group the stage name and email in a fieldset with the legend "About you", and the slot and minutes in
one with the legend "Your slot". The form element itself has `id="signup-form"`.

Wrap each text, email, select, and number control, with its label and hint, in
`<div class="field">`. Wrap each radio or checkbox and its label in `<div class="choice">`. The CSS
expects those classes.

---

## Steps

### Part A · Monday · Named, labelled, grouped

**Step 1. Start the server.** In a terminal, in `labs/w05/`:

```
python app.py --port 8405 --reset
```

*You should see:* `Database rebuilt: openmic.db`, then
`Open Mic sign-ups at http://127.0.0.1:8405/  (Ctrl+C to stop)`. Open that address. The page has a
heading and a link, and no form.

**Step 2. Read the specification table** above, all of it, before you type. **Record** one sentence:
which three controls in it send something different from what the person sees?

**Step 3. The form and the first fieldset.** In `templates/signup.html`, replace the comment that
says your form goes here with a `<form>` whose `id` is `signup-form`, whose `action` is `/echo`, and
whose `method` is `get`. Inside it, write the "About you" fieldset with the stage name and email,
each with a label, a hint paragraph with an `id`, and the attributes in the table. Add a submit
button so you can test.

*You should see:* after a reload, the two fields. Clicking a label puts the cursor in its box.

**Step 4. Send it, then break it on purpose.** Type an invented stage name and address and press
Enter. **Record** the full address the browser went to, and the rows on the echo page.

Now delete `name="email"` from the email input, reload the form, and send it again. **Record** what
changed on the echo page and whether anything warned you. Then put the name back.

*You should see:* the email vanishes from the address and the echo page, and nothing warns you.

**Step 5. The act, the slot, and the minutes.** Add the "Kind of act" fieldset with its four radios,
and the "Your slot" fieldset. For the slot options, use this loop, which reads the slots the server
passes to the page:

```html
<select id="slot" name="slot" required>
  <option value="">Choose a time</option>
  {% for s in slots %}
  <option value="{{ s.id }}">{{ s.label }}, {{ s.places_left }} places left</option>
  {% endfor %}
</select>
```

*You should see:* four time options with places left. A slot with no room says "0 places left".
Tab into the radio group once, then use the arrow keys to move between the choices.

**Step 6. The needs, the agreement, and the buttons.** Add the "What you need from us" fieldset with
three checkboxes that **share** `name="needs"`, the agreement checkbox, and the submit and reset
buttons in `<div class="buttons">`. Then send the form with two needs ticked and the agreement not
ticked.

*You should see:* `needs` appears twice on the echo page, and `agree` does not appear at all.
**Record** why each of those happened.

**Step 7. Check it.** With the server running, in a second terminal in `labs/w05/`:

```
python save_page.py --port 8405 home saved/form.html
```

Then, from the repository root:

```
node tools/web-check/check.js labs/w05/saved/form.html
```

Adjust the path if your repository keeps labs somewhere else. Then take your hand off the mouse and
Tab through the whole form.

*You should see:* `PASS`, and a Tab order that matches the order on screen. **Record** the checker
output. If it fails, fix what it names, save again, and check again. Stop the server with Ctrl+C.

### Part B · Tuesday · Where the data goes

**Step 8. Point the form at the server.** Change the form's `action` to `/signup` and its `method`
to `post`. Start the server again, without `--reset`. Open dev tools, **Network** panel, and tick
**Preserve log**. Fill the form and press Sign up.

*You should see:* a page that says `The /signup route is not written yet. See Lab W05-01, step 9.`
In the Network panel, a `signup` row with method POST and status **501**. Click it and open
**Payload**. **Record** the payload text exactly.

**Step 9. Store it.** In `app.py`, write the `/signup` route the TODO describes: open the database
with `with open_db() as db:`, INSERT one row using `?` placeholders and the values from
`request.form`, store the needs joined with commas, and return
`redirect(url_for("list_signups", added=new_id), code=303)`. Stop and restart the server so it loads
your change.

*You should see:* after Sign up, the list page with your row highlighted and "You are signed up."
In the Network panel, `signup` with status **303**, then `signups?added=...` with 200. **Record**
both rows.

**Step 10. Break the action on purpose.** In the Elements panel, change the form's `method` to
`get` and submit.

*You should see:* `Method Not Allowed` and `The method is not allowed for the requested URL.`
**Record** the status code and one sentence on why. Reload the page to put the method back.

**Step 11. The web service.** Open `http://127.0.0.1:8405/api/slots` in a new tab. **Record** the
JSON. Then go back to the form, keep the Network panel open, and Tab into the slot list.

*You should see:* a new row named `slots` in the Network panel the moment the list gets focus, and
option text that says how many places are left. A full slot is greyed out.

Read Part 1 of `static/signup.js`. **Record** a paragraph of four to six sentences: what a web
service is, which line calls it, what the page does with the answer, and why the server must still
check whether a slot is full when someone presses Sign up.

**Step 12. Submit.** Stop the server with Ctrl+C and **record** the last lines the terminal shows.
Commit and push.

---

## Acceptance criteria

- [ ] The form matches the specification: every name, id, label, legend, value, and attribute
- [ ] Radio buttons share one name, checkboxes in the group share one name
- [ ] `lab-notes.md` has the GET address, the missing-email result, and the `needs` and `agree` explanation
- [ ] `web-check` reports PASS on the saved page, output recorded
- [ ] The form posts to `/signup`, and a submission appears on `/signups`
- [ ] The INSERT uses `?` placeholders for every value
- [ ] The Payload text, the 303, and the 405 are recorded
- [ ] The `/api/slots` JSON and the web service paragraph are recorded
- [ ] Every data value you typed is invented

---

## If it breaks

| What you see | What it means |
|---|---|
| `Port 8405 is already in use. Stop the other server first (find its terminal and press Ctrl+C).` | A server is still running from earlier. Find its terminal and press Ctrl+C. |
| `jinja2.exceptions.TemplateSyntaxError` in the terminal and `Internal Server Error` in the browser | A `{%` or `{{` in the template is not closed. The terminal names the line. |
| A field is missing on the echo page | That control has no `name`, or its checkbox was not ticked. |
| `405 Method Not Allowed` | The form's method does not match the route. `/signup` takes POST only. |
| `400 Bad Request` with "The browser (or proxy) sent a request that this server could not understand." | You read a field with `request.form["..."]` and it was not sent. Use `request.form.get("...")`. |
| Your change to `app.py` does nothing | The server was not restarted, or an old server is still running. Stop every server and start one. |
| `The /signup route is not written yet` after step 9 | The server is still running the old code. Restart it. |

---

## Stretch goal

Add a `<textarea name="intro">` for a one-line introduction the host can read aloud, at most 80
characters, with a hint. Store it: you will need to add a column, which means adding it to
`schema.sql` and rebuilding with `--reset`. **Record** what happened to the existing sign-ups when
you did.

---

## Submission checklist

- [ ] `labs/w05/templates/signup.html` with the complete form
- [ ] `labs/w05/app.py` with the `/signup` route
- [ ] `labs/w05/lab-notes.md` with every record item
- [ ] `labs/w05/saved/form.html` and the checker output
- [ ] Every server stopped
- [ ] AI usage log entry for any AI use
- [ ] Committed and pushed by the end of Tuesday Build 2

---

## Extended options

All four assess the same competencies and are graded on the same scale.

### Three observable signals for choosing

| What you see by the end of Monday Build 1 | Give them |
|---|---|
| Still on step 3, or labels not tied to inputs | SCAFFOLDED |
| Step 4 recorded with the missing-email result | STANDARD |
| Finished Part A early and asking about JSON or APIs | EXTENDED |
| Says a coffee shop open mic is not their thing | APPLIED |

### SCAFFOLDED

Your instructor gives you the "About you" fieldset already written, as a model. You write the other
three groups by copying its pattern, and you check in with your instructor after step 5 and after
step 9. Steps 10 and 11 are the same. For step 11's paragraph, finish these three sentence starters:
"A web service is...", "The page uses the answer to...", "The server still checks because...".

### STANDARD

The lab as written.

### EXTENDED

Everything in STANDARD, plus a second web service: `GET /api/signups` returning every sign-up as
JSON, **without** the email addresses. Then answer in writing: which fields did you leave out, why,
and who could call this address.

*Hint, not the answer:* look at how `api_slots` builds its list in `app.py`, and at what the
`/signups` page already chooses not to show.

### APPLIED

Same skills, a form you specify yourself for something real in your life: a carpool sign-up for a
team, a lunch order for a club meeting, a tryout sign-up. Your specification table comes first, in
the same columns as the one above, with at least one of every control type. Then build it against
the same server by copying `app.py` and changing the table and the route. Invented data only.
