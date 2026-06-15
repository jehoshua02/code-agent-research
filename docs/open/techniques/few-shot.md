---
name: "Few-shot / in-context learning"
license_category: "n/a"
status: "active"
url: "https://arxiv.org/abs/2005.14165"
last_verified: "2026-06-14"
applies_at: "model"
problem: "Zero-shot prompts rely on the model's internal priors, producing inconsistent or off-format output for tasks with unusual schemas or domain conventions"
best_for: ["coding", "data", "writing", "automation"]
notes: ""
---

# Few-shot / in-context learning

_Last verified: 2026-06-14_

## 0. TL;DR

Few-shot prompting means putting a handful of worked examples directly in the prompt so the model learns the expected format and style from them — no model training required. Use it when zero-shot instructions produce inconsistent output formats or when your task has domain conventions the model doesn't naturally match. The main catch: examples consume context window tokens, and poor example selection (wrong format, unrepresentative cases) can mislead the model as much as help it.

## 1. What It Is

Few-shot prompting (in-context learning) places a small number of input-output examples in the prompt so the model can infer the task format and style without any weight updates. Documented at scale by Brown et al. (GPT-3, 2020). Effective when examples cover the expected input distribution.

## 2. Problem It Solves

Zero-shot prompts rely on the model's internal priors for output format, reasoning style, and level of detail. For tasks with unusual output schemas, domain-specific conventions, or edge cases the model hasn't seen in training, zero-shot produces inconsistent or off-format responses that require post-processing or simply fail downstream.

## 3. How It Works

K labeled input-output pairs are prepended to the prompt before the live query. The model treats these examples as implicit demonstrations of the expected behavior — format, length, vocabulary, and reasoning style — and generalizes the pattern to the new input. No weight updates occur; the learning happens entirely within the context window. Documented at scale by Brown et al. 2020 (GPT-3).

```
prompt = ""
for input, output in examples[:k]:
    prompt += f"Input: {input}\nOutput: {output}\n\n"
prompt += f"Input: {live_query}\nOutput:"
response = llm(prompt)
```

## 4. When To Use

Few-shot is effective for format-sensitive tasks (structured extraction, specific JSON schemas), tasks with uncommon output conventions the model wasn't trained on, and situations where fine-tuning is not feasible. It is a cheap intervention that often closes the gap between zero-shot and fine-tuned performance.

## 5. When Not To Use

Skip few-shot when the examples don't fit in the context window, when the examples are poor quality or unrepresentative (bad examples actively mislead the model), or when the task is already well-covered by the model's zero-shot instruction following. Example selection matters significantly — random examples can hurt.

## 6. Implementations

- **Prompt engineering** — no library required; manually prepend examples to system or user message
- **DSPy** — `BootstrapFewShot` optimizer automatically selects and generates effective few-shot examples from a labeled dataset
- **LangChain** — `FewShotPromptTemplate` structures example formatting; `SemanticSimilarityExampleSelector` picks relevant examples dynamically

## 7. Sources

- [Language Models are Few-Shot Learners (Brown et al., 2020)](https://arxiv.org/abs/2005.14165) — observed 2026-06-14
