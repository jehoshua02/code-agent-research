---
name: "RAG (retrieval-augmented generation)"
license_category: "n/a"
status: "active"
url: "https://arxiv.org/abs/2005.11401"
last_verified: "2026-06-14"
applies_at: "framework"
problem: "LLMs have no access to private, domain-specific, or recently updated information beyond their training cutoff"
best_for: ["research", "data", "automation"]
notes: ""
---

# RAG (retrieval-augmented generation)

_Last verified: 2026-06-14_

## 0. TL;DR

RAG (retrieval-augmented generation) is the best-known way to give an LLM access to private or recent knowledge: before the model answers, your app searches a document store and pastes the relevant excerpts into the prompt. Use it when the model's training data doesn't cover your domain — internal docs, recent news, proprietary data. The main catch: answer quality is only as good as retrieval quality; if the wrong chunks are fetched, the model confidently answers from the wrong source.

## 1. What It Is

Retrieval-augmented generation grounds LLM responses by retrieving relevant documents from an external store (typically vector-indexed) at inference time and feeding them as context. Introduced by Lewis et al. (2020). Reduces hallucination and lets the model answer about information not in its training data.

## 2. Problem It Solves

LLMs encode knowledge only up to their training cutoff and have no access to private, domain-specific, or recently updated information. Without RAG, a model answering questions about a company's internal documentation or last week's news must either hallucinate a plausible-sounding answer or refuse. The longer the gap between training and deployment, the worse this gets.

## 3. How It Works

At query time, the user's question is embedded into a vector, and a similarity search retrieves the top-K most relevant chunks from a document store. Those chunks are prepended to the prompt as context before the model generates a response. The model never searches the store itself — the retrieval step is handled by the application layer. Introduced by Lewis et al. 2022.

```
query_vec = embed(user_query)
docs = vector_store.search(query_vec, top_k=5)
prompt = system_prompt + format(docs) + user_query
response = llm(prompt)
```

## 4. When To Use

Use RAG when the target knowledge is too large to fit in the context window, changes frequently (product catalogs, news, internal wikis), or is private and was never in the model's training data. It is the standard solution for domain-specific Q&A over large corpora.

## 5. When Not To Use

Skip RAG when the fact set is small and static enough to fit directly in the context window, when retrieval latency is unacceptable, or when your retrieval pipeline produces low-quality results (wrong chunks surface and mislead the model more than no context would). Poor retrieval quality is a common failure mode that can make answers worse than zero-shot.

## 6. Implementations

- **LangChain** — `RetrievalQA` and `create_retrieval_chain` wrappers with pluggable vector stores
- **LlamaIndex** — `VectorStoreIndex` with `as_query_engine()`; strong document ingestion pipeline
- **Haystack** — `DocumentStore` + `Retriever` + `Reader` pipeline, production-focused
- **bare retrieval + any LLM API** — embed with OpenAI or a local model, search with Pinecone / Chroma / pgvector, assemble prompt manually

## 7. Sources

- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (Lewis et al., 2020)](https://arxiv.org/abs/2005.11401) — observed 2026-06-14
