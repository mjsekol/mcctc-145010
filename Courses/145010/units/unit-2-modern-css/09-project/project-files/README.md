# What Dana attached · Week 2

These files go with [The League Goes Mobile](../MCCTC_145010_Project_W02_LeagueGoesMobile.md). Copy
them into your own `league-season-page/` folder: the media into `media/`, and the map into `embeds/`.

| File | What it is |
|---|---|
| `opening-day.jpg` | The opening-day photo, 1600 by 1067 |
| `season-opener.webm` | The season opener highlight, WebM, about 9 seconds, narrated |
| `season-opener.mp4` | The same clip as MP4 |
| `season-opener.vtt` | Captions for the clip, three timed lines |
| `season-opener-poster.jpg` | A still frame from the end of the clip |
| `field-map.html` | A local page that stands in for the park district's map embed |

**Everything here is invented.** The league, the park, and the teams do not exist. The photo and the
clip were generated for this course, and the narration is a computer voice. No real person appears in
any of it.

**About `field-map.html`.** A real site would paste an embed snippet from the park district, and that
snippet would load a page from the district's own site. This file lets you build and test the embed
with no account and no network. Treat it as a page somebody else controls.

**Captions need a served page.** Chrome does not load a `.vtt` file for a page opened by double-clicking
it. Inside your folder, run `python -m http.server 8000`, open `http://127.0.0.1:8000/`, and stop the
server with Ctrl+C when you are done.
