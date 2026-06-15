# KV cache reuse

_Last verified: 2026-06-14_

## 0. TL;DR

KV cache reuse is a runtime-level optimization where the inference engine stores the intermediate attention computations for already-processed tokens and reuses them on the next request, instead of reprocessing the same prefix from scratch every time. It's automatic in production inference runtimes (vLLM, TGI, etc.) and is what makes [prompt caching](../GLOSSARY.md#prompt-caching) possible at the provider level. The main catch: this is infrastructure plumbing, not an agent technique — as an agent developer, you benefit from it indirectly by keeping prompt prefixes stable.

## 1. What It Is

Key-value attention tensors from already-processed tokens are stored in GPU memory and reused on the next decode step, avoiding redundant recomputation. Cross-request prefix sharing was formalized by Kwon et al. (2023, PagedAttention) and is now standard in production-grade inference runtimes.

## 2. Problem It Solves

In multi-turn conversations and agentic loops, the model processes the same prefix tokens — system prompt, conversation history, shared document — on every request from scratch. Recomputing the key-value attention tensors for thousands of tokens that haven't changed wastes GPU compute and adds directly to response latency, scaling linearly with context length.

## 3. How It Works

After the model processes a sequence of tokens, the resulting key and value tensors for every layer are stored in a cache (GPU memory, or offloaded to CPU). On the next request, if the new input shares a prefix with a cached sequence, those tensors are retrieved directly and computation begins at the first new token. Cross-request prefix sharing was formalized by Kwon et al. 2023 (PagedAttention), which manages KV cache memory in fixed-size pages to eliminate fragmentation and allow fine-grained sharing.

```
# Conceptual flow; the runtime handles this automatically
if prefix_in_cache(input_tokens):
    kv = cache.get(common_prefix)
    new_kv = model.forward(new_tokens_only, past_kv=kv)
else:
    new_kv = model.forward(all_tokens)
cache.store(all_tokens, new_kv)
```

## 4. When To Use

KV cache reuse is most valuable in multi-turn chat (where the conversation history grows across turns), agentic loops where the same long context or tool list is reprocessed on every step, and document Q&A where many questions share the same large document as a prefix.

## 5. When Not To Use

Single-turn requests with no shared prefix get no benefit, since there is nothing to reuse. When GPU memory is already under pressure, caching a large number of KV tensors can evict other cached sequences or reduce the effective batch size. Very short sessions may not amortize the overhead of cache management.

## 6. Implementations

- **vLLM** — PagedAttention manages KV cache automatically across all requests; prefix caching enabled by default from v0.4
- **llama.cpp** — `n_keep` parameter specifies how many tokens to pin in the KV cache across sessions
- **TGI (Text Generation Inference)** — automatic KV cache management per request
- **TensorRT-LLM** — paged KV cache with configurable pool sizes
- **SGLang** — RadixAttention extends prefix sharing across concurrent requests via a radix tree index

## 7. Sources

- [Efficient Memory Management for Large Language Model Serving with PagedAttention (Kwon et al., 2023)](https://arxiv.org/abs/2309.06180) — observed 2026-06-14
