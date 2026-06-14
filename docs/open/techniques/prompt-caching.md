# Prompt caching

_Last verified: 2026-06-14_

## 1. What It Is

Prompt caching has the provider cache the server-side key-value state for a static prompt prefix and reuse it across requests, paying full compute only on cache misses. Reduces both cost and latency for repeated long prefixes. Available in Anthropic and OpenAI APIs and in some self-hosted runtimes.

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

- [Anthropic Prompt Caching documentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) — observed 2026-06-14
