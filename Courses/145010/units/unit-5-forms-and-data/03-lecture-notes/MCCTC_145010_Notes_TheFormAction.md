# Lecture Notes: The Form Action, and Where the Data Goes
## 145010 Web Design & Senior Capstone · Unit 5 · Week 5, Tuesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W05_TheFormAction.md).
There is no exported deck yet. To generate one, from the repository root:
`node tools/gamma.js Courses/145010/units/unit-5-forms-and-data/04-slides/MCCTC_145010_Slides_W05_TheFormAction.md --export pptx`

If you missed class, you can learn this concept from this file alone, with the lab app running on
port 8405.

**Competencies:** 6.4.4 explain the concept of a form action · 6.4.7 code scripting to interact
with data sources, including databases and web services · 1.4.6 use an electronic database to access
and create business and technical information.

---

## Why this exists

Yesterday your form sent its answers to a page that only showed them back. That proves the form
works. It does not do anything. Today the answers go somewhere that keeps them, and you watch the
whole trip happen in dev tools instead of taking it on trust.

When a form "does nothing" in your capstone, the Network panel is where you find out why.

---

## The concept in plain language

**The action is an address and a method.**

```html
<form action="/signup" method="post">
```

`action` is where the browser sends the answers. `method` is how.

| | GET | POST |
|---|---|---|
| Where the pairs go | In the address, after `?` | In the request body |
| Seen in | The address bar, history, bookmarks, server logs | The Network panel's Payload tab |
| Use it for | Searches and filters, which people bookmark and share | Anything that changes data: sign-ups, orders, logins |
| Refresh the result page | Sends it again, harmlessly | The browser warns before sending it again |

**POST is not secret.** It keeps the data out of the address. HTTPS is what encrypts it, for GET and
POST alike.

**The body of a POST uses the same encoding as a GET address:**
`performer_name=Nova+Park&email=nova.park%40example.com`, with the header
`Content-Type: application/x-www-form-urlencoded`. The `@` became `%40`.

**The server's side, in Flask:**

```python
@app.post("/signup")
def signup():
    name = request.form.get("performer_name", "")
```

`request.form` holds the POST pairs. `request.args` holds the GET pairs.

**After a successful POST, redirect.** The server answers `303 See Other` with a `Location`, and the
browser GETs that page. Refreshing the result page now repeats a harmless GET, not the sign-up. This
is called **Post/Redirect/Get**.

**A web service is the same server answering a script instead of a person.** `/api/slots` returns
JSON. JavaScript on the page asks for it with `fetch()`, and the page updates without submitting
anything.

---

## Worked example 1: watching a POST in dev tools

1. Open the form at `http://127.0.0.1:8405/`.
2. Dev tools, **Network** panel, tick **Preserve log**, so the list survives the redirect.
3. Fill the form and press **Sign up**.

The Network panel shows, among the rows:

| Name | Method | Status |
|---|---|---|
| `signup` | POST | 303 |
| `signups?added=4` | GET | 200 |

Click `signup`. **Headers** shows `Content-Type: application/x-www-form-urlencoded`. **Payload**
shows, verified on the build machine:

```
performer_name=Nova+Park&email=nova.park%40example.com&act_type=poetry&slot=3&minutes=4&needs=mic&agree=yes
```

That is the whole request, in plain text, in the order the controls appear in the form.

---

## Worked example 2: receiving and storing it

```python
@app.post("/signup")
def signup():
    with open_db() as db:
        # ? placeholders: the values travel separately from the SQL text, so
        # nothing a person typed can ever change the query.
        cursor = db.execute(
            """
            INSERT INTO signups (performer_name, email, act_type, slot_id, minutes, needs)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (request.form.get("performer_name", ""), request.form.get("email", ""),
             request.form.get("act_type", ""), request.form.get("slot", ""),
             request.form.get("minutes", ""), ",".join(request.form.getlist("needs"))),
        )
        new_id = cursor.lastrowid
    return redirect(url_for("list_signups", added=new_id), code=303)
```

After submitting, `/signups` shows the new row highlighted with "You are signed up. Your sign-up
number is 4." on a freshly reset database. This version stores whatever arrives. Wednesday fixes
that, and this example is exactly what Wednesday attacks.

`getlist("needs")` collects every ticked box. `",".join(...)` stores them as one text value, which is
simple and fine for a short list.

---

## Worked example 3: a web service, read by script

`http://127.0.0.1:8405/api/slots` returns, on a freshly reset database:

```json
[{"capacity":2,"id":1,"label":"7:00 pm","places_left":0},
 {"capacity":2,"id":2,"label":"7:20 pm","places_left":1},
 {"capacity":2,"id":3,"label":"7:40 pm","places_left":2},
 {"capacity":2,"id":4,"label":"8:00 pm","places_left":2}]
```

`signup.js` asks for it when the slot list gets focus:

```js
async function refreshSlots() {
  try {
    const response = await fetch("/api/slots");
    if (!response.ok) {
      return;
    }
    const slots = await response.json();
    for (const slot of slots) {
      const option = slotSelect.querySelector(`option[value="${slot.id}"]`);
      if (!option) {
        continue;
      }
      const left = slot.places_left;
      option.textContent = `${slot.label}, ${left > 0 ? left + " left" : "no places left"}`;
      option.disabled = left <= 0;
    }
  } catch (error) {
    console.warn("Could not refresh slots:", error.message);
  }
}
```

Focus the slot list with the Network panel open and a row named `slots` appears. Verified: the 7:00
pm option became `7:00 pm, no places left` and was disabled. **The server still checks** whether a
slot is full, because someone can take the last place between this request and Submit. The lab's
version of this function is slightly longer, with the singular "place".

---

## The wrong version, and the exact error

Change the form's method to GET, in the Elements panel, and submit. Flask answers:

```
405 Method Not Allowed
The method is not allowed for the requested URL.
```

`/signup` was written with `@app.post`, so it accepts POST only. The action has two parts, and both
have to match what the server expects.

A second one you will meet alone. Reading a field that was not sent with square brackets:

```python
agree = request.form["agree"]      # the box was not ticked
```

Flask answers:

```
400 Bad Request
The browser (or proxy) sent a request that this server could not understand.
```

Use `request.form.get("agree")`, which gives `None`, and check it.

---

## Why the wrong version is tempting

GET is the default. A form with no `method` sends GET, and a sign-up that "works" with GET puts
every answer in the address bar and in the history of a shared lab computer. The server refusing GET
is the server protecting you from that.

`request.form["agree"]` looks like every dictionary you have used. It is one, and it raises on a
missing key, and an unticked checkbox is a missing key.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Form action** | The address the form sends its answers to |
| **Method** | How: GET in the address, POST in the body |
| **Request body** | The data sent after the headers in a POST |
| **`application/x-www-form-urlencoded`** | The encoding a normal form uses: `name=value&name=value` |
| **Payload tab** | Where the Network panel shows a request's body |
| **Status code** | The server's one-number answer: 200 fine, 303 go here, 400 refused, 405 wrong method, 500 the server failed |
| **Post/Redirect/Get** | Answer a successful POST with a redirect, so a refresh cannot repeat it |
| **Web service** | An address that answers a program, often with JSON |
| **`fetch`** | The browser function a script uses to call a web service |
| **Placeholder** | A `?` in SQL, filled with a value that can never change the query |

---

## Self-check

**Question 1.** A sign-up form has no `method` attribute. What method does it use, and what problem
does that cause?

**Question 2.** You submit a form and the page changes, but the Network panel is empty. What did you
forget, and why did it matter?

**Question 3.** The slot list disables full slots using `/api/slots`. A teammate says the server no
longer needs to check for full slots. Give two reasons they are wrong.

---

### Answers

**1.** GET, the default. Every answer, including the email, ends up in the address bar, the browser
history, and the server's log of addresses.

**2.** **Preserve log.** The successful POST redirects to a new page, and without Preserve log the
Network panel clears on the new page, taking the POST with it.

**3.** Someone can take the last place between the page asking and the form being sent. And anyone
can send the form without the page at all, with a script or with the disabled option re-enabled in
dev tools.
