# What a Page Costs to Deliver
---
## Slide 1: Two pages that look identical
- Same text, same photo, same layout
- One loads in 3.3 seconds on Slow 4G
- The other takes 14.7 seconds
- You cannot see the difference. You can measure it.
Speaker notes: These two pages look exactly the same on screen. On a slow connection, one takes more than four times as long as the other. Every page you build loads instantly on the lab machines, which tells you nothing about the parent at the ball field with one bar of signal. Today you learn to measure what a page costs, and to say which of two problems is making it slow.
Image: Two identical phone screenshots side by side, with a stopwatch under each showing different times.
---
## Slide 2: Three words that are not the same
- Volume: how many bytes have to move
- Bandwidth: how many bits per second the link carries
- Latency: how long each request waits first
- Eight bits in a byte
Speaker notes: Volume is the amount of water in the tank. Bandwidth is how wide the pipe is. Latency is how long before the tap starts running, and you pay it every time you open a tap. Files are measured in bytes and links in bits, and there are eight bits in a byte, so a link of about one and a half megabits moves about one hundred and eighty kilobytes a second.
Image: A water tank, a pipe, and a tap with a small clock on it, each labelled with one of the three words.
---
## Slide 3: The rough model
```
time  is about  (latency x the rounds of requests that wait)
              + (volume / bandwidth)
```
Speaker notes: This is not exact, and it does not need to be. It tells you which half is hurting. A big file on a narrow link, the second half dominates. Lots of small files on a laggy link, the first half dominates, because the browser opens only a handful of connections to one server and every round of requests waits again.
Image: None. This slide is code.
---
## Slide 4: How to measure it
- Serve the page over HTTP, never file://
- Network panel, tick Disable cache
- Pick a throttling setting
- Reload, then read requests, transferred, Load
Speaker notes: Four steps. Serve the page, because a double-clicked file never crosses a network. Open the Network panel and tick Disable cache, and keep dev tools open or the tick does nothing. Choose a throttling setting from the menu at the top. Reload, and read the three numbers in the status bar at the bottom.
Image: The Network panel with the Disable cache box, the throttling menu, and the status bar each outlined.
---
## Slide 5: Start the server, say the port
```
cd 05-labs\lab-w04-02-files
python serve.py --port 8404
```
Speaker notes: Our lab server takes its port every time, and I am saying it out loud: eight four zero four. It generates the photos in memory when it starts and prints their sizes. When the period ends we stop it with Control C, and you paste the word Stopped into your lab notes as proof.
Image: None. This slide is code.
---
## Slide 6: The photo, measured
```
page          requests  transferred  Slow 4G   Slow 3G
photo-full    3         2,376.5 kB   14.7 s    52.7 s
photo-sized   3           382.1 kB    3.3 s    11.9 s
```
Speaker notes: Same look, six times the bytes, more than four times the wait. Check it against the model. Two point four million bytes at one hundred and eighty thousand a second is thirteen and a half seconds, plus the waiting for three requests. That lands close to the fourteen point seven we measured. This is bandwidth.
Image: None. This slide is code.
---
## Slide 7: The wrong way
- "I made the photo 480 wide in CSS"
- "So it loads faster now"
- Transferred still says 2,376.5 kB
- CSS changes the drawing, not the download
Speaker notes: This is the mistake, and it is a sentence rather than a line of code. In Week 2 you resized images with CSS, and that was the right skill for layout. It does nothing for the download. The browser still fetches every byte and then draws it smaller. The transferred column is the proof. The fix is a smaller file.
Image: A large photo being squeezed into a small frame, with the full-size file still sitting in a download tray.
---
## Slide 8: The icons, measured
```
page         requests  transferred  none    Slow 4G  Slow 3G
icons-many   32        39.3 kB      40 ms   4.0 s    14.2 s
icons-one    3         29.7 kB      16 ms   1.3 s     4.7 s
```
Speaker notes: Now the byte counts are almost the same, and the times are three times apart. Bandwidth cannot explain that. Latency can. Thirty-two requests wait in rounds and pay the delay every round. And look at the no-throttling column: twenty-four milliseconds of difference, which nobody notices. That is why this problem never shows up on the machine you build on.
Image: None. This slide is code.
---
## Slide 9: Which fix for which problem
- One huge row: shrink the file
- Many small rows: make fewer requests
- Fine fast, slow slow: test at the worst setting
- Throttling compares pages. It does not predict one phone.
Speaker notes: The Network panel tells you which problem you have. One big row with a long download bar is volume on limited bandwidth, so make the file smaller. Many small rows that sit waiting is latency, so make fewer requests. And be honest about what throttling is: a fixed delay and a speed cap, good for comparing two versions of your page, not a promise about one real phone.
Image: A simplified waterfall chart with one long bar in one panel and many short, late-starting bars in another.
---
## Slide 10: What you are about to build
- Lab W04-02: four pages, two settings, eight rows
- Answer which problem each pair shows, with numbers
- Then measure your own component under Slow 4G
- Stop every server you start
Speaker notes: Build one is the measurement lab. Eight rows, all real, and two answers that use numbers from your own table. Build two is your project, and in the last fifteen minutes you serve your own folder on port eight four one four, measure it under Slow 4G, and put the three numbers in your README. Then stop the server and say so.
Image: A lab notebook table with eight filled rows, and a terminal showing the word Stopped.
---
