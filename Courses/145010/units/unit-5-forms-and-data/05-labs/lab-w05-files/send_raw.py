"""
send_raw.py · Lab W05-02 · send a form submission without a browser

Why this exists: every check in a web page runs in the browser, and the
browser belongs to the person using it. This program skips the browser and
sends exactly what it is told to, the way any script, bot, or curious student
can. If the server trusts the page, this gets straight in.

Run it while app.py is running, with the same port:

    python send_raw.py --port 8405 good       a correct sign-up
    python send_raw.py --port 8405 garbage    every field wrong, sent to /signup
    python send_raw.py --port 8405 naive      the same garbage, sent to /naive/signup
    python send_raw.py --port 8405 full       a correct sign-up for a slot that is full
    python send_raw.py --port 8405 badslot    garbage with a slot that does not exist, to /naive/signup

Standard library only. It never follows a redirect, so you see the server's
first answer exactly as it was sent.
"""

import argparse
import re
import urllib.error
import urllib.parse
import urllib.request

GOOD = [
    ("performer_name", "Casey Lin"),
    ("email", "casey.lin@example.com"),
    ("act_type", "music"),
    ("slot", "4"),
    ("minutes", "5"),
    ("needs", "mic"),
    ("agree", "yes"),
]

# Every value here is something the form's own controls would refuse.
# There is no agree field at all: an unticked box sends nothing.
GARBAGE = [
    ("performer_name", ""),
    ("email", "not-an-email"),
    ("act_type", "fire-juggling"),
    ("slot", "1"),
    ("minutes", "banana"),
    ("needs", "fog machine"),
]

CASES = {
    "good": ("/signup", GOOD),
    "garbage": ("/signup", GARBAGE),
    "naive": ("/naive/signup", GARBAGE),
    "full": ("/signup", [(k, "1" if k == "slot" else v) for k, v in GOOD]),
    "badslot": ("/naive/signup", [(k, "99" if k == "slot" else v) for k, v in GARBAGE]),
}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    """Report a redirect instead of following it."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def main():
    parser = argparse.ArgumentParser(description="Send a sign-up without a browser")
    parser.add_argument("--port", type=int, required=True, help="the port app.py is using")
    parser.add_argument("case", choices=sorted(CASES))
    args = parser.parse_args()

    path, fields = CASES[args.case]
    body = urllib.parse.urlencode(fields).encode("utf-8")
    url = f"http://127.0.0.1:{args.port}{path}"
    request = urllib.request.Request(
        url, data=body, method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect)

    print(f"POST {path}")
    print(f"body: {body.decode('utf-8')}")
    try:
        with opener.open(request, timeout=5) as response:
            status, headers, text = response.status, response.headers, response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        status, headers, text = error.code, error.headers, error.read().decode("utf-8", "replace")
        error.close()
    except urllib.error.URLError as error:
        print(f"Could not reach the server on port {args.port}. Is app.py running? ({error.reason})")
        return 1

    print(f"status: {status}")
    if headers.get("Location"):
        print(f"redirected to: {headers['Location']}")
    # Pull the server's messages out of the page, if there are any.
    messages = re.findall(r'class="field-error"[^>]*>(?:<span[^>]*>Error: </span>)?([^<]+)<', text)
    for message in messages:
        print(f"  server said: {message}")
    if status >= 500:
        print("  the server failed while handling this request")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
