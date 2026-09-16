# Track Guide · Industrial / HMI
## 145010 Senior Capstone · Read before Week 8

**Why this track exists.** Most employers near this school make things. The software they need
reads machines, shows an operator what is happening, and raises a hand when something is wrong.
You built a WPF operator panel reading a Raspberry Pi in 145065. This track takes that skill to
a real person with a real machine-side problem.

**What makes it hard.** It has more moving parts than either other track: a device, a sensor, a
service, a database, a desktop panel, and a web page. Any one of them can stop the others. It is
also the only track where a mistake can hurt someone, which is why this guide has a safety
section you read twice.

**Competencies this track evidences most heavily:** 1.3.5 (safety compliance measures), 1.4.4
(system hardware to support software applications), 2.12.2 (a test system that mimics external
interfaces), 2.11.2 to 2.11.8 (troubleshooting), 6.5.13 (responsive design, in the dashboard).

---

## The typical shape

```
sensor(s) --> Raspberry Pi logger service --> local database
                                          |
                                          +--> small HTTP API --> C# WPF operator panel
                                          |                   --> web dashboard (read-only)
                                          +--> health log (written by the service itself)
```

**One direction of data.** Readings flow from the sensor to the people. Nothing flows back to
the machine. See [Monitor, do not control](#monitor-do-not-control).

---

## A composite example

**This is a composite, not a real organization.** The maintenance lead at a small fabrication
shop says the air compressor room gets hot on summer afternoons, and the compressor has shut
itself down on heat more than once. Nobody notices until air tools stop working on the floor.
They want to know before that happens.

That is a good capstone problem. It names a person, a pain, and a frequency, and "before that
happens" is measurable. It is also the example used in
[Scope Calibration](MCCTC_145010_Capstone_ScopeCalibration.md#example-1--industrial--hmi).

---

## The minimum viable version

The smallest thing that is still a real deliverable to a real person.

- **One sensor type**, read on a fixed interval, by a service that starts when the Pi boots.
- **Every reading stored** with a timestamp in a local database.
- **A WPF operator panel** that shows the current value, the time of the last reading, and an
  alarm state. It shows the difference between **stale** data (the last reading is old) and
  **missing** data (there has never been a reading, or the service is unreachable).
- **One alarm** with a threshold the stakeholder chose, an acknowledge action with a
  confirmation, and an alarm history.
- **A read-only web dashboard** showing the current value and the last 24 hours, valid HTML,
  readable on a phone.
- **A health log** the service writes by itself.
- **A test mode** that replays recorded or generated readings, so everything above the Pi can
  be tested without the hardware. That is your 2.12.2 evidence.

If that is all you finish, and it runs for thirty days, and the stakeholder accepts it, that is
a strong capstone.

## What a stretch looks like

Name these in Week 8. Start them only when every acceptance criterion passes.

- A second sensor type, with its own threshold.
- Trend view on the panel with selectable ranges.
- A daily summary page on the dashboard: highs, lows, time in alarm.
- Operator notes attached to an alarm acknowledgement.
- An exported CSV the stakeholder can open in a spreadsheet.

**Not stretch goals, because they change the risk of the project:** anything that switches a
machine on or off, any text or email alerting that needs an account or a paid service, and any
connection to the stakeholder's existing control equipment.

---

## Safety · read this twice

**This section states principles.** The rules you follow are the ones in the **Lab Acceptable
Use and Safety Agreement** you and your parent or guardian signed, section 5, and whatever your
instructor adds for your specific hardware. Where those are more specific than this page, they
win.

### On the bench

- **Power down and disconnect before you change any wiring.** Never work on a powered circuit.
- **Use the grounding strap and mat** before handling bare boards or components.
- **Low-voltage hobby components only**, from the lab's approved stock. You do not wire anything
  that plugs into a wall outlet, and you do not open anything that does.
- **Report any heat, smell, damage, or injury immediately**, however small.
- **Put everything back** at the end of every session.

### Monitor, do not control

**Your capstone watches and reports. It does not act on equipment.** The software you write is
not a safety system, and nothing you build may be relied on to keep a person safe. If a
stakeholder says "and then it could shut the machine off," the answer is that switching real
equipment is a job for the people qualified to do it and for safety devices designed for it. Your
project can tell a person that something needs attention. A person decides what happens next.

If your instructor approves an output on the bench, such as an indicator light or a buzzer, it
stays on the bench.

### At the stakeholder's site

- **Nothing is installed at a workplace without that workplace's written permission**, and
  without your instructor arranging the visit through the school.
- **Their safety rules apply to you**, including where you may stand and what you may touch.
  Ask for them before the visit. Your proposal records what they are. That is your 1.3.5 evidence.
- **Ask whether any safety data sheets or posted procedures apply** to the area where a sensor
  would sit. Record what you were told.
- **You never visit alone**, and a site visit is always arranged through the school.

---

## The technical risks that sink this track

In the order they usually strike.

**1. The hardware arrives late or does not work.** Every week spent waiting for a part is a week
not building. **Fix it in Week 9:** confirm with your instructor that the Pi and your sensor are
in the lab and that you have read a value from the sensor before Week 10 ends. If the part is not
here, your test mode becomes the first thing you build.

**2. Nothing works without the Pi.** Students build the panel against the live device and then
cannot demonstrate or test anything when the device is on the other side of the room. **Fix it
with the test mode from day one.** The panel and dashboard talk to an API. The API does not care
whether the readings came from a sensor or a replay file.

**3. The service dies and nobody notices.** A logger that stops after four days looks exactly
like a quiet week. **Fix it with the health log and the stale-data display.** A panel that says
"last reading 3 hours ago" in red has caught the failure for you.

**4. The network is not yours.** The lab runs on an isolated network, and you never bridge lab
equipment to the school network without your instructor's direct authorization. A stakeholder's
network belongs to them. **Where the device lives and how anyone reaches the dashboard is decided
with your instructor in Week 10 and written in your architecture.** Do not design around a
connection you have not been given.

**5. Time on the device drifts.** A Pi with no network time source can record readings with the
wrong time. **Check it in Week 11** and write down what your device does. [VERIFY on the lab's Pi
image]

**6. The SD card fills or wears.** A logger that writes every second forever will eventually
fail. **Decide your interval and a retention rule in Week 10**, write the arithmetic in your
architecture, and test what happens when the database is large.

---

## Where it runs and who can reach it

Requirement 2 says someone other than you must be able to use it. For this track, there are
three shapes, and your instructor decides which is available:

| Shape | What it looks like | What it needs |
|---|---|---|
| **On the lab bench** | The device and panel run in the lab. The stakeholder, or someone acting for them, uses the panel and dashboard on a lab machine without you present. | Instructor arrangement. The simplest shape. |
| **At the stakeholder's site** | The device is installed at their site, near the equipment and never attached to it. | Their written permission, their network owner's approval, a school-arranged visit. [VERIFY with your instructor] |
| **Bench device, reachable dashboard** | The device stays in the lab and the dashboard is reachable from elsewhere. | Explicit authorization for any connection out of the lab network. [VERIFY with your instructor and district IT] |

**Write the shape and the reason in your decision log.** A student who planned for the second
shape and got the first has not failed, provided the change is recorded.

---

## Surviving thirty days, on this track

**What "manual intervention" looks like here:** unplugging and replugging the Pi because it
stopped, restarting the logger by hand, deleting rows to make room, fixing the clock.

**How you prove it did not happen:**

1. **The logger runs as a service that starts at boot and restarts itself if it exits.** On a
   Linux-based Pi image that is usually a systemd unit with a restart policy. [VERIFY on the lab's
   Pi image] A restart the service manager performs is not an intervention. Log it anyway.
2. **The service writes a heartbeat row to the health log on a fixed interval**, whether or not
   the sensor reading succeeded. Each row records the time, whether the sensor answered, the
   number of readings stored since the last heartbeat, and free storage.
3. **The panel and dashboard show the age of the last reading.** Screenshots of the stale state,
   produced on purpose, go in your evidence.
4. **A planned power-loss test.** Pull power on purpose, once, as a recorded release event,
   restore it, and show the service came back and the gap appears honestly in the data. That is
   the test that proves the "starts at boot" claim.
5. **The thirty-day record** counts consecutive days where every expected heartbeat is present or
   explained by a recorded planned event.

A heartbeat line might look like this. It is program data, so the timestamp belongs there:

```
2027-04-23T14:15:00  result=ok  sensor=ok  stored_since_last=15  free_mb=21840
```

---

## Where Strand 6 lives in this track

The WebXam post-test is in Week 16 and more than half of it is web development. **Your dashboard
is where this track practices it.** Build it with semantic HTML, valid markup, a responsive
layout, and an accessible table for the recent readings. Run it through the course's web checker
the same way you did in the instruction phase. A dashboard you built by hand from Weeks 1-6 skills
is also a strong defense answer.

---

## Defense questions this track is most vulnerable to

1. "Your panel shows 31 degrees. How old is that number, and how would an operator know?"
2. "What happens to the panel when the Pi loses power? Show me."
3. "Why does this project not switch anything off?"
4. "How much storage does a year of readings take at your interval?"
5. "How did you test the alarm without making the room hot?"

The full bank is in [Defense Question Bank](MCCTC_145010_Capstone_DefenseQuestionBank.md).
