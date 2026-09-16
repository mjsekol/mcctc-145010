"""serve.py (STARTER): publish site/ over HTTP and count page views without tracking anyone.

Copy this file into your sitekit folder, next to build.py, then:

    python build.py
    python serve.py --port 8606

Right now it serves your pages and counts nothing. The lab walks you through the TODOs.

The rule for everything you add: store the page address and the day. Nothing else.
No IP address, no cookie, no browser description, no visitor ID. Your visitors
include people under 18, and a count does not need to know who anyone is.
Standard library only.
"""
import argparse
import datetime
import json
import os
import sys
import threading
import traceback
from functools import partial
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAX_BODY_BYTES = 1024          # a real hit is under 100 bytes
ANSWERS = ("yes", "no")


class CountStore:
    """Counts kept in one JSON file: {"views": {...}, "helpful": {...}}."""

    def __init__(self, path):
        self.path = Path(path)
        self.lock = threading.Lock()
        if self.path.exists():
            self.data = json.loads(self.path.read_text(encoding="utf-8"))
        else:
            self.data = {"views": {}, "helpful": {}}

    def _save(self):
        # Write a temporary file, then swap it in, so a crash never leaves half a file.
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temp = self.path.with_suffix(".tmp")
        temp.write_text(json.dumps(self.data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        os.replace(temp, self.path)

    def add_view(self, page):
        # TODO step 5: add one to self.data["views"][page][today], inside the lock, then save.
        # today is datetime.date.today().isoformat()
        raise NotImplementedError("add_view is step 5")

    def add_helpful(self, page, answer):
        # TODO step 8: add one to self.data["helpful"][page][answer], inside the lock, then save.
        raise NotImplementedError("add_helpful is step 8")

    def snapshot(self):
        with self.lock:
            return json.loads(json.dumps(self.data))


def normalise(path):
    """'/index.html' and '/' are the same page. Drop any ?query or #fragment."""
    path = path.split("?", 1)[0].split("#", 1)[0]
    return "/" if path in ("", "/index.html") else path


class SiteHandler(SimpleHTTPRequestHandler):
    store = None          # set in main()
    known_pages = ()      # set in main(), from site/pages.json

    # TODO step 2: the standard handler's log line starts with something you must not keep.
    # Override log_request(self, code="-", size="-") here so it writes only the method,
    # the address asked for, and the status.

    def _read_body(self):
        length = int(self.headers.get("Content-Length") or 0)
        if length > MAX_BODY_BYTES:
            return None
        return self.rfile.read(length).decode("utf-8", errors="replace")

    def _reply(self, status, payload=None):
        body = b"" if payload is None else (json.dumps(payload) + "\n").encode("utf-8")
        self.send_response(status)
        if payload is not None:
            self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        if body:
            self.wfile.write(body)

    def do_GET(self):
        if self.path.split("?", 1)[0] == "/api/stats":
            self._reply(HTTPStatus.OK, self.store.snapshot())
            return
        super().do_GET()

    def do_POST(self):
        route = self.path.split("?", 1)[0]
        body = self._read_body()
        if body is None:
            self._reply(HTTPStatus.REQUEST_ENTITY_TOO_LARGE, {"error": "body too large"})
            return
        if route == "/api/hit":
            self._hit(body)
        elif route == "/api/helpful":
            self._helpful(body)
        else:
            self._reply(HTTPStatus.NOT_FOUND, {"error": "no such endpoint"})

    def _hit(self, body):
        # TODO step 4: body is JSON text like {"path": "/layout.html"}.
        #   Parse it. If it is not JSON or has no "path", reply 400.
        #   normalise() the path. If it is not in self.known_pages, reply 400.
        #   Otherwise call self.store.add_view(page) and reply 204.
        self._reply(HTTPStatus.NOT_IMPLEMENTED, {"error": "counting is step 4"})

    def _helpful(self, body):
        # TODO step 8: body is form text like page=%2Flayout.html&answer=yes
        #   (urllib.parse.parse_qs reads it). Refuse unknown pages and any answer not in ANSWERS.
        #   Count it. If the Accept header contains application/json, reply 204.
        #   Otherwise reply 303 with a Location header of the page, taken from your own
        #   known_pages, so a plain form sends the visitor back where they were.
        self._reply(HTTPStatus.NOT_IMPLEMENTED, {"error": "the usefulness question is step 8"})


class QuietServer(ThreadingHTTPServer):
    """TODO step 4: when a request crashes, the standard server prints a line naming
    the visitor's address above the traceback. Override
    handle_error(self, request, client_address) so it prints the traceback only.
    traceback.print_exc() prints the current traceback."""


def main(argv=None):
    parser = argparse.ArgumentParser(description="Serve site/ and count page views without tracking anyone.")
    parser.add_argument("--port", type=int, default=None, help="required unless the PORT environment variable is set")
    parser.add_argument("--host", default="127.0.0.1", help="127.0.0.1 for this machine only")
    parser.add_argument("--site", default=str(HERE / "site"))
    parser.add_argument("--data", default=str(HERE / "data" / "counts.json"))
    args = parser.parse_args(argv)

    port = args.port if args.port is not None else os.environ.get("PORT")
    if port is None:
        parser.error("say which port: --port 8606")
    site = Path(args.site)
    pages_file = site / "pages.json"
    if not pages_file.exists():
        parser.error(f"{pages_file} not found. Run python build.py first.")

    SiteHandler.store = CountStore(args.data)
    SiteHandler.known_pages = tuple(json.loads(pages_file.read_text(encoding="utf-8")))
    handler = partial(SiteHandler, directory=str(site))
    server = QuietServer((args.host, int(port)), handler)
    print(f"Serving {site.name}/ at http://{args.host}:{port}/  (Ctrl+C to stop)", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
