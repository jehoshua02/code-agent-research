# DSPy

_Last verified: 2026-06-14_

## 0. TL;DR

DSPy is fundamentally different from other agent frameworks — instead of writing prompts, you write programs using typed signatures and modules, then let DSPy's optimizer automatically find the best prompts and few-shot examples for your task. Pick it if you have labeled data (or can generate it) and want the model's behavior tuned automatically rather than hand-crafting instructions. The main catch is the mental shift: you don't write prompts at all, which is unfamiliar and requires understanding the compile/optimize loop before you see results.

## 1. What It Is

DSPy is an MIT-licensed Python framework from Stanford NLP (stanfordnlp/dspy). Active. Treats prompts as programs to be compiled and optimized, separating program logic from prompt text via signatures and modules.

## 2. Install

Python >=3.10 and <3.15 required; Linux, macOS, Windows supported.

```bash
pip install dspy
```

Latest from main:

```bash
pip install git+https://github.com/stanfordnlp/dspy.git
```

No mandatory provider extras — configure at runtime via `dspy.configure()`.

## 3. Model Compatibility

All inference is routed through [LiteLLM](https://litellm.ai/) internally (`dspy.clients._litellm`), so any LiteLLM-supported provider works: OpenAI, Anthropic, Google Gemini, Mistral, Cohere, AWS Bedrock, Azure OpenAI, Groq, Ollama (local), vLLM (OpenAI-compat), and **OpenRouter** (via `openrouter/` model prefix). Configure with:

```python
import dspy
dspy.configure(lm=dspy.LM("openai/gpt-4o", api_key="..."))
```

Source: [DSPy source — dspy/clients/lm.py](https://github.com/stanfordnlp/dspy/blob/main/dspy/clients/lm.py).

## 4. Agent Capabilities

Declarative LM programming framework (compile prompts as programs). Tools are plain Python functions wrapped in `dspy.Tool(func)`; auto-schema from signature/docstring; MCP support via `dspy.Tool.from_mcp_tool`; native function-calling opt-in (`ChatAdapter(use_native_function_calling=True)`). Planning via ReAct loop in `dspy.ReAct(signature, tools=[...], max_iters=20)` — each iter produces thought/tool_name/tool_args; built-in `finish` tool; offline "compile-time" planning via optimizers (MIPROv2, BootstrapFewShot, SIMBA). Memory: in-loop `trajectory` dict (working memory, oldest entries truncated); `dspy.History` for conversational (explicit, not auto-tracked); no built-in long-term store (use retrieval as tools). Multi-agent via DSPy module composition (no dedicated primitive); `dspy.Parallel` for concurrent module exec. HITL not interrupt-based; uses `dspy.BestOfN` and `dspy.Refine` (replaced `dspy.Assert`/`dspy.Suggest`) with human-authored `reward_fn`. State persistence: `Module.save("path.json")` (state-only) or `save_program=True` (full cloudpickle); API keys never serialized; transactional load. Observability: `dspy.inspect_history(n)`, MLflow autologging (zero-code), custom `BaseCallback`. Retry: ReAct tool errors → text observations for LLM self-correction; `truncate_trajectory` (3 retries) on context overflow; `BestOfN`/`Refine` for output-level retry. Both sync and async (`module(...)` vs `await module.acall(...)`, `aforward`). Source: dspy.ai.

## 5. MCP Support

Not supported natively. No MCP integration is present in the DSPy codebase or documented as of June 2026. Source: review of [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) repository.

## 6. Programming Model

Declarative / program-based (distinct from all other frameworks listed). Logic is expressed as compositions of typed `Signature` objects (input/output field specs) and `Module` subclasses (analogous to PyTorch layers). Instead of writing prompts, developers write Python programs; DSPy's optimizer (`BootstrapFewShot`, `MIPROv2`, etc.) compiles them into optimized prompts or fine-tuned weights. Example:

```python
import dspy

class QA(dspy.Signature):
    question: str = dspy.InputField()
    answer: str = dspy.OutputField()

class SimpleQA(dspy.Module):
    def __init__(self):
        self.predict = dspy.Predict(QA)
    def forward(self, question):
        return self.predict(question=question)

dspy.configure(lm=dspy.LM("openai/gpt-4o"))
prog = SimpleQA()
print(prog(question="What is LangGraph?").answer)
```

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) — observed 2026-06-14
