# View — By License

Open-weight licenses vary in commercial-use freedom, redistribution terms, and downstream restrictions. Each section links to model entries (and other entities) that ship under that license. Verify the current license text on each entity — projects re-license.

## 1. Apache 2.0

_Permissive. Patent grant. Most permissive common open-weight license._

- **Models:** [Qwen](../models/qwen.md) (Qwen3 all sizes), [OLMo](../models/olmo.md), [Granite](../models/granite.md), [SmolLM](../models/smollm.md), [Yi](../models/yi.md) (Yi and Yi-1.5), [Falcon](../models/falcon.md) (Falcon-7B/40B, Falcon3, Falcon-H1/H1R), [Mistral](../models/mistral.md) (Mistral-7B, Mixtral 8x7B/8x22B, NeMo, Small 3.1, Large 3), [Gemma](../models/gemma.md) (Gemma 4 only)
- **Runtimes:** [vLLM](../runtimes/vllm.md), [SGLang](../runtimes/sglang.md), [TGI](../runtimes/tgi.md), [transformers](../runtimes/transformers.md), [llamafile](../runtimes/llamafile.md), [gemma.cpp](../runtimes/gemma-cpp.md)
- **Frameworks:** [CrewAI](../frameworks/crewai.md), [Letta](../frameworks/letta.md), [Smolagents](../frameworks/smolagents.md), [Haystack Agents](../frameworks/haystack-agents.md), [BeeAI](../frameworks/beeai.md), [mcp-agent](../frameworks/mcp-agent.md), [agno](../frameworks/agno.md)
- **Applications:** [Aider](../applications/aider.md), [Continue](../applications/continue.md), [Mentat](../applications/mentat.md), [Goose](../applications/goose.md), [Gemma Gem](../applications/gemma-gem.md)

## 2. MIT

_Permissive. No patent grant. Common for code, less common for weights._

- **Models:** [Phi](../models/phi.md) (all Phi-3, Phi-3.5, Phi-4 variants), [DeepSeek](../models/deepseek.md) (R1 and all R1-Distill variants; V2/V3 use the DeepSeek License)
- **Runtimes:** [llama.cpp](../runtimes/llama-cpp.md), [Ollama](../runtimes/ollama.md), [MLX](../runtimes/mlx.md), [ExLlamaV2](../runtimes/exllamav2.md), [LocalAI](../runtimes/localai.md)
- **Frameworks:** [LangGraph](../frameworks/langgraph.md), [OpenAI Swarm](../frameworks/openai-swarm.md), [LlamaIndex Agents](../frameworks/llamaindex-agents.md), [Pydantic AI](../frameworks/pydantic-ai.md), [DSPy](../frameworks/dspy.md), [Atomic Agents](../frameworks/atomic-agents.md)
- **Applications:** [OpenCode](../applications/opencode.md), [OpenHands](../applications/openhands.md), [AutoGPT](../applications/autogpt.md) (core), [GPT-Engineer](../applications/gpt-engineer.md), [SWE-agent](../applications/swe-agent.md), [OpenClaw](../applications/openclaw.md), [GSD-PI](../applications/gsd-pi.md), [Gemma Chat](../applications/gemma-chat.md)

## 3. Custom permissive (Llama-style)

_Permits commercial use under conditions (e.g. 700M MAU cap, naming, AUP). Read the actual license — terms vary by model._

- **Models:** [Llama](../models/llama.md) (Llama Community License; 700M MAU cap for commercial deployments), [Hermes](../models/hermes.md) (Llama-based variants inherit Llama Community License; Qwen-based variants are Apache 2.0)
- **Frameworks:** [AutoGen](../frameworks/autogen.md) (CC-BY-4.0 — permissive but note: attribution required, not standard Apache/MIT)

## 4. Source-available / non-commercial

_Research-only or non-commercial only. Not free for production use._

- **Models:** [Command R](../models/command-r.md) (CC-BY-NC 4.0; commercial use requires a separate Cohere license agreement), [StarCoder2](../models/starcoder2.md) (BigCode OpenRAIL-M; commercial use permitted with use-based restrictions; gated download), [Mistral](../models/mistral.md) (Mistral-Large-Instruct-2407 under Mistral Research License; Codestral-22B v0.1 under MNLP-0.1 — both non-commercial)
- **Applications:** [Open Interpreter](../applications/open-interpreter.md) (AGPL-3.0 — copyleft; self-hosted use OK but distribution triggers share-alike)
- **Runtimes:** [Aphrodite Engine](../runtimes/aphrodite-engine.md), [KoboldCpp](../runtimes/koboldcpp.md), [Text Generation WebUI](../runtimes/text-generation-webui.md), [Jan](../runtimes/jan.md) (all AGPL-3.0)

## 5. Other

_Unique or proprietary terms — verify current license on each entity before use._

- **Models:** [Gemma](../models/gemma.md) (Gemma 1–3 under Gemma Terms of Use; permissive but not OSI-open; gated), [DBRX](../models/dbrx.md) (Databricks Open Model License; commercial use permitted; gated), [Nemotron](../models/nemotron.md) (NVIDIA Open Model License; commercial use permitted; attribution required; Llama-Nemotron additionally inherits Llama 3.1 license), [Hunyuan](../models/hunyuan.md) (Tencent proprietary license; commercial-use restrictions in some jurisdictions — requires legal review), [DeepSeek](../models/deepseek.md) (V2/V3 under DeepSeek License; commercial use and derivatives permitted, but distinct from MIT/Apache), [Falcon](../models/falcon.md) (Falcon-180B under TII Falcon License — custom Apache-2.0-based with extra restrictions)
- **Runtimes:** [LM Studio](../runtimes/lm-studio.md) (proprietary closed-source; free to use but not open-source)
