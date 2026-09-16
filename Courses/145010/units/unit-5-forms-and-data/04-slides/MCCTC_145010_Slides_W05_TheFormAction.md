# The Form Action, and Where the Data Goes
---
## Slide 1: You pressed Sign up. Then what?
- The page changed
- Did anything get saved?
- Where did your answers go?
- You can watch the whole trip
Speaker notes: Every form you have ever used made a promise when you pressed the button. Today you stop taking that promise on trust. Dev tools will show you the exact request your form sent, the exact answer the server gave, and the page it sent you to afterwards. When your capstone form does nothing, this is where you look.
Image: A sign-up button with a dotted path leading off-screen, labelled with a question mark.
---
## Slide 2: The action is an address and a method
```html
<form action="/signup" method="post">
```
Speaker notes: Two attributes. Action is where the answers go. Method is how. Leave method out and you get get, which is the default, and which is wrong for a sign-up.
Image: None. This slide is code.
---
## Slide 3: GET and POST carry the same pairs
- GET: in the address, after the question mark
- POST: in the request body
- Same encoding: name equals value, joined by ampersands
- Neither one is encrypted. HTTPS is.
Speaker notes: The difference is where the pairs travel, not what they look like. GET puts them in the address, so they land in history, bookmarks, and server logs, which is right for a search and wrong for a sign-up. POST puts them in the body. POST is not secret. Anyone with dev tools can read it, and only HTTPS encrypts either one.
Image: Two envelopes, one with writing on the outside and one with writing on a letter inside.
---
## Slide 4: What the Network panel shows
```
signup           POST   303
signups?added=4  GET    200

Payload:
performer_name=Nova+Park&email=nova.park%40example.com&act_type=poetry&slot=3&minutes=4&needs=mic&agree=yes
```
Speaker notes: This is the real capture from the build machine. The sign-up went out as a POST and the server answered three oh three, which means go and get this other page. The browser did, and got a two hundred. Click the signup row, open Payload, and there is every answer in plain text. Tick Preserve log first, or the redirect wipes the list.
Image: None. This slide is code.
---
## Slide 5: The server's side
```python
@app.post("/signup")
def signup():
    with open_db() as db:
        cursor = db.execute(
            "INSERT INTO signups (performer_name, email, act_type, slot_id, minutes, needs) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (request.form.get("performer_name", ""), request.form.get("email", ""),
             request.form.get("act_type", ""), request.form.get("slot", ""),
             request.form.get("minutes", ""), ",".join(request.form.getlist("needs"))),
        )
    return redirect(url_for("list_signups", added=cursor.lastrowid), code=303)
```
Speaker notes: You have written this in 145130. request dot form holds the POST pairs. getlist collects every ticked box. The question marks keep every value out of the SQL text. And the answer is a three oh three redirect, so refreshing the next page repeats a harmless GET and not the sign-up. This version stores whatever arrives. Tomorrow we attack it.
Image: None. This slide is code.
---
## Slide 6: The wrong way
```
method="get" on a form whose action only accepts POST

405 Method Not Allowed
The method is not allowed for the requested URL.
```
Speaker notes: I change the method to get in the Elements panel and submit. Flask answers four oh five. The route was written for POST only. The action is two things, the address and the method, and both have to match what the server expects. The address alone is not enough.
Image: None. This slide is code.
---
## Slide 7: Status codes you will see this week
- 200: here is the page
- 303: done, now go here
- 400: refused, and here is why
- 405: right address, wrong method
- 500: the server itself failed
Speaker notes: Five numbers. Two hundred is fine. Three oh three is the answer to a successful POST. Four hundred is the server refusing what you sent, which you will make it do tomorrow. Four oh five you saw a moment ago. Five hundred means the server crashed, and a person should never see it.
Image: Five status codes as badges, green, blue, amber, amber, red.
---
## Slide 8: Post, redirect, get
- A successful POST answers with 303
- The browser GETs the result page
- Refresh repeats the GET, not the sign-up
- No accidental double sign-ups
Speaker notes: If the server answered the POST with a page directly, refreshing that page would send the sign-up again, and the browser would ask a confusing question about resubmitting. Redirecting first means the page on screen came from a GET. Refresh all you like.
Image: A three-step arrow diagram: POST, 303, GET.
---
## Slide 9: A web service is the same server, answering a script
- /api/slots returns JSON
- signup.js asks for it with fetch
- The slot list shows places left
- The server still checks on submit
Speaker notes: Open slash api slash slots in a tab and you get JSON, not a page. That is a web service. The script on the form calls it when the slot list gets focus and disables full slots. It is a convenience. Someone can take the last place in the seconds before you press Sign up, and anyone can send the form without the page, so the server checks again.
Image: A browser tab showing a small block of JSON beside the form's drop-down list.
---
## Slide 10: What you are about to build
- Lab W05-01, steps 8 to 12
- Switch the form to POST /signup
- Write the INSERT with placeholders
- Record the Payload, the 303, and the 405
Speaker notes: Build one switches your form to post to slash signup and has you write the insert. Tick Preserve log and record what the Payload tab shows. Then cause the four oh five on purpose. Build two is the web service: watch the api slash slots request appear when the slot list gets focus, and explain why the server still checks. The lab is due at the end of Build two.
Image: The Network panel with the signup row selected and the Payload tab open.
---
