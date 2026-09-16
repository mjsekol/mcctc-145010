"""check_site.py: check a running website the way a visitor and a crawler would meet it.

    python check_site.py http://127.0.0.1:8660 --as https://portfolio.example

The first address is where the site is running now. --as is the address the site will
have once it is published, which is what sitemap.xml must contain. The checker swaps one
for the other so it can test a sitemap before the site is live.

It checks:
    every link on every page you can reach from the home page
    every address in sitemap.xml, and that each one is a full address
    that robots.txt exists and does not block the whole site
    that every page has a title and a description, and no two pages share one

It does not check whether a search engine will list your site. Nothing can promise that.
Standard library only. Exit code 0 means no problems.
"""
import argparse
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit

OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))
SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"


class PageReader(HTMLParser):
    """Collect the links, the title, and the meta description from one page."""

    def __init__(self):
        super().__init__()
        self.links, self.title, self.description = [], "", None
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        elif tag == "title":
            self._in_title = True
        elif tag == "meta" and (a.get("name") or "").lower() == "description":
            self.description = (a.get("content") or "").strip()

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def fetch(url):
    """Return (status, text). A status of 0 means the server could not be reached."""
    try:
        with OPENER.open(url, timeout=5) as response:
            return response.status, response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as error:
        error.close()
        return error.code, ""
    except (urllib.error.URLError, TimeoutError) as error:
        return 0, str(error)


def robots_blocks_everything(text):
    """True when the group for every crawler (User-agent: *) says Disallow: /"""
    applies = False
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if ":" not in line:
            continue
        field, value = (part.strip() for part in line.split(":", 1))
        field = field.lower()
        if field == "user-agent":
            applies = value == "*"
        elif field == "disallow" and applies and value == "/":
            return True
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="where the site is running now, for example http://127.0.0.1:8660")
    parser.add_argument("--as", dest="public", required=True, help="the published address, for example https://portfolio.example")
    args = parser.parse_args()
    local = args.url.rstrip("/")
    public = args.public.rstrip("/")
    problems, notes = [], []

    status, _ = fetch(local + "/")
    if status == 0:
        print(f"Cannot reach {local}. Is the server running on that port?")
        return 2

    # robots.txt
    status, robots = fetch(local + "/robots.txt")
    if status != 200:
        problems.append(f"robots.txt: HTTP {status}")
    else:
        if robots_blocks_everything(robots):
            problems.append("robots.txt tells every crawler to stay out of the whole site (Disallow: /)")
        if "sitemap:" not in robots.lower():
            notes.append("robots.txt does not say where the sitemap is")

    # sitemap.xml
    sitemap_pages = set()
    status, xml_text = fetch(local + "/sitemap.xml")
    if status != 200:
        problems.append(f"sitemap.xml: HTTP {status}")
    else:
        try:
            root = ET.fromstring(xml_text)
            for loc in root.iter(SITEMAP_NS + "loc"):
                address = (loc.text or "").strip()
                if not address.startswith(public + "/"):
                    problems.append(f"sitemap.xml: {address!r} is not a full address under {public}")
                    continue
                path = address[len(public):]
                sitemap_pages.add(path)
                code, _ = fetch(local + path)
                if code != 200:
                    problems.append(f"sitemap.xml lists {address} but it answers HTTP {code}")
        except ET.ParseError as error:
            problems.append(f"sitemap.xml is not well-formed XML: {error}")

    # Crawl from the home page, following links that stay on this site.
    seen, queue, titles, descriptions = set(), ["/"], {}, {}
    while queue:
        path = queue.pop(0)
        if path in seen:
            continue
        seen.add(path)
        code, text = fetch(local + path)
        if code != 200:
            problems.append(f"{path}: HTTP {code}")
            continue
        if not (path.endswith(".html") or path.endswith("/")):
            continue
        reader = PageReader()
        reader.feed(text)
        titles.setdefault(reader.title.strip(), []).append(path)
        if not reader.description:
            problems.append(f"{path}: no meta description")
        else:
            descriptions.setdefault(reader.description, []).append(path)
        for href in reader.links:
            target = urlsplit(urljoin(local + path, href))
            if href.startswith(("mailto:", "tel:")) or target.netloc != urlsplit(local).netloc:
                continue
            # index.html and / are the same page. Count it once.
            target_path = "/" if target.path in ("", "/index.html") else target.path
            if target_path not in seen:
                queue.append(target_path)

    for label, table in (("title", titles), ("description", descriptions)):
        for value, paths in table.items():
            if not value:
                problems.append(f"empty {label} on {', '.join(paths)}")
            elif len(paths) > 1:
                problems.append(f"{len(paths)} pages share the {label} {value[:50]!r}: {', '.join(sorted(paths))}")

    html_pages = {p for p in seen if p.endswith(".html") or p == "/"}
    for path in sorted(html_pages - sitemap_pages):
        notes.append(f"{path} is linked but not in sitemap.xml")
    for path in sorted(sitemap_pages - html_pages):
        notes.append(f"{path} is in sitemap.xml but no page links to it")

    print(f"Checked {len(seen)} address(es) and {len(sitemap_pages)} sitemap entr{'y' if len(sitemap_pages) == 1 else 'ies'}.")
    for n in notes:
        print(f"NOTE     {n}")
    for p in problems:
        print(f"PROBLEM  {p}")
    print("No problems found." if not problems else f"{len(problems)} problem(s).")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
