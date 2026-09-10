#!/usr/bin/env python3
"""Save a light-themed PDF copy of the day's wires to records/ for the archive.

The live site defaults to the dark "night desk" theme; light is opt-in and held
in the visitor's localStorage, which a one-shot headless print cannot set. So
this script fetches each live page, pins it to the light theme (adds
data-theme="light" and a <base href> so the stylesheet still resolves), and
prints that local copy with headless Chrome (or Edge / Chromium).

Run it only after the deploy is confirmed live — see SKILL.md Step 8. Output
lives in records/, which is git-ignored: it is a run artifact, not site content.

Only wires that were actually published that day are exported — the script
looks for _news/<date>.md and _general/<date>.md and skips whichever is absent.

    python scripts/wire_pdf.py 2026-09-09
"""
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "google-chrome",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
]

SITE = "https://riskmaverick.com"

# A real brief page prints to ~350 KB; a GitHub Pages 404 or an unstyled page is
# an order smaller.
MIN_PDF_BYTES = 120_000


def find_chrome():
    for cand in CHROME_CANDIDATES:
        if cand.endswith(".exe") or os.path.sep in cand:
            if Path(cand).exists():
                return cand
        else:
            found = shutil.which(cand)
            if found:
                return found
    return None


def light_html(url):
    """Fetch a live page and pin it to the light theme."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        html = resp.read().decode("utf-8", "replace")
    # <base> so /assets/... still resolves once the page is a local file.
    html = html.replace("<head>", f'<head><base href="{SITE}/">', 1)
    # The dark theme is the default; this is how the site's own toggle opts out.
    html = html.replace('<html lang="en">', '<html lang="en" data-theme="light">', 1)
    return html


def render(chrome, url, out_path):
    try:
        html = light_html(url)
    except Exception as exc:  # network, 404, decode
        return False, f"fetch failed: {exc}"

    with tempfile.TemporaryDirectory() as work:
        page = Path(work) / "page.html"
        page.write_text(html, encoding="utf-8")
        profile = Path(work) / "profile"
        proc = subprocess.run(
            [
                chrome,
                "--headless",
                "--disable-gpu",
                "--no-pdf-header-footer",
                "--virtual-time-budget=12000",
                f"--user-data-dir={profile}",
                f"--print-to-pdf={out_path}",
                page.as_uri(),
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )

    size = out_path.stat().st_size if out_path.exists() else 0
    if size < MIN_PDF_BYTES:
        return False, (proc.stderr or "").strip()[-400:] or f"only {size} bytes written"
    return True, size


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python scripts/wire_pdf.py <YYYY-MM-DD>")
    date = sys.argv[1]

    repo = Path(__file__).resolve().parent.parent
    jobs = []
    if (repo / "_news" / f"{date}.md").exists():
        jobs.append((f"{date}-risk-wire.pdf", f"{SITE}/news/{date}/"))
    if (repo / "_general" / f"{date}.md").exists():
        jobs.append((f"{date}-general-wire.pdf", f"{SITE}/general-wire/{date}/"))
    if not jobs:
        sys.exit(f"no brief files for {date} in _news/ or _general/ — nothing to export")

    chrome = find_chrome()
    if not chrome:
        sys.exit("no Chrome / Edge / Chromium found for PDF export")

    out_dir = repo / "records"
    out_dir.mkdir(exist_ok=True)

    failures = []
    for name, url in jobs:
        out_path = out_dir / name
        ok, detail = render(chrome, url, out_path)
        if ok:
            print(f"  wrote records/{name}  ({detail:,} bytes)  <- {url}")
        else:
            failures.append(f"{name}: {detail}")

    if failures:
        sys.exit("PDF export failed:\n  " + "\n  ".join(failures))
    print(f"records/ updated for {date}")


if __name__ == "__main__":
    main()
