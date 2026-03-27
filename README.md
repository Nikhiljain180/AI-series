# Enterprise RAG: What Breaks at Scale

Most RAG walkthroughs stop once cosine similarity looks good on a toy folder of PDFs. I wrote this series for the rest of the pipeline: how you chunk, how you search, who is allowed to see a hit, what happens when the index is stale, and how you know something is wrong before a customer tells you. Everything runs on your machine—sentence-transformers, Chroma, BM25, a small cross-encoder—no vendor lock-in for the learning part.

## Read the series in the browser

Static HTML exports live in [`docs/`](docs/). After you turn on **GitHub Pages** (repo **Settings → Pages → Deploy from branch `main` / folder `/docs`**), the landing page is:

**[https://nikhiljain180.github.io/AI-series/](https://nikhiljain180.github.io/AI-series/)**

Each topic on that page links to its HTML notebook. If your username or repo name is different, swap it in the URL.

---

## The ten parts

### 1. Not all vectors are equal

I still see teams treat the embedding model as an afterthought—whatever shipped with the sample repo. In practice, that choice drives recall, latency, and how much pain you will have when queries are phrased nothing like your documents. This part runs the same small corpus through two different sentence-transformers models so you can see the tradeoff on real top-1 hits, not on a leaderboard in isolation.

**[Read as HTML →](https://nikhiljain180.github.io/AI-series/01_not_all_vectors_are_equal_embedding_choice.html)**  
*Notebook:* [`01_not_all_vectors_are_equal_embedding_choice.ipynb`](01_not_all_vectors_are_equal_embedding_choice.ipynb)

### 2. The right chunk, wrong context

Fixed-size chunking is easy to implement and miserable to debug: the embedding looks relevant because half of the answer sits in the *next* window. I walk one policy-style document with a buried identifier and compare fixed windows to paragraph-aware splits so the failure mode is obvious.

**[Read as HTML →](https://nikhiljain180.github.io/AI-series/02_right_chunk_wrong_context_structural_chunking.html)**  
*Notebook:* [`02_right_chunk_wrong_context_structural_chunking.ipynb`](02_right_chunk_wrong_context_structural_chunking.ipynb)

### 3. When dense search misses keywords

Pure vector search can look smooth in a demo and then lose error codes, SKUs, and internal names that users type verbatim. Here I combine BM25 with the vector store and fuse rankings with RRF—small enough to read in one sitting, concrete enough to steal for a prototype.

**[Read as HTML →](https://nikhiljain180.github.io/AI-series/03_when_dense_search_misses_keywords_hybrid_bm25.html)**  
*Notebook:* [`03_when_dense_search_misses_keywords_hybrid_bm25.ipynb`](03_when_dense_search_misses_keywords_hybrid_bm25.ipynb)

### 4. Cross-encoder reranking: cost vs quality

Bi-encoders are fast because query and document never attend to each other; that is also why ordering is sometimes wrong. I retrieve a short list with the bi-encoder, then rerank with a small cross-encoder—the pattern I default to when stakeholders care about precision more than p50 latency.

**[Read as HTML →](https://nikhiljain180.github.io/AI-series/04_cross_encoder_rerank_cost_vs_quality.html)**  
*Notebook:* [`04_cross_encoder_rerank_cost_vs_quality.ipynb`](04_cross_encoder_rerank_cost_vs_quality.ipynb)

### 5. ACL at query time

If you retrieve first and “filter in the prompt,” you have already lost: the model may still see text it should not, and auditors will not care about your intentions. This notebook uses two synthetic tenants in one Chroma collection and shows the difference between an unfiltered query and a metadata filter applied at retrieval time.

**[Read as HTML →](https://nikhiljain180.github.io/AI-series/05_acl_at_query_time_why_rag_leaks_or_blocks_wrong.html)**  
*Notebook:* [`05_acl_at_query_time_why_rag_leaks_or_blocks_wrong.ipynb`](05_acl_at_query_time_why_rag_leaks_or_blocks_wrong.ipynb)

### 6. Semantic cache, TTL, invalidation

Exact-match caches miss paraphrases; semantic caches answer faster—and can confidently return something that was true last week. I keep a toy in-memory cache keyed by embedding similarity and show what happens when you bump a knowledge-base version without invalidating entries.

**[Read as HTML →](https://nikhiljain180.github.io/AI-series/06_semantic_cache_similarity_ttl_and_invalidation.html)**  
*Notebook:* [`06_semantic_cache_similarity_ttl_and_invalidation.ipynb`](06_semantic_cache_similarity_ttl_and_invalidation.ipynb)

### 7. Stale index, updates, tombstones

Your source of truth changes; the vector index is always a little behind. The painful bugs are the ones where an old chunk still ranks high after a policy change. I simulate two versions of a “policy” document and delete the stale id so you can see how a hard delete changes what retrieval returns.

**[Read as HTML →](https://nikhiljain180.github.io/AI-series/07_stale_index_incremental_updates_and_tombstones.html)**  
*Notebook:* [`07_stale_index_incremental_updates_and_tombstones.ipynb`](07_stale_index_incremental_updates_and_tombstones.ipynb)

### 8. Grounded or confidently wrong

Before you add a fancier judge model, it helps to have a blunt heuristic: flag sentences whose content words never appear in the retrieved context. This is not a replacement for human review or NLI, but it is cheap and it catches the “free lifetime license” class of hallucination in demos.

**[Read as HTML →](https://nikhiljain180.github.io/AI-series/08_grounded_or_confidently_wrong_faithfulness_checks.html)**  
*Notebook:* [`08_grounded_or_confidently_wrong_faithfulness_checks.ipynb`](08_grounded_or_confidently_wrong_faithfulness_checks.ipynb)

### 9. RAG is not one metric

I split the problem in two: did we fetch the right chunk, and only then whether the model said something faithful. With a tiny labeled set and chunk ids, I compute Recall@k for retrieval—something you can regression-test when someone swaps embeddings or chunking strategy.

**[Read as HTML →](https://nikhiljain180.github.io/AI-series/09_rag_is_not_one_metric_retrieval_and_generation_eval.html)**  
*Notebook:* [`09_rag_is_not_one_metric_retrieval_and_generation_eval.ipynb`](09_rag_is_not_one_metric_retrieval_and_generation_eval.ipynb)

### 10. Prompt injection and PII boundaries

Retrieved text is user-supplied in the worst sense: it can carry instructions meant for the model, not the end user. I contrast a naive single “context” blob with an explicit trusted vs untrusted split, and show a tiny regex redaction for emails and phone numbers—production needs more layers, but you have to start somewhere visible.

**[Read as HTML →](https://nikhiljain180.github.io/AI-series/10_prompt_injection_and_pii_boundary_for_rag_apps.html)**  
*Notebook:* [`10_prompt_injection_and_pii_boundary_for_rag_apps.ipynb`](10_prompt_injection_and_pii_boundary_for_rag_apps.ipynb)

---

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
