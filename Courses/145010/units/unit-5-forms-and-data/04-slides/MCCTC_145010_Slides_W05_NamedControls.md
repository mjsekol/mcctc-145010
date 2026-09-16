# A Form Is Named, Labelled, Grouped Controls
---
## Slide 1: The email that never arrived
- A person typed their email
- The page showed it
- The server never received it
- No error, anywhere
Speaker notes: Here is a sign-up form that looks perfect and loses every email address it is given. Nothing crashes. Nothing turns red. The person thinks they signed up, and the club never hears from them. By the end of fifteen minutes you will know the one missing attribute that causes it, and how to catch it before you write a line of server code.
Image: A sign-up form with a filled email box, and a server inbox beside it showing the email field blank.
---
## Slide 2: What a form actually sends
- Every control with a name and a value
- As name equals value pairs
- To the form's action address
- Nothing else, ever
Speaker notes: This is the whole rule. When a form is submitted, the browser walks its controls and, for each one that has a name and a value, adds a pair. A control with no name is skipped. An unticked checkbox has no value, so it is skipped. Everything this week builds on that sentence.
Image: A form on the left with arrows from named controls only into a small envelope on the right.
---
## Slide 3: id is for the label, name is for the server
```html
<label for="email">Email (required)</label>
<input id="email" name="email" type="email" required>
```
Speaker notes: Two attributes, two jobs. The label's for points at the input's id, which is how clicking the label focuses the box and how a screen reader knows what to call it. The name is what the server receives. Most controls need both, and they are often the same word, which is exactly why people forget one.
Image: None. This slide is code.
---
## Slide 4: A group with a question
```html
<fieldset>
  <legend>Kind of act (required)</legend>
  <input type="radio" id="act-music" name="act_type" value="music" required>
  <label for="act-music">Music</label>
  <input type="radio" id="act-poetry" name="act_type" value="poetry">
  <label for="act-poetry">Poetry</label>
</fieldset>
```
Speaker notes: The fieldset groups the choices and the legend is the question. A screen reader reads the legend with each option, so Music is heard as an answer to kind of act. Both radios share one name, act underscore type. That shared name is what makes them one group, where choosing one clears the other.
Image: None. This slide is code.
---
## Slide 5: Every control, and what it sends
- Text, email, number: what was typed
- Radio group: the one chosen value
- Checkbox group: one pair per ticked box
- Select: the option's value, not its text
- Unticked checkbox: nothing at all
Speaker notes: Five rules to know cold. A select sends the value attribute of the chosen option, so the person reads seven twenty p m and the server receives the number two. A checkbox group with a shared name can send that name several times. And an unticked checkbox sends nothing, not false, nothing. Your server has to expect that.
Image: A table of control icons, each with a small envelope showing what it sends.
---
## Slide 6: Watch this
```html
<form action="/echo" method="get">
  <input name="performer_name" value="Nova Park">
  <input id="noname" value="nova@example.com">
  <input type="checkbox" name="needs" value="mic" checked>
  <input type="checkbox" name="needs" value="amp" checked>
  <input type="checkbox" name="agree" value="yes">
  <button>Go</button>
</form>
```
Speaker notes: Before I press Go, write down the address you think the browser will go to. Look at every control and decide whether it is sent. Then I will submit it to the echo page, which shows exactly what arrived.
Image: None. This slide is code.
---
## Slide 7: What actually arrived
```
/echo?performer_name=Nova+Park&needs=mic&needs=amp
```
Speaker notes: This is the real address from the build machine. The email is gone, because that input has an id and no name. Agree is gone, because it was not ticked. Needs arrives twice, once per box. And the space became a plus sign. No error told us any of this. The echo page did.
Image: None. This slide is code.
---
## Slide 8: Radios with two names are two groups
- name="size_s" and name="size_m"
- Both can be checked at once
- The fieldset does not group them
- One shared name does
Speaker notes: The second silent bug. Somebody copies a radio button and changes everything on the copy, including the name. Now the browser sees two groups of one, and a person can choose small and medium together. We checked this in Chrome and both stayed checked. Sitting in the same fieldset does not help, because the fieldset is for people and the name is for the browser.
Image: Two radio buttons both filled in, with a red circle around their different name attributes.
---
## Slide 9: The two buttons
- Submit sends the form
- Enter in a text field also sends it
- Reset returns every control to its starting value
- Reset sends nothing
Speaker notes: Submit is the one you know. Pressing Enter in a text box submits too, so test with the keyboard. Reset is the one people misunderstand. It does not clear the form. It puts every control back to the value the page loaded with. On Thursday you will see a page where that means putting back the person's old answers.
Image: A submit button and a reset button, each with a small arrow showing what happens.
---
## Slide 10: What you are about to build
- Lab W05-01: the Open Mic sign-up form
- Start the app on port 8405
- Send it to the echo page by GET
- Remove a name on purpose and record what vanished
Speaker notes: Build one starts the lab app on port eight four zero five and has you write the first part of the form, sent to the echo page. Then you remove one name on purpose and write down what disappeared. Build two finishes every control in the specification and runs the checker. Stop the server with Control C before you leave.
Image: The echo page showing a table of names and values next to the form that sent them.
---
