# What Tools Cannot See
---
## Slide 1: Six out of twenty-four
- The pantry page has twenty-four planted problems
- web-check fully reported six
- The swap board: two of eight
- Whose job is the rest
Speaker notes: You have audited two pages now. Put the numbers side by side. The tool is not bad. It reports what it can prove from a page sitting still, and it is fast and consistent. But it has never used a page in its life. Today is about the rest of the list, and about how you find it on purpose rather than by luck.
Image: A bar showing six of twenty-four segments filled in light blue, the rest outlined in navy.
---
## Slide 2: Three layers of testing
- Automated: web-check, seconds, every save
- Walkthrough: you, a checklist, keyboard and screen reader
- Usability test: someone else, real tasks, you stay quiet
- You need all three
Speaker notes: Layer one is the tool. Layer two is you, with a checklist, using the page the way a keyboard user and a screen reader user would. Layer three is a person who did not build it, trying to do something real while you watch. Each one catches things the others cannot.
Image: Three stacked layers labelled Automated, Walkthrough, and People, widening toward the bottom.
---
## Slide 3: Passes every check, traps every keyboard
```
PASS  h_trap_back.html
  axe at 360px: 0 violation(s)
  axe at 1280px: 0 violation(s)

  10  <input#volunteer-phone> textbox "Phone (optional)"
  11  <input#volunteer-phone> ...  <- did not move
  TRAP: Tab pressed three times and focus did not move.
```
Speaker notes: This is the rebuilt pantry page with one small script added back. It tidies the phone number when you press Tab, and it cancels the Tab key to do it. Every automated check passes. No keyboard user can finish the form. That is 2.1.2, Level A, and only a person pressing keys finds it.
Image: None. This slide is code.
---
## Slide 4: Narrator, the controls you need
- Ctrl + Windows + Enter starts and stops it
- Narrator key: Caps Lock or Insert
- Narrator + Space: scan mode
- H for headings, D for landmarks
- Headphones on, volume low
Speaker notes: Narrator is built into Windows. I checked these keys on a lab machine before class, and if any of them differ on yours, tell me. Scan mode lets you move by element. H moves by heading and D by landmark. NVDA is the other common free screen reader, and its keys are in your notes, marked verify. Headphones on and the volume low, because thirty screen readers on speakers make every test in this room useless.
Image: A keyboard with Ctrl, the Windows key, Enter, and Caps Lock highlighted, beside a pair of headphones.
---
## Slide 5: What the screen reader can navigate by
```
Before:  HEADINGS   h1 Volunteer with us / h4 How it works
         LANDMARKS  form
After:   HEADINGS   h1 ... / h2 How it works / h2 Pantry hours /
                    h2 This week's shifts / h2 Sign up for a shift ...
         LANDMARKS  banner / navigation Main / main / ... / contentinfo
```
Speaker notes: This is what the browser offers a screen reader on each version of the page. Before, two headings and no main. After, a table of contents and a map. The walkthrough checklist asks you to hear this for yourself, with checks S2 and S3, not to trust the printout.
Image: None. This slide is code.
---
## Slide 6: Watch me run a bad usability test
- I read the task, then explain the table
- My tester finishes in ten seconds
- I write: task one, passed
- I learned nothing
Speaker notes: This is the deliberate failure, and it is the one everyone commits. I read the task and then I help, because watching someone struggle with my page is uncomfortable. The task gets done, the record says passed, and I have tested my own explanation instead of my page. The rule is: read it once, then be quiet. If they are stuck for sixty seconds, say let's move on and write down where they stopped. That place is the finding.
Image: A facilitator pointing at a screen while the participant sits back, with a red cross over the pointing hand.
---
## Slide 7: Tasks are goals, not instructions
- Find out whether Thursday's sorting shift has space
- Not: tab to the table
- Record finished, time, and where they hesitated
- Make one change because of what you saw
Speaker notes: This is 6.5.10, develop and execute a usability test. A task names a goal a real person has. An instruction names a control and tests nothing. Write down three things per task. And a test that changes nothing was not worth running, so make one change and say which observation caused it.
Image: A small record sheet with three task rows and columns for finished, time, and hesitation.
---
## Slide 8: Who is missing from your test
- Classmates who think like you
- On the same laptops, in the same language
- A keyboard-only classmate is a stand-in
- Not a person who uses one daily
Speaker notes: This is where bias lives in testing. If everyone in your test is like you, the test tells you the page works for people like you. Today your partner stands in for a keyboard user, and that is useful. It is not the same as testing with someone who uses a keyboard or a screen reader every day, and your write-up says so. In the capstone, with real users in Weeks 15 and 16, that is the gap to close. And a real participant is recruited, agrees, can stop, and is thanked. Nobody is a prop.
Image: A group of four similar silhouettes with an empty fifth chair outlined in light blue.
---
## Slide 9: A safe test station
- Clean shared headphones before and after
- Cables off the floor when you move
- Stand up at the reset
- Screen reader off before you leave
- Flashing and motion are health decisions too
Speaker notes: Competency 1.3.2 is about the protocols that keep a workplace clean, safe, and healthy, and a room full of screen reader tests has real ones. The last bullet is the design side. Flashing content can trigger seizures, which is why 2.3.1 exists, and motion can make people sick. That is about users, not the workplace, but it is the same habit of thinking about the person on the other end.
Image: A tidy workstation with headphones on a stand and a cable clipped to the desk edge.
---
## Slide 10: What you are about to build
- Build 1: rebuild the pantry page from your audit
- Rerun web-check after every few fixes
- Build 2: pass at three widths, then keyboard walk
- Partner test, three tasks, then one change
Speaker notes: Build 1 is the rebuild. Work down your audit log, fix, and rerun the checker every few fixes. Build 2 starts with the checker passing at all three widths. Then mouse away, checks K1 to K10. Then swap with your partner for the usability test. Tomorrow, after Gate 2 and the quiz, you do the screen reader walkthrough and the recording.
Image: A before and after pair of the pantry page with a green PASS badge and a keyboard icon on the after side.
---
