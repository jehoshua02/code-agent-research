# Runtimes — Index

| Runtime | License | Formats | API | Hardware | Notes |
|---|---|---|---|---|---|
| [vLLM](vllm.md) | Apache 2.0 | safetensors, AWQ, GPTQ, FP8, bitsandbytes, compressed-tensors, GGUF (experimental) | OpenAI-compat | CUDA, ROCm, CPU (x86/ARM), TPU, Gaudi, XPU; Metal via plugin | _stub_ |
| [llama.cpp](llama-cpp.md) | MIT | GGUF (all llama.cpp quants) | OpenAI-compat | CUDA, ROCm, Metal, Vulkan, SYCL, MUSA, CANN, CPU | _stub_ |
| [Ollama](ollama.md) | MIT | GGUF (imports safetensors/PyTorch) | OpenAI-compat | CUDA, ROCm, Metal, Vulkan, CPU | wraps llama.cpp |
| [LM Studio](lm-studio.md) | Proprietary (free-to-use) | GGUF, MLX | OpenAI-compat | CUDA, ROCm (Linux), Vulkan, Metal, CPU | closed-source |
| [MLX / mlx-lm](mlx.md) | MIT | MLX native (safetensors); GGUF export only | _stub_ | Apple Silicon Metal only | _stub_ |
| [TGI](tgi.md) | Apache 2.0 | safetensors, GPTQ, AWQ, FP8, bitsandbytes, EETQ, Marlin, EXL2 | OpenAI-compat | CUDA, ROCm, Inferentia, Gaudi, TPU, Intel GPU | _stub_ |
| [SGLang](sglang.md) | Apache 2.0 | safetensors, GPTQ, AWQ, FP8, GGUF, FP4/MXFP4, bitsandbytes, torchao | OpenAI-compat | CUDA, ROCm, CPU (Xeon), TPU, Ascend, XPU | _stub_ |
| [ExLlamaV2 / V3](exllamav2.md) | MIT | EXL2, GPTQ, safetensors | _stub_ | CUDA only (Ampere+) | _stub_ |
| [Aphrodite Engine](aphrodite-engine.md) | AGPL-3.0 | GGUF, AWQ, GPTQ, EXL2, AQLM, BitNet, FP8, MXFP4, bitsandbytes, QuIP#, SqueezeLLM, Marlin, + more | OpenAI-compat | CUDA, ROCm, CPU, XPU, TPU, Inferentia | vLLM fork |
| [KoboldCpp](koboldcpp.md) | AGPL-3.0 | GGUF (legacy GGML) | OpenAI-compat | CUDA, ROCm, Metal, Vulkan, CPU | llama.cpp-based |
| [Text Generation WebUI](text-generation-webui.md) | AGPL-3.0 | GGUF, EXL2, GPTQ, AWQ, safetensors, bitsandbytes, TRT-LLM, HQQ | _stub_ | CUDA, ROCm (Linux), Vulkan, Metal, CPU | maintained by oobabooga |
| [Jan](jan.md) | AGPL-3.0 | GGUF, MLX (TensorRT-LLM via Cortex) | _stub_ | CUDA, ROCm (Linux, experimental), Metal/MLX, Vulkan, CPU | desktop app |
| [LocalAI](localai.md) | MIT | GGUF, safetensors, GPTQ, AWQ, diffusion, audio | OpenAI-compat | CUDA, ROCm, Metal/MLX, Intel SYCL, Vulkan, CPU, Jetson | multi-backend |
| [llamafile](llamafile.md) | Apache 2.0 | GGUF (embedded or external) | OpenAI-compat | CUDA, ROCm, Metal, CPU (AVX/AVX2/AVX-512, NEON) | single-file portable |
| [transformers](transformers.md) | Apache 2.0 | safetensors, PyTorch, GGUF (load); bitsandbytes, GPTQ, AWQ, AQLM, FP8, torchao, HQQ | _stub_ | CUDA, ROCm, Metal (MPS), CPU | library, not server |
| [gemma.cpp](gemma-cpp.md) | Apache 2.0 | Custom .sbs (bf16, fp32, fp8, NUQ 4-bit) | _stub_ | CPU only (SIMD via Highway; x86, ARM, any) | model-specific (Gemma) |
