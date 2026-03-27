#!/usr/bin/env python3
"""Export all series notebooks to docs/ for GitHub Pages (static HTML)."""
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
NOTEBOOKS = sorted(ROOT.glob("*.ipynb"))
# Keep Jupyter from writing under ~/.jupyter (CI / sandbox friendly)
_JUPYTER_LOCAL = ROOT / ".jupyter_export"
_JUPYTER_LOCAL.mkdir(exist_ok=True)

TOPNAV = """
<div id="series-topnav" style="font-family:system-ui,-apple-system,sans-serif;font-size:14px;padding:12px 20px;background:#1e293b;color:#e2e8f0;border-bottom:1px solid #334155;">
  <a href="index.html" style="color:#38bdf8;font-weight:600;text-decoration:none;">← All topics</a>
  <span style="opacity:0.75;margin-left:12px;font-size:13px;">Enterprise RAG series</span>
</div>
"""


def inject_topnav(html_path: Path) -> None:
    """Add back-link bar to exported notebook HTML (not index.html)."""
    if html_path.name == "index.html":
        return
    text = html_path.read_text(encoding="utf-8")
    if 'id="series-topnav"' in text:
        return
    m = re.search(r"<body[^>]*>", text, flags=re.IGNORECASE)
    if not m:
        return
    html_path.write_text(text[: m.end()] + TOPNAV + text[m.end() :], encoding="utf-8")


def main() -> int:
    DOCS.mkdir(exist_ok=True)
    (DOCS / ".nojekyll").touch()
    env = os.environ.copy()
    env["JUPYTER_CONFIG_DIR"] = str(_JUPYTER_LOCAL / "config")
    env["JUPYTER_DATA_DIR"] = str(_JUPYTER_LOCAL / "data")
    env["JUPYTER_RUNTIME_DIR"] = str(_JUPYTER_LOCAL / "runtime")
    for d in ("config", "data", "runtime"):
        (_JUPYTER_LOCAL / d).mkdir(parents=True, exist_ok=True)
    for nb in NOTEBOOKS:
        if nb.name.startswith("."):
            continue
        cmd = [
            sys.executable,
            "-m",
            "jupyter",
            "nbconvert",
            "--to",
            "html",
            "--output-dir",
            str(DOCS),
            str(nb),
        ]
        print(" ".join(cmd))
        subprocess.run(cmd, check=True, cwd=str(ROOT), env=env)
    for html in sorted(DOCS.glob("*.html")):
        inject_topnav(html)
    print("Wrote", len(NOTEBOOKS), "HTML files to", DOCS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
