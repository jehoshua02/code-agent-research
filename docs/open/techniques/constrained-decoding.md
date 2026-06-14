# Constrained decoding (JSON mode, grammar)

_Last verified: 2026-06-14_

## 1. What It Is

Constrained decoding masks token logits at each generation step to enforce a grammar or schema (JSON, regex, context-free grammar), guaranteeing parseable output. Implemented in llama.cpp grammars, dottxt/Outlines, vLLM's structured output, and OpenAI Structured Outputs.

## 2. Problem It Solves

What goes wrong without it.

## 3. How It Works

Mechanism in plain terms. Pseudocode or diagram if needed.

## 4. When To Use

Conditions where it pays off.

## 5. When Not To Use

Conditions where it hurts more than helps.

## 6. Implementations

Libraries, frameworks, or runtimes that ship it.

## 7. Sources

- [OpenAI Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) — observed 2026-06-14
