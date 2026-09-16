"""
serve.py - static site server with first-party analytics for the Quarry Hill Skate Crew.

Usage:
    python serve.py --port 8616

Serves everything in ./site and records page views to hits.csv.
GET /api/stats returns total views and unique visitors per page.
"""
import argparse
import csv
import datetime
import json
import sys
import threading
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE_DIR = HERE / "site"
HITS_FILE = HERE / "hits.csv"
PAGES = {"/", "/index.html", "/schedule.html", "/volunteer.html"}

_lock = threading.Lock()


def record_hit(page, visitor, client_ip):
    """Append one page view. Anonymous: stores no names or emails."""
    new_file = not HITS_FILE.exists()
    with _lock, HITS_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["timestamp", "page", "visitor", "ip"])
        writer.writerow([datetime.datetime.now().isoformat(timespec="seconds"), page, visitor, client_ip])


def load_stats():
    """Total views and unique visitors for each page."""
    stats = {}
    if not HITS_FILE.exists():
        return stats
    with HITS_FILE.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            page = stats.setdefault(row["page"], {"views": 0, "visitors": set()})
            page["views"] += 1
            page["visitors"].add(row["visitor"])
    return {p: {"views": s["views"], "unique_visitors": len(s["visitors"])} for p, s in stats.items()}


class AnalyticsHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/stats":
            body = json.dumps(load_stats(), indent=2).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def do_POST(self):
        if self.path != "/api/hit":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", 0))
        try:
            data = json.loads(self.rfile.read(length))
            page = "/" if data["path"] == "/index.html" else data["path"]
        except (ValueError, KeyError, TypeError):
            self.send_error(400, "Invalid hit")
            return
        if page not in PAGES:
            self.send_error(400, "Unknown page")
            return
        record_hit(page, data.get("visitor", ""), self.client_address[0])
        self.send_response(204)
        self.end_headers()


def main():
    parser = argparse.ArgumentParser(description="Quarry Hill Skate Crew site server")
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("--host", default="127.0.0.1")
    args = parser.parse_args()
    handler = partial(AnalyticsHandler, directory=str(SITE_DIR))
    server = ThreadingHTTPServer((args.host, args.port), handler)
    print(f"Serving on http://{args.host}:{args.port}/")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
