<!-- Same layout as docs/index.html — blog & notebook export links use GitHub Pages URLs so clicks open the deployed site (not github.com blob HTML). -->

<style>
  :root {
    --bg: #0f172a;
    --text: #f1f5f9;
    --muted: #94a3b8;
    --accent: #38bdf8;
    --hover: #7dd3fc;
    --blog: #a7f3d0;
  }
  .readme-index * { box-sizing: border-box; }
  .readme-index {
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.55;
    padding: 2.5rem 1.25rem 4rem;
    margin: -1rem -1rem 0 -1rem;
    max-width: 40rem;
  }
  .readme-index h1 {
    font-size: 1.5rem;
    font-weight: 700;
    letter-spacing: -0.02em;
    margin: 0 0 0.35rem;
    border: none;
    padding: 0;
  }
  .readme-index .sub {
    color: var(--muted);
    font-size: 0.95rem;
    margin: 0 0 2rem;
  }
  .readme-index ol.topics { list-style: none; padding: 0; margin: 0; }
  .readme-index ol.topics li {
    margin: 0;
    padding-bottom: 1.35rem;
    border-bottom: 1px solid #334155;
  }
  .readme-index ol.topics li:first-child { border-top: 1px solid #334155; padding-top: 0.25rem; }
  .readme-index ol.topics a.lesson {
    display: block;
    margin: 0 0 0.75rem;
    color: var(--accent);
    text-decoration: none;
    font-weight: 600;
    font-size: 1.05rem;
    line-height: 1.55;
  }
  .readme-index ol.topics a.lesson:hover { color: var(--hover); text-decoration: underline; }
  .readme-index ol.topics a.github, .readme-index ol.topics a.export {
    font-size: 0.85rem;
    color: var(--muted);
    text-decoration: underline;
    text-underline-offset: 3px;
    margin-right: 0.75rem;
  }
  .readme-index ol.topics a.github:hover, .readme-index ol.topics a.export:hover { color: var(--accent); }
  .readme-index footer {
    margin-top: 2.5rem;
    font-size: 0.85rem;
    color: var(--muted);
  }
  .readme-index footer a { color: var(--accent); }
</style>

<div class="readme-index" style="font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif; background: #0f172a; color: #f1f5f9; line-height: 1.55; padding: 2.5rem 1.25rem 4rem; max-width: 40rem; margin: 0 auto;">
  <h1>Enterprise RAG: What Breaks at Scale</h1>
  <p class="sub"><strong style="color:#a7f3d0;">Read the blog</strong> for long-form explanations (plain language, written like a serious article). <strong style="color:#38bdf8;">Notebook export</strong> is the auto-generated HTML from Jupyter—useful for code cells. <strong>GitHub</strong> opens the <code>.ipynb</code> to run or edit locally.</p>

  <ol class="topics">
    <li>
      <a class="lesson" href="https://nikhiljain180.github.io/AI-series/articles/01-not-all-vectors-equal.html"><strong>1.</strong> Chunking (fixed, semantic, hierarchical) and embedding models—explained for students and production engineers.</a>
      <a class="export" href="https://nikhiljain180.github.io/AI-series/01_not_all_vectors_are_equal_embedding_choice.html">Notebook HTML export →</a>
      <a class="github" href="https://github.com/Nikhiljain180/AI-series/blob/main/01_not_all_vectors_are_equal_embedding_choice.ipynb">Run on GitHub →</a>
    </li>
    <li>
      <a class="lesson" href="https://nikhiljain180.github.io/AI-series/articles/02-right-chunk-wrong-context.html"><strong>2.</strong> Structural chunking, boundaries, and why “relevant” fragments still miss the exception clause.</a>
      <a class="export" href="https://nikhiljain180.github.io/AI-series/02_right_chunk_wrong_context_structural_chunking.html">Notebook HTML export →</a>
      <a class="github" href="https://github.com/Nikhiljain180/AI-series/blob/main/02_right_chunk_wrong_context_structural_chunking.ipynb">Run on GitHub →</a>
    </li>
    <li>
      <a class="lesson" href="https://nikhiljain180.github.io/AI-series/articles/03-hybrid-search-bm25-vectors.html"><strong>3.</strong> Hybrid BM25 + vectors, fusion (RRF), and logging which leg saved the query.</a>
      <a class="export" href="https://nikhiljain180.github.io/AI-series/03_when_dense_search_misses_keywords_hybrid_bm25.html">Notebook HTML export →</a>
      <a class="github" href="https://github.com/Nikhiljain180/AI-series/blob/main/03_when_dense_search_misses_keywords_hybrid_bm25.ipynb">Run on GitHub →</a>
    </li>
    <li>
      <a class="lesson" href="https://nikhiljain180.github.io/AI-series/articles/04-cross-encoder-reranking.html"><strong>4.</strong> Retrieve wide, rerank narrow: quality vs latency vs GPU memory.</a>
      <a class="export" href="https://nikhiljain180.github.io/AI-series/04_cross_encoder_rerank_cost_vs_quality.html">Notebook HTML export →</a>
      <a class="github" href="https://github.com/Nikhiljain180/AI-series/blob/main/04_cross_encoder_rerank_cost_vs_quality.ipynb">Run on GitHub →</a>
    </li>
    <li>
      <a class="lesson" href="https://nikhiljain180.github.io/AI-series/articles/05-acl-at-query-time.html"><strong>5.</strong> Enforce authorization in retrieval—filters, audits, cross-tenant tests.</a>
      <a class="export" href="https://nikhiljain180.github.io/AI-series/05_acl_at_query_time_why_rag_leaks_or_blocks_wrong.html">Notebook HTML export →</a>
      <a class="github" href="https://github.com/Nikhiljain180/AI-series/blob/main/05_acl_at_query_time_why_rag_leaks_or_blocks_wrong.ipynb">Run on GitHub →</a>
    </li>
    <li>
      <a class="lesson" href="https://nikhiljain180.github.io/AI-series/articles/06-semantic-cache-invalidation.html"><strong>6.</strong> Similarity + version tags, TTL, false hits—cache without lying.</a>
      <a class="export" href="https://nikhiljain180.github.io/AI-series/06_semantic_cache_similarity_ttl_and_invalidation.html">Notebook HTML export →</a>
      <a class="github" href="https://github.com/Nikhiljain180/AI-series/blob/main/06_semantic_cache_similarity_ttl_and_invalidation.ipynb">Run on GitHub →</a>
    </li>
    <li>
      <a class="lesson" href="https://nikhiljain180.github.io/AI-series/articles/07-stale-index-tombstones.html"><strong>7.</strong> Incremental updates, stable IDs, deletes, ingestion lag.</a>
      <a class="export" href="https://nikhiljain180.github.io/AI-series/07_stale_index_incremental_updates_and_tombstones.html">Notebook HTML export →</a>
      <a class="github" href="https://github.com/Nikhiljain180/AI-series/blob/main/07_stale_index_incremental_updates_and_tombstones.ipynb">Run on GitHub →</a>
    </li>
    <li>
      <a class="lesson" href="https://nikhiljain180.github.io/AI-series/articles/08-faithfulness-and-grounding.html"><strong>8.</strong> Cheap faithfulness checks, abstention, and rubrics—before the LLM sounds sure.</a>
      <a class="export" href="https://nikhiljain180.github.io/AI-series/08_grounded_or_confidently_wrong_faithfulness_checks.html">Notebook HTML export →</a>
      <a class="github" href="https://github.com/Nikhiljain180/AI-series/blob/main/08_grounded_or_confidently_wrong_faithfulness_checks.ipynb">Run on GitHub →</a>
    </li>
    <li>
      <a class="lesson" href="https://nikhiljain180.github.io/AI-series/articles/09-rag-evaluation-metrics.html"><strong>9.</strong> Recall@k, slicing, golden sets—retrieval vs generation eval.</a>
      <a class="export" href="https://nikhiljain180.github.io/AI-series/09_rag_is_not_one_metric_retrieval_and_generation_eval.html">Notebook HTML export →</a>
      <a class="github" href="https://github.com/Nikhiljain180/AI-series/blob/main/09_rag_is_not_one_metric_retrieval_and_generation_eval.ipynb">Run on GitHub →</a>
    </li>
    <li>
      <a class="lesson" href="https://nikhiljain180.github.io/AI-series/articles/10-prompt-injection-pii.html"><strong>10.</strong> Untrusted chunks, layered defenses, PII boundaries.</a>
      <a class="export" href="https://nikhiljain180.github.io/AI-series/10_prompt_injection_and_pii_boundary_for_rag_apps.html">Notebook HTML export →</a>
      <a class="github" href="https://github.com/Nikhiljain180/AI-series/blob/main/10_prompt_injection_and_pii_boundary_for_rag_apps.ipynb">Run on GitHub →</a>
    </li>
  </ol>

  <footer>
    <p>Nikhil Jain — <a href="https://www.linkedin.com/in/nikhiljain180/">LinkedIn</a> · <a href="https://github.com/Nikhiljain180/AI-series">Repository</a></p>
  </footer>
</div>
