"""test_counter.py: check your serve.py before you trust its numbers.

Copy this file into your sitekit folder, next to serve.py, then:

    python build.py
    python test_counter.py

It starts your server's handler on port 8662 with a temporary counts file, so it never
touches data/counts.json or a server you already have running on 8606.
Every test name says what it proves. Read the name of any test that fails.
"""
import io
import json
import shutil
import sys
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from functools import partial
from http.server import ThreadingHTTPServer
from pathlib import Path

import serve

HERE = Path(__file__).resolve().parent
PORT = 8662
BASE = f"http://127.0.0.1:{PORT}"


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())


def post(path, body, headers=None):
    request = urllib.request.Request(BASE + path, data=body.encode("utf-8"), headers=headers or {}, method="POST")
    try:
        with OPENER.open(request, timeout=5) as response:
            return response.status, dict(response.headers), response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        text = error.read().decode("utf-8")
        headers = dict(error.headers)
        error.close()
        return error.code, headers, text


class CounterTests(unittest.TestCase):
    """Start serve.py's handler on port 8661 with a temporary counts file."""

    @classmethod
    def setUpClass(cls):
        if not (HERE / "site" / "pages.json").exists():
            raise unittest.SkipTest("run python build.py first")
        cls.tmp = Path(tempfile.mkdtemp())
        cls.counts = cls.tmp / "counts.json"
        serve.SiteHandler.store = serve.CountStore(cls.counts)
        serve.SiteHandler.known_pages = tuple(json.loads((HERE / "site" / "pages.json").read_text(encoding="utf-8")))
        cls.log = io.StringIO()
        handler = partial(serve.SiteHandler, directory=str(HERE / "site"))
        cls.server = ThreadingHTTPServer(("127.0.0.1", PORT), handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls._stderr = sys.stderr
        sys.stderr = cls.log
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        sys.stderr = cls._stderr
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def test_a_hit_on_a_real_page_is_counted(self):
        status, headers, _ = post("/api/hit", json.dumps({"path": "/layout.html"}))
        self.assertEqual(status, 204)
        views = serve.SiteHandler.store.snapshot()["views"]["/layout.html"]
        self.assertGreaterEqual(sum(views.values()), 1)

    def test_index_html_and_slash_are_one_page(self):
        post("/api/hit", json.dumps({"path": "/index.html"}))
        post("/api/hit", json.dumps({"path": "/"}))
        data = serve.SiteHandler.store.snapshot()["views"]
        self.assertNotIn("/index.html", data)
        self.assertGreaterEqual(sum(data["/"].values()), 2)

    def test_unknown_page_is_refused(self):
        status, _, body = post("/api/hit", json.dumps({"path": "/admin.php"}))
        self.assertEqual(status, 400)
        self.assertNotIn("/admin.php", serve.SiteHandler.store.snapshot()["views"])

    def test_garbage_body_is_refused(self):
        status, _, _ = post("/api/hit", "not json")
        self.assertEqual(status, 400)

    def test_oversized_body_is_refused(self):
        status, _, _ = post("/api/hit", json.dumps({"path": "/", "padding": "x" * 2000}))
        self.assertEqual(status, 413)

    def test_helpful_from_script_returns_204(self):
        status, _, _ = post("/api/helpful", "page=%2Flayout.html&answer=yes", {"Accept": "application/json"})
        self.assertEqual(status, 204)
        self.assertGreaterEqual(serve.SiteHandler.store.snapshot()["helpful"]["/layout.html"]["yes"], 1)

    def test_helpful_plain_form_redirects_back_to_the_page(self):
        status, headers, _ = post("/api/helpful", "page=%2Fmedia.html&answer=no")
        self.assertEqual(status, 303)
        self.assertEqual(headers["Location"], "/media.html")

    def test_helpful_cannot_redirect_off_site(self):
        status, headers, _ = post("/api/helpful", "page=https%3A%2F%2Fevil.example%2F&answer=yes")
        self.assertEqual(status, 400)
        self.assertNotIn("Location", headers)

    def test_helpful_rejects_answers_other_than_yes_and_no(self):
        status, _, _ = post("/api/helpful", "page=%2F&answer=maybe")
        self.assertEqual(status, 400)

    def test_no_cookie_is_ever_set(self):
        _, headers, _ = post("/api/hit", json.dumps({"path": "/"}))
        self.assertNotIn("Set-Cookie", headers)
        with OPENER.open(BASE + "/", timeout=5) as response:
            self.assertIsNone(response.headers.get("Set-Cookie"))

    def test_nothing_stored_or_logged_identifies_a_visitor(self):
        post("/api/hit", json.dumps({"path": "/document.html"}), {"User-Agent": "TestBrowser/1.0"})
        with OPENER.open(BASE + "/document.html", timeout=5) as response:
            response.read()
        stored = self.counts.read_text(encoding="utf-8")
        for needle in ("127.0.0.1", "TestBrowser"):
            self.assertNotIn(needle, stored)
            self.assertNotIn(needle, self.log.getvalue())
        self.assertIn("GET /document.html 200", self.log.getvalue())

    def test_a_crash_report_does_not_name_the_visitor(self):
        server = serve.QuietServer(("127.0.0.1", 0), serve.SiteHandler)
        try:
            before = len(self.log.getvalue())
            try:
                raise RuntimeError("pretend a handler crashed")
            except RuntimeError:
                server.handle_error(None, ("203.0.113.9", 5555))
            report_text = self.log.getvalue()[before:]
        finally:
            server.server_close()
        self.assertIn("pretend a handler crashed", report_text)
        self.assertNotIn("203.0.113.9", report_text)

    def test_stats_are_served(self):
        with OPENER.open(BASE + "/api/stats", timeout=5) as response:
            data = json.loads(response.read().decode("utf-8"))
        self.assertEqual(set(data), {"views", "helpful"})


if __name__ == "__main__":
    unittest.main(verbosity=1)
