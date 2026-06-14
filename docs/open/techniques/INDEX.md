# Techniques — Index

| Technique | Problem | Notes |
|---|---|---|
| [RAG](rag.md) | LLM knowledge is frozen at training and lacks private/current information | Best for large/dynamic/private corpora; not for small static fact sets or latency-critical paths |
| [ReAct](react.md) | Pure reasoning hallucinates; pure tool use lacks reasoning to guide actions | Best for multi-step tool-using tasks; not for single-turn or latency-critical calls |
| [Plan-and-execute](plan-and-execute.md) | Single-step agents lose track of long multi-step tasks without an explicit plan | Best for long-horizon auditable tasks; not for dynamic environments or simple single-step work |
| [Chain-of-thought](chain-of-thought.md) | Models skip intermediate steps and fail multi-step reasoning without prompting | Best for math, logic, multi-step reasoning; not for simple lookups or latency-critical paths |
| [Tree-of-thought](tree-of-thought.md) | Linear reasoning chains cannot backtrack when an early step is wrong | Best for discrete planning and puzzles with verifiable states; not for open-ended or cost-sensitive tasks |
| [Tool use / function calling](tool-use.md) | LLMs cannot take actions or fetch live data without external tool access | Best for live data, computation, and side effects; not for pure text generation |
| [Self-consistency](self-consistency.md) | Greedy or beam-search decoding is brittle on reasoning tasks | Best for discrete-answer accuracy when cost is flexible; not for open-ended generation or tight budgets |
| [Reflection](reflection.md) | Agents repeat mistakes without a mechanism to learn from failure | Best for code generation and verifiable tasks with clear critique signals; not for latency-critical or simple tasks |
| [Prompt caching](prompt-caching.md) | Reprocessing the same large prefix on every request wastes compute and latency | Best for long repeated system prompts in agentic loops; not when prompts change every turn |
| [Few-shot / in-context learning](few-shot.md) | Zero-shot prompts give no format or style guidance without training | Best for unusual output formats and schemas; not when examples are poor quality or context is too short |
| [Constrained decoding](constrained-decoding.md) | LLMs output malformed JSON or invalid structures that break downstream parsers | Best for guaranteed schema-valid output; not for creative tasks or when native JSON mode suffices |
| [Speculative decoding](speculative-decoding.md) | Autoregressive token-by-token generation underutilizes parallel hardware | Best for low-latency interactive inference with a good draft model; not for high-throughput batch serving |
| [KV cache reuse](kv-cache-reuse.md) | Recomputing attention states for repeated prefixes wastes compute | Best for multi-turn chat and agentic loops with long shared context; not for single-turn or memory-constrained deployments |
