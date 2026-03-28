"""Render article HTML shells for Enterprise RAG series."""
from __future__ import annotations

from html import escape as esc


def article_page(
    *,
    page_title: str,
    description: str,
    kicker: str,
    h1: str,
    deck_html: str,
    meta_html: str,
    reading_path_html: str,
    toc_html: str,
    body_html: str,
    footer_extra: str = "",
    github_ipynb: str,
) -> str:
    nav = (
        f'<nav class="article-nav"><a href="../index.html">← All topics</a> · '
        f'<a href="{esc(github_ipynb, quote=True)}">Run the code (Jupyter on GitHub)</a></nav>'
    )
    foot = (
        f'<div class="footer-article">\n'
        f'        <p><a href="../index.html">← Back to all topics</a> · '
        f'<a href="{esc(github_ipynb, quote=True)}">Jupyter notebook on GitHub</a></p>\n'
        f"        {footer_extra}\n"
        f"        <p>— Nikhil Jain</p>\n"
        f"      </div>"
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(page_title)}</title>
  <meta name="description" content="{esc(description)}" />
  <link rel="stylesheet" href="../css/article.css" />
</head>
<body>
  <div class="wrap">
    {nav}

    <article>
      <p class="kicker">{esc(kicker)}</p>
      <h1>{h1}</h1>
      <p class="deck">{deck_html}</p>
      <p class="meta">{meta_html}</p>

      {reading_path_html}

      {toc_html}

      {body_html}

      {foot}
    </article>
  </div>
</body>
</html>
"""


def toc(items: list[tuple[str, str]]) -> str:
    lis = "\n".join(f'          <li><a href="#{esc(anchor)}">{esc(label)}</a></li>' for anchor, label in items)
    return f"""      <nav class="toc" aria-label="Table of contents">
        <strong>On this page</strong>
        <ol>
{lis}
        </ol>
      </nav>"""


def write_if_changed(path: str, content: str) -> None:
    from pathlib import Path

    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    old = p.read_text(encoding="utf-8") if p.exists() else None
    if old != content:
        p.write_text(content, encoding="utf-8")
