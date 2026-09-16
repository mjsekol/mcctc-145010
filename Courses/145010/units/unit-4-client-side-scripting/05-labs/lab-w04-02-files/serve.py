"""
serve.py · Lab W04-02 · a local web server for measuring page cost

Why this exists: dev tools can only show you what a page costs to deliver if
the page arrives over HTTP. A file opened with a double-click never touches a
network, so there is nothing to measure. This server gives you a real request
and a real response, on your own machine, with no internet needed.

Run it from this folder, with the port stated every time:

    python serve.py --port 8404

Then open http://127.0.0.1:8404/ in Chrome. Stop it with Ctrl+C.

What it serves:
  - everything in the site/ folder, as ordinary files
  - two photos that are generated in memory when the server starts, so the
    lab folder stays small:
        /img/field-full.png    the photo at 1200 x 675, straight off a phone
        /img/field-sized.png   the same photo cut to 480 x 270, the size the
                               page actually shows it at
  - thirty small icon files, /icons/i01.svg to /icons/i30.svg, and one file
    that holds all thirty, /icons/sheet.svg

Every response carries "Cache-Control: no-store", so every reload downloads
everything again and your measurements repeat.

Standard library only. Python 3.10 or newer.
"""

import argparse
import http.server
import pathlib
import random
import struct
import zlib

SITE = pathlib.Path(__file__).parent / "site"


def make_png(width, height, seed):
    """Build a PNG of coloured noise.

    Noise does not compress, so the file is about as large as the raw pixels:
    width x height x 3 bytes. That makes the size predictable, which is what a
    measurement lab needs. A real photo compresses better than this, but a real
    photo straight off a phone is also far larger than 1200 pixels wide.
    """
    rng = random.Random(seed)
    rows = bytearray()
    for _ in range(height):
        rows.append(0)                     # PNG filter type 0 for each row
        rows += rng.randbytes(width * 3)   # red, green, blue for each pixel

    def chunk(kind, data):
        body = kind + data
        return struct.pack(">I", len(data)) + body + struct.pack(">I", zlib.crc32(body))

    header = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header)
            + chunk(b"IDAT", zlib.compress(bytes(rows), 9)) + chunk(b"IEND", b""))


def make_icon(number):
    """One small SVG icon, padded with a comment so each is close to 1 kB."""
    hue = (number * 37) % 360
    padding = "x" * 800
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40" width="40" height="40">'
        f"<!-- icon {number:02d} {padding} -->"
        f'<circle cx="20" cy="20" r="16" fill="hsl({hue},60%,40%)"/>'
        f'<text x="20" y="25" font-size="14" text-anchor="middle" fill="#fff">{number}</text>'
        "</svg>"
    ).encode("utf-8")


def make_sheet():
    """All thirty icons in one file: the same bytes, one request."""
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 120" width="400" height="120">']
    for n in range(1, 31):
        x = ((n - 1) % 10) * 40 + 20
        y = ((n - 1) // 10) * 40 + 20
        hue = (n * 37) % 360
        parts.append(f"<!-- icon {n:02d} {'x' * 800} -->")
        parts.append(f'<circle cx="{x}" cy="{y}" r="16" fill="hsl({hue},60%,40%)"/>')
        parts.append(f'<text x="{x}" y="{y + 5}" font-size="14" text-anchor="middle" fill="#fff">{n}</text>')
    parts.append("</svg>")
    return "".join(parts).encode("utf-8")


GENERATED = {}


def build_generated():
    GENERATED["/img/field-full.png"] = ("image/png", make_png(1200, 675, seed=4))
    GENERATED["/img/field-sized.png"] = ("image/png", make_png(480, 270, seed=4))
    for n in range(1, 31):
        GENERATED[f"/icons/i{n:02d}.svg"] = ("image/svg+xml", make_icon(n))
    GENERATED["/icons/sheet.svg"] = ("image/svg+xml", make_sheet())


class Handler(http.server.SimpleHTTPRequestHandler):
    # HTTP/1.1 lets the browser reuse a connection for several requests,
    # which is how real servers behave. The default here is HTTP/1.0.
    protocol_version = "HTTP/1.1"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SITE), **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path in GENERATED:
            content_type, body = GENERATED[path]
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def log_request(self, code="-", size="-"):
        # One short line per request, so you can count requests in the terminal too.
        print(f"  {self.command} {self.path} -> {int(code) if str(code).isdigit() else code}")

    def log_message(self, fmt, *args):
        # Silence the default second line for errors. log_request already printed it.
        pass


class LabServer(http.server.ThreadingHTTPServer):
    # Refuse to share a port. With the default setting, Windows lets a second
    # server bind the same port without any error, and your browser then talks
    # to whichever one answers. A clear failure is better than a silent one.
    allow_reuse_address = False


def main():
    parser = argparse.ArgumentParser(description="Lab W04-02 measurement server")
    parser.add_argument("--port", type=int, required=True,
                        help="the port to listen on. Say it out loud. The lab uses 8404.")
    args = parser.parse_args()

    build_generated()
    print("Generated files and their sizes in bytes:")
    for name in ("/img/field-full.png", "/img/field-sized.png", "/icons/i01.svg", "/icons/sheet.svg"):
        print(f"  {name:<22} {len(GENERATED[name][1]):>9,}")
    print(f"  thirty icons together  {sum(len(GENERATED[f'/icons/i{n:02d}.svg'][1]) for n in range(1, 31)):>9,}")

    # 127.0.0.1 only: nobody else on the network can reach this server.
    server = LabServer(("127.0.0.1", args.port), Handler)
    print(f"\nServing site/ at http://127.0.0.1:{args.port}/  (Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
