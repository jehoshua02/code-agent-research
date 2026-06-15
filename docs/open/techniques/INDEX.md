# Techniques — Index

| Technique | Problem | Notes |
|---|---|---|
| [Chain-of-thought](chain-of-thought.md) | LLMs jump directly to answers by pattern-matching, producing confidently wrong results on multi-step reasoning tasks | _stub_ |
| [Constrained decoding (JSON mode, grammar)](constrained-decoding.md) | LLMs generate free-form text that may not conform to required schemas, causing downstream parse failures that require expensive retry logic | Requires access to token logits at inference time; not available via standard hosted chat-completion APIs without a structured-output wrapper |
| [Few-shot / in-context learning](few-shot.md) | Zero-shot prompts rely on the model's internal priors, producing inconsistent or off-format output for tasks with unusual schemas or domain conventions | _stub_ |
| [KV cache reuse](kv-cache-reuse.md) | In multi-turn conversations and agentic loops, the model recomputes key-value attention tensors for unchanged prefix tokens on every request, wasting GPU compute | Automatic in production runtimes; agent developers benefit by keeping prompt prefixes stable |
| [Plan-and-execute](plan-and-execute.md) | Step-by-step agents decide what to do next based only on the most recent observation, so they drift from the original goal on long tasks | _stub_ |
| [Prompt caching](prompt-caching.md) | A large static system prompt sent on every request in an agentic loop is billed at full input-token rates, making high-frequency loops expensive | Cache TTL is ~5 minutes on Anthropic; any prefix change causes a full cache miss |
| [RAG (retrieval-augmented generation)](rag.md) | LLMs have no access to private, domain-specific, or recently updated information beyond their training cutoff | _stub_ |
| [ReAct](react.md) | An LLM acting in a loop has no mechanism to verify intermediate steps, so errors compound silently without real-world feedback | _stub_ |
| [Reflection](reflection.md) | LLMs produce errors silently with no feedback loop, so the same mistake recurs and cannot be corrected within a session | _stub_ |
| [Self-consistency](self-consistency.md) | A single chain-of-thought sample can follow a plausible but incorrect reasoning path and return a confident wrong answer | Multiplies inference cost by N samples; only justified when accuracy is the top priority |
| [Speculative decoding](speculative-decoding.md) | Autoregressive decoding generates one token per full model forward pass, making large model generation slow and memory-bandwidth-bound | Infrastructure concern; cannot be configured from a prompt or API call |
| [Tool use / function calling](tool-use.md) | LLMs have a frozen knowledge cutoff and no mechanism to take actions or read live state, so they fabricate answers or refuse real-world tasks | _stub_ |
| [Tree-of-thought](tree-of-thought.md) | Chain-of-thought reasoning is strictly linear, so a wrong turn early in a multi-step problem taints the entire chain with no way to backtrack | Expensive in tokens and LLM calls; most production systems prefer simpler heuristics |
