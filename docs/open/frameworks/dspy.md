# DSPy

_Last verified: 2026-06-14_

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

Tool use, planning, memory, multi-agent, human-in-the-loop, state persistence.

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
