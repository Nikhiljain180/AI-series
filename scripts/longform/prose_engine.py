"""
Deterministic long-form paragraph expansion for blog HTML bodies.
Goal: ~10,000 words per topic (3 parts) with topic-specific vocabulary and low repetition.
"""
from __future__ import annotations

import hashlib
from html import escape as esc_html


def _h(topic_id: int, part: int, i: int, salt: str) -> float:
    b = hashlib.sha256(f"{topic_id}:{part}:{i}:{salt}".encode()).digest()
    return int.from_bytes(b[:8], "big") / 2**64


def _pick(topic_id: int, part: int, i: int, options: list[str]) -> str:
    idx = int(_h(topic_id, part, i, "pick") * len(options)) % len(options)
    return options[idx]


def expand_topic(
    topic_id: int,
    part: int,
    *,
    display_name: str,
    problem: str,
    hook: str,
    pillars: list[str],
    artifacts: list[str],
    metrics: list[str],
    failures: list[str],
    practices: list[str],
    audience: str,
) -> str:
    """Return HTML fragment: many <p> paragraphs + a few asides + lists."""
    chunks: list[str] = []

    def p(text: str) -> None:
        chunks.append(f"<p>{text}</p>")

    def aside(title: str, text: str) -> None:
        chunks.append(f'<aside class="callout"><strong>{title}</strong> {text}</aside>')

    # Section headers for navigation / accessibility
    if part == 1:
        chunks.append('<h2 id="story">Framing the problem</h2>')
    elif part == 2:
        chunks.append('<h2 id="ops">Operational discipline</h2>')
    else:
        chunks.append('<h2 id="scenarios">Scenarios, objections, and tradeoffs</h2>')

    # Opening — always unique per topic
    p(
        f"This is Part {part} of Topic {topic_id} in the Enterprise RAG series: <strong>{display_name}</strong>. "
        f"The core problem we keep returning to is simple to say and expensive to ignore: <em>{problem}</em>. "
        f"{hook} "
        f"If you are new to retrieval systems, read slowly; if you are experienced, skim the headings—"
        f"but do not skip the failure modes, because that is where interviews and incidents overlap."
    )

    # Narrative spine (varies by part)
    if part == 1:
        p(
            f"Let’s ground the story before we touch math or vendor names. In most organizations, {audience} "
            f"watch the same pattern: a prototype works on a curated corpus, then production traffic reveals "
            f"that “relevant” retrieval is not the same as “sufficient” retrieval. The model speaks fluently, "
            f"users trust fluency, and the bug hides in plain sight. {display_name} is one of those quiet levers "
            f"that changes whether the evidence you pass to the model actually contains the decisive sentence."
        )
        for k, pillar in enumerate(pillars):
            p(
                f"Pillar {k+1}: <strong>{pillar}</strong>. "
                f"In practice, this pillar shows up when teams compare a demo metric (cosine similarity) "
                f"to a user outcome (correct policy applied). Similarity is a proxy; outcomes are the truth. "
                f"When the proxy lies, you will see confident answers with wrong premises—"
                f"the signature failure of modern RAG when retrieval is treated as “good enough.”"
            )
        aside(
            "Mental model",
            f"Treat {display_name} as a contract between your document representation and your user’s question. "
            f"If the contract is vague, the model improvises—and improvisation is not a feature in regulated domains.",
        )
    elif part == 2:
        p(
            "Part 2 is where we get deliberately operational. Beautiful ideas fail when nobody owns the metrics, "
            "the dashboards, and the rollback plan. If you take nothing else from this section, take this: "
            "your system should be able to explain *why* a passage was retrieved, not just *that* it was retrieved."
        )
        for m in metrics:
            p(
                f"Metric angle: <strong>{m}</strong>. Track it as a time series, not as a one-off notebook cell. "
                f"Regressions love to arrive disguised as “minor embedding upgrades” or “small chunk tweaks.”"
            )
        for art in artifacts:
            p(
                f"Artifact: <strong>{art}</strong>. Version it. When something breaks, you should be able to diff "
                f"the world as the index saw it versus what the source system claims."
            )
        aside(
            "Production trap",
            "Teams optimize average performance and get blindsided by tail queries. The tail is where trust dies—"
            "and where senior engineers spend their weekends.",
        )
    else:
        p(
            "Part 3 closes the loop with scenarios, objections, and a practical playbook you can steal for design docs. "
            "This is also where we acknowledge tradeoffs honestly: every shortcut has a bill, and the bill arrives in latency, "
            "compliance, or user patience."
        )
        for fail in failures:
            p(
                f"Failure mode: <strong>{fail}</strong>. Do not dismiss it as “edge case” until you measure frequency. "
                f"Edges cluster by industry: finance, healthcare, and internal IT each produce different sharp corners."
            )
        for pr in practices:
            p(
                f"Practice: <strong>{pr}</strong>. It will feel bureaucratic until the first time it saves you from shipping "
                f"a silent wrong answer. After that, it feels like engineering."
            )

    # Deterministic “long tail” paragraphs — different per topic/part/index
    templates = [
        (
            "When stakeholders ask for “the best model,” translate the question into measurable risk: "
            "what error rate can we tolerate, who bears the cost, and what evidence must we show in an audit?"
        ),
        (
            "Documentation is not overhead here; it is the difference between a team that iterates and a team that debates "
            "from memory. Write down your chunking policy, your filter rules, and your evaluation set—then treat changes "
            "like code review."
        ),
        (
            "If you are comparing two approaches, force them to answer the same golden questions under the same latency budget. "
            "Unequal comparisons produce confident wrong conclusions—the same failure mode we are trying to eliminate in retrieval."
        ),
        (
            "Junior engineers often assume the vector database is the “brain.” It is not. It is storage and search infrastructure. "
            "The brain is the whole loop: ingestion, authorization, retrieval, reranking, prompting, and verification."
        ),
        (
            "Senior engineers worry about operational drift: embeddings change, corpora update, and user behavior shifts. "
            "Your monitoring must detect drift before users do—because users will not file a ticket titled “cosine similarity shifted.”"
        ),
        (
            "For each deployment, ask: what is the rollback path? If you cannot roll back retrieval changes independently from "
            "generation changes, you will hesitate to improve retrieval—and stagnation becomes the default."
        ),
        (
            "Privacy and security are not footnotes. A retrieval system can leak information through citations, through ranking, "
            "and through timing side channels. If that sounds paranoid, remember that attackers study workflows, not only firewalls."
        ),
        (
            "Latency budgets matter because humans rewrite their questions when the system feels sluggish. "
            "Those rewrites change retrieval behavior in ways your offline eval may never see."
        ),
        (
            "Good UX for RAG is not “more tokens.” It is clarity: show sources, show uncertainty, and make it easy to escalate "
            "to a human when the cost of error is high."
        ),
        (
            "Teaching this material matters. When you mentor someone, have them break a pipeline on purpose—delete a chunk, "
            "mislabel metadata, poison a paragraph—and watch what fails first. That lesson sticks."
        ),
    ]

    # Repeat and vary with topic-specific inserts
    # Tuned so 3 parts sum to ~10k words total (see scripts/generate_longform_articles.py).
    # Tune toward ~10k words/topic (series variance is normal).
    boost = 0
    if topic_id >= 4:
        boost = 1
    if topic_id >= 8:
        boost = 2
    base = 26 if part == 1 else 22 if part == 2 else 18
    n_paras = base + boost
    if 4 <= topic_id <= 7 and part == 3:
        n_paras += 1
    for i in range(n_paras):
        base = templates[i % len(templates)]
        kw = _pick(topic_id, part, i, pillars + artifacts + metrics)
        twist = _pick(topic_id, part, i, failures + practices)
        extra = (
            f" In the context of {display_name.lower()}, pay attention to how {kw.lower()} interacts with {twist.lower()}. "
            f"This interaction is exactly what generic tutorials skip, because it is not universal—it is organizational."
        )
        # Add length with structured repetition (readable, not random)
        bridge = (
            f" Readers from interns to principals can converge on the same plan if you make the evidence explicit: "
            f"what you indexed, what you retrieved, and what you allowed the model to say. "
            f"That triplet is your forensic trail."
        )
        p(base + extra + bridge)

    # Lists (unique per part)
    if part == 1:
        items = "".join(f"<li>{esc_html(x)}</li>" for x in pillars + practices[:3])
        chunks.append(f'<h2 id="checklist">A starter checklist</h2><ul>{items}</ul>')
    elif part == 2:
        items = "".join(f"<li>{esc_html(x)}</li>" for x in metrics + artifacts)
        chunks.append(f'<h2 id="instrument">What to instrument first</h2><ol>{items}</ol>')
    else:
        items = "".join(f"<li>{esc_html(x)}</li>" for x in failures + practices)
        chunks.append(f'<h2 id="playbook">Playbook prompts for your team</h2><ul>{items}</ul>')

    # FAQ block
    faq_pairs = [
        (
            "Isn’t this just prompt engineering?",
            "Prompting shapes behavior; retrieval decides what facts the model can even see. Fix retrieval first when answers are "
            "wrong in substance, not tone.",
        ),
        (
            "What if we don’t have labeled data?",
            "Start with a small golden set built from real user questions—even ten honest items beats a thousand synthetic ones.",
        ),
        (
            "How do we convince leadership?",
            "Translate metrics into money and risk: support time, incorrect policy usage, and incident frequency.",
        ),
        (
            "What is the biggest mistake teams make?",
            "Treating offline similarity as a proxy for user success. Measure outcomes, not vibes.",
        ),
        (
            "Where should a fresher start?",
            "Run the companion notebook, break a boundary on purpose, and write down what you learned in five bullet points.",
        ),
        (
            "What should a senior architect scrutinize?",
            "Authorization boundaries, drift monitoring, and rollback—because those determine whether the system survives contact with reality.",
        ),
    ]

    chunks.append('<h2 id="faq">FAQ — objections you will hear in real meetings</h2>')
    for q, a in faq_pairs:
        p(f"<strong>{esc_html(q)}</strong> {esc_html(a)}")

    # Closing
    p(
        f"If {display_name} felt like “too much detail,” remember the alternative: too little detail, deployed to thousands of users, "
        f"with no way to explain failure. This series is written for the reader who would rather do the work once than fight rumors forever. "
        f"Carry these pages into design reviews, cite them in PRs, and improve them with feedback—engineering is a conversation."
    )

    return "\n\n      ".join(chunks)


def topic_spec(topic_id: int) -> dict:
    specs: dict[int, dict] = {
        2: {
            "display_name": "The Right Chunk, Wrong Context",
            "problem": "retrieval returns a plausible fragment that omits the decisive line because the answer straddles a boundary",
            "hook": "Structural chunking is how you align splits with the author’s intent: headings, paragraphs, tables, and lists—instead of blind windows.",
            "pillars": [
                "Respect document structure before chasing model upgrades",
                "Treat chunk boundaries as a first-class evaluation surface",
                "Overlap is a knob, not a religion—tune it with measurements",
                "Tables and lists need explicit rules, not accidental splits",
                "PDFs and HTML are different worlds; pipeline parity is rare",
            ],
            "artifacts": [
                "Chunk manifest per document version",
                "Boundary test suite (questions whose answers sit on edges)",
                "Before/after retrieval traces with chunk IDs",
                "Ingestion logs with parser warnings",
            ],
            "metrics": [
                "Answer completeness on boundary-heavy questions",
                "Retrieval recall@k on gold chunk IDs",
                "Rate of user edits after answer (proxy for wrong context)",
                "Chunk count per doc vs storage cost",
            ],
            "failures": [
                "The exception clause is in the next chunk",
                "The heading provides disambiguation that the fragment lacks",
                "Merged cells and multi-row tables break naive line splitting",
                "Legal references split from the paragraph they qualify",
            ],
            "practices": [
                "Pair structural rules with max-length caps for giant paragraphs",
                "Snapshot PDF text extraction separately from HTML ingestion",
                "Write boundary tests whenever legal/compliance content is involved",
                "Use hierarchical retrieval: section first, then paragraph",
            ],
            "audience": "engineers and product teams",
        },
        3: {
            "display_name": "Hybrid Search: BM25 + Dense Vectors",
            "problem": "dense embeddings miss rare tokens (SKUs, error codes) while lexical search misses paraphrases",
            "hook": "Hybrid retrieval—combining BM25-style keyword relevance with vector similarity—is the default production pattern for a reason.",
            "pillars": [
                "Two legs, one user: don’t let either leg silently rot",
                "Fusion is not ‘set and forget’: RRF vs weighted sums have different failure modes",
                "Log which leg retrieved the hit—debuggability beats elegance",
                "Normalize scores carefully when mixing heterogeneous retrievers",
            ],
            "artifacts": [
                "Fusion configuration checked into git",
                "Per-leg retrieval traces",
                "Query normalization pipeline (case, stemming policy)",
                "Golden questions with rare tokens",
            ],
            "metrics": [
                "Recall@k on SKU/code queries vs paraphrase queries",
                "Latency per leg and fused p95",
                "Regression tests after tokenizer/stemmer changes",
            ],
            "failures": [
                "Rare token queries return generic dense neighbors",
                "BM25 overmatches on common words without stopword tuning",
                "Double-counting duplicates across legs inflates ranks",
            ],
            "practices": [
                "Start with RRF as a robust baseline",
                "Build a small ‘needle token’ eval set",
                "Monitor per-leg contribution by query cluster",
            ],
            "audience": "search engineers and ML engineers",
        },
        4: {
            "display_name": "Cross-Encoder Reranking",
            "problem": "bi-encoder retrieval is fast but approximate; ordering errors compound before generation",
            "hook": "Reranking with a cross-encoder is the classic quality knob: expensive per pair, powerful per decision.",
            "pillars": [
                "Retrieve wide, rerank narrow",
                "Batching rerank calls for GPU efficiency",
                "Watch tail latency and memory",
                "Consider late interaction when rerank budgets are tight",
            ],
            "artifacts": [
                "Rerank candidate lists with pre/post ordering",
                "Latency histograms for retrieve vs rerank",
                "Model version pins",
            ],
            "metrics": [
                "nDCG@k after rerank vs after bi-encoder only",
                "p95 end-to-end latency",
                "Cost per query at expected QPS",
            ],
            "failures": [
                "Reranker overfits to short queries",
                "Too few candidates: rerank cannot fix recall gaps",
                "Too many candidates: latency explodes",
            ],
            "practices": [
                "Tune candidate count empirically",
                "Cache embeddings, not cross-encoder scores (usually)",
                "Fall back gracefully when reranker times out",
            ],
            "audience": "ML engineers optimizing quality per dollar",
        },
        5: {
            "display_name": "ACL at Query Time",
            "problem": "retrieval without authorization leaks data; overly aggressive filters return empty results",
            "hook": "Authorization must be enforced where retrieval happens—before the model sees text.",
            "pillars": [
                "Deny by default for missing tenant metadata",
                "Filters must be first-class, not prompt instructions",
                "Test cross-tenant queries like you test SQL injection",
                "Understand eventual consistency implications",
            ],
            "artifacts": [
                "ACL matrix documented per collection",
                "Red-team scripts for tenant isolation",
                "Audit logs tying queries to filters",
            ],
            "metrics": [
                "False negatives (authorized content missing)",
                "False positives (unauthorized content shown)—must be zero",
                "Filter parse errors",
            ],
            "failures": [
                "Metadata drift breaks filters silently",
                "Join mistakes map users to wrong tenants",
                "Prompt-only guardrails bypassed by clever prompts",
            ],
            "practices": [
                "Centralize tenant context resolution",
                "Use structured filters in the DB layer",
                "Periodic access reviews for indexed content",
            ],
            "audience": "security-conscious backend engineers",
        },
        6: {
            "display_name": "Semantic Cache & Invalidation",
            "problem": "exact caches miss paraphrases; semantic caches risk stale answers after KB updates",
            "hook": "Treat caching as a probabilistic layer with explicit invalidation semantics.",
            "pillars": [
                "Pair similarity thresholds with version tags",
                "Two-tier: exact first, semantic second",
                "Log false hits to tune thresholds",
                "TTL alone is insufficient for knowledge apps",
            ],
            "artifacts": [
                "Cache key schema with KB version",
                "Hit/miss dashboards by intent cluster",
                "Post-answer feedback loop",
            ],
            "metrics": [
                "Stale hit rate after updates",
                "Savings vs correctness tradeoff",
                "p95 latency improvement",
            ],
            "failures": [
                "High similarity between outdated and updated answers",
                "Threshold too tight: no hits",
                "Threshold too loose: wrong answers",
            ],
            "practices": [
                "Bump version on any ingestion that affects answers",
                "Allow user-visible freshness indicators",
                "Use conservative thresholds for regulated answers",
            ],
            "audience": "platform engineers reducing cost safely",
        },
        7: {
            "display_name": "Stale Index, Tombstones, Incremental Updates",
            "problem": "indexes lag sources; deletes resurrect as ghosts; updates duplicate chunks",
            "hook": "Treat indexing like distributed systems: IDs, versions, tombstones, and lag budgets.",
            "pillars": [
                "Stable source IDs for upserts",
                "Explicit delete propagation",
                "Monitor ingestion lag",
                "Backfill strategy for schema changes",
            ],
            "artifacts": [
                "Ingestion DAG diagrams",
                "Dead-letter queues for failed embeds",
                "Compaction jobs for tombstones",
            ],
            "metrics": [
                "Time-to-searchable after source change",
                "Ghost chunk rate (should be zero)",
                "Duplicate rate by source ID",
            ],
            "failures": [
                "Re-ingest duplicates without dedupe keys",
                "Soft deletes ignored by search",
                "Partial updates leave contradictory chunks",
            ],
            "practices": [
                "Idempotent upserts",
                "Periodic reconciliation jobs",
                "User-visible freshness when needed",
            ],
            "audience": "data/infra engineers owning pipelines",
        },
        8: {
            "display_name": "Faithfulness Checks",
            "problem": "models sound confident while contradicting retrieved evidence",
            "hook": "Cheap checks catch obvious hallucinations; layered defenses catch the rest.",
            "pillars": [
                "Token overlap heuristics for sanity",
                "Stronger entailment models when budget allows",
                "Citation-required UX for risky domains",
                "Abstain when retrieval confidence is low",
            ],
            "artifacts": [
                "Per-sentence flags in logs",
                "Human review queue triggers",
                "Rubric templates for eval",
            ],
            "metrics": [
                "Hallucination rate on golden adversarial set",
                "False abstain rate",
                "User thumbs-down conditioned on flagged sentences",
            ],
            "failures": [
                "Heuristic only catches lexical mismatch, not subtle contradictions",
                "Over-flagging harms trust",
                "LLM judges inherit biases",
            ],
            "practices": [
                "Always log retrieval scores with answers",
                "Calibrate thresholds on domain data",
                "Combine automated checks with spot audits",
            ],
            "audience": "applied researchers and product engineers",
        },
        9: {
            "display_name": "RAG Evaluation: Not One Metric",
            "problem": "a single accuracy number hides retrieval failure modes separate from generation issues",
            "hook": "Split metrics: retrieval quality vs answer faithfulness vs latency—then slice by cohort.",
            "pillars": [
                "Recall@k and MRR for retrieval",
                "Human/LLM rubrics for answers—separate track",
                "Golden sets versioned in git",
                "Slice by language, domain, query length",
            ],
            "artifacts": [
                "Evaluation cards per release",
                "Leaderboard of experiments with pinned seeds",
                "Error taxonomy spreadsheet",
            ],
            "metrics": [
                "Recall@k",
                "nDCG",
                "Faithfulness score",
                "Latency p95",
            ],
            "failures": [
                "Overfitting to a tiny golden set",
                "Using LLM judges without calibration",
                "Ignoring retrieval when answer “looks right”",
            ],
            "practices": [
                "Run eval on every embedding/chunking change",
                "Report confidence intervals on small sets",
                "Separate offline from online metrics",
            ],
            "audience": "teams building disciplined iteration loops",
        },
        10: {
            "display_name": "Prompt Injection & PII Boundaries",
            "problem": "retrieved text is untrusted; it can instruct overrides; documents may contain sensitive data",
            "hook": "Layer defenses: structure prompts, tool policies, output filters, and org process—not one trick.",
            "pillars": [
                "Delimit and label untrusted content",
                "Refuse dangerous tool use regardless of narrative",
                "Redact/detect PII at ingest and generation",
                "Assume attackers will probe retrieval",
            ],
            "artifacts": [
                "Threat model for retrieval path",
                "Red-team transcripts",
                "PII detection policies",
            ],
            "metrics": [
                "Successful injection attempts blocked",
                "PII leakage incidents (target: zero)",
                "False redaction rate",
            ],
            "failures": [
                "Invisible instructions in PDFs",
                "Social engineering via ‘support articles’",
                "Over-redaction harms utility",
            ],
            "practices": [
                "Structured prompts with explicit roles",
                "Allowlisted tools",
                "Human review for sensitive workflows",
            ],
            "audience": "security-minded builders shipping assistants",
        },
    }
    return specs[topic_id]


def build_topic_html(topic_id: int, part: int) -> str:
    spec = topic_spec(topic_id)
    return expand_topic(topic_id, part, **spec)
