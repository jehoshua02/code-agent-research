# Speculative decoding

_Last verified: 2026-06-14_

## 1. What It Is

A small draft model proposes multiple tokens; the large target model verifies them in one parallel forward pass, accepting matching tokens and resampling the first mismatch. Introduced by Leviathan et al. (2022) and Chen et al. (2023). Speeds up decoding without changing the output distribution.

## 2. Problem It Solves

Autoregressive LLM decoding generates one token per forward pass through the full model. Large models are memory-bandwidth-bound, meaning the GPU spends most of its time reading model weights rather than performing computation. This makes generation slow in proportion to model size, with little benefit from extra GPU parallelism since each token depends on the previous one.

## 3. How It Works

A small, fast draft model autoregressively proposes K candidate tokens. The large target model then runs a single forward pass over all K tokens in parallel, computing the probability of each under the target distribution. Tokens are accepted greedily while the draft probabilities are close to the target probabilities; the first rejected token is resampled from a corrected distribution. The output distribution is mathematically identical to sampling from the target model directly. Introduced by Leviathan et al. 2022 and Chen et al. 2023.

```
draft_tokens = draft_model.generate(prompt, k=5)
target_probs = target_model.forward(prompt + draft_tokens)   # one parallel pass
accepted = verify_and_accept(draft_tokens, target_probs)     # accept/reject each
next_token = resample_at_first_rejection(target_probs, accepted)
return accepted_tokens + [next_token]
```

## 4. When To Use

Speculative decoding reduces latency at batch size 1 (interactive inference) when a good draft model exists — typically a 7B or smaller model that shares the target's vocabulary. It is most effective when draft tokens have high acceptance rates (text-heavy tasks, low temperature).

## 5. When Not To Use

Speculative decoding hurts throughput for large batches because the draft model adds overhead that doesn't parallelize efficiently across many concurrent requests. It also degrades when the draft model's distribution is very different from the target (low acceptance rate means the draft overhead is wasted). Heavily quantized models may have poor draft quality.

## 6. Implementations

- **Hugging Face Transformers** — `generate(assistant_model=draft_model)` parameter
- **vLLM** — `speculative_model` server argument; supports draft models and also "ngram" matching
- **llama.cpp** — `--model-draft` flag to specify a draft model
- **TensorRT-LLM** — speculative decoding support in the engine builder configuration

## 7. Sources

- [Fast Inference from Transformers via Speculative Decoding (Leviathan et al., 2022)](https://arxiv.org/abs/2211.17192) — observed 2026-06-14
