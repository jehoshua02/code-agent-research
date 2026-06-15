---
name: "ReAct"
license_category: "n/a"
status: "active"
url: "https://arxiv.org/abs/2210.03629"
last_verified: "2026-06-14"
applies_at: "framework"
problem: "An LLM acting in a loop has no mechanism to verify intermediate steps, so errors compound silently without real-world feedback"
best_for: ["coding", "research", "automation", "data"]
notes: ""
---

# ReAct

_Last verified: 2026-06-14_

## 0. TL;DR

ReAct is the most common [agent loop](../GLOSSARY.md#agent-loop) pattern: the model alternates between thinking out loud, calling a [tool](../GLOSSARY.md#tool), and reading the result — repeating until the task is done. Use it any time the agent needs to gather information or take actions across multiple steps before it can answer. The main catch: errors in early steps compound silently, so long ReAct chains can drift far off track without any built-in replanning mechanism.

## 1. What It Is

ReAct interleaves Thought, Action, and Observation steps so the model can reason about a task, invoke external tools, and react to their results in a loop. Introduced by Yao et al. (2022). The canonical pattern behind most modern agent frameworks.

## 2. Problem It Solves

An LLM acting in a loop has no mechanism to verify whether its intermediate steps are correct. Without real-world feedback between reasoning steps, errors compound silently: a wrong assumption in step 2 cascades into confidently wrong final answers, and the model never knows it went off the rails.

## 3. How It Works

The model is prompted to alternate between three labeled steps: a Thought (internal reasoning about what to do next), an Action (a tool call with parameters), and an Observation (the tool's return value). The loop repeats until the model produces a final answer. The structure is enforced by the prompt template and by stopping the LLM on the Observation line so the runtime can inject the real tool result. Introduced by Yao et al. 2022.

```
while not done:
    thought = llm(prompt + history)          # "I need to search for X"
    action, args = parse_action(thought)     # search("X")
    observation = execute_tool(action, args) # "X is defined as..."
    history += thought + observation
return parse_final_answer(history)
```

## 4. When To Use

ReAct is the right default pattern for multi-step tasks that require external tools — web search, calculators, APIs, databases. It is especially useful when the task cannot be decomposed in advance because each action's result determines the next step.

## 5. When Not To Use

Avoid ReAct for single-turn factual questions where one tool call suffices (plain tool use is cheaper). It adds overhead for latency-critical paths because every loop iteration requires at least one LLM call plus tool round-trip. If no tools are available, the Thought/Action structure adds tokens without benefit.

## 6. Implementations

- **LangChain** — `AgentExecutor` with `zero-shot-react-description` agent type; also `create_react_agent`
- **LlamaIndex** — `ReActAgent` with pluggable tool list
- **smolagents** (Hugging Face) — `ReactCodeAgent` and `ReactToolCallingAgent`
- **custom** — the pattern is a prompt template plus a parse-and-dispatch loop; no library strictly required

## 7. Sources

- [ReAct: Synergizing Reasoning and Acting in Language Models (Yao et al., 2022)](https://arxiv.org/abs/2210.03629) — observed 2026-06-14
