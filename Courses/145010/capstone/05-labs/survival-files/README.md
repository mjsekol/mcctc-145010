# Survival Files
## 145010 Senior Capstone · tools for the thirty-day survival record

Everything here uses the Python standard library only. Instructions are in
[the Thirty-Day Survival Record template](../MCCTC_145010_Template_ThirtyDaySurvival.md).

| File | What it is |
|---|---|
| `health_check.py` | Calls a health address once and appends one line to a health log. Run it on a schedule. |
| `survival_report.py` | Reads a health log and an events log and reports the longest run without manual intervention. |
| `sample-health-log.txt` | **Invented** health log, 40 days, one check every 30 minutes. For practice. |
| `sample-events.txt` | **Invented** events log: one early intervention, two planned releases. |
| `sample-events-late-intervention.txt` | The same, plus one intervention in the middle. Compare the two reports. |

Every address you pass to `health_check.py` includes its port. Nothing in these files is a real
system, a real organization, or a real person.
