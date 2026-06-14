# KV cache reuse

_Last verified: 2026-06-14_

## 1. What It Is

Key-value attention tensors from already-processed tokens are stored in GPU memory and reused on the next decode step, avoiding redundant recomputation. Cross-request prefix sharing was formalized by Kwon et al. (2023, PagedAttention) and is now standard in production-grade inference runtimes.

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

- [Efficient Memory Management for Large Language Model Serving with PagedAttention (Kwon et al., 2023)](https://arxiv.org/abs/2309.06180) — observed 2026-06-14
