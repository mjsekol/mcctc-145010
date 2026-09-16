# Keyboard Access and Focus
---
## Slide 1: Put the mouse behind the monitor
- Right now. Everyone
- Open yesterday's swap board
- Turn on the notification switch
- You have two minutes
Speaker notes: Do it. Mouse behind the monitor. Open the swap board and turn on the text notification switch using only the keyboard. Two minutes. When the time is up I want to hear who managed it. Nobody will, and that is the lesson of the day. A page that works perfectly with a mouse can be completely closed to a keyboard.
Image: A mouse turned upside down behind a monitor, with a keyboard in front, navy and light blue.
---
## Slide 2: How the keyboard moves
- Tab forward, Shift+Tab back
- Enter activates links and buttons
- Space presses buttons and toggles checkboxes
- Arrow keys move inside radio groups and lists
- Focus follows the HTML source order
Speaker notes: This is the whole keyboard model. Focus is the one element that will receive what you type next. Tab moves it forward in source order, not visual order. If CSS moves something to the top of the screen, the keyboard still finds it where it is in the file. A radio group is one Tab stop, and arrows move inside it. People report that as a bug. It is how radio groups work.
Image: A keyboard with Tab, Shift, Enter, Space, and the arrow keys highlighted in light blue.
---
## Slide 3: Four criteria for today
- 2.1.1 Keyboard, Level A
- 2.1.2 No Keyboard Trap, Level A
- 2.4.3 Focus Order, Level A
- 2.4.7 Focus Visible, Level AA
Speaker notes: Everything works from a keyboard. If focus can get in, it can get out. The order keeps the meaning. And you can always see where you are. Three of those four are Level A, the minimum. And web-check tests almost none of them, because it never presses a key.
Image: Four numbered cards in a row, each with a small keyboard icon.
---
## Slide 4: A keyboard walk, before
```
   1  <input> textbox "Email"  focus ring: NONE
   2  <a> link "Shifts"  focus ring: NONE
   5  <a> link ""  focus ring: NONE
   9  <input#phone> textbox ""  focus ring: NONE
  10  <input#phone> textbox ""  focus ring: NONE  <- did not move
  TRAP: Tab pressed three times and focus did not move.
```
Speaker notes: This is the pantry page, walked with Tab. The first stop is the Email field halfway down the page, because of tabindex one. No stop shows a ring, because one CSS line removed it. Stop five has no name. And at the phone field, focus stops moving. A script cancels the Tab key. web-check reported none of these four.
Image: None. This slide is code.
---
## Slide 5: A keyboard walk, after
```
   1  <a> link "Skip to main content"  focus ring: visible
   8  <input#volunteer-name> textbox "Your name"  focus ring: visible
  12  <input> radio "Yes"  focus ring: visible
  13  <button> button "Sign up"  focus ring: visible
  14  <a> link "Directions to the side door"  focus ring: visible
```
Speaker notes: The rebuilt page. A skip link first. A ring on every stop. The radio group as one stop. And stop thirteen, the Sign up button, which did not exist for the keyboard before. That is the button the volunteer could not reach.
Image: None. This slide is code.
---
## Slide 6: Watch me fix the switch the wrong way
- I add tabindex="0" to the div
- Tab reaches it now
- I press Space. Nothing happens
- I press Enter. Nothing happens
- The tree calls it generic, with no state
Speaker notes: This is the deliberate failure, and I checked it in Chrome before class. Tabindex zero makes the div focusable, so the checklist item reachable looks ticked. But onclick on a div does not fire from the keyboard. Space does nothing, Enter does nothing. And a screen reader user who lands on it hears no role and no state. One attribute felt like a fix and was not.
Image: A grey toggle switch with a focus ring around it and a keyboard Space key with a question mark.
---
## Slide 7: The element that already does the job
```html
<input type="checkbox" id="notify">
<label for="notify">Text me when a new swap is posted</label>

<!--  5  <input#notify> checkbox "Text me when a new swap is posted"  -->
```
Speaker notes: Replace the div with a checkbox and a label. Tab reaches it. Space toggles it. The screen reader says checkbox, the label, and whether it is checked. I wrote no script for any of that. The browser already knew how.
Image: None. This slide is code.
---
## Slide 8: tabindex, carefully
- 0 adds an element in source order
- Minus 1 lets script focus it
- 1 or higher jumps ahead of everything
- Never use a positive value
Speaker notes: Tabindex zero is for custom widgets that also get keyboard handling and a role, and you should almost always use a real element instead. Minus one is for moving focus on purpose, which is Week 5. Any positive value drags that element ahead of the entire page. On the pantry page it made the Email field the first thing a keyboard user reached.
Image: A row of numbered stepping stones with one stone labelled 1 pulled out of line to the front.
---
## Slide 9: Keep the ring, give it contrast
```css
:focus-visible { outline: 3px solid #1d4ed8; outline-offset: 2px; }
.site-header :focus-visible { outline-color: #f4c542; }
```
Speaker notes: Designers ask to remove the focus ring because it shows up on mouse clicks. Focus visible is the answer. The browser shows it when the ring is needed, which is mostly keyboard use. The second rule is there because blue on a dark green header disappears. Check your ring on every background it can land on.
Image: None. This slide is code.
---
## Slide 10: What you are about to build
- Build 1: swap board, Part 3, keyboard
- Mouse out of reach for the whole build
- Build 2: the Lantern Street audit, passes 3 and 4
- Commit the audit before you fix anything
Speaker notes: Build 1 finishes the swap board. Delete the line that hides focus and replace the switch with a checkbox. Then write the tab order in your commit message. Build 2 is the keyboard pass on the pantry page. You will get trapped in the phone field. Write down exactly what happened before you escape with the mouse. By the end of the period, commit the audit with the message Audit complete. Tomorrow you fix it.
Image: A checklist titled Keyboard pass with the first three boxes ticked.
---
