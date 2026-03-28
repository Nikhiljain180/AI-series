#!/usr/bin/env python3
"""
Generate docs/articles/*.html for Topics 2–10 (~10k words each, 3 parts).
Run from repo root: python scripts/generate_longform_articles.py
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from longform.prose_engine import build_topic_html  # noqa: E402
from longform.render import article_page, toc, write_if_changed  # noqa: E402

GITHUB_BASE = "https://github.com/Nikhiljain180/AI-series/blob/main/"

# topic_id, part1 file, part2 file, part3 file, ipynb filename, short slug for titles
LAYOUT = [
    (
        2,
        "02-right-chunk-wrong-context.html",
        "02b-structural-chunking-deep-dive.html",
        "02c-supplement-scenarios.html",
        "02_right_chunk_wrong_context_structural_chunking.ipynb",
        "Right Chunk, Wrong Context",
    ),
    (
        3,
        "03-hybrid-search-bm25-vectors.html",
        "03b-fusion-logging-and-regressions.html",
        "03c-supplement-scenarios.html",
        "03_when_dense_search_misses_keywords_hybrid_bm25.ipynb",
        "Hybrid BM25 + Vectors",
    ),
    (
        4,
        "04-cross-encoder-reranking.html",
        "04b-latency-cost-and-candidates.html",
        "04c-supplement-scenarios.html",
        "04_cross_encoder_rerank_cost_vs_quality.ipynb",
        "Cross-Encoder Reranking",
    ),
    (
        5,
        "05-acl-at-query-time.html",
        "05b-filters-audits-and-threats.html",
        "05c-supplement-scenarios.html",
        "05_acl_at_query_time_why_rag_leaks_or_blocks_wrong.ipynb",
        "ACL at Query Time",
    ),
    (
        6,
        "06-semantic-cache-invalidation.html",
        "06b-metrics-and-two-tier-caching.html",
        "06c-supplement-scenarios.html",
        "06_semantic_cache_similarity_ttl_and_invalidation.ipynb",
        "Semantic Cache & Invalidation",
    ),
    (
        7,
        "07-stale-index-tombstones.html",
        "07b-incremental-updates-and-ops.html",
        "07c-supplement-scenarios.html",
        "07_stale_index_incremental_updates_and_tombstones.ipynb",
        "Stale Index & Tombstones",
    ),
    (
        8,
        "08-faithfulness-and-grounding.html",
        "08b-layered-guards-and-rubrics.html",
        "08c-supplement-scenarios.html",
        "08_grounded_or_confidently_wrong_faithfulness_checks.ipynb",
        "Faithfulness Checks",
    ),
    (
        9,
        "09-rag-evaluation-metrics.html",
        "09b-golden-sets-and-slicing.html",
        "09c-supplement-scenarios.html",
        "09_rag_is_not_one_metric_retrieval_and_generation_eval.ipynb",
        "RAG Evaluation",
    ),
    (
        10,
        "10-prompt-injection-pii.html",
        "10b-layered-defenses-and-ux.html",
        "10c-supplement-scenarios.html",
        "10_prompt_injection_and_pii_boundary_for_rag_apps.ipynb",
        "Prompt Injection & PII",
    ),
]


def toc_for_part(part: int) -> list[tuple[str, str]]:
    base = [
        ("story", "Framing the problem"),
        ("checklist", "Checklists and concrete next steps"),
        ("faq", "FAQ — objections from real meetings"),
    ]
    if part == 2:
        return [
            ("ops", "Operational discipline"),
            ("instrument", "Instrumentation"),
            ("checklist", "What to measure"),
            ("faq", "FAQ"),
        ]
    if part == 3:
        return [
            ("scenarios", "Scenarios and tradeoffs"),
            ("playbook", "Playbook prompts"),
            ("faq", "FAQ"),
        ]
    return base


def reading_path(topic_id: int, part: int, f1: str, f2: str, f3: str) -> str:
    if part == 1:
        text = f'Reading path: Part 1 (this page), continue to <a href="{f2}">Part 2</a>, then <a href="{f3}">Part 3</a>. Together these parts form one ~10k-word essay for Topic {topic_id}.'
    elif part == 2:
        text = f'Reading path: <a href="{f1}">Part 1</a>, Part 2 (this page), <a href="{f3}">Part 3</a>.'
    else:
        text = f'Reading path: <a href="{f1}">Part 1</a>, <a href="{f2}">Part 2</a>, Part 3 (this page).'
    return f'<p style="font-size:0.95rem;color:#57534e;margin-bottom:1.5rem;">{text}</p>'


def nav_footer(part: int, f1: str, f2: str, f3: str) -> str:
    if part == 1:
        return f'<p style="margin-top:2rem;"><a href="{f2}"><strong>Continue to Part 2 →</strong></a></p>'
    if part == 2:
        return f'<p style="margin-top:2rem;"><a href="{f3}"><strong>Continue to Part 3 →</strong></a></p>'
    return f'<p style="margin-top:2rem;"><a href="{f1}"><strong>← Back to Part 1</strong></a> · <a href="../index.html"><strong>All topics</strong></a></p>'


def main() -> None:
    out_dir = ROOT / "docs" / "articles"
    for (
        topic_id,
        f1,
        f2,
        f3,
        ipynb,
        short_title,
    ) in LAYOUT:
        gh = GITHUB_BASE + ipynb
        deck = (
            f"Enterprise RAG · Topic {topic_id}: <em>{short_title}</em>. "
            "Written for readers from interns to principal engineers—plain language first, production truth always."
        )
        for part, fname in ((1, f1), (2, f2), (3, f3)):
            body = build_topic_html(topic_id, part)
            # Anchors in prose_engine may not match toc_for_part — align minimally
            body = body + "\n\n      " + nav_footer(part, f1, f2, f3)
            kicker = f"Enterprise RAG · Topic {topic_id} · Part {part}"
            page_title = f"{short_title} — Part {part} (Topic {topic_id})"
            description = (
                f"Long-form guide: {short_title} (Topic {topic_id}, Part {part}). "
                "Enterprise RAG series by Nikhil Jain."
            )
            meta = (
                f"Topic {topic_id}, Part {part} of 3. Together with the other parts, this topic is designed as a "
                f"~10,000-word reading path—deep enough for a weekend, structured enough for a design review."
            )
            h1_plain = f"{short_title}: a field guide (Part {part})"
            h1 = h1_plain  # escaped in template via esc - actually we use raw in render - need escape
            from html import escape as esc

            html_doc = article_page(
                page_title=page_title,
                description=description,
                kicker=kicker,
                h1=esc(h1_plain),
                deck_html=deck,
                meta_html=meta,
                reading_path_html=reading_path(topic_id, part, f1, f2, f3),
                toc_html=toc(toc_for_part(part)),
                body_html=body,
                footer_extra="",
                github_ipynb=gh,
            )
            write_if_changed(str(out_dir / fname), html_doc)

    print(f"Wrote topics 2–10 articles under {out_dir}")


if __name__ == "__main__":
    main()
