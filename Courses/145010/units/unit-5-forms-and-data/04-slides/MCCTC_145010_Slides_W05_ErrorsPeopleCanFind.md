# Errors People Can Find, and tabindex
---
## Slide 1: Something went wrong. Where?
- A red box at the top says fix the following
- You are at the bottom of the form
- Your answers are gone
- Your screen reader said nothing
Speaker notes: Yesterday your server learned to say no. Today it learns to say no in a way everybody can act on. The error handling most tutorials show passes the automated checker and fails most people. We are going to build the version that works for a keyboard user, a screen reader user, and someone in a hurry.
Image: A long form with a small red box at the very top and an empty form below it.
---
## Slide 2: Six parts, six jobs
- Title starts with Error:
- A summary of links, with a heading
- Focus moves to the summary
- Each message next to its field, tied with aria-describedby
- aria-invalid on the field, and the answers kept
Speaker notes: This is the accessible error pattern. The title is the first thing a screen reader announces on a new page. The summary says how many problems and links to each. Focus goes there so nobody starts from the top. Each message sits by its field and is tied to it, so it is read when the person reaches the field. And the answers stay, so they fix one thing instead of retyping eight.
Image: The error page with six numbered callouts.
---
## Slide 3: One field, done properly
```html
<p class="field-error" id="email-error"><span class="visually-hidden">Error: </span>Enter an email address in the form name@example.com.</p>
<input id="email" name="email" type="email" required
       value="not-an-email" aria-describedby="email-hint email-error" aria-invalid="true">
```
Speaker notes: This is exactly what our server sent for a bad email. The value is kept. The input is described by its hint and then its error. It is marked invalid. And the hidden word error is read aloud, because a screen reader cannot see red.
Image: None. This slide is code.
---
## Slide 4: The summary, and where focus goes
```html
<div class="error-summary" id="error-summary" tabindex="-1"
     aria-labelledby="error-summary-title">
  <h2 id="error-summary-title">There are 7 problems with your sign-up</h2>
  <ul>
    <li><a href="#email">Enter an email address in the form name@example.com.</a></li>
  </ul>
</div>
```
Speaker notes: Tabindex minus one means script can put focus here, and Tab never will. One line of script moves focus to it when the page arrives, and on the build machine the focused element after a refused submission was exactly this box. Each link goes to its field, and the script makes the link put focus in the field and scroll its label into view.
Image: None. This slide is code.
---
## Slide 5: tabindex, three values
- 0: in the tab order, in source order
- -1: focusable by script, never by Tab
- 1 or more: pulled ahead of everything
- The fix for bad order is better source order
Speaker notes: Zero is for something that is not normally focusable but should be, like a scrolling table. Minus one is for something script needs to focus, like our summary. Any positive number jumps the queue, ahead of every link and field on the page. That is almost never what anyone wants.
Image: A queue of people, one with a number one badge cutting to the front.
---
## Slide 6: The wrong way
```js
document.querySelector("#agree").setAttribute("tabindex", "1");
```
```
Tab order: agree > performer-name > email > act-music
```
Speaker notes: I set tabindex one on the agree box, the last thing on the form, and press Tab from the address bar. The real order on the build machine: agree first, then name, then email. Nobody reading the page expects to agree to the house rules before typing their name. And every field anyone adds later lands behind it.
Image: None. This slide is code.
---
## Slide 7: The same pattern before sending
- form.noValidate = true, set by the script
- On submit, check with the same rules
- Build the same summary with textContent
- preventDefault, then move focus
Speaker notes: In the browser, the script replaces the one-at-a-time bubbles with the same summary the server sends, so there is one pattern to learn. Novalidate is set by the script, not in the HTML, so if the script fails, the browser's own checks still protect the person. And everything is built with create element and text content, never inner H T M L.
Image: A submit button with a stop sign and the error summary appearing above the form.
---
## Slide 8: The red list that passes the checker
- A list of messages at the top
- No links, no focus, no title
- Nothing tied to any field
- Answers wiped. The checker says PASS.
Speaker notes: This is the version in tomorrow's Gate 2, and it passes our checker with zero errors. Tab to the name field with a screen reader and you hear your name, edit text, and nothing about what is wrong. Automated tools read the markup. Only a person using the form finds this.
Image: A checklist with a green PASS stamp beside a frustrated person at a keyboard.
---
## Slide 9: Test it the way people use it
- Submit empty with the keyboard
- Where did focus go?
- Tab to a field. What is announced?
- Turn on Narrator and listen
Speaker notes: Three tests you can run in two minutes. Submit with Enter and say where focus landed. Follow a summary link and say where you are. Then Windows key, control, enter starts Narrator, and you listen to what it says on the summary and on a field with an error. Write the words down. That is your evidence.
Image: A keyboard and a pair of headphones next to the error summary.
---
## Slide 10: What you are about to build
- Lab W05-02, Part B
- The server's error page, all six parts
- The same pattern in signup.js
- Keyboard test, tabindex test, Narrator check
Speaker notes: Build one: add the title, summary, messages, attributes, and kept answers to your template, then save the error page and run the checker on it. Then write check form and show errors. Build two starts with the submit handler and the focus on load, then the three tests, and the lab is due twenty-five minutes in. The rest of the period is your project.
Image: The finished error page with focus ring on the summary.
---
