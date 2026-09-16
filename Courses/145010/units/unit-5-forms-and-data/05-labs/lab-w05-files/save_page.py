"""
save_page.py · save a page exactly as the server sent it, so web-check can read it

Why this exists: tools/web-check reads files, and your page is built by Flask
on every request. This fetches the page from your running server, saves the
HTML the server sent (not what the browser turned it into), fixes the
/static/ links so they work from a file, and copies static/ next to it.

    python save_page.py --port 8405 home saved/form.html
    python save_page.py --port 8405 signups saved/signups.html

To save the page the server sends back with errors, send an empty form:

    python save_page.py --port 8405 signup saved/form-errors.html --post

Pages are named without a leading slash, and "home" means the form page.
Git Bash rewrites anything starting with / into a Windows folder path, so a
leading slash would break in that terminal.

Then, from the repository root:

    node tools/web-check/check.js <your folder>/saved/form.html

Standard library only.
"""

import argparse
import pathlib
import shutil
import urllib.error
import urllib.request

HERE = pathlib.Path(__file__).parent


def main():
    parser = argparse.ArgumentParser(description="Save a server-rendered page for web-check")
    parser.add_argument("--port", type=int, required=True)
    parser.add_argument("page", help='the page on the server: home, signups, signup, echo')
    parser.add_argument("out", help="where to save it, such as saved/form.html")
    parser.add_argument("--post", action="store_true", help="send an empty POST instead of a GET")
    args = parser.parse_args()

    path = "/" if args.page == "home" else "/" + args.page.lstrip("/")
    if " " in path or ":" in path:
        print(f"That does not look like a page name: {args.page}")
        return 2
    url = f"http://127.0.0.1:{args.port}{path}"
    request = urllib.request.Request(url, data=b"" if args.post else None)
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(request, timeout=5) as response:
            status, body = response.status, response.read()
    except urllib.error.HTTPError as error:
        # A 400 page is still a page worth checking.
        status, body = error.code, error.read()
        error.close()
    except urllib.error.URLError as error:
        print(f"Could not reach {url}. Is app.py running on port {args.port}? ({error.reason})")
        return 1

    html = body.decode("utf-8").replace('"/static/', '"static/')
    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8", newline="\n")
    shutil.copytree(HERE / "static", out.parent / "static", dirs_exist_ok=True)
    print(f"{status} {path} saved to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
