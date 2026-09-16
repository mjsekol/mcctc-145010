"""Thirty-day survival report.

Reads a health log and an events log and answers one question: what is the
longest stretch in which the system ran without manual intervention?

A run is broken by any of these:
  1. an intervention recorded in the events log
  2. a gap between health lines longer than --max-gap-minutes that no planned
     event explains
  3. failed checks lasting longer than --max-outage-minutes

A planned release recorded in the events log does not break a run. A gap that
contains a planned release is excused.

Usage (standard library only, Python 3.10 or newer):

    python survival_report.py --health health-log.txt --events events-log.txt
        --max-gap-minutes 45 --max-outage-minutes 60

Health log lines (written by health_check.py or by your own service):

    2027-04-23T14:15:02  result=ok  status=200  ms=412

Events log lines, written by you on the day, one event per line:

    2027-04-24T15:02:00  planned  released version 1.3.0 by the documented steps
    2027-04-29T08:40:00  intervention  restarted the service by hand after it hung

Blank lines and lines starting with # are ignored in both files.
"""

import argparse
import datetime

DAYS_REQUIRED = 30


def parse_time(text, source, number):
    try:
        return datetime.datetime.fromisoformat(text)
    except ValueError:
        raise SystemExit(f"{source} line {number}: cannot read the timestamp {text!r}")


def read_health(path):
    """Return a sorted list of (time, ok) pairs."""
    checks = []
    with open(path, encoding="utf-8") as handle:
        for number, raw in enumerate(handle, 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            when = parse_time(parts[0], path, number)
            fields = dict(p.split("=", 1) for p in parts[1:] if "=" in p)
            if "result" not in fields:
                raise SystemExit(f"{path} line {number}: no result= field")
            checks.append((when, fields["result"] == "ok"))
    if not checks:
        raise SystemExit(f"{path}: no health lines found")
    checks.sort()
    return checks


def read_events(path):
    """Return two sorted lists of (time, description): planned and interventions."""
    planned, interventions = [], []
    if path is None:
        return planned, interventions
    with open(path, encoding="utf-8") as handle:
        for number, raw in enumerate(handle, 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(None, 2)
            if len(parts) < 2 or parts[1] not in ("planned", "intervention"):
                raise SystemExit(f"{path} line {number}: expected 'planned' or 'intervention'")
            when = parse_time(parts[0], path, number)
            description = parts[2] if len(parts) == 3 else ""
            (planned if parts[1] == "planned" else interventions).append((when, description))
    planned.sort()
    interventions.sort()
    return planned, interventions


def find_breaks(checks, planned, interventions, max_gap, max_outage):
    """Return a sorted list of (start, end, reason). No run may overlap one."""
    breaks = [(when, when, f"intervention: {text}") for when, text in interventions]

    # Gaps between consecutive health lines.
    for (before, _), (after, _) in zip(checks, checks[1:]):
        if after - before > max_gap:
            excused = any(before <= when <= after for when, _ in planned)
            if not excused:
                breaks.append((before, after, f"unexplained gap of {after - before}"))

    # Outages: consecutive failed checks, measured to the next good check.
    outage_start = None
    for when, ok in checks:
        if not ok and outage_start is None:
            outage_start = when
        elif ok and outage_start is not None:
            if when - outage_start > max_outage:
                breaks.append((outage_start, when, f"failed checks for {when - outage_start}"))
            outage_start = None
    if outage_start is not None and checks[-1][0] - outage_start > max_outage:
        breaks.append((outage_start, checks[-1][0], "failing when the log ends"))

    breaks.sort()
    return breaks


def longest_run(first, last, breaks):
    """Return (length, start, end) of the longest stretch that touches no break."""
    best = (datetime.timedelta(0), first, first)
    cursor = first
    for start, end, _ in breaks + [(last, last, "end of log")]:
        if start - cursor > best[0]:
            best = (start - cursor, cursor, start)
        cursor = max(cursor, end)
    return best


def main():
    parser = argparse.ArgumentParser(description="Report the longest unattended run.")
    parser.add_argument("--health", required=True, help="the health log")
    parser.add_argument("--events", help="the events log of planned releases and interventions")
    parser.add_argument("--max-gap-minutes", type=float, required=True,
                        help="longest allowed silence between health lines, "
                             "usually a little more than twice your check interval")
    parser.add_argument("--max-outage-minutes", type=float, required=True,
                        help="longest allowed stretch of failed checks, from your requirements")
    args = parser.parse_args()

    checks = read_health(args.health)
    planned, interventions = read_events(args.events)
    max_gap = datetime.timedelta(minutes=args.max_gap_minutes)
    max_outage = datetime.timedelta(minutes=args.max_outage_minutes)
    breaks = find_breaks(checks, planned, interventions, max_gap, max_outage)

    first, last = checks[0][0], checks[-1][0]
    failed = sum(1 for _, ok in checks if not ok)
    length, run_start, run_end = longest_run(first, last, breaks)
    days = length.total_seconds() / 86400

    print(f"health lines        {len(checks)}  ({failed} failed)")
    print(f"observed            {first.isoformat()}  to  {last.isoformat()}")
    print(f"planned releases    {len(planned)}")
    print(f"interventions       {len(interventions)}")
    print(f"run breaks          {len(breaks)}")
    for start, _, reason in breaks:
        print(f"  {start.isoformat()}  {reason}")
    print(f"longest run         {days:.1f} days  ({run_start.isoformat()}  to  {run_end.isoformat()})")
    reached = days >= DAYS_REQUIRED
    print(f"thirty days reached {'yes' if reached else 'no'}")
    return 0 if reached else 1


if __name__ == "__main__":
    raise SystemExit(main())
