"""Stand-in for the deployed Parts Bin Board, as the health checker sees it.

Composite example for the Week 10 clinic "Stand-ins that mimic the outside".
The Parts Bin Board is a composite project, not a real organization's system.

The real board runs on an approved host. The host is the piece you do not control:
it can be asleep, slow, or broken. This stand-in answers the same address the real
board answers (GET /health) with the same shape of reply, and it can pretend to be
in three states, so the health checker can be tested on a lab machine at any time.

Standard library only. The port is always explicit.

Run it (one mode at a time, from this folder):
    python stand_in_server.py --port 5320 --mode normal
    python stand_in_server.py --port 5320 --mode slow
    python stand_in_server.py --port 5320 --mode error
Stop it with Ctrl+C.
"""
import argparse
import json
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

VERSION = "0.1.0-stand-in"
SLOW_SECONDS = 3  # a free-tier host waking up after a quiet night

# What the real /health reply looks like in each state. Same keys every time,
# because the checker reads these keys.
REPLIES = {
    "normal": (200, {"status": "ok", "database": "ok", "version": VERSION}),
    "slow": (200, {"status": "ok", "database": "ok", "version": VERSION}),
    "error": (503, {"status": "error", "database": "unreachable", "version": VERSION}),
}


def make_handler(mode):
    class StandInHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path != "/health":
                self.send_reply(404, {"status": "error", "detail": "not found"})
                return
            if mode == "slow":
                time.sleep(SLOW_SECONDS)
            code, body = REPLIES[mode]
            self.send_reply(code, body)

        def send_reply(self, code, body):
            data = json.dumps(body).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def log_message(self, fmt, *args):
            # One short line per request. No client address: the log never
            # records who asked, only what was asked and what was answered.
            print(f"stand-in [{mode}] {self.command} {self.path} -> {args[1]}", flush=True)

    return StandInHandler


def main():
    parser = argparse.ArgumentParser(description="Stand-in for the Parts Bin Board host")
    parser.add_argument("--port", type=int, required=True, help="explicit port, for example 5320")
    parser.add_argument("--mode", choices=sorted(REPLIES), default="normal")
    args = parser.parse_args()

    server = ThreadingHTTPServer(("127.0.0.1", args.port), make_handler(args.mode))
    print(f"stand-in listening on http://127.0.0.1:{args.port} mode={args.mode}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        print("stand-in stopped", flush=True)


if __name__ == "__main__":
    main()
