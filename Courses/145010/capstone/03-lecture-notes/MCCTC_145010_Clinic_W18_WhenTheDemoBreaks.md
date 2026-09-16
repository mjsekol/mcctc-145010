# Clinic · When the Demo Breaks
## 145010 Senior Capstone · Clinic · Week 18, Monday

**The signal:** demo plans with no fallback column, or a fallback that says "it won't break."
Presentations start tomorrow.

**Slides:** This clinic has no slide outline. It runs from the board.

**If you missed it,** you can learn the skill from this file alone. The local fallback check in
example 2 was run on the build machine with Python 3.13 and Flask 3.1, and the output is pasted
exactly. The server was stopped afterward.

**Competencies:** 1.2.2 (deliver formal presentations), 1.2.5 (communicate for an intended audience
and purpose), 2.11.1 (identify the problem), 2.11.2 (select a troubleshooting methodology), 6.5.12
(publish the completed website to a web server)

**Every example below is a composite**, except the port check in example 2, which really happened on
the build machine. The Northside Community Garden is an invented organization.

---

## The idea in plain language

**Live demos break on stage. It happens to professionals.** What the panel scores is what you do
next. You plan for it by writing a fallback for every demo step, and by rehearsing the four moves:
say what broke, say what you will do, do it, and come back once at the end if there is time.

## Why it exists

The rubric's live demonstration part says it directly: a demo that breaks and is handled well can
score 4 of 4. A student who names what broke and moves to the recorded fallback without panic shows
the panel something a flawless demo cannot: that they understand their system well enough to route
around it.

**It is also the most stressful minute of the capstone.** Your heart rate goes up, your hands shake,
and the instinct is to start typing. The plan exists so that you do not have to think in that minute.

---

## Worked example 1 · a demo plan with a fallback for every step

From the [Final Presentation Outline](../05-labs/MCCTC_145010_Template_FinalPresentationOutline.md):

```
## The live demo plan
| Step | What you do                              | What the panel should see                  | If it fails                                    |
| 1    | Open the deployed sign-up page on the projector | "Northside Garden · This week's beds"  | Say so; open the local copy on port 8168       |
| 2    | Claim bed 4 as "Tessa" (invented)       | "Bed 4 is yours"                           | Show screenshot 2 (invented data), explain in one sentence |
| 3    | Open the coordinator page, reload       | Tessa on bed 4                             | Screenshot 3                                   |
| 4    | Stop the database on the local copy     | "Sign-up is down, try again in a few minutes" | Screenshot 4; cite AC-4 re-run in the record |

Before my slot:
[x] deployed page loaded 10 minutes ago, so a sleeping free tier is awake
[x] invented demo data in place, no real names
[x] local copy running on 127.0.0.1:8168, checked
[x] screenshots of every step, invented data, in presentation/
[x] notifications off, nothing personal open
```

**Three layers:** the deployed system, then a local copy, then screenshots. Each one is ready before
you walk up, not found during the break.

## Worked example 2 · check the fallback, and check it is yours

A local copy only helps if it is running and answering on the port you think. The check, from a small
script with no proxy:

```python
import urllib.request, urllib.error
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
for url in ["http://127.0.0.1:8168/health", "http://127.0.0.1:8167/health"]:
    try:
        with opener.open(url, timeout=5) as r:
            print(url, r.status, r.read().decode())
    except urllib.error.URLError as e:
        print(url, "URLError", e.reason)
```

With the local copy started by `python -m flask --app app run --host 127.0.0.1 --port 8168`:

```
http://127.0.0.1:8168/health 200 ok
http://127.0.0.1:8167/health URLError [WinError 10061] No connection could be made because the target machine actively refused it
```

**The first line is the fallback answering. The second is a wrong port**, and "actively refused"
means nothing is listening there.

**Something real happened while this note was being written.** A first check on a different port got
an answer, but the answer came from another program that was using that port at the same time, not
from the demo app. The page loaded. It was the wrong page. **Check what the fallback says, not only
that it answers.** In a shared lab, pick an explicit port, check it before your slot, and look at the
content.

## Worked example 3 · the break, handled

```
(Step 1: the projector shows "This site can't be reached")

STUDENT   The hosted page is not answering. I will show the same steps on my
          local copy, which runs the same commit.
          (switches to the local tab, 5 seconds)
          Here is this week's beds page. I will claim bed 4 as Tessa, an
          invented volunteer...
          (demo continues through step 4)
          ...
          (at the end, 20 seconds left)
          Let me try the hosted page once more.
          (it loads)
          It is back. The first load after a quiet period can take up to a
          minute on this host, which is in my rollout plan's contingency
          section and my user guide.
```

**The four moves are all there.** One sentence on what broke. One sentence on what happens next.
Doing it, in five seconds. One brief return at the end, with the reason, pointing at documents the
panel can read. And the student did not debug in front of the panel.

---

## The wrong version, and what it produces

```
(Step 1: "This site can't be reached")

STUDENT   Oh no. Sorry. Um, it worked this morning, I swear. Sorry. Let me
          just... (opens a terminal) ...hold on, let me check the logs...
          (two minutes pass) ...sorry, the school Wi-Fi is really bad...
          I guess I can't show it. Sorry. So, it basically lets you sign up.
```

**What it produces:** two minutes of a ten-minute slot spent debugging, five apologies, blame on the
network, and no demonstration at all. The rubric's 0-1 band for the demo is "no demonstration, or a
failure the student cannot explain." The panel also now doubts the parts of the talk they did not
see, and the defense questions will follow that doubt.

## Why the wrong version is tempting

Your instinct as a developer is to fix what is broken, right now, and you are good at it. On stage
that instinct costs the slot. The failure also feels like it must be explained, so the words pour out.
**One sentence is enough.** The panel cares much more about what you do next than about why it
happened.

---

## What to do in your project today

1. Add the "If it fails" column to your demo plan. Every step gets a fallback.
2. Start a local copy on an explicit port. Check it answers, and check that the answer is your app.
   Write the port in the plan.
3. Take a screenshot of every demo step, with invented data only. Put them in `presentation/`.
4. Rehearse the break with your partner: have them say "the site is down" at a random step, and do
   the four moves out loud.
5. Load the deployed system ten minutes before your slot. Turn notifications off.
6. Tag `capstone-final` before your slot, as the specification requires, and commit your rehearsal
   record.
7. Stop your local server when your presentation ends, and make sure the port is free.

---

## Vocabulary

| Term | Meaning |
|---|---|
| **Fallback** | The next way to show a step when the first way fails |
| **Local copy** | Your app running on your machine, on an explicit port, from the same commit |
| **Explicit port** | A port number you chose and wrote down, never a default |
| **Connection refused** | Nothing is listening on that address and port |
| **The four moves** | Say what broke, say what you will do, do it, come back once |

---

## Check yourself

1. The deployed page fails at step 2 of 4. What do you say, in one sentence each, for the first two
   moves?
2. Your local fallback check returns a page, but it is not your app. What happened, and what do you do?
3. Why are screenshots the last layer and not the first?

---

## Check your answers

**1.** Something like: "The hosted page stopped answering." Then: "I will show the rest on my local
copy, which runs the same commit." Then do it.

**2.** Another program is using that port. Stop and choose a different explicit port, start your app
there, and check the content again. Update the port in your demo plan.

**3.** A screenshot shows that something worked once. A live system, even a local one, shows it
working now. The rubric's full marks go to the deployed system, then credit a well-handled fallback,
so you use the most live option that works.
