"""structure_check.py: the checks web-check does not make.

    python structure_check.py page.html [more.html ...]

web-check (tools/web-check/check.js) validates your markup and runs an automated
accessibility audit. It passes plenty of pages that are still wrong. This script
reads the same file and reports the structural problems it misses:

  1. HEADINGS   the outline, and any level that skips (h1 straight to h3)
  2. LANDMARKS  header, nav, main, footer, aside, and whether there is one main
  3. DIVS       every div and span, and which ones look like an element exists for them
  4. ANCHORS    in-page links (#something) that point at an id nobody has
  5. FILES      local links and sources (href, src) that point at a file that is not there
  6. LINKS      link text that says nothing on its own ("click here"), email and
                phone links, plain http links, and what a download link hands people
  7. TABLES     tables with no header cells, and tables marked as layout

It uses only the Python standard library. It never touches the network, so an
absolute https link is reported as "not checked" rather than guessed at.

Exit code 1 if any line is marked FAIL. WARN lines are judgment calls: read them,
decide, and write your decision down.
"""
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

LANDMARKS = ("header", "nav", "main", "footer", "aside")
# Words in a class or id that usually mean a real element already exists for the job.
HINTS = {
    "header": "<header>", "masthead": "<header>", "banner": "<header>",
    "nav": "<nav>", "navbar": "<nav>", "menu": "<nav> with a list",
    "main": "<main>", "content": "<main>",
    "footer": "<footer>",
    "sidebar": "<aside>", "aside": "<aside>",
    "article": "<article>", "post": "<article>", "card": "<article>",
    "section": "<section>",
    "list": "<ul> or <ol>", "item": "<li>",
    "button": "<button>", "btn": "<button>",
    "table": "<table>", "row": "<tr>", "cell": "<td>",
    "figure": "<figure>", "caption": "<figcaption> or <caption>",
    "title": "a heading, <h1> to <h6>", "heading": "a heading, <h1> to <h6>",
    "subhead": "a heading, <h1> to <h6>", "subtitle": "a heading, <h1> to <h6>",
    "headline": "a heading, <h1> to <h6>",
    "date": "<time>", "time": "<time>", "address": "<address>",
    "quote": "<blockquote>",
}
VAGUE = {"click here", "here", "click", "read more", "more", "link", "this",
         "this link", "go", "learn more", "details", "info"}
RISKY_DOWNLOADS = {"exe", "msi", "bat", "cmd", "com", "scr", "ps1", "vbs", "js",
                   "jar", "hta", "docm", "xlsm", "pptm", "lnk", "reg", "apk"}
SOURCE_ATTRS = {"a": "href", "link": "href", "img": "src", "script": "src",
                "source": "src", "track": "src", "video": "src", "audio": "src",
                "iframe": "src", "embed": "src"}


class Reader(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.headings = []        # (line, level, text)
        self.landmarks = []       # (line, tag)
        self.generic = []         # (line, tag, class, id, has_onclick)
        self.ids = {}             # id -> first line
        self.refs = []            # (line, tag, attr, value, attrs)
        self.links = []           # (line, href, text, attrs)
        self.tables = []          # dict per table
        self._heading = None
        self._link = None
        self._tables = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        line = self.getpos()[0]
        if a.get("id"):
            self.ids.setdefault(a["id"], line)
        if tag == "a" and a.get("name"):
            # Old pages use <a name="..."> as a jump target. Browsers still honor it.
            self.ids.setdefault(a["name"], line)
        if tag in LANDMARKS:
            self.landmarks.append((line, tag))
        if tag in ("div", "span"):
            self.generic.append((line, tag, a.get("class") or "", a.get("id") or "",
                                 "onclick" in a))
        if re.fullmatch(r"h[1-6]", tag):
            self._heading = [line, int(tag[1]), ""]
        if tag in SOURCE_ATTRS and a.get(SOURCE_ATTRS[tag]) is not None:
            self.refs.append((line, tag, SOURCE_ATTRS[tag], a[SOURCE_ATTRS[tag]], a))
        if tag == "img" and a.get("srcset"):
            for part in a["srcset"].split(","):
                url = part.strip().split(" ")[0]
                if url:
                    self.refs.append((line, tag, "srcset", url, a))
        if tag == "a" and "href" in a:
            self._link = [line, a["href"], "", a]
        if tag == "img" and self._link is not None:
            # An image inside a link contributes its alt text to the link's name.
            self._link[2] += " " + (a.get("alt") or "")
        if tag == "table":
            t = {"line": line, "th": 0, "caption": False, "role": a.get("role", "")}
            self._tables.append(t)
            self.tables.append(t)
        if tag == "th" and self._tables:
            self._tables[-1]["th"] += 1
        if tag == "caption" and self._tables:
            self._tables[-1]["caption"] = True

    def handle_endtag(self, tag):
        if self._heading and tag == f"h{self._heading[1]}":
            self.headings.append(tuple(self._heading))
            self._heading = None
        if tag == "a" and self._link is not None:
            self.links.append(tuple(self._link))
            self._link = None
        if tag == "table" and self._tables:
            self._tables.pop()

    def handle_data(self, data):
        if self._heading is not None:
            self._heading[2] += data
        if self._link is not None:
            self._link[2] += data


def tidy(text):
    return " ".join(text.split())


def check(path):
    fails, warns, info = [], [], []
    with open(path, encoding="utf-8") as handle:
        source = handle.read()
    reader = Reader()
    reader.feed(source)
    reader.close()
    folder = os.path.dirname(os.path.abspath(path))

    # 1. Headings
    info.append("HEADINGS  the outline a screen reader user hears:")
    if not reader.headings:
        fails.append("HEADINGS  no headings at all")
    previous = 0
    h1_count = 0
    for line, level, text in reader.headings:
        info.append(f"    line {line:>4}  {'  ' * (level - 1)}h{level}  {tidy(text)}")
        if level == 1:
            h1_count += 1
        if previous == 0 and level != 1:
            fails.append(f"HEADINGS  line {line}: the first heading is h{level}, expected h1")
        elif previous and level > previous + 1:
            fails.append(f"HEADINGS  line {line}: h{previous} jumps to h{level}, "
                         f"skipping h{previous + 1} ({tidy(text)!r})")
        if not tidy(text):
            fails.append(f"HEADINGS  line {line}: h{level} has no text")
        previous = level
    if h1_count > 1:
        warns.append(f"HEADINGS  {h1_count} h1 elements. One h1 per page is the usual rule")

    # 2. Landmarks
    found = [tag for _, tag in reader.landmarks]
    info.append("LANDMARKS " + (", ".join(f"{t} x{found.count(t)}" for t in LANDMARKS
                                          if t in found) or "none"))
    if found.count("main") != 1:
        fails.append(f"LANDMARKS {found.count('main')} <main> elements, expected exactly 1")
    for tag in ("header", "nav", "footer"):
        if tag not in found:
            warns.append(f"LANDMARKS no <{tag}>. Fine if the page has no {tag}, "
                         f"wrong if a div is doing its job")

    # 3. Generic containers
    info.append(f"DIVS      {sum(1 for g in reader.generic if g[1] == 'div')} div, "
                f"{sum(1 for g in reader.generic if g[1] == 'span')} span")
    for line, tag, cls, ident, onclick in reader.generic:
        label = f"<{tag}" + (f' class="{cls}"' if cls else "") + (f' id="{ident}"' if ident else "") + ">"
        if onclick:
            fails.append(f"DIVS      line {line}: {label} has onclick. A <button> exists for this")
            continue
        words = re.findall(r"[a-z]+", f"{cls} {ident}".lower())
        hits = sorted({HINTS[w] for w in words if w in HINTS})
        if hits:
            warns.append(f"DIVS      line {line}: {label} may be doing the job of {' or '.join(hits)}")

    # 4 and 5. Anchors and local files
    for line, tag, attr, value, attrs in reader.refs:
        value = value.strip()
        parts = urlsplit(value)
        if parts.scheme in ("http", "https", "mailto", "tel", "data", "javascript") or value.startswith("//"):
            if parts.scheme == "javascript":
                fails.append(f"FILES     line {line}: {attr}=\"{value}\" runs script from a link. Use a <button>")
            continue
        if value == "#":
            fails.append(f"ANCHORS   line {line}: <{tag} {attr}=\"#\"> is a placeholder. "
                         f"It only jumps to the top of this page")
            continue
        if value == "":
            fails.append(f"ANCHORS   line {line}: <{tag} {attr}=\"\"> is empty. "
                         f"It points back at this same page")
            continue
        if value.startswith("#"):
            target = unquote(value[1:])
            if target not in reader.ids and target.lower() != "top":
                fails.append(f"ANCHORS   line {line}: {value} has no element with id=\"{target}\" on this page")
            continue
        local = os.path.normpath(os.path.join(folder, unquote(parts.path)))
        if not os.path.exists(local):
            fails.append(f"FILES     line {line}: <{tag} {attr}=\"{value}\"> points at a file that is not there")
            continue
        if parts.fragment and local.lower().endswith((".html", ".htm")):
            other = Reader()
            with open(local, encoding="utf-8") as handle:
                other.feed(handle.read())
            if unquote(parts.fragment) not in other.ids:
                fails.append(f"ANCHORS   line {line}: {value} opens the file, but it has no id=\"{parts.fragment}\"")

    # 6. Links
    for line, href, text, attrs in reader.links:
        name = tidy(text) or tidy(attrs.get("aria-label", ""))
        scheme = urlsplit(href.strip()).scheme
        if not name:
            fails.append(f"LINKS     line {line}: <a href=\"{href}\"> has no text a person could read")
        elif name.lower().strip(" .:") in VAGUE:
            warns.append(f"LINKS     line {line}: link text {name!r} says nothing out of context")
        if scheme == "mailto":
            info.append(f"LINKS     line {line}: email link to {href[7:].split('?')[0]} "
                        f"(anyone who reads the page source can collect this address)")
        elif scheme == "tel":
            info.append(f"LINKS     line {line}: phone link to {href[4:]}")
        elif scheme == "http":
            warns.append(f"LINKS     line {line}: {href} is plain http. Anything sent there travels unencrypted")
        elif scheme == "https" or href.startswith("//"):
            info.append(f"LINKS     line {line}: {href} is absolute (not checked, this script stays offline)")
        if "download" in attrs:
            ext = os.path.splitext(urlsplit(href).path)[1].lstrip(".").lower()
            message = f"LINKS     line {line}: download link hands people a .{ext or '(no extension)'} file ({name!r})"
            if ext in RISKY_DOWNLOADS:
                fails.append(message + ". That file type can run code on their machine")
            else:
                info.append(message)

    # 7. Tables
    for t in reader.tables:
        if t["role"] in ("presentation", "none"):
            warns.append(f"TABLES    line {t['line']}: table marked role=\"{t['role']}\". "
                         f"A table used for layout. Use grid or flexbox")
        elif t["th"] == 0:
            fails.append(f"TABLES    line {t['line']}: table has no <th> header cells. "
                         f"A data table needs them, and a layout table should not exist")
        elif not t["caption"]:
            warns.append(f"TABLES    line {t['line']}: data table has no <caption>")

    return fails, warns, info


def main(paths):
    if not paths:
        print(__doc__)
        return 2
    failed = False
    for path in paths:
        if not os.path.isfile(path):
            print(f"MISSING  {path}")
            failed = True
            continue
        fails, warns, info = check(path)
        failed = failed or bool(fails)
        print(f"{'FAIL' if fails else 'PASS'}  {path}")
        for line in info:
            print(f"  {line}")
        for line in warns:
            print(f"  WARN {line}")
        for line in fails:
            print(f"  FAIL {line}")
        print(f"  {len(fails)} fail, {len(warns)} warn")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
