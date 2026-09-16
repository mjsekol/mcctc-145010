"""A tiny health checker for the Week 10 stand-in clinic.

Composite example. It calls GET /health once and prints one log line. The real
thirty-day checker runs this on a schedule and adds a timestamp to each line.

Run it (from this folder, with the stand-in running on the same port):
    python check_health.py --port 5320
"""
import argparse
import json
import time
import urllib.error
import urllib.request

LIMIT_MS = 2000      # from the composite requirement: health answers within 2 seconds
TIMEOUT_SECONDS = 5  # after this, stop waiting and call it a timeout

# Ignore any proxy setting on the machine. This request goes to this computer only.
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def check(port):
    url = f"http://127.0.0.1:{port}/health"
    start = time.perf_counter()
    try:
        with opener.open(url, timeout=TIMEOUT_SECONDS) as response:
            body = json.loads(response.read().decode("utf-8"))
            status = response.status
    except urllib.error.HTTPError as error:  # must come before URLError
        ms = round((time.perf_counter() - start) * 1000)
        body = json.loads(error.read().decode("utf-8"))
        error.close()
        return f"result=error status={error.code} ms={ms} database={body.get('database')}"
    except urllib.error.URLError as error:
        if isinstance(error.reason, TimeoutError):
            return f"result=timeout status=none ms={TIMEOUT_SECONDS * 1000}"
        return "result=down status=none ms=0"
    except TimeoutError:
        return f"result=timeout status=none ms={TIMEOUT_SECONDS * 1000}"

    ms = round((time.perf_counter() - start) * 1000)
    result = "ok" if ms <= LIMIT_MS else "slow"
    return f"result={result} status={status} ms={ms} database={body.get('database')}"


def main():
    parser = argparse.ArgumentParser(description="Check /health once")
    parser.add_argument("--port", type=int, required=True, help="explicit port, for example 5320")
    args = parser.parse_args()
    print(check(args.port))


if __name__ == "__main__":
    main()
