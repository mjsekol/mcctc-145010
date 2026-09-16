# Lecture Notes: What a Page Costs to Deliver
## 145010 Web Design & Senior Capstone · Unit 4 · Week 4, Thursday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145010_Slides_W04_WhatAPageCosts.md).
There is no exported deck yet. To generate one, from the repository root:
`node tools/gamma.js Courses/145010/units/unit-4-client-side-scripting/04-slides/MCCTC_145010_Slides_W04_WhatAPageCosts.md --export pptx`

If you missed class, you can learn this concept from this file alone, and every number below was
measured, so you can check your own against it. **If you were at BPA,** read this file, then run
Lab W04-02 on your own. It takes about 40 minutes.

**Competency:** 2.7.5 explain the relationship between data transmission volumes, bandwidth, and
latency.

---

## Why this exists

Your pages load instantly on the lab machines. That tells you almost nothing. The server is either
on your own computer or on a fast school network a few metres away.

The people your capstone serves may be on a phone at a ball field, on a bus, or on a rural
connection. A page that is correct and takes fifty seconds to load is, for them, a page that does
not work. You cannot fix what you have not measured, and Chrome will measure it for you.

---

## The concept in plain language

Three words, and they are not the same thing.

| Word | What it is | Unit | Everyday version |
|---|---|---|---|
| **Volume** | How much data has to move | bytes (kB, MB) | How much water is in the tank |
| **Bandwidth** | How much data the link can carry per second | bits per second (Mbps) | How wide the pipe is |
| **Latency** | How long a request waits before any data moves | milliseconds (ms) | How long before the tap starts running, every time you open it |

**Bytes and bits.** Files are measured in bytes. Links are measured in bits per second. There are
8 bits in a byte. A 1.44 Mbps link moves about 180 kB per second.

**The relationship, as a rough model:**

```
time  is about  (latency x the rounds of requests that have to wait)
              + (volume / bandwidth)
```

Two consequences, and they are the whole lesson:

1. **A big file is slow on low bandwidth.** The second half of the formula dominates.
2. **Many files are slow on high latency, even when they are tiny.** The first half dominates.
   A browser opens only a handful of connections to one server at a time, so thirty requests wait
   in several rounds, and every round pays the latency again.

---

## How to measure it

1. Serve the page over HTTP. A file opened by double-clicking never touches a network. In the lab:
   `python serve.py --port 8404`.
2. Open dev tools, **Network** panel. Tick **Disable cache**. Leave dev tools open.
3. Choose a throttling setting from the menu at the top of the Network panel. [VERIFY] the preset
   names on your Chrome; the build machine used the settings puppeteer calls Fast 4G, Slow 4G, and
   Slow 3G.
4. Reload. Read the status bar at the bottom: **requests**, **transferred**, and **Load**.

The throttling settings the numbers below were measured with:

| Setting | Bandwidth down | Added latency per request |
|---|---|---|
| Fast 4G | about 8.1 Mbps (1,012,500 bytes per second) | 165 ms |
| Slow 4G | about 1.44 Mbps (180,000 bytes per second) | 562.5 ms |
| Slow 3G, shown as 3G in some menus | 0.4 Mbps (50,000 bytes per second) | 2,000 ms |

**What throttling is and is not.** DevTools adds a fixed wait to each request and caps the speed. A
real network also drops data and changes speed as you move. Throttling is a fair way to compare two
pages, not a prediction for one particular phone.

---

## Worked example 1: the photo that looks the same

`photo-full.html` shows a 1200 x 675 image at 480 pixels wide. `photo-sized.html` shows a
480 x 270 image at 480 pixels wide. **On screen they look identical.**

Measured on the build machine, cache disabled, two loads each:

| Page | Requests | Transferred | No throttling | Fast 4G | Slow 4G | Slow 3G |
|---|---|---|---|---|---|---|
| photo-full | 3 | 2,376.5 kB | 15 to 129 ms | 2.8 s | 14.7 s | 52.7 s |
| photo-sized | 3 | 382.1 kB | about 20 ms | 0.75 s | 3.3 s | 11.9 s |

Check the formula against Slow 4G. The full photo is 2,431,483 bytes. At 180,000 bytes per second
that is **13.5 seconds** of transfer. Add the latency for three requests and you are close to the
measured **14.7**.

Resizing an image with CSS, which you did in Week 2, changes how big it is drawn. **It does not
change what is downloaded.** To save bandwidth, the file itself has to be smaller.

---

## Worked example 2: thirty small files against one

`icons-many.html` loads thirty badge icons as thirty files, about 1 kB each. `icons-one.html` loads
the same thirty badges from one file.

| Page | Requests | Transferred | No throttling | Fast 4G | Slow 4G | Slow 3G |
|---|---|---|---|---|---|---|
| icons-many | 32 | 39.3 kB | about 40 ms | 1.26 s | 4.0 s | 14.2 s |
| icons-one | 3 | 29.7 kB | about 16 ms | 0.39 s | 1.3 s | 4.7 s |

The byte counts are nearly the same. Bandwidth cannot explain a threefold difference: 39.3 kB takes
a fraction of a second even at 1.44 Mbps. **Latency does.** Thirty-two requests pay the wait in
several rounds. Three requests pay it once or twice.

With no throttling the gap is about 24 milliseconds, which nobody notices. That is why this bug
never shows up on the machine you build on.

---

## Worked example 3: which fix for which problem

| Symptom in the Network panel | Which one is hurting | The fix that helps |
|---|---|---|
| One row with a huge Size, long green bar | Volume on limited bandwidth | Make the file smaller: an image sized for its display, compressed |
| Many rows, each small, long wait before each | Latency | Fewer requests: combine small files, remove ones you do not need |
| Fine on Fast 4G, slow on Slow 3G | Both, and it is where your users are | Measure at the worst setting your users will have |

The Network panel's **Waterfall** column shows the difference. A long bar that is mostly one colour
is download time. A row that sits for a long time before its bar starts is waiting.

---

## The wrong version, and what it shows

Double-click `photo-full.html` in File Explorer instead of loading it from the server. The address
bar starts with `file:///`. The Network panel shows the files, but there is no network between you
and them, and throttling does not describe anything real about how that page will reach a visitor.
**Always measure over HTTP.**

The other wrong version is not a mistake in dev tools. It is this sentence: "I resized the photo in
CSS, so it loads faster now." It does not. The transferred column is the proof.

---

## Why the wrong version is tempting

Everything is fast on your machine, so you never see the problem. And "I made it smaller" feels
true when you can see it is smaller on screen. The Network panel is the habit that replaces the
feeling with a number.

---

## Vocabulary

| Term | What it means |
|---|---|
| **Volume** | The amount of data transferred, in bytes |
| **Bandwidth** | The data a link can carry per second, in bits per second |
| **Latency** | The delay before data starts to move for a request, in milliseconds |
| **Throughput** | What actually got through per second, which bandwidth limits |
| **Request** | One file asked for and delivered. Each row in the Network panel. |
| **Transferred** | Bytes that crossed the network, shown in the Network status bar |
| **Throttling** | DevTools slowing the connection on purpose to imitate a slower network |
| **Waterfall** | The Network panel column showing when each request waited and downloaded |

---

## Self-check

**Question 1.** A 4 MB video poster image is shown at 300 pixels wide using CSS. A classmate says
it is fine because it looks small. Using the Slow 4G bandwidth above, roughly how long does that one
file take to transfer, and what is the fix?

**Question 2.** Page A: 2 requests, 800 kB. Page B: 60 requests, 90 kB. Which is likely slower on a
high-latency, high-bandwidth connection, and which on a low-latency, low-bandwidth one?

**Question 3.** Why does throttling in dev tools matter more for your capstone than a speed test on
your own phone?

---

### Answers

**1.** 4 MB is about 4,000,000 bytes. At 180,000 bytes per second that is about 22 seconds, plus
latency. Displaying it small does not change the download. The fix is to serve an image file sized
for its 300-pixel display, and compressed.

**2.** On high latency with plenty of bandwidth, page B is slower, because sixty requests pay the
wait in many rounds and the bytes are cheap. On low bandwidth with little latency, page A is
slower, because 800 kB takes much longer to push through a narrow link than 90 kB.

**3.** Your phone's speed test measures your phone, in one place, once. Throttling lets you load
the same page under the same slow settings every time, so you can compare two versions of your
page fairly and see what your stakeholder's users will see on a worse connection than yours.
