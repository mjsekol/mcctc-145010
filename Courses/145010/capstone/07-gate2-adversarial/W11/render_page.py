# render_page.py
#
# Render the Parts Bin Board home page to an HTML file, without starting a
# server. This uses Flask's test client, so you can run web-check on the result.
#
# Usage:
#     python render_page.py <output.html>
#
# The database path comes from the PARTS_DB environment variable, the same as
# parts_board.py. Set it to a file you own, for example in your scratch folder,
# so nothing is written into the repository:
#
#     set PARTS_DB=C:\path\to\your\parts_board.db     (Windows)
#     python render_page.py restock-home.html

import sys

import parts_board


def main():
    if len(sys.argv) != 2:
        print("usage: python render_page.py <output.html>")
        return 2
    output_path = sys.argv[1]
    # Build and seed the database this render will read from.
    parts_board.init_db()
    client = parts_board.app.test_client()
    response = client.get("/")
    html = response.get_data(as_text=True)
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(html)
    print(f"Wrote {len(html)} characters to {output_path} (HTTP {response.status_code})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
