# Enterprise RAG: What Breaks at Scale

**Series landing page (rendered `docs/index.html`): [open in browser →](https://nikhiljain180.github.io/AI-series/)** — With [GitHub Pages](https://docs.github.com/pages) serving the `docs/` folder, that URL is the same entry point as [`docs/index.html`](docs/index.html); it is not a separate copy.

GitHub’s README preview only renders Markdown. It cannot embed the full styled HTML of `index.html` inside this file (no live iframe of your site). Use the link above for the **same preview** you get from the deployed landing page. To inspect the file in the repo, open [`docs/index.html`](docs/index.html) (you may see source or GitHub’s HTML view depending on the UI).

Long-form **blog articles** (readable in the browser, ~10k words per topic across three parts) plus runnable **Jupyter notebooks** on chunking, hybrid search, access control, caching, stale indexes, evaluation, and safety. Stack: sentence-transformers, Chroma, BM25, cross-encoder—runs locally.

## Topics (blog + notebook)

Each topic has **Part 1–3** under `docs/articles/` (together ~10k words). **Notebook export** is auto-generated HTML from Jupyter; **GitHub** links open the `.ipynb`.

1. **Not all vectors are equal** — Blog: [Part 1](https://nikhiljain180.github.io/AI-series/articles/01-not-all-vectors-equal.html) · [Part 2](https://nikhiljain180.github.io/AI-series/articles/01b-embeddings-deep-dive.html) · [Part 3](https://nikhiljain180.github.io/AI-series/articles/01c-supplement-scenarios.html) · [Notebook export](https://nikhiljain180.github.io/AI-series/01_not_all_vectors_are_equal_embedding_choice.html)
2. **The right chunk, wrong context** — Blog: [Part 1](https://nikhiljain180.github.io/AI-series/articles/02-right-chunk-wrong-context.html) · [Part 2](https://nikhiljain180.github.io/AI-series/articles/02b-structural-chunking-deep-dive.html) · [Part 3](https://nikhiljain180.github.io/AI-series/articles/02c-supplement-scenarios.html) · [Notebook export](https://nikhiljain180.github.io/AI-series/02_right_chunk_wrong_context_structural_chunking.html)
3. **When dense search misses keywords** — Blog: [Part 1](https://nikhiljain180.github.io/AI-series/articles/03-hybrid-search-bm25-vectors.html) · [Part 2](https://nikhiljain180.github.io/AI-series/articles/03b-fusion-logging-and-regressions.html) · [Part 3](https://nikhiljain180.github.io/AI-series/articles/03c-supplement-scenarios.html) · [Notebook export](https://nikhiljain180.github.io/AI-series/03_when_dense_search_misses_keywords_hybrid_bm25.html)
4. **Cross-encoder reranking** — Blog: [Part 1](https://nikhiljain180.github.io/AI-series/articles/04-cross-encoder-reranking.html) · [Part 2](https://nikhiljain180.github.io/AI-series/articles/04b-latency-cost-and-candidates.html) · [Part 3](https://nikhiljain180.github.io/AI-series/articles/04c-supplement-scenarios.html) · [Notebook export](https://nikhiljain180.github.io/AI-series/04_cross_encoder_rerank_cost_vs_quality.html)
5. **ACL at query time** — Blog: [Part 1](https://nikhiljain180.github.io/AI-series/articles/05-acl-at-query-time.html) · [Part 2](https://nikhiljain180.github.io/AI-series/articles/05b-filters-audits-and-threats.html) · [Part 3](https://nikhiljain180.github.io/AI-series/articles/05c-supplement-scenarios.html) · [Notebook export](https://nikhiljain180.github.io/AI-series/05_acl_at_query_time_why_rag_leaks_or_blocks_wrong.html)
6. **Semantic cache & invalidation** — Blog: [Part 1](https://nikhiljain180.github.io/AI-series/articles/06-semantic-cache-invalidation.html) · [Part 2](https://nikhiljain180.github.io/AI-series/articles/06b-metrics-and-two-tier-caching.html) · [Part 3](https://nikhiljain180.github.io/AI-series/articles/06c-supplement-scenarios.html) · [Notebook export](https://nikhiljain180.github.io/AI-series/06_semantic_cache_similarity_ttl_and_invalidation.html)
7. **Stale index & tombstones** — Blog: [Part 1](https://nikhiljain180.github.io/AI-series/articles/07-stale-index-tombstones.html) · [Part 2](https://nikhiljain180.github.io/AI-series/articles/07b-incremental-updates-and-ops.html) · [Part 3](https://nikhiljain180.github.io/AI-series/articles/07c-supplement-scenarios.html) · [Notebook export](https://nikhiljain180.github.io/AI-series/07_stale_index_incremental_updates_and_tombstones.html)
8. **Grounded or confidently wrong** — Blog: [Part 1](https://nikhiljain180.github.io/AI-series/articles/08-faithfulness-and-grounding.html) · [Part 2](https://nikhiljain180.github.io/AI-series/articles/08b-layered-guards-and-rubrics.html) · [Part 3](https://nikhiljain180.github.io/AI-series/articles/08c-supplement-scenarios.html) · [Notebook export](https://nikhiljain180.github.io/AI-series/08_grounded_or_confidently_wrong_faithfulness_checks.html)
9. **RAG is not one metric** — Blog: [Part 1](https://nikhiljain180.github.io/AI-series/articles/09-rag-evaluation-metrics.html) · [Part 2](https://nikhiljain180.github.io/AI-series/articles/09b-golden-sets-and-slicing.html) · [Part 3](https://nikhiljain180.github.io/AI-series/articles/09c-supplement-scenarios.html) · [Notebook export](https://nikhiljain180.github.io/AI-series/09_rag_is_not_one_metric_retrieval_and_generation_eval.html)
10. **Prompt injection & PII** — Blog: [Part 1](https://nikhiljain180.github.io/AI-series/articles/10-prompt-injection-pii.html) · [Part 2](https://nikhiljain180.github.io/AI-series/articles/10b-layered-defenses-and-ux.html) · [Part 3](https://nikhiljain180.github.io/AI-series/articles/10c-supplement-scenarios.html) · [Notebook export](https://nikhiljain180.github.io/AI-series/10_prompt_injection_and_pii_boundary_for_rag_apps.html)

### Regenerating long-form HTML (topics 2–10)

Blog HTML for topics 2–10 is generated from `scripts/longform/prose_engine.py` and written by:

```bash
python scripts/generate_longform_articles.py
```

## Run locally

```bash
git clone https://github.com/Nikhiljain180/AI-series.git
cd AI-series
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

Work from the repo root so `src/` imports work. First run downloads model weights (~hundreds of MB).

## About

**Nikhil Jain** — AI Engineer · [LinkedIn](https://www.linkedin.com/in/nikhiljain180/)

MIT — [LICENSE](LICENSE)
