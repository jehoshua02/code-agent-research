---
name: "Prompt caching"
license_category: "n/a"
status: "active"
url: "https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching"
last_verified: "2026-06-14"
applies_at: "runtime"
problem: "A large static system prompt sent on every request in an agentic loop is billed at full input-token rates, making high-frequency loops expensive"
best_for: ["automation", "data", "research"]
notes: "Cache TTL is ~5 minutes on Anthropic; any prefix change causes a full cache miss"
---

# Prompt caching

_Last verified: 2026-06-14_

## 0. TL;DR

Prompt caching is a runtime-level optimization where the provider saves the processed state of a long, repeated prompt prefix — system prompt, tool definitions, documents — so subsequent requests reuse it at a fraction of the cost. Use it when your agent sends the same large system prompt or context on every turn, which is nearly always. The main catch: caching is tied to an exact prefix match with a short TTL (around 5 minutes on Anthropic), so any change to the prefix before the TTL expires causes a full cache miss.

## 1. What It Is

Prompt caching has the provider cache the server-side key-value state for a static prompt prefix and reuse it across requests, paying full compute only on cache misses. Reduces both cost and latency for repeated long prefixes. Available in Anthropic and OpenAI APIs and in some self-hosted runtimes.

## 2. Problem It Solves

In agentic loops and multi-turn conversations, a large static system prompt — tool definitions, background documents, persona instructions — is sent on every request and billed at full input-token rates. This makes high-frequency loops expensive: a 10,000-token system prompt sent 100 times costs 1 million input tokens even though the content never changed.

## 3. How It Works

The provider computes and caches the key-value attention state for a designated prompt prefix after the first request. On subsequent requests that share the same prefix, the provider skips recomputation and serves the cached state at a reduced price (Anthropic charges ~10% of normal input price for cache reads). The developer marks cache breakpoints explicitly (Anthropic `cache_control` parameter) or the provider handles caching automatically (OpenAI). Cache entries have a TTL (typically 5 minutes on Anthropic, longer on OpenAI) and are invalidated when the prefix changes.

## 4. When To Use

Use prompt caching when a large static block — system prompt, tool list, retrieved documents — appears at the start of many requests in a short time window. It is especially valuable in agentic loops, multi-turn chat with a long persona, and document Q&A where the same document is queried repeatedly.

## 5. When Not To Use

Prompt caching provides no benefit when the prompt changes significantly on every request, because the prefix never matches and the cache is never hit. It is also ineffective when the interval between requests exceeds the cache TTL, or when the prompt is too short for the cache overhead to matter. Not all providers support it — verify before designing around it.

## 6. Implementations

- **Anthropic API** — `cache_control: {"type": "ephemeral"}` breakpoint on `system`, `user`, or `tool` content blocks; 5-minute TTL by default
- **OpenAI API** — automatic prompt caching for prompts over 1,024 tokens; no explicit markup required
- **Google Gemini** — explicit context caching API (`cachedContents`) with configurable TTL

## 7. Sources

- [Anthropic Prompt Caching documentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) — observed 2026-06-14
