# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

RAG (Retrieval-Augmented Generation) playground comparing three retrieval methods — BM25, Vector, and Hybrid — on a Wikipedia dataset (3,200 passages, 918 QA pairs). Educational assignment from YBIGTA.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit UI
streamlit run app/streamlit_app.py

# Download dataset directly
python data/download.py
```

No test suite exists. Verification is done through the Streamlit UI's Search Playground and RAG Test tabs.

## Architecture

Four-stage pipeline: **Download → Embed/Index → Retrieve → Generate**

```
data/download.py          → data/raw/corpus.jsonl, qa.jsonl
ingest/embedding.py       → data/processed/embeddings.npy, embedding_ids.json
ingest/elastic/ingest.py  → Elasticsearch index "wiki-bm25" (text only)
ingest/pinecone/ingest.py → Pinecone index "ragsession" (vectors only)
ingest/hybrid/ingest.py   → Elasticsearch index "wiki-hybrid" (text + vectors)
retrievers/elastic/       → BM25 keyword search
retrievers/pinecone/      → Vector cosine similarity search
retrievers/hybrid/        → RRF (Reciprocal Rank Fusion) combining BM25 + kNN
app/llm.py                → Solar LLM answer generation (solar-mini, OpenAI-compatible)
app/streamlit_app.py      → UI with 3 tabs: Data Management, Search Playground, RAG Test
```

## Key Constants

- Embedding dimension: 4096 (Upstage Solar `solar-embedding-1-large-passage/query`)
- Embedding batch size: 100, max chars per passage: 12,000
- Pinecone metadata text truncated to 1,000 chars
- Elasticsearch BM25 bulk chunk_size: 500; Hybrid chunk_size: 100
- LLM: `solar-mini`, temperature=0, max_tokens=1024
- RRF rank constant: 60

## External Services (configured via `.env`)

- **Upstage Solar API** — embeddings and LLM generation (`UPSTAGE_API_KEY`)
- **Pinecone** — vector database (`PINECONE_API_KEY`, `PINECONE_INDEX`)
- **Elasticsearch Cloud** — BM25 and hybrid indices (`ELASTIC_ENDPOINT`, `ELASTIC_API_KEY`)

## Implementation Status

The project has 9 TODO functions to implement across 4 modules:

1. `ingest/embedding.py` — `embed_passages()`, `embed_query()`
2. `ingest/elastic/ingest.py` — `ingest()`
3. `ingest/pinecone/ingest.py` — `ingest()`
4. `ingest/hybrid/ingest.py` — `ingest()`
5. `retrievers/elastic/retriever.py` — `search()`
6. `retrievers/pinecone/retriever.py` — `search()`
7. `retrievers/hybrid/retriever.py` — `search()`
8. `app/llm.py` — `generate()`

Each function has detailed docstrings and hints in the source code. `data/download.py` and `app/streamlit_app.py` are already complete.

## Retriever Return Format

All retriever `search()` functions must return `list[dict]` with keys: `id`, `text`, `score`, `method` (one of `"bm25"`, `"vector"`, `"hybrid"`).