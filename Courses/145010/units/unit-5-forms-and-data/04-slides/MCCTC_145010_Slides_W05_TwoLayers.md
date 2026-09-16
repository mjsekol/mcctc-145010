# Two Layers of Validation
---
## Slide 1: The form said required. The database says otherwise.
- A sign-up with no name
- Minutes: banana
- Act: fire-juggling
- The form made none of that possible
Speaker notes: This row is in our database. The form has required on the name, a number box for minutes, and radio buttons for the act. None of those could have produced this row. And yet here it is. Today you will put it there yourself, in about ten seconds, and then write the code that stops it.
Image: A database table with one row of plainly wrong values highlighted in red.
---
## Slide 2: The sentence for the week
- Client-side validation is a convenience
- Server-side validation is the defence
- The browser belongs to the person using it
- The server belongs to you
Speaker notes: Write this down. Checks in the browser help honest people fix mistakes before a round trip. They run on a computer the person controls, so they protect nothing. The server checks every rule again, on every request, because it is the only part of the system you control.
Image: A small helpful sign on a door, and a locked gate behind it.
---
## Slide 3: The browser's checks
- required, type, min, max, minlength, maxlength, pattern
- The browser refuses to send
- It shows its own message
- Please fill out this field.
Speaker notes: These attributes are good, and you should keep using them. When one fails, Chrome shows its own bubble. We captured the real text: please fill out this field, and for an email without an at sign, please include an at in the email address. They are a kindness. They are not a lock.
Image: A form field with Chrome's validation bubble pointing at it.
---
## Slide 4: Four ways past them
- Delete the attribute in the Elements panel
- Call form.submit() in the Console
- Turn off the script that checks
- Send the request from a program
Speaker notes: Every one of these takes under a minute. The first two need nothing but dev tools. The last is how bots and scripts talk to servers every day. In the lab, send underscore raw dot p y does it in a handful of lines of standard library Python.
Image: Four paths around a small fence, each labelled.
---
## Slide 5: The wrong way, and what it stores
```
python send_raw.py --port 8405 naive

POST /naive/signup
body: performer_name=&email=not-an-email&act_type=fire-juggling&slot=1&minutes=banana&needs=fog+machine
status: 303
redirected to: /signups
```
Speaker notes: The naive route believes the page. It uses placeholders, so nothing was injected. It still stored an empty name, fire juggling, and banana minutes, into a slot that was already full. Safe to store and valid to store are different questions.
Image: None. This slide is code.
---
## Slide 6: The server's rules
```python
name = (form.get("performer_name") or "").strip()
if not (2 <= len(name) <= 40):
    errors["performer_name"] = "Enter a stage name between 2 and 40 characters."

act = form.get("act_type") or ""
if act not in {"music", "comedy", "poetry", "other"}:
    errors["act_type"] = "Choose the kind of act: music, comedy, poetry, or other."
```
Speaker notes: Three habits. Trim before measuring, so spaces do not count as a name. Check against a list of allowed values, never against looks reasonable. And collect every problem, so the person fixes them all in one go. The slot check also needs the database, because only the database knows how many places are left.
Image: None. This slide is code.
---
## Slide 7: The same garbage, defended
```
python send_raw.py --port 8405 garbage

status: 400
  server said: Enter a stage name between 2 and 40 characters.
  server said: Enter an email address in the form name@example.com.
  server said: Choose the kind of act: music, comedy, poetry, or other.
  server said: That slot is now full. Choose another time.
  server said: Enter how long your act is, a whole number from 1 to 8 minutes.
  server said: Choose only from the equipment listed.
  server said: Tick the box to agree to the house rules.
```
Speaker notes: Same request, sent to the defended route. Four hundred, seven sentences, nothing stored. And a correct request still gets its three oh three. That is the target for the end of today.
Image: None. This slide is code.
---
## Slide 8: The database is a third layer, not a second
- A foreign key refused slot 99
- Nothing was stored
- The person got a 500 crash page
- Every other bad value would have gone in
Speaker notes: Some people say let the database catch it. We tried. Sending slot ninety nine to the naive route gave a five hundred, because the foreign key refused it. That is a crash page for the person, and the database only knew about one of the seven problems. Constraints are worth having. They do not replace validation.
Image: Three layered shields labelled browser, server, database, with the middle one thickest.
---
## Slide 9: Point at the line
- For every rule in your form
- Point at the server line that checks it
- If you cannot, the rule is decoration
- The tests make you prove it
Speaker notes: Here is the habit to take into your capstone. Read your form, one attribute at a time, and point at the line on the server that checks the same thing. If there is no line, the rule only exists for honest people. The lab's test file has fifteen tests, and they will not pass until every rule has its line.
Image: A form on the left and server code on the right, with lines connecting matching rules.
---
## Slide 10: What you are about to build
- Lab W05-02, Part A
- Send garbage past the browser and record it
- Write validation.py until fifteen tests pass
- Wire it into /signup, then send the garbage again
Speaker notes: Build one: run the raw sender against your own app before you add any checks, and record what got stored. Then write validation dot p y until python test underscore validation dot p y prints O K. Build two: use it in your signup route and send the garbage again. You want four hundred for garbage, four hundred for a full slot, and three oh three for a good sign-up.
Image: A terminal showing Ran 15 tests and OK.
---
