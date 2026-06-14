# Chain-of-thought

_Last verified: 2026-06-14_

## 1. What It Is

Chain-of-thought (CoT) prompting elicits intermediate reasoning steps before the final answer, via worked examples or the trigger phrase "Let's think step by step." Introduced by Wei et al. (2022). Improves performance on multi-step reasoning tasks but increases output tokens and latency.

## 2. Problem It Solves

When asked a multi-step math or logic problem without prompting, an LLM jumps directly to an answer by pattern-matching against superficially similar training examples. This produces confidently wrong answers because the model never checks intermediate results. The failure is especially sharp on problems that look familiar but have different numerical values or logical structure.

## 3. How It Works

The model is prompted to produce reasoning steps before the final answer, either by appending "Let's think step by step" to the query (zero-shot CoT) or by providing a few worked examples where reasoning is shown explicitly (few-shot CoT). The intermediate tokens force the model to "carry" partial results through its generation, reducing errors that arise from compressing multi-step reasoning into a single prediction. Introduced by Wei et al. 2022.

```
# Zero-shot CoT
prompt = user_question + "\nLet's think step by step."
response = llm(prompt)
answer = parse_final_answer(response)

# Few-shot CoT
prompt = cot_examples + "\n" + user_question
response = llm(prompt)
```

## 4. When To Use

CoT is most effective on arithmetic, symbolic reasoning, commonsense reasoning, and logic problems — tasks where explicit intermediate steps map onto the correct solution path. It provides the biggest gains on larger models (generally 10B+ parameters); smaller models may not benefit.

## 5. When Not To Use

Avoid CoT for simple factual lookups or classification tasks where intermediate reasoning adds tokens without improving accuracy. On latency-critical paths, the extra output tokens increase both response time and cost. If the task is well-covered by the model's training distribution, zero-shot without CoT is usually sufficient.

## 6. Implementations

- **Prompt engineering** — no library required; add "Let's think step by step" or include worked examples in the system/user prompt
- **DSPy** — `ChainOfThought` module wraps a signature with automatic CoT elicitation and supports optimization
- **LangChain** — `LLMChain` with a CoT prompt template; also integrates with DSPy modules

## 7. Sources

- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models (Wei et al., 2022)](https://arxiv.org/abs/2201.11903) — observed 2026-06-14
