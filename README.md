# Enterprise RAG: What Breaks at Scale

A practical notebook series on why RAG and LLM systems fail in production — and how to fix them. Each part is a focused **Jupyter notebook** with runnable code, baselines compared to stronger approaches, and clear takeaways.

Most tutorials stop at “chunk, embed, retrieve.” That works on a handful of documents. With many sources, permissions, caching, and evaluation gaps, quality degrades quietly until users see wrong answers.

## The Series

| Part | Topic | Notebook |
| ---- | ----- | -------- |
| 1 | Embedding choice: not all vectors are equal | [01_not_all_vectors_are_equal_embedding_choice.ipynb](01_not_all_vectors_are_equal_embedding_choice.ipynb) |
| 2 | Chunking: right snippet, wrong context | [02_right_chunk_wrong_context_structural_chunking.ipynb](02_right_chunk_wrong_context_structural_chunking.ipynb) |
| 3 | Hybrid search: when dense search misses keywords | [03_when_dense_search_misses_keywords_hybrid_bm25.ipynb](03_when_dense_search_misses_keywords_hybrid_bm25.ipynb) |
| 4 | Reranking: cost vs quality | [04_cross_encoder_rerank_cost_vs_quality.ipynb](04_cross_encoder_rerank_cost_vs_quality.ipynb) |
| 5 | ACL at query time: leaks and over-blocking | [05_acl_at_query_time_why_rag_leaks_or_blocks_wrong.ipynb](05_acl_at_query_time_why_rag_leaks_or_blocks_wrong.ipynb) |
| 6 | Caching: semantic keys, TTL, invalidation | [06_semantic_cache_similarity_ttl_and_invalidation.ipynb](06_semantic_cache_similarity_ttl_and_invalidation.ipynb) |
| 7 | Stale index: updates and tombstones | [07_stale_index_incremental_updates_and_tombstones.ipynb](07_stale_index_incremental_updates_and_tombstones.ipynb) |
| 8 | Hallucination: grounding and when not to answer | [08_grounded_or_confidently_wrong_faithfulness_checks.ipynb](08_grounded_or_confidently_wrong_faithfulness_checks.ipynb) |
| 9 | Evaluation: retrieval and generation metrics | [09_rag_is_not_one_metric_retrieval_and_generation_eval.ipynb](09_rag_is_not_one_metric_retrieval_and_generation_eval.ipynb) |
| 10 | Security: prompt injection and PII boundaries | [10_prompt_injection_and_pii_boundary_for_rag_apps.ipynb](10_prompt_injection_and_pii_boundary_for_rag_apps.ipynb) |

## Stack

Runs **locally**. No paid API keys required.

| Component | Tool |
| --------- | ---- |
| Embeddings | sentence-transformers |
| Vector store | ChromaDB |
| Sparse retrieval | rank-bm25 |
| Reranker | cross-encoder (sentence-transformers) |
| Notebooks | Jupyter |

Optional: use **Ollama** for generation-only experiments (install separately).

## Quick start

```bash
git clone <your-repo-url>.git
cd AI-series
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

Open any notebook from the **repository root** so `src/` imports resolve.

The first run **downloads** Hugging Face models (sentence-transformers / cross-encoder); allow network access and expect several hundred MB on disk.

To **regenerate** all notebook files from the template script (after editing `scripts/generate_all_notebooks.py`):

```bash
python scripts/generate_all_notebooks.py
```

### NLTK (for BM25 tokenization in some notebooks)

```python
import nltk
nltk.download("punkt", quiet=True)
```

Run once in a notebook or Python shell if `punkt` is missing.

## About

Built by **Nikhil Jain** — AI Engineer.

[Connect on LinkedIn](https://www.linkedin.com/in/nikhiljain180/)

## License

MIT — see [LICENSE](LICENSE).
