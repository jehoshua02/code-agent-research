# MLX / mlx-lm

_Last verified: 2026-06-14_

## 1. What It Is

MLX (ml-explore/mlx) and mlx-lm (ml-explore/mlx-lm) are MIT-licensed Apple frameworks. Active. Apple-Silicon-native array library and LLM tooling using the Metal GPU; macOS-only, designed to exploit unified memory on M-series chips.

## 2. Install

Apple Silicon Mac (M1 or later), macOS ≥ 14.0 (15.0+ recommended for memory-wiring optimizations on large models), Python ≥ 3.10.

```bash
pip install mlx-lm
# or
conda install -c conda-forge mlx-lm
```

The `mlx` core array framework is installed automatically as a dependency. No Linux or Windows support for the Apple Silicon backend; no CUDA or ROCm path. (Linux-only `mlx[cuda]`/`mlx[cpu]` variants of the core framework exist but are outside the mlx-lm workflow.)

## 3. Hardware Support

- **Metal / Apple Silicon only:** M1, M2, M3, M4 (base/Pro/Max/Ultra). Metal backend; no extra drivers.
- **No CUDA, no ROCm, no Intel/AMD GPU.**
- **Unified memory:** CPU and GPU share the same physical RAM pool — no separate VRAM budget; all system RAM is addressable by the GPU.
- **CPU fallback:** Available within the same unified memory space; significantly slower than Metal.
- **Multi-GPU:** Not applicable (Apple Silicon is single-chip; M-Ultra variants present as a single device).

## 4. Model Formats

- **Native MLX format:** Directory of `.safetensors` shards with `config.json` and tokenizer files; auto-sharded when > 5 GB. Thousands of pre-converted models on the `mlx-community` Hugging Face org.
- **Convert from HuggingFace safetensors:** `mlx_lm.convert --hf-path <repo> --mlx-path ./mlx_model`.
- **Quantization:** `-q` flag defaults to 4-bit affine, group size 64. Options: `--q-bits` (2/3/4/6/8), `--q-group-size`, `--q-mode` (`affine` default, `mxfp4`, `nvfp4`, `mxfp8`), `--quant-predicate` for mixed recipes (`mixed_2_6`, `mixed_3_4`, `mixed_3_6`, `mixed_4_6`).
- **GGUF:** No native loading. `mlx_lm.fuse --export-gguf` can export (Llama/Mistral/Mixtral only, fp16). Importing GGUF requires a third-party tool (e.g., `gguf2mlx`).

## 5. API Surface

OpenAI-compatible? Native API? Streaming? Tool calling? Embeddings?

## 6. Performance

Throughput (tok/s), latency, batch support. Cite source or note "not benchmarked".

## 7. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent comparisons. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 9. Sources

- [ml-explore/mlx-lm](https://github.com/ml-explore/mlx-lm) — observed 2026-06-14
