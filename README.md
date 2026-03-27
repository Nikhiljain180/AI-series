# Enterprise RAG: What Breaks at Scale

Ten Jupyter notebooks on RAG outside the toy demo: chunking, hybrid search, access control, caching, stale indexes, evaluation, and safety. Runs locally with sentence-transformers, Chroma, BM25, and a small cross-encoder.

**[Browse the series (HTML)](https://nikhiljain180.github.io/AI-series/)**

## Topics

1. [Not all vectors are equal](https://nikhiljain180.github.io/AI-series/01_not_all_vectors_are_equal_embedding_choice.html) · [`01_not_all_vectors_are_equal_embedding_choice.ipynb`](01_not_all_vectors_are_equal_embedding_choice.ipynb)
2. [The right chunk, wrong context](https://nikhiljain180.github.io/AI-series/02_right_chunk_wrong_context_structural_chunking.html) · [`02_right_chunk_wrong_context_structural_chunking.ipynb`](02_right_chunk_wrong_context_structural_chunking.ipynb)
3. [When dense search misses keywords](https://nikhiljain180.github.io/AI-series/03_when_dense_search_misses_keywords_hybrid_bm25.html) · [`03_when_dense_search_misses_keywords_hybrid_bm25.ipynb`](03_when_dense_search_misses_keywords_hybrid_bm25.ipynb)
4. [Cross-encoder reranking](https://nikhiljain180.github.io/AI-series/04_cross_encoder_rerank_cost_vs_quality.html) · [`04_cross_encoder_rerank_cost_vs_quality.ipynb`](04_cross_encoder_rerank_cost_vs_quality.ipynb)
5. [ACL at query time](https://nikhiljain180.github.io/AI-series/05_acl_at_query_time_why_rag_leaks_or_blocks_wrong.html) · [`05_acl_at_query_time_why_rag_leaks_or_blocks_wrong.ipynb`](05_acl_at_query_time_why_rag_leaks_or_blocks_wrong.ipynb)
6. [Semantic cache & invalidation](https://nikhiljain180.github.io/AI-series/06_semantic_cache_similarity_ttl_and_invalidation.html) · [`06_semantic_cache_similarity_ttl_and_invalidation.ipynb`](06_semantic_cache_similarity_ttl_and_invalidation.ipynb)
7. [Stale index & tombstones](https://nikhiljain180.github.io/AI-series/07_stale_index_incremental_updates_and_tombstones.html) · [`07_stale_index_incremental_updates_and_tombstones.ipynb`](07_stale_index_incremental_updates_and_tombstones.ipynb)
8. [Grounded or confidently wrong](https://nikhiljain180.github.io/AI-series/08_grounded_or_confidently_wrong_faithfulness_checks.html) · [`08_grounded_or_confidently_wrong_faithfulness_checks.ipynb`](08_grounded_or_confidently_wrong_faithfulness_checks.ipynb)
9. [RAG is not one metric](https://nikhiljain180.github.io/AI-series/09_rag_is_not_one_metric_retrieval_and_generation_eval.html) · [`09_rag_is_not_one_metric_retrieval_and_generation_eval.ipynb`](09_rag_is_not_one_metric_retrieval_and_generation_eval.ipynb)
10. [Prompt injection & PII](https://nikhiljain180.github.io/AI-series/10_prompt_injection_and_pii_boundary_for_rag_apps.html) · [`10_prompt_injection_and_pii_boundary_for_rag_apps.ipynb`](10_prompt_injection_and_pii_boundary_for_rag_apps.ipynb)

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
