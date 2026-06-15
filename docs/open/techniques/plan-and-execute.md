---
name: "Plan-and-execute"
license_category: "n/a"
status: "active"
url: "https://arxiv.org/abs/2305.04091"
last_verified: "2026-06-14"
applies_at: "model"
problem: "Step-by-step agents decide what to do next based only on the most recent observation, so they drift from the original goal on long tasks"
best_for: ["coding", "research", "automation"]
notes: ""
---

# Plan-and-execute

_Last verified: 2026-06-14_

## 0. TL;DR

Plan-and-execute splits work into two phases: a planner LLM call lays out all the steps upfront, then a separate executor works through them one by one with [tools](../GLOSSARY.md#tool). Use it when tasks are long-horizon and a pure [ReAct](../GLOSSARY.md#react) loop tends to go off track — the explicit plan keeps the agent anchored. The main catch: the plan is generated before any execution, so it may be wrong; you need a replanning step when reality doesn't match the plan's assumptions.

## 1. What It Is

Plan-and-execute separates a planner LLM call (which decomposes the task into ordered sub-tasks) from an executor (which carries out each sub-task with tools). Popularized by Wang et al. (2023, Plan-and-Solve). Keeps long-horizon tasks on track at the cost of an extra round trip per plan revision.

## 2. Problem It Solves

ReAct-style step-by-step agents decide what to do next based only on the most recent observation, so they tend to drift from the original goal on long tasks. After several tool calls, the model may pursue a tangent or forget an earlier constraint, producing work that is locally coherent but globally wrong.

## 3. How It Works

A dedicated planner LLM call receives the task and produces an ordered list of sub-tasks. A separate executor then works through that list, running each sub-task with tools or sub-agents. The plan is explicit and inspectable; the executor only needs to handle one step at a time. If a step fails or reveals new information, the planner can be called again to revise remaining steps. Popularized by Wang et al. 2023 (Plan-and-Solve).

```
plan = planner_llm(task)          # ["Step 1: ...", "Step 2: ...", ...]
results = []
for step in plan:
    result = executor_llm(step, context=results)
    results.append(result)
return synthesize(results)
```

## 4. When To Use

Use plan-and-execute for long-horizon tasks with multiple distinct phases that can be named in advance — research pipelines, multi-stage code generation, report assembly. The explicit plan also makes the agent's behavior auditable, which matters in production.

## 5. When Not To Use

Skip it for simple single-step tasks where planning overhead is wasted. It is a poor fit for dynamic environments where conditions change faster than the plan can be revised — a fixed plan becomes a liability when early steps invalidate later assumptions. Real-time or latency-critical tasks cannot afford the extra planning round-trip.

## 6. Implementations

- **LangChain** — `PlanAndExecute` agent (`langchain_experimental.plan_and_execute`)
- **LlamaIndex** — `SubQuestionQueryEngine` decomposes questions into sub-queries before executing
- **AutoGen** — multi-agent conversation pattern where one agent plans and others execute
- **custom** — a planner prompt + a loop over sub-tasks with any executor is sufficient

## 7. Sources

- [Plan-and-Solve Prompting (Wang et al., 2023)](https://arxiv.org/abs/2305.04091) — observed 2026-06-14
