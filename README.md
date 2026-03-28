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
  .readme-index .blog-row {
    font-size: 0.88rem;
    margin: 0.5rem 0 0.35rem;
    line-height: 1.6;
  }
  .readme-index .blog-row a { color: var(--blog); font-weight: 600; text-decoration: none; }
  .readme-index .blog-row a:hover { text-decoration: underline; }
  .readme-index ol.topics a.lesson {
    display: inline-block;
    margin-top: 0.85rem;
    color: var(--accent);
    text-decoration: none;
    font-weight: 600;
    font-size: 1.05rem;
  }
  .readme-index ol.topics a.lesson:hover { color: var(--hover); text-decoration: underline; }
  .readme-index ol.topics .teach {
    margin: 0.5rem 0 0.65rem;
    font-size: 0.9rem;
    color: #cbd5e1;
  }
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
      <div class="blog-row">Blog (~10k words): <a href="https://nikhiljain180.github.io/AI-series/articles/01-not-all-vectors-equal.html">Part 1</a> · <a href="https://nikhiljain180.github.io/AI-series/articles/01b-embeddings-deep-dive.html">Part 2</a> · <a href="https://nikhiljain180.github.io/AI-series/articles/01c-supplement-scenarios.html">Part 3</a></div>
      <a class="lesson" href="https://nikhiljain180.github.io/AI-series/articles/01-not-all-vectors-equal.html">1. Not all vectors are equal</a>
      <p class="teach">Chunking (fixed, semantic, hierarchical) and embedding models—explained for students and production engineers. Start with Part 1.</p>
      <a class="export" href="https://nikhiljain180.github.io/AI-series/01_not_all_vectors_are_equal_embedding_choice.html">Notebook HTML export →</a>
      <a class="github" href="https://github.com/Nikhiljain180/AI-series/blob/main/01_not_all_vectors_are_equal_embedding_choice.ipynb">Run on GitHub →</a>
    </li>
    <li>
      <div class="blog-row">Blog (~10k words): <a href="https://nikhiljain180.github.io/AI-series/articles/02-right-chunk-wrong-context.html">Part 1</a> · <a href="https://nikhiljain180.github.io/AI-series/articles/02b-structural-chunking-deep-dive.html">Part 2</a> · <a href="https://nikhiljain180.github.io/AI-series/articles/02c-supplement-scenarios.html">Part 3</a></div>
      <a class="lesson" href="https://nikhiljain180.github.io/AI-series/articles/02-right-chunk-wrong-context.html">2. The right chunk, wrong context</a>
      <p class="teach">Structural chunking, boundaries, and why “relevant” fragments still miss the exception clause. Start with Part 1; run the notebook for code.</p>
      <a class="export" href="https://nikhiljain180.github.io/AI-series/02_right_chunk_wrong_context_structural_chunking.html">Notebook HTML export →</a>
      <a class="github" href="https://github.com/Nikhiljain180/AI-series/blob/main/02_right_chunk_wrong_context_structural_chunking.ipynb">Run on GitHub →</a>
    </li>
    <li>
      <div class="blog-row">Blog (~10k words): <a href="https://nikhiljain180.github.io/AI-series/articles/03-hybrid-search-bm25-vectors.html">Part 1</a> · <a href="https://nikhiljain180.github.io/AI-series/articles/03b-fusion-logging-and-regressions.html">Part 2</a> · <a href="https://nikhiljain180.github.io/AI-series/articles/03c-supplement-scenarios.html">Part 3</a></div>
      <a class="lesson" href="https://nikhiljain180.github.io/AI-series/articles/03-hybrid-search-bm25-vectors.html">3. When dense search misses keywords</a>
      <p class="teach">Hybrid BM25 + vectors, fusion (RRF), and logging which leg saved the query. Start with Part 1.</p>
      <a class="export" href="https://nikhiljain180.github.io/AI-series/03_when_dense_search_misses_keywords_hybrid_bm25.html">Notebook HTML export →</a>
      <a class="github" href="https://github.com/Nikhiljain180/AI-series/blob/main/03_when_dense_search_misses_keywords_hybrid_bm25.ipynb">Run on GitHub →</a>
    </li>
    <li>
      <div class="blog-row">Blog (~10k words): <a href="https://nikhiljain180.github.io/AI-series/articles/04-cross-encoder-reranking.html">Part 1</a> · <a href="https://nikhiljain180.github.io/AI-series/articles/04b-latency-cost-and-candidates.html">Part 2</a> · <a href="https://nikhiljain180.github.io/AI-series/articles/04c-supplement-scenarios.html">Part 3</a></div>
      <a class="lesson" href="https://nikhiljain180.github.io/AI-series/articles/04-cross-encoder-reranking.html">4. Cross-encoder reranking</a>
      <p class="teach">Retrieve wide, rerank narrow: quality vs latency vs GPU memory. Start with Part 1.</p>
      <a class="export" href="https://nikhiljain180.github.io/AI-series/04_cross_encoder_rerank_cost_vs_quality.html">Notebook HTML export →</a>
      <a class="github" href="https://github.com/Nikhiljain180/AI-series/blob/main/04_cross_encoder_rerank_cost_vs_quality.ipynb">Run on GitHub →</a>
    </li>
    <li>
      <div class="blog-row">Blog (~10k words): <a href="https://nikhiljain180.github.io/AI-series/articles/05-acl-at-query-time.html">Part 1</a> · <a href="https://nikhiljain180.github.io/AI-series/articles/05b-filters-audits-and-threats.html">Part 2</a> · <a href="https://nikhiljain180.github.io/AI-series/articles/05c-supplement-scenarios.html">Part 3</a></div>
      <a class="lesson" href="https://nikhiljain180.github.io/AI-series/articles/05-acl-at-query-time.html">5. ACL at query time</a>
      <p class="teach">Enforce authorization in retrieval—filters, audits, cross-tenant tests. Start with Part 1.</p>
      <a class="export" href="https://nikhiljain180.github.io/AI-series/05_acl_at_query_time_why_rag_leaks_or_blocks_wrong.html">Notebook HTML export →</a>
      <a class="github" href="https://github.com/Nikhiljain180/AI-series/blob/main/05_acl_at_query_time_why_rag_leaks_or_blocks_wrong.ipynb">Run on GitHub →</a>
    </li>
    <li>
      <div class="blog-row">Blog (~10k words): <a href="https://nikhiljain180.github.io/AI-series/articles/06-semantic-cache-invalidation.html">Part 1</a> · <a href="https://nikhiljain180.github.io/AI-series/articles/06b-metrics-and-two-tier-caching.html">Part 2</a> · <a href="https://nikhiljain180.github.io/AI-series/articles/06c-supplement-scenarios.html">Part 3</a></div>
      <a class="lesson" href="https://nikhiljain180.github.io/AI-series/articles/06-semantic-cache-invalidation.html">6. Semantic cache &amp; invalidation</a>
      <p class="teach">Similarity + version tags, TTL, false hits—cache without lying. Start with Part 1.</p>
      <a class="export" href="https://nikhiljain180.github.io/AI-series/06_semantic_cache_similarity_ttl_and_invalidation.html">Notebook HTML export →</a>
      <a class="github" href="https://github.com/Nikhiljain180/AI-series/blob/main/06_semantic_cache_similarity_ttl_and_invalidation.ipynb">Run on GitHub →</a>
    </li>
    <li>
      <div class="blog-row">Blog (~10k words): <a href="https://nikhiljain180.github.io/AI-series/articles/07-stale-index-tombstones.html">Part 1</a> · <a href="https://nikhiljain180.github.io/AI-series/articles/07b-incremental-updates-and-ops.html">Part 2</a> · <a href="https://nikhiljain180.github.io/AI-series/articles/07c-supplement-scenarios.html">Part 3</a></div>
      <a class="lesson" href="https://nikhiljain180.github.io/AI-series/articles/07-stale-index-tombstones.html">7. Stale index &amp; tombstones</a>
      <p class="teach">Incremental updates, stable IDs, deletes, ingestion lag. Start with Part 1.</p>
      <a class="export" href="https://nikhiljain180.github.io/AI-series/07_stale_index_incremental_updates_and_tombstones.html">Notebook HTML export →</a>
      <a class="github" href="https://github.com/Nikhiljain180/AI-series/blob/main/07_stale_index_incremental_updates_and_tombstones.ipynb">Run on GitHub →</a>
    </li>
    <li>
      <div class="blog-row">Blog (~10k words): <a href="https://nikhiljain180.github.io/AI-series/articles/08-faithfulness-and-grounding.html">Part 1</a> · <a href="https://nikhiljain180.github.io/AI-series/articles/08b-layered-guards-and-rubrics.html">Part 2</a> · <a href="https://nikhiljain180.github.io/AI-series/articles/08c-supplement-scenarios.html">Part 3</a></div>
      <a class="lesson" href="https://nikhiljain180.github.io/AI-series/articles/08-faithfulness-and-grounding.html">8. Grounded or confidently wrong</a>
      <p class="teach">Cheap faithfulness checks, abstention, and rubrics—before the LLM sounds sure. Start with Part 1.</p>
      <a class="export" href="https://nikhiljain180.github.io/AI-series/08_grounded_or_confidently_wrong_faithfulness_checks.html">Notebook HTML export →</a>
      <a class="github" href="https://github.com/Nikhiljain180/AI-series/blob/main/08_grounded_or_confidently_wrong_faithfulness_checks.ipynb">Run on GitHub →</a>
    </li>
    <li>
      <div class="blog-row">Blog (~10k words): <a href="https://nikhiljain180.github.io/AI-series/articles/09-rag-evaluation-metrics.html">Part 1</a> · <a href="https://nikhiljain180.github.io/AI-series/articles/09b-golden-sets-and-slicing.html">Part 2</a> · <a href="https://nikhiljain180.github.io/AI-series/articles/09c-supplement-scenarios.html">Part 3</a></div>
      <a class="lesson" href="https://nikhiljain180.github.io/AI-series/articles/09-rag-evaluation-metrics.html">9. RAG is not one metric</a>
      <p class="teach">Recall@k, slicing, golden sets—retrieval vs generation eval. Start with Part 1.</p>
      <a class="export" href="https://nikhiljain180.github.io/AI-series/09_rag_is_not_one_metric_retrieval_and_generation_eval.html">Notebook HTML export →</a>
      <a class="github" href="https://github.com/Nikhiljain180/AI-series/blob/main/09_rag_is_not_one_metric_retrieval_and_generation_eval.ipynb">Run on GitHub →</a>
    </li>
    <li>
      <div class="blog-row">Blog (~10k words): <a href="https://nikhiljain180.github.io/AI-series/articles/10-prompt-injection-pii.html">Part 1</a> · <a href="https://nikhiljain180.github.io/AI-series/articles/10b-layered-defenses-and-ux.html">Part 2</a> · <a href="https://nikhiljain180.github.io/AI-series/articles/10c-supplement-scenarios.html">Part 3</a></div>
      <a class="lesson" href="https://nikhiljain180.github.io/AI-series/articles/10-prompt-injection-pii.html">10. Prompt injection &amp; PII</a>
      <p class="teach">Untrusted chunks, layered defenses, PII boundaries. Start with Part 1.</p>
      <a class="export" href="https://nikhiljain180.github.io/AI-series/10_prompt_injection_and_pii_boundary_for_rag_apps.html">Notebook HTML export →</a>
      <a class="github" href="https://github.com/Nikhiljain180/AI-series/blob/main/10_prompt_injection_and_pii_boundary_for_rag_apps.ipynb">Run on GitHub →</a>
    </li>
  </ol>

  <footer>
    <p>Nikhil Jain — <a href="https://www.linkedin.com/in/nikhiljain180/">LinkedIn</a> · <a href="https://github.com/Nikhiljain180/AI-series">Repository</a></p>
  </footer>
</div>
