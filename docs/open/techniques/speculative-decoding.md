# Speculative decoding

_Last verified: 2026-06-14_

## 1. What It Is

A small draft model proposes multiple tokens; the large target model verifies them in one parallel forward pass, accepting matching tokens and resampling the first mismatch. Introduced by Leviathan et al. (2022) and Chen et al. (2023). Speeds up decoding without changing the output distribution.

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

- [Fast Inference from Transformers via Speculative Decoding (Leviathan et al., 2022)](https://arxiv.org/abs/2211.17192) — observed 2026-06-14
