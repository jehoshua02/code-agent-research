# Tree-of-thought

_Last verified: 2026-06-14_

## 0. TL;DR

Tree-of-thought extends [chain-of-thought](../GLOSSARY.md#chain-of-thought) by exploring multiple reasoning branches in parallel and pruning dead ends — like a chess engine considering several moves before committing. Use it for planning or puzzle problems where the correct path isn't obvious and a single linear chain frequently gets stuck. The main catch: it multiplies LLM calls dramatically, making it expensive and slow; most production systems find simpler heuristics or ReAct loops sufficient.

## 1. What It Is

Tree-of-thought (ToT) maintains a tree of partial reasoning paths with branching and backtracking, searched BFS or DFS, evaluating intermediate states before committing. Introduced by Yao et al. (2023). Useful where linear chains hit dead ends but expensive in tokens and time.

## 2. Problem It Solves

Chain-of-thought reasoning is strictly linear: the model commits to each token as it generates it, with no ability to backtrack. If the model takes a wrong turn early in a multi-step problem, the entire chain is tainted and the error cannot be corrected without restarting. This makes CoT brittle on problems that require planning or exploration.

## 3. How It Works

At each reasoning step, the model generates multiple candidate continuations (the "branches"). A separate evaluator — either another LLM call or a heuristic — scores each branch. A search algorithm (BFS for shallow exploration, DFS for depth-first commitment) selects which branches to expand and which to prune. The process continues until a branch reaches a satisfactory final answer or the budget is exhausted. Introduced by Yao et al. 2023.

```
tree = [initial_state]
for step in range(max_depth):
    candidates = []
    for node in tree:
        candidates += llm.generate_n(node, n=branching_factor)
    scores = evaluator(candidates)
    tree = select_top_k(candidates, scores, k=beam_width)
return best(tree)
```

## 4. When To Use

ToT is appropriate for discrete planning problems, puzzles (e.g., Game of 24, crosswords), and tasks where intermediate states are verifiable and wrong paths can be detected early. The benefit is greatest when CoT already fails, indicating that linear reasoning is insufficient.

## 5. When Not To Use

ToT is expensive: branching factor N at depth D requires O(N^D) LLM calls in the worst case. For open-ended generation tasks there is no meaningful way to evaluate intermediate states, so the evaluator adds cost without signal. Avoid it when CoT already achieves acceptable accuracy or when latency and cost are primary constraints.

## 6. Implementations

- **princeton-nlp/tree-of-thought-llm** — reference implementation from the original paper, task-specific examples included
- **LangChain experimental** — `ToTChain` in `langchain_experimental.tot`
- **custom BFS/DFS loop** — the pattern is straightforward to implement with any LLM API; the key component is the per-node evaluator prompt

## 7. Sources

- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models (Yao et al., 2023)](https://arxiv.org/abs/2305.10601) — observed 2026-06-14
