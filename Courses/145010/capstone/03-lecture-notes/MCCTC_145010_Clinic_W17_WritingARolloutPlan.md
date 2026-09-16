# Clinic · Writing a Rollout Plan
## 145010 Senior Capstone · Clinic · Week 17, Monday

**The signal:** rollout plan drafts with no contingency section, or with the student's own name in
the support column. The plan is sent to the stakeholder tomorrow.

**Slides:** This clinic has no slide outline. It runs from the board.

**If you missed it,** you can learn the skill from this file alone.

**Competencies:** 2.13.1 (include overall project goals and timelines in the rollout plan), 2.13.2
(communicate rollout plans to key stakeholders in a timely manner), 2.13.4 (identify support staff,
training needs, and contingency plans), 1.4.4 (use system hardware to support software
applications), 1.10.4 (procedures for initiating product and service improvements)

**Every example below is a composite.** The Northside Community Garden and Birchwood Auto Parts are
invented organizations.

---

## The idea in plain language

**A rollout plan answers one question: how does the stakeholder keep using this after you leave?**
It says what changes on the day it goes live, who gets access, who is trained, who helps when
something goes wrong, what to do when it breaks, and how to go back to the old way if they need to.
The template is the [Rollout Plan](../05-labs/MCCTC_145010_Template_RolloutPlan.md).

## Why it exists

After Week 18 you are gone. A project with no plan for that works until the first unexpected
Tuesday, and then it stops being used. **Handing something over is a project of its own**, and the
WebXam names its parts: goals and timelines (2.13.1), support staff, training needs, and contingency
plans (2.13.4).

**"Timely" means before, not during.** The plan goes to the stakeholder on Tuesday so that
Thursday's training and Friday's handoff hold no surprises. That is what 2.13.2 means.

**This is harder than it looks**, because it asks you to imagine your project failing when you are
not there. Most students have not done that yet.

---

## Worked example 1 · support staff, with nobody who is leaving

```
## 6. Support staff
| Situation                         | Who handles it          | What they need to know                        | Where it is written      |
| A volunteer cannot sign up        | garden coordinator      | the three most common problems and fixes      | User guide, section 6    |
| The sign-up page does not load    | garden coordinator      | wait one minute, reload; then the fallback    | Contingency plan, row 1  |
| A new coordinator needs an account| garden board secretary  | how to create a coordinator account           | User guide, section 8    |
| Nobody at the garden can fix it   | nobody is available; the paper sheet is used, and a future student may be asked through the school | the way back, below | Section 8 |
```

**Read the last row.** It does not pretend. It says what happens when nobody can fix it, and it
points at a fallback that already works. **The student's name appears nowhere**, because after Week
18 that support line would be false.

## Worked example 2 · contingency plans that can be followed

```
## 8. Contingency plans
| If this happens                      | The first sign                          | What to do                                   | Who does it        | Fallback while it is broken      |
| The free host puts the app to sleep  | the page takes 30-60 s to load          | wait one minute and reload                   | any user           | none needed                      |
| The free host changes its terms or the app is removed | page shows the host's error, all day | check the host's status page; tell the board | garden coordinator | the paper sign-up sheet by the shed |
| The database fills up                | new claims show "Sign-up is down"       | nothing by hand: the retention rule removes last season's rows each night; if it persists, use the fallback | garden coordinator | paper sheet |
| The trained coordinator leaves       | no one can create accounts              | the board secretary follows user guide section 8 | board secretary  | coordinator account shared by the board until then |

The way back: the paper sheet stays by the shed for the first two weeks. To return
to paper for good, print the current week from the export page, pin it up, and stop
sharing the link. No data needs to be moved; the app can be left off.
```

**Each row has a first sign.** A contingency plan nobody notices is needed is not a plan. Each row has
a fallback, so a failure costs the garden a paper sheet, not a Saturday.

**Hardware version (1.4.4), from an Industrial/HMI composite.** For a temperature monitor at Birchwood
Auto Parts, a row reads: "The lab-owned Raspberry Pi is returned to the lab in Week 18 | the dashboard
shows 'no reading for 10 min' | the shop manager decides, before Week 18, whether the shop buys its own
device; setup steps are in the README | shop manager | the wall thermometer and the paper log." The
plan says who owns the hardware after the course, because that is where hardware projects most often
stop.

## Worked example 3 · the timeline and the Tuesday message

```
## 3. Timeline
| When          | Step                                                        | Who                          |
| Week 17, Tue  | Rollout plan sent for review                                 | Student                      |
| Week 17, Wed  | User guide and training materials delivered                  | Student                      |
| Week 17, Thu  | Training session at school, 30 minutes                       | Student and coordinator      |
| Week 17, Fri  | Final test on the delivered system; handoff checklist; final approval | Student and coordinator |
| Week 18, end  | Student support ends, unless agreed otherwise in writing     |                              |
```

The Tuesday message follows section 7 of the
[Stakeholder Communication Guide](../05-labs/MCCTC_145010_Guide_StakeholderCommunication.md#7-handoff-and-training):
what is attached, the training time, who looks after it once you have graduated, what to do if it
stops, what you will fix and until when, and a specific question with a reply date.

**The result:** the stakeholder can say "the support section is wrong, the secretary is leaving
too" on Wednesday, while there is still time to fix it.

---

## The wrong version, and what it produces

```markdown
# Rollout Plan
We will launch on Friday. I will train the coordinator.
If anything breaks, they can contact me and I will fix it.
Contingency: restart the server.
```

**What it produces:** a plan that fails its first real test. "Contact me" breaks the school-channel
rule now and becomes false after Week 18. "Restart the server" is an instruction the coordinator
cannot follow, and a hand restart is exactly the manual intervention the thirty-day rule counts
against you. There is no first sign, no fallback, no way back, and no timeline. Sent on Friday, it
also misses "timely." The rubric's handoff part asks for a plan sent before the handoff, and this one
arrived with it.

## Why the wrong version is tempting

You are the person who knows how it works, so naming yourself feels responsible. Planning for
failure also feels like predicting your own project will break. **It will, eventually, like every
system, and the plan is what decides whether that day is a shrug or the end of the project.**

---

## What to do in your project today

1. Copy the [Rollout Plan template](../05-labs/MCCTC_145010_Template_RolloutPlan.md) into
   `docs/control/rollout-plan.md`.
2. Section 6 first: for every support line, a role at the stakeholder's organization, or an honest
   "nobody." Remove your name from every line that runs past Week 18.
3. Section 8: at least three contingencies, each with a first sign and a fallback. Write the way
   back.
4. Section 9: where it runs after Week 18, and anything with a time limit, such as a free tier or a
   lab device.
5. Section 10: how a future improvement would be requested, pointing at your future improvements
   list.
6. Draft Tuesday's message. Your instructor reads it before it goes. Commit both.

---

## Vocabulary

| Term | Meaning |
|---|---|
| **Rollout plan** | How the project goes into use and keeps being used after you leave |
| **Support staff** | The roles at the organization who help users after handoff |
| **Training needs** | Who must learn what, how, and how you know they learned it |
| **Contingency plan** | What happens when something fails, with a first sign and a fallback |
| **Way back** | How to return to the old process without losing anything |
| **Timely** | Sent before the handoff, with time to change it |

---

## Check yourself

1. Why is "restart the server" a weak contingency, even if it would work?
2. Your project runs on a lab machine that stays in the lab. What must section 9 say?
3. Your stakeholder has no one who can fix code. Is it honest to write a support line anyway? What
   do you write?

---

## Check your answers

**1.** It names an action the stakeholder probably cannot take, it has no first sign or fallback, and
a hand restart is a manual intervention. A strong row says what the user will notice, what they can
do themselves, who does the rest, and what they use while it is broken.

**2.** That the lab machine stays in the lab after Week 18, what that means for the project (it stops
being reachable, or the instructor agrees to keep it running), and the decision the stakeholder has
to make before then, such as moving it to a device or host they control.

**3.** Yes, if the line is true. Write the situation, "nobody at the organization can fix the code,"
and what happens: the fallback is used, and a future student may be asked through the school, with
nothing promised. An honest "nobody" is better than a name that will not answer.
