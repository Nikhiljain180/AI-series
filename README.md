# Enterprise RAG: What Breaks at Scale

Notebooks on retrieval-augmented generation beyond the happy path: chunking, hybrid search, permissions, caching, stale indexes, evaluation, and safety. All runnable locally (sentence-transformers, Chroma, BM25, cross-encoder).

## Start here (read in the browser)

**[Open the series — 10 topic links](https://nikhiljain180.github.io/AI-series/)**

That page lists every topic; each link opens the **full notebook exported as HTML**. Under each topic you’ll see the matching `.ipynb` on GitHub if you want to clone and run it.

## Topics (click = notebook as HTML)

1. **[Not all vectors are equal](https://nikhiljain180.github.io/AI-series/01_not_all_vectors_are_equal_embedding_choice.html)** — [`01_not_all_vectors_are_equal_embedding_choice.ipynb`](01_not_all_vectors_are_equal_embedding_choice.ipynb)
2. **[The right chunk, wrong context](https://nikhiljain180.github.io/AI-series/02_right_chunk_wrong_context_structural_chunking.html)** — [`02_right_chunk_wrong_context_structural_chunking.ipynb`](02_right_chunk_wrong_context_structural_chunking.ipynb)
3. **[When dense search misses keywords](https://nikhiljain180.github.io/AI-series/03_when_dense_search_misses_keywords_hybrid_bm25.html)** — [`03_when_dense_search_misses_keywords_hybrid_bm25.ipynb`](03_when_dense_search_misses_keywords_hybrid_bm25.ipynb)
4. **[Cross-encoder reranking](https://nikhiljain180.github.io/AI-series/04_cross_encoder_rerank_cost_vs_quality.html)** — [`04_cross_encoder_rerank_cost_vs_quality.ipynb`](04_cross_encoder_rerank_cost_vs_quality.ipynb)
5. **[ACL at query time](https://nikhiljain180.github.io/AI-series/05_acl_at_query_time_why_rag_leaks_or_blocks_wrong.html)** — [`05_acl_at_query_time_why_rag_leaks_or_blocks_wrong.ipynb`](05_acl_at_query_time_why_rag_leaks_or_blocks_wrong.ipynb)
6. **[Semantic cache & invalidation](https://nikhiljain180.github.io/AI-series/06_semantic_cache_similarity_ttl_and_invalidation.html)** — [`06_semantic_cache_similarity_ttl_and_invalidation.ipynb`](06_semantic_cache_similarity_ttl_and_invalidation.ipynb)
7. **[Stale index & tombstones](https://nikhiljain180.github.io/AI-series/07_stale_index_incremental_updates_and_tombstones.html)** — [`07_stale_index_incremental_updates_and_tombstones.ipynb`](07_stale_index_incremental_updates_and_tombstones.ipynb)
8. **[Grounded or confidently wrong](https://nikhiljain180.github.io/AI-series/08_grounded_or_confidently_wrong_faithfulness_checks.html)** — [`08_grounded_or_confidently_wrong_faithfulness_checks.ipynb`](08_grounded_or_confidently_wrong_faithfulness_checks.ipynb)
9. **[RAG is not one metric](https://nikhiljain180.github.io/AI-series/09_rag_is_not_one_metric_retrieval_and_generation_eval.html)** — [`09_rag_is_not_one_metric_retrieval_and_generation_eval.ipynb`](09_rag_is_not_one_metric_retrieval_and_generation_eval.ipynb)
10. **[Prompt injection & PII](https://nikhiljain180.github.io/AI-series/10_prompt_injection_and_pii_boundary_for_rag_apps.html)** — [`10_prompt_injection_and_pii_boundary_for_rag_apps.ipynb`](10_prompt_injection_and_pii_boundary_for_rag_apps.ipynb)

## If links return 404

1. **Use the URL GitHub shows you.** Repo **Settings → Pages**: copy **Visit site** (or the published URL). Path casing can differ (e.g. `AI-series` vs `ai-series`)—your settings page is the source of truth.
2. **Publish `docs/` correctly.** Either:
   - **Branch:** Source = branch `main`, folder **`/docs`**, and the branch must contain [`docs/`](docs/) with the `.html` files and [`.nojekyll`](docs/.nojekyll); **or**
   - **GitHub Actions:** Source = **GitHub Actions**, then push so [`.github/workflows/deploy-pages.yml`](.github/workflows/deploy-pages.yml) runs (check the **Actions** tab for a green run).
3. **Wait a minute** after the first deploy, then hard-refresh.

Do not use only the `/docs/` path on **github.com** for reading HTML—GitHub does not render those pages as a live site. The live site is always `https://<user>.github.io/<repo>/...`.

## Stack

Runs **locally**. No paid API keys required.

| Component | Tool |
| --------- | ---- |
| Embeddings | sentence-transformers |
| Vector store | ChromaDB |
| Sparse retrieval | rank-bm25 |
| Reranker | cross-encoder (sentence-transformers) |
| Notebooks | Jupyter |

Optional: **Ollama** for generation-only experiments (install separately).

## Quick start (run the notebooks)

```bash
git clone https://github.com/Nikhiljain180/AI-series.git
cd AI-series
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

Open notebooks from the **repository root** so `src/` imports resolve. The first run **downloads** Hugging Face models; allow network access and expect several hundred MB on disk.

### Regenerate notebook HTML (for GitHub Pages)

After you change any `.ipynb`, refresh the files in `docs/`:

```bash
python scripts/export_notebooks_to_html.py
```

Then commit the updated `docs/*.html` (and `docs/index.html` if you edited it).

### Regenerate `.ipynb` from the template script

```bash
python scripts/generate_all_notebooks.py
```

### NLTK (BM25 helpers in some paths)

```python
import nltk
nltk.download("punkt", quiet=True)
```

## About

Built by **Nikhil Jain** — AI Engineer.

[Connect on LinkedIn](https://www.linkedin.com/in/nikhiljain180/)

## License

MIT — see [LICENSE](LICENSE).
