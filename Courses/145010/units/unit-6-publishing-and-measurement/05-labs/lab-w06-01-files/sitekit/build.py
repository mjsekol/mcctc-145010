"""build.py: turn one template and a folder of content files into a website.

    python build.py            build into site/, print warnings
    python build.py --strict   build, and fail if there is any warning

This is the idea every content management system is built on: the words live in one
place (content/), the layout lives in another (template.html), and a program puts
them together. Change the template once and every page changes.

A content file looks like this. The lines above --- are the page's own facts.
Everything below --- is the page body.

    title: Pizza Order Splitter
    description: A small calculator that works out how many pizzas a group needs.
    nav_label: Widget
    ---
    <h1>Pizza order splitter</h1>
    ...

Standard library only, so it runs on any lab machine with Python 3.
"""
import html
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTENT_DIR = HERE / "content"
STATIC_DIR = HERE / "static"
OUT_DIR = HERE / "site"
REQUIRED_KEYS = ("title", "description", "nav_label")

# Course rule for this week, not a search engine rule: a description long enough to
# say something and short enough to read at a glance.
DESCRIPTION_MIN = 50
DESCRIPTION_MAX = 160


def read_content(path):
    """Split one content file into (facts, body). Raise ValueError with the reason."""
    text = path.read_text(encoding="utf-8")
    if "\n---\n" not in text:
        raise ValueError(f"{path.name}: no line containing only --- between the facts and the body")
    head, body = text.split("\n---\n", 1)
    facts = {}
    for number, line in enumerate(head.splitlines(), 1):
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"{path.name} line {number}: expected 'key: value', got {line!r}")
        key, value = line.split(":", 1)
        facts[key.strip()] = value.strip()
    missing = [k for k in REQUIRED_KEYS if not facts.get(k)]
    if missing:
        raise ValueError(f"{path.name}: missing {', '.join(missing)}")
    return facts, body.strip()


def page_path(slug):
    """The address a visitor uses. The home page is '/', every other page is '/slug.html'."""
    return "/" if slug == "index" else f"/{slug}.html"


def build_nav(pages, nav_order, current_slug):
    """One list of links, in the order site.json gives, with the current page marked."""
    items = []
    for slug in nav_order:
        facts = pages[slug][0]
        href = "index.html" if slug == "index" else f"{slug}.html"
        current = ' aria-current="page"' if slug == current_slug else ""
        items.append(f'<li><a href="{href}"{current}>{html.escape(facts["nav_label"])}</a></li>')
    return "\n        ".join(items)


def render(template, values):
    """Replace every {{name}} with its value, then refuse to ship a leftover placeholder."""
    out = template
    for name, value in values.items():
        out = out.replace("{{" + name + "}}", value)
    if "{{" in out:
        start = out.index("{{")
        raise ValueError(f"template still has a placeholder nobody filled: {out[start:start + 30]!r}")
    return out


def build(strict=False):
    config = json.loads((HERE / "site.json").read_text(encoding="utf-8"))
    template = (HERE / "template.html").read_text(encoding="utf-8")
    warnings = []

    # A template with no slot for a fact gives every page the same value for it.
    if "{{content}}" not in template:
        raise ValueError("template.html has no {{content}} slot, so no page would have a body")
    for slot in ("title", "description", "nav"):
        if "{{" + slot + "}}" not in template:
            warnings.append(f"template.html never uses {{{{{slot}}}}}, so every page gets the same {slot}")

    pages = {}
    for path in sorted(CONTENT_DIR.glob("*.html")):
        pages[path.stem] = read_content(path)

    nav_order = config["nav"]
    for slug in nav_order:
        if slug not in pages:
            raise ValueError(f"site.json nav lists '{slug}' but content/{slug}.html does not exist")
    for slug in pages:
        if slug not in nav_order:
            warnings.append(f"content/{slug}.html is not in the navigation, so a visitor cannot reach it by clicking")

    # Every page must describe itself. A shared title or description is a template bug.
    for key in ("title", "description"):
        seen = {}
        for slug, (facts, _) in pages.items():
            seen.setdefault(facts[key], []).append(slug)
        for value, slugs in seen.items():
            if len(slugs) > 1:
                warnings.append(f"{len(slugs)} pages share the {key} {value!r}: {', '.join(slugs)}")
    for slug, (facts, _) in pages.items():
        length = len(facts["description"])
        if not DESCRIPTION_MIN <= length <= DESCRIPTION_MAX:
            warnings.append(f"{slug}: description is {length} characters, course rule is {DESCRIPTION_MIN}-{DESCRIPTION_MAX}")

    # Copy the static files over whatever is there. Deleting the whole folder first
    # fails on Windows whenever a server or an editor has it open, so remove only the
    # pages, which is enough to make a deleted content file disappear from the site.
    OUT_DIR.mkdir(exist_ok=True)
    for old_page in OUT_DIR.glob("*.html"):
        old_page.unlink()
    shutil.copytree(STATIC_DIR, OUT_DIR, dirs_exist_ok=True)

    base_url = config.get("base_url", "").rstrip("/")
    for slug, (facts, body) in pages.items():
        values = {
            "lang": config.get("language", "en"),
            "site_name": html.escape(config["site_name"]),
            "title": html.escape(facts["title"]),
            "description": html.escape(facts["description"]),
            "canonical": html.escape(base_url + page_path(slug)),
            "page_path": page_path(slug),
            "nav": build_nav(pages, nav_order, slug),
            "content": body,
        }
        (OUT_DIR / f"{slug}.html").write_text(render(template, values), encoding="utf-8")

    # The list of real addresses. serve.py counts visits only to these.
    known = [page_path(slug) for slug in nav_order]
    (OUT_DIR / "pages.json").write_text(json.dumps(known, indent=2) + "\n", encoding="utf-8")

    # A sitemap needs full addresses, so it can only be written once you know where
    # the site will live. That is why base_url is in site.json.
    if base_url:
        urls = "\n".join(f"  <url><loc>{html.escape(base_url + p)}</loc></url>" for p in known)
        sitemap = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{urls}\n"
            "</urlset>\n"
        )
        (OUT_DIR / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    else:
        warnings.append("site.json has no base_url, so no sitemap.xml was written")

    print(f"Built {len(pages)} page(s) into {OUT_DIR.name}/")
    for w in warnings:
        print(f"WARNING: {w}")
    if strict and warnings:
        print(f"Strict build failed: {len(warnings)} warning(s).")
        return 1
    return 0


if __name__ == "__main__":
    try:
        sys.exit(build(strict="--strict" in sys.argv))
    except ValueError as problem:
        print(f"BUILD STOPPED: {problem}")
        sys.exit(1)
