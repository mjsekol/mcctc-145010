"""report.py: turn the counts serve.py kept into a traffic report you can read.

    python report.py                        reads data/counts.json
    python report.py --data other.json
    python report.py --url http://127.0.0.1:8660    asks a running server instead

The numbers answer two questions and only two:
    Which pages get loaded, and on which days?
    Of the people who answered, how many said the page was useful?

They cannot tell you how many people visited. A page view is a page load, not a person.
"""
import argparse
import json
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(args):
    if args.url:
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        with opener.open(args.url.rstrip("/") + "/api/stats", timeout=5) as response:
            return json.loads(response.read().decode("utf-8"))
    path = Path(args.data)
    if not path.exists():
        return {"views": {}, "helpful": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def report(data):
    views = data.get("views", {})
    helpful = data.get("helpful", {})
    pages = sorted(set(views) | set(helpful))
    days = sorted({day for by_day in views.values() for day in by_day})

    lines = ["Traffic report", ""]
    if not pages:
        lines.append("No page views recorded yet.")
        return "\n".join(lines)

    lines.append(f"{'Page':<16}{'Views':>7}{'Useful':>8}{'Not':>6}{'Useful %':>10}")
    total_views = 0
    for page in pages:
        count = sum(views.get(page, {}).values())
        total_views += count
        yes = helpful.get(page, {}).get("yes", 0)
        no = helpful.get(page, {}).get("no", 0)
        answered = yes + no
        rate = f"{100 * yes / answered:.0f}%" if answered else "n/a"
        lines.append(f"{page:<16}{count:>7}{yes:>8}{no:>6}{rate:>10}")
    lines.append(f"{'Total':<16}{total_views:>7}")
    lines.append("")
    lines.append("Views by day")
    for day in days:
        lines.append(f"  {day}  {sum(v.get(day, 0) for v in views.values())}")
    lines.append("")
    lines.append("A view is a page load, not a person. Your own visits and reloads are in these numbers.")
    answered_total = sum(t.get("yes", 0) + t.get("no", 0) for t in helpful.values())
    if answered_total < 10:
        lines.append(f"Only {answered_total} usefulness answer(s) so far. Too few to call it a pattern.")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default=str(HERE / "data" / "counts.json"))
    parser.add_argument("--url", default=None)
    print(report(load(parser.parse_args())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
