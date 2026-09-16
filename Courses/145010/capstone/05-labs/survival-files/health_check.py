"""One health check, one log line.

Calls a health address once and appends one line to a health log. Run it on a
schedule (a scheduled task on an approved lab machine, or a scheduler your host
provides) to build the evidence for the thirty-day survival record.

Why one check per run instead of a loop: a scheduler that starts this every
fifteen minutes keeps working after a reboot. A loop you started by hand does
not, and restarting it by hand would be a manual intervention.

Usage (standard library only, Python 3.10 or newer):

    python health_check.py --url http://127.0.0.1:8150/health --log health-log.txt

Every address passes its port explicitly. A check that reaches the wrong server
does not fail. It answers.

Log line format, shared by every track:

    2027-04-23T14:15:02  result=ok  status=200  ms=412
    2027-04-23T14:30:02  result=fail  error=URLError

The timestamp is program data. The line never contains a response body, because
a body can contain data that does not belong in a log.

Exit code: 0 when the check succeeded, 1 when it failed, 2 for bad arguments.
"""

import argparse
import datetime
import time
import urllib.error
import urllib.request


def check_once(url, timeout):
    """Return the log fields for one call to the health address."""
    started = time.monotonic()
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            status = response.status
    except urllib.error.HTTPError as err:
        # The server answered, with an error status. That is a failed check,
        # and the status is worth keeping.
        status = err.code
    except (urllib.error.URLError, TimeoutError, ConnectionError) as err:
        # Nothing answered. Record only the kind of failure, never its text,
        # because messages can carry addresses and paths.
        return {"result": "fail", "error": type(err).__name__}
    elapsed_ms = round((time.monotonic() - started) * 1000)
    result = "ok" if 200 <= status < 300 else "fail"
    return {"result": result, "status": str(status), "ms": str(elapsed_ms)}


def format_line(fields, now=None):
    """Timestamp first, then key=value pairs separated by two spaces."""
    now = now or datetime.datetime.now().replace(microsecond=0)
    parts = [now.isoformat()] + [f"{key}={value}" for key, value in fields.items()]
    return "  ".join(parts)


def main():
    parser = argparse.ArgumentParser(description="Append one health check result to a log.")
    parser.add_argument("--url", required=True,
                        help="full health address including the port, for example "
                             "http://127.0.0.1:8150/health")
    parser.add_argument("--log", required=True, help="the health log file to append to")
    parser.add_argument("--timeout", type=float, default=30.0,
                        help="seconds to wait. Longer than your host's wake-up time. Default 30")
    args = parser.parse_args()

    if not args.url.startswith(("http://", "https://")):
        parser.error("--url must start with http:// or https://")

    fields = check_once(args.url, args.timeout)
    line = format_line(fields)
    with open(args.log, "a", encoding="utf-8") as log:
        log.write(line + "\n")
    print(line)
    return 0 if fields["result"] == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
