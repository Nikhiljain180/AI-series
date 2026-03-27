#!/usr/bin/env python3
"""Export all series notebooks to docs/ for GitHub Pages (static HTML)."""
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
NOTEBOOKS = sorted(ROOT.glob("*.ipynb"))
# Keep Jupyter from writing under ~/.jupyter (CI / sandbox friendly)
_JUPYTER_LOCAL = ROOT / ".jupyter_export"
_JUPYTER_LOCAL.mkdir(exist_ok=True)


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
    print("Wrote", len(NOTEBOOKS), "HTML files to", DOCS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
