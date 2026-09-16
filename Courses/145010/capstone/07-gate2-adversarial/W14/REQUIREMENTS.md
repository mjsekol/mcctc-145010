# Requirements · Parts checkout list

**Ridgeview Robotics Club is an invented organization, a composite of high school robotics clubs. No
real club is involved, and every name and note in the data is invented.**

The robotics club shares a cabinet of parts. Members were writing checkouts on a clipboard, and it
kept getting lost. This page replaces the clipboard. It was built from these requirements. Read them
before you read a line of code.

1. Show every checked-out part with the part name, the member who has it, the note, and the date it
   is due back.
2. A member can add a checkout by typing a part and a short note. The new checkout appears in the
   list right away.
3. A filter box narrows the list as the member types.
4. Show a count of parts **due back within 7 days**. A part due back in exactly 7 days is within 7
   days.
5. A member's note is shown as text. Whatever a member types appears literally on the page and can
   never run as code.
6. The page runs from a file, offline, with no framework and no network. The data lives in a local
   file.
7. **The page meets WCAG 2.1 AA and passes the course web-check with zero violations.** Every control
   has a label a screen reader can announce.
8. Names and comments match the code. A comment says what the code under it actually does.
9. Typing in the filter must not redo work that did not change. Sorting the whole list again on every
   keystroke is redoing work that did not change.

## The reference date

The "due back within 7 days" count is measured from a fixed reference date, `TODAY`, set in
`parts-data.js`. It is invented sample data, not a real calendar date, so the count is the same every
time the page loads. Read that value before you check the count by hand.

## How to run it

Open `index.html` in Chrome. To run web-check, from the repository root:

```
node tools/web-check/check.js Courses/145010/capstone/07-gate2-adversarial/W14/index.html
```
