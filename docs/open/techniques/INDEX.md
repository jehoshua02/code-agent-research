# Techniques — Index

| Technique | Problem | Notes |
|---|---|---|
| [RAG](rag.md) | LLM knowledge is frozen at training and lacks private/current information | _stub_ |
| [ReAct](react.md) | Pure reasoning hallucinates; pure tool use lacks reasoning to guide actions | _stub_ |
| [Plan-and-execute](plan-and-execute.md) | Single-step agents lose track of long multi-step tasks without an explicit plan | _stub_ |
| [Chain-of-thought](chain-of-thought.md) | Models skip intermediate steps and fail multi-step reasoning without prompting | _stub_ |
| [Tree-of-thought](tree-of-thought.md) | Linear reasoning chains cannot backtrack when an early step is wrong | _stub_ |
| [Tool use / function calling](tool-use.md) | LLMs cannot take actions or fetch live data without external tool access | _stub_ |
| [Self-consistency](self-consistency.md) | Greedy or beam-search decoding is brittle on reasoning tasks | _stub_ |
| [Reflection](reflection.md) | Agents repeat mistakes without a mechanism to learn from failure | _stub_ |
| [Prompt caching](prompt-caching.md) | Reprocessing the same large prefix on every request wastes compute and latency | _stub_ |
| [Few-shot / in-context learning](few-shot.md) | Zero-shot prompts give no format or style guidance without training | _stub_ |
| [Constrained decoding](constrained-decoding.md) | LLMs output malformed JSON or invalid structures that break downstream parsers | _stub_ |
| [Speculative decoding](speculative-decoding.md) | Autoregressive token-by-token generation underutilizes parallel hardware | _stub_ |
| [KV cache reuse](kv-cache-reuse.md) | Recomputing attention states for repeated prefixes wastes compute | _stub_ |
