# Runtimes — Index

| Runtime | License | Formats | API | Hardware | Notes |
|---|---|---|---|---|---|
| [Aphrodite Engine](aphrodite-engine.md) | AGPL-3.0 | safetensors, gguf, awq, gptq, exl2, fp8, bitsandbytes | OpenAI-compat | cuda, rocm, cpu, tpu, xpu | vLLM fork with broader quantization support (EXL2, GGUF, AQLM, BitNet); AGPL-3.0 has copyleft implications. |
| [ExLlamaV2](exllamav2.md) | MIT | exl2, gptq, safetensors | _stub_ | cuda | NVIDIA Ampere (sm_80) minimum; no OpenAI server built-in — TabbyAPI recommended for HTTP serving. |
| [gemma.cpp](gemma-cpp.md) | Apache-2.0 | sbs | _stub_ | cpu | Gemma-family only; CPU-only (no GPU); proprietary .sbs format with closed-source safetensors converter. |
| [Jan](jan.md) | AGPL-3.0 | gguf, mlx | OpenAI-compat | cuda, rocm, metal, cpu, vulkan | Desktop chat app; GGUF-only for primary llama.cpp path; MLX backend added v0.7.7 for Apple Silicon. |
| [KoboldCpp](koboldcpp.md) | AGPL-3.0 | gguf | OpenAI-compat | cuda, rocm, metal, cpu, vulkan | Single-binary llama.cpp wrapper with bundled browser UI for story/roleplay; AGPL-3.0 copyleft. |
| [llama.cpp](llama-cpp.md) | MIT | gguf | OpenAI-compat | cuda, rocm, metal, cpu, vulkan, sycl | Upstream of Ollama, KoboldCpp, and llamafile; GGUF is the sole inference format. |
| [llamafile](llamafile.md) | Apache-2.0 | gguf | OpenAI-compat | cuda, rocm, metal, cpu | Single-file portable executable via Cosmopolitan Libc; CUDA JIT is Linux-only (no CUDA on Windows as of v0.10.0). |
| [LM Studio](lm-studio.md) | Proprietary | gguf, mlx | OpenAI-compat | cuda, rocm, metal, cpu, vulkan | Closed-source, free-to-use; macOS supports Apple Silicon only (no Intel Mac). |
| [LocalAI](localai.md) | MIT | gguf, safetensors, gptq, awq | OpenAI-compat | cuda, rocm, metal, cpu, vulkan, sycl | Multi-backend routing layer (36+ backends); also exposes Anthropic, Ollama, and ElevenLabs-compatible APIs. |
| [MLX / mlx-lm](mlx.md) | MIT | safetensors | OpenAI-compat | metal | Apple Silicon and macOS only; built-in server is not recommended for production. |
| [Ollama](ollama.md) | MIT | gguf | OpenAI-compat | cuda, rocm, metal, cpu, vulkan | Wraps llama.cpp; bundled CUDA libs — no separate toolkit install required. |
| [SGLang](sglang.md) | Apache-2.0 | safetensors, gptq, awq, fp8, gguf | OpenAI-compat | cuda, rocm, cpu, tpu, xpu, ascend | macOS support is experimental (MLX backend, Python 3.11 only); Windows unsupported. |
| [Text Generation WebUI](text-generation-webui.md) | AGPL-3.0 | gguf, exl2, gptq, awq, safetensors | OpenAI-compat | cuda, rocm, metal, cpu, vulkan | Multi-backend web UI (~10 GB install); hot-swap between llama.cpp, ExLlamaV2, Transformers without restart. |
| [TGI](tgi.md) | Apache-2.0 | safetensors, gptq, awq, fp8, bitsandbytes | OpenAI-compat | cuda, rocm | Now in maintenance mode; README redirects new projects to vLLM, SGLang, and llama.cpp. |
| [transformers](transformers.md) | Apache-2.0 | safetensors, gguf, gptq, awq | _stub_ | cuda, rocm, metal, cpu | Library, not a server; GGUF loads as dequantized FP32 — for inference use llama.cpp or vLLM. |
| [vLLM](vllm.md) | Apache-2.0 | safetensors, gguf, awq, gptq, fp8, bitsandbytes | OpenAI-compat | cuda, rocm, metal, cpu, tpu, xpu, gaudi, ascend | GGUF support is highly experimental; macOS via unsupported community plugin only. |
