# The Page Waits for You
---
## Slide 1: A button that works for you and nobody else
- It looks like a button
- It works when you click it
- Press Tab. Focus never lands on it.
- The checker says the page passes
Speaker notes: Today starts with a control that works perfectly when you test it, because you test with a mouse. A keyboard user cannot reach it. A screen reader does not call it a control. And the automated checker you trusted in Week 3 says the page is fine. By the end of today you will know why, and you will never build it again.
Image: A mouse pointer clicking a styled box successfully, and a keyboard beside it with a red cross.
---
## Slide 2: Python runs and ends. A page runs and waits.
- The script runs top to bottom once
- Mostly it leaves instructions for later
- Then it waits for the person
- Every later line runs because someone acted
Speaker notes: This is the biggest change from everything you have written before. A Python program runs and finishes. A page script runs once, registers what should happen when the person does things, and then sits there, sometimes for an hour. Almost all the code you write this week runs later, when the person decides.
Image: A timeline: one short burst of setup, then a long flat line with small spikes where the person clicks.
---
## Slide 3: A listener is an instruction for later
```js
console.log("1");
document.querySelector("#go").addEventListener("click", () => {
  console.log("2");
});
console.log("3");
```
Speaker notes: Nobody clicks. What prints? One, then three. Two never prints, because addEventListener does not run the function. It leaves a note for the browser. If the person clicks twice, you get two, twice, later.
Image: None. This slide is code.
---
## Slide 4: One handler, three ways in
```js
document.querySelector("#ready").addEventListener("click", (event) => {
  log.textContent = `click from ${event.target.id}, detail ${event.detail}`;
});
```
Speaker notes: Click it with the mouse and the log says detail one. Tab to it and press Enter, detail zero. Press Space, detail zero. The keyboard fired a real click event, and the same listener handled it. That is what a button element gives you for free.
Image: None. This slide is code.
---
## Slide 5: What a button gives you
- A place in the tab order
- Enter and Space fire click
- A role a screen reader announces
- A disabled state that actually disables
Speaker notes: Four things, all free, all correct in every browser. A div gives you none of them. You can add them to a div by hand with tabindex, a role, and a keydown listener, and people do, and they usually get one of the three wrong. Use the element that already does it.
Image: A button element with four labelled callouts around it.
---
## Slide 6: The wrong way
```html
<div id="cancel" class="fake-button">Cancel order</div>
```
```
PASS  .../live-demos-w04/tuesday.html
  axe at 360px: 0 violation(s)
```
Speaker notes: Here is the div with a click listener attached, and here is the real checker output for the page it lives on. It passes. The checker reads the tree and sees a div with text in it, which is perfectly valid. It cannot see the listener. Tab through the page and focus skips it. The only test that finds this bug is a person with a keyboard.
Image: None. This slide is code.
---
## Slide 7: The browser does one thing at a time
- Events wait in a line
- One handler runs to the end
- The page draws, then the next one runs
- A slow handler freezes everything
Speaker notes: This is the event loop from the person's side. The browser takes one event, runs its handler all the way through, draws the changes, and only then takes the next one. So while your handler runs, the page cannot respond, cannot scroll smoothly, cannot even show the message you set at the top of the handler.
Image: A single-lane road with cars labelled click, input, and click queued behind one long truck.
---
## Slide 8: Watch the freeze
```js
document.querySelector("#freeze").addEventListener("click", () => {
  log.textContent = "Recounting...";
  const stopAt = Date.now() + 3000;
  while (Date.now() < stopAt) { laps += 1; }
  log.textContent = "Recount finished.";
});
```
Speaker notes: I click recount, then I click mark order ready straight away. Nothing happens for three seconds. Then the ready message appears. On the build machine the freeze ended at about three thousand and seventy milliseconds and the waiting click ran nine milliseconds later. Recounting never appeared at all, because the browser only draws between handlers.
Image: None. This slide is code.
---
## Slide 9: Pick the right event
- click: mouse, Enter, or Space on a button
- input: every change in a text box
- change: when the person commits a choice
- keydown: a specific key, like Escape
Speaker notes: Four events cover almost everything this week. click for buttons. input for a live counter, because it fires on every keystroke and paste. change for a select or a checkbox, or when someone leaves a text box. keydown only when you need a particular key, like Escape to close a panel, and never as a way to make a div act like a button.
Image: Four small cards, each with an event name and a matching control.
---
## Slide 10: What you are about to build
- Lab W04-01, steps 6 to 12
- A rules toggle that says whether it is open
- Take-shift buttons with a running total
- Test every control with your hand off the mouse
Speaker notes: Build one is the rules toggle with aria-expanded kept in step with what is on screen. Build two is the shift buttons and the running total. The acceptance test for both is the same: keep your hand off the mouse and do everything with Tab, Enter, and Space. If you cannot, it is not finished.
Image: A keyboard with Tab, Enter, and Space highlighted, next to the shift board page.
---
