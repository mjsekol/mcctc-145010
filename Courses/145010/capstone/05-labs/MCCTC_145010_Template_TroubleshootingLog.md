# Template · Troubleshooting Log
## 145010 Senior Capstone · Weeks 9-18, written as it happens

**Commit as:** `troubleshooting-log.md` at the top of your repository.
**Due:** continuously. An entry for every real problem that takes you more than twenty minutes, and
for every manual intervention on the deployed system.

**Competencies this evidences:** 2.11.1 (identify the problem), 2.11.2 (select a troubleshooting
methodology), 2.11.3 (investigate symptoms), 2.11.4 (gather and analyze data), 2.11.5 (design a
solution), 2.11.6 (test a solution), 2.11.7 (implement a solution), 2.11.8 (document the problem
and the verified solution).

---

## Why this exists

**Troubleshooting is a whole WebXam outcome**, and it is the one the capstone exercises every day.
The exam asks you to name a method and follow it. This log is where you practice doing that on
purpose instead of by trial and error.

**It is also where your best defense answer comes from.** "Tell me about the worst bug you found"
is a standard defense question. A student with this log answers in forty-five seconds with a
method, evidence, and a verified fix.

**The failure to avoid is writing only the fix.** "Changed the port, works now" tells a reader
nothing next time. The symptom, the method, and the evidence are what make the entry useful.

---

## The four methods

| Method | Use it when | How it goes |
|---|---|---|
| **Top down** | You suspect how the pieces fit together | Start at what the user sees. Work inward one layer at a time. |
| **Bottom up** | You suspect a low-level piece | Start at the device, database, or model server. Confirm each works, then move outward. |
| **Follow the path** | Data goes in right and comes out wrong | Check the data at every step it passes through, in order, until it changes. |
| **Spot the differences** | It works in one place and not another | List every difference between the two. Change one at a time. |

**Pick one before you start, and write down which.** Switching is allowed. Write down when and why.

---

```markdown
# Troubleshooting Log · <project name>

## TS-<n> · <the symptom in a few words>
**Found:** Week <n>, <day>   **Resolved:** Week <n>, <day>
**Intervention on the deployed system?** <no / yes, recorded in the events log>

**1. The problem** *(2.11.1)*
<What happens, exactly. The message, the wrong value, the missing line. Where and when.>

**2. The method** *(2.11.2)*
<Top down / bottom up / follow the path / spot the differences, and why this one.>

**3. What I investigated** *(2.11.3)*
| Step | What I checked | What I found |
|---|---|---|
| 1 | | |
| 2 | | |

**4. The evidence** *(2.11.4)*
<Log lines, output, measurements, comparisons. Pasted, not described. No personal data, no
secrets.>

**5. The cause**
<One or two sentences.>

**6. The solution** *(2.11.5, 2.11.7)*
<What you changed, with file and commit.>

**7. How I proved it worked** *(2.11.6)*
<The test case, the command, the output.>

**8. What stops it happening again**
<A test, a check, a design change, a note in the user guide.>

**Related:** <decision log, AI usage log, test plan case>
```

---

## A worked example

**Composite example.** Write your own.

```markdown
## TS-4 · Dashboard shows no readings after a reboot
**Found:** Week 12, Tuesday   **Resolved:** Week 12, Wednesday
**Intervention on the deployed system?** yes, recorded in the events log. Clock restarted.

**1. The problem**
After the Pi was rebooted for a planned release, the web dashboard showed "no data yet" and the
panel showed "service unreachable." The Pi was powered and on the lab network.

**2. The method**
Bottom up. The panel and dashboard both failed, so the shared lower layer was the likely cause.

**3. What I investigated**
| Step | What I checked | What I found |
|---|---|---|
| 1 | Sensor read by hand with the test script | Reading returned normally |
| 2 | Whether the logger service was running | Not running |
| 3 | The service manager's status for the logger | Service was not enabled to start at boot |

**4. The evidence**
The health log had no lines after the reboot. The service status said the unit was disabled.

**5. The cause**
The service had been started by hand in Week 11 and was never enabled to start at boot.

**6. The solution**
Enabled the logger service to start at boot and added the step to the deployment steps in the
architecture document. Commit a41c9e0.

**7. How I proved it worked**
Planned power-loss test, recorded as a planned event. Health log lines resumed 70 seconds after
power returned, with no command typed.

**8. What stops it happening again**
Test case T-15, "reboot and confirm the health log resumes," added to the test plan and run
after every release.

**Related:** D-11, events log Week 12 Wednesday.
```

---

## Before you commit · self-check

- [ ] The method is named before the investigation.
- [ ] The evidence is pasted, not described.
- [ ] Every "resolved" entry has a proof under it.
- [ ] Every intervention on the deployed system appears in the events log too.
