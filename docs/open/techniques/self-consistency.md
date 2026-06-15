# Self-consistency

_Last verified: 2026-06-14_

## 0. TL;DR

Self-consistency runs the same prompt multiple times with some randomness, then picks the answer that comes up most often — majority voting instead of a single shot. Use it when accuracy on reasoning tasks matters more than cost or latency and a single [chain-of-thought](../GLOSSARY.md#chain-of-thought) answer isn't reliable enough. The main catch: it multiplies your inference cost by however many samples you take (typically 5–20x), so it's only practical for tasks where that trade-off is justified.

## 1. What It Is

Self-consistency samples multiple chain-of-thought reasoning paths at non-zero temperature, then majority-votes the most frequent final answer. Introduced by Wang et al. (2022). Trades cost for accuracy on reasoning benchmarks.

## 2. Problem It Solves

A single chain-of-thought sample can follow a plausible but incorrect reasoning path and arrive at a confident wrong answer. Because stochastic decoding is inherently variable, different runs of the same prompt can produce different answers — some correct, some not. Greedy decoding always takes the single most likely path, which may not be the most reliable.

## 3. How It Works

The same prompt is sent to the model N times with temperature > 0, producing N independent chain-of-thought responses that may take different reasoning paths. The final answers are extracted from each response and aggregated by majority vote — the most frequent answer is returned. The approach relies on the assumption that correct reasoning paths, though varied, will converge on the same answer more often than incorrect paths. Introduced by Wang et al. 2022.

```
answers = []
for _ in range(N):
    response = llm(prompt, temperature=0.7)
    answers.append(parse_final_answer(response))
return majority_vote(answers)
```

## 4. When To Use

Self-consistency is most effective on tasks with discrete, verifiable answers — math problems, logical reasoning, classification. Use it when accuracy is the top priority and you can afford N× the token cost. It reliably improves over single-sample CoT across benchmarks.

## 5. When Not To Use

Do not use self-consistency for open-ended generation tasks where there is no single correct answer and majority voting is meaningless. It multiplies cost by N, so it is unsuitable for latency-critical or budget-constrained paths. If the model is already highly accurate with a single sample, the gain is marginal relative to the added cost.

## 6. Implementations

- **DSPy** — `Predict` with `n` samples and built-in majority vote aggregation
- **Custom sampling loop** — call any LLM API N times with `temperature > 0`, extract answers, apply `Counter.most_common(1)`
- **LangChain** — no first-class self-consistency module; implement with multiple `chain.invoke()` calls and manual aggregation

## 7. Sources

- [Self-Consistency Improves Chain of Thought Reasoning in Language Models (Wang et al., 2022)](https://arxiv.org/abs/2203.11171) — observed 2026-06-14
