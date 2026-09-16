# Acceptance run log · Kennel Care Log
## 145010 Senior Capstone · Gate 2 source file · Week 16 · invented composite

**Invented for a Gate 2 exercise.** The student's run sheet, written during the run and typed up
the same afternoon as `docs/control/acceptance-run-log.md`, plus the contact log lines for Weeks
15-16. Lines are numbered so you can cite `L14`.

---

## The run

```
L1   Run: Week 16, Wednesday, at school
L2   Present: the volunteer coordinator, the instructor, the student
L3   Not present: the shelter manager (backup contact, not needed for the run)
L4   Procedure: test plan section 7, committed at 4e7a2c1, agreement version 1.0
L5   Deployed system at commit 9b3f0d2
L6   Devices: front-desk tablet (brought by the coordinator, held upright),
     test phone at 360 px, coordinator's laptop
L7   Pre-run script read aloud as written: yes
L8
L9   AC-1  PASS  coordinator recorded a walk for Biscuit on the phone.
L10              laptop board showed "Biscuit  Walked 10:42" after about 2 seconds
L11  AC-2  PASS  test clock 11:00. Board opened with Pepper, Juniper, Moose as
L12              the first three rows under "Not walked yet"
L13  AC-3  PASS  private window, coordinator page address -> Sign in page,
L14              no animal names on screen
L15  AC-4  FAIL  student turned on Database offline and said so first.
L16              Coordinator opened Biscuit on the tablet, pressed Record walk,
L17              following the procedure step by step.
L18              Page showed "Saved". Expected "Not saved. Write it on the paper sheet."
L19              Student turned the switch off. Biscuit's second walk is not on
L20              the board and not in the database. The walk was lost and the
L21              page said it was saved.
L22              Server log at that moment:
L23              WARNING save_walk: database unavailable, returning ok
L24  AC-5  FAIL  phone at 360 px: all controls visible, no sideways scrolling.
L25              tablet upright: the Record walk button runs past the right edge.
L26              Coordinator tapped the visible part twice before it registered,
L27              then scrolled sideways to see the whole button.
L28  AC-6  PASS  Export week opened a CSV, 23 rows, one per walk.
L29              Volunteer column shows first name and last initial only
L30
L31  First run: PASS 4  FAIL 2  NOT RUN 0
L32
L33  Coordinator's words, their opinion:
L34    "The not-walked list is the part I'll use every morning."
L35    "So if the database is down, my volunteers think it saved.
L36     That's the one that worries me."
L37  Cases the coordinator did not understand: none
L38
L39  Changes to any criterion proposed or agreed during or after the run: none.
L40  The coordinator asked what happens next with AC-4 and AC-5. Student said
L41  both would be written up and sent with options by Friday.
L42
L43  Decision: not given at the run. The coordinator will decide in writing
L44  after reading the results.
L45
L46  Cause found after the run (student, same afternoon):
L47    routes/walks.py line 48, save_walk() catches the database error, logs a
L48    warning, and returns success. The page trusts that and shows "Saved".
L49    AC-5: the tablet's upright width is 800 px. The walk form has a fixed
L50    minimum width of 860 px (static/app.css line 112).
```

## Contact log, Weeks 15-16

```
C1   Week 15, Friday     Update 5 sent by school email, instructor copied
C2   Week 16, Monday     Coordinator confirmed the Wednesday acceptance run by school email
C3   Week 16, Wednesday  Acceptance run at school, instructor present (this log)
C4   Week 16, Wednesday  Nothing else. No call, no meeting, no email after the run
```
