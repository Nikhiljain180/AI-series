"""
Shared helpers for the Enterprise RAG notebook series.
Keep notebooks readable; import from here for Chroma paths, chunking, and fusion.
"""

from __future__ import annotations

import hashlib
import os
import re
import uuid

import chromadb
from chromadb.config import Settings

# Default persist dir (per-notebook subdirs avoid collisions)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROMA_ROOT = os.path.join(ROOT, "chroma_data")


def chroma_path(notebook_slug: str) -> str:
    path = os.path.join(CHROMA_ROOT, notebook_slug)
    os.makedirs(path, exist_ok=True)
    return path


def get_client(persist_dir: str) -> chromadb.ClientAPI:
    return chromadb.PersistentClient(
        path=persist_dir,
        settings=Settings(anonymized_telemetry=False),
    )


def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+", text.lower(), flags=re.ASCII)


def chunk_fixed_size(text: str, chunk_size: int = 280, overlap: int = 40) -> list[str]:
    chunks: list[str] = []
    start = 0
    n = len(text)
    while start < n:
        end = min(start + chunk_size, n)
        chunks.append(text[start:end].strip())
        start = end - overlap if end < n else n
    return [c for c in chunks if c]


def chunk_by_paragraphs(text: str, max_chars: int = 500) -> list[str]:
    parts = [p.strip() for p in re.split(r"\n\s*\n+", text) if p.strip()]
    merged: list[str] = []
    buf = ""
    for p in parts:
        if len(buf) + len(p) + 2 <= max_chars:
            buf = f"{buf}\n\n{p}" if buf else p
        else:
            if buf:
                merged.append(buf)
            buf = p
    if buf:
        merged.append(buf)
    return merged


def reciprocal_rank_fusion(
    ranked_lists: list[list[str]],
    k: int = 60,
    top_n: int = 10,
) -> list[tuple[str, float]]:
    scores: dict[str, float] = {}
    for ids in ranked_lists:
        for rank, doc_id in enumerate(ids, start=1):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank)
    ordered = sorted(scores.items(), key=lambda x: -x[1])
    return ordered[:top_n]


def stable_id(*parts: str) -> str:
    h = hashlib.sha256("|".join(parts).encode()).hexdigest()[:16]
    return h


def new_run_id() -> str:
    return str(uuid.uuid4())[:8]
