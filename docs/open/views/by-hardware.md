# View — By Hardware

What fits at each VRAM tier. Each section links to relevant model entries that fit comfortably at that tier. Tier descriptions are rough rules of thumb — exact fit depends on quantization, context length, KV cache, and concurrent processes. System RAM matters when offloading.

## 1. 8 GB

_RTX 3070 / 4060 / 4060 Ti 8GB-class. 7B Q4_K_M fits with room for context. 13B is tight and may require heavy quant or partial offload._

- **Models that fit:** [SmolLM](../models/smollm.md) (1.7B FP16 ~3.4 GB), [Phi](../models/phi.md) (Phi-4-mini 3.8B Q4 ~2.5 GB), [Qwen](../models/qwen.md) (Qwen3-4B FP16 ~8 GB at limit), [Gemma](../models/gemma.md) (Gemma 3 4B ~8 GB FP16), [Granite](../models/granite.md) (Granite-3.x-2B FP16 ~5 GB)
- **Runtimes that target this tier:** [llama.cpp](../runtimes/llama-cpp.md), [Ollama](../runtimes/ollama.md), [MLX](../runtimes/mlx.md) (Apple Silicon)

## 2. 12 GB

_RTX 3060 12G / 4070 / 5070-class. 13B Q4 fits. 14B is feasible at smaller context._

- **Models that fit:** [Llama](../models/llama.md) (Llama 3.1 8B Q8 ~8 GB; FP16 at limit), [Mistral](../models/mistral.md) (Mistral-7B Q8 ~7.5 GB), [Falcon](../models/falcon.md) (Falcon3-10B Q4 ~6 GB), [OLMo](../models/olmo.md) (OLMo-2-7B Q8 ~7–8 GB), [StarCoder2](../models/starcoder2.md) (StarCoder2-7B Q8 ~7.7 GB)
- **Runtimes that target this tier:** [llama.cpp](../runtimes/llama-cpp.md), [Ollama](../runtimes/ollama.md), [MLX](../runtimes/mlx.md)

## 3. 16 GB

_RTX 4080 / 4070 Ti Super / pro 16G. ~20B Q4 fits. MoE starts to make sense — active params determine compute, total params determine VRAM, so MoE only helps if total fits._

- **Models that fit:** [Phi](../models/phi.md) (Phi-4 14B Q4 ~7–8 GB; Q8 ~14–16 GB), [Mistral](../models/mistral.md) (Mistral NeMo 12B Q8 ~12 GB), [StarCoder2](../models/starcoder2.md) (StarCoder2-15B Q8 ~16.9 GB at limit), [OLMo](../models/olmo.md) (OLMo-2-13B Q8 ~13–14 GB), [Yi](../models/yi.md) (Yi-9B Q8 ~9 GB), [Llama](../models/llama.md) (Llama 3.1 8B FP16 ~16 GB)
- **Runtimes that target this tier:** [llama.cpp](../runtimes/llama-cpp.md), [Ollama](../runtimes/ollama.md), [vLLM](../runtimes/vllm.md), [transformers](../runtimes/transformers.md)

## 4. 24 GB

_RTX 3090 / 4090. 30–34B Q4 comfortable. 70B requires heavy quant (Q2/Q3) and CPU offload — workable but slower._

- **Models that fit:** [Mistral](../models/mistral.md) (Mistral Small 3.1 24B Q4 ~13 GB; Codestral-22B Q4 ~12 GB), [Qwen](../models/qwen.md) (Qwen3-32B Q4 ~18 GB), [Yi](../models/yi.md) (Yi-34B Q4 ~17 GB), [DeepSeek](../models/deepseek.md) (R1-Distill-Qwen-14B Q4 ~8 GB; R1-Distill-Qwen-32B Q4 ~18 GB), [Gemma](../models/gemma.md) (Gemma 2/3 27B Q4 ~15 GB), [Hermes](../models/hermes.md) (Hermes-3-8B FP16 ~16 GB), [Granite](../models/granite.md) (Granite-3.x-8B FP16 ~16 GB)
- **Runtimes that target this tier:** [llama.cpp](../runtimes/llama-cpp.md), [Ollama](../runtimes/ollama.md), [vLLM](../runtimes/vllm.md), [ExLlamaV2](../runtimes/exllamav2.md)

## 5. 24 GB+ multi-GPU

_2× 3090 / single 5090 / pro cards. 70B Q4 comfortable. 100B+ MoE feasible with enough system RAM for offload._

- **Models that fit:** [Llama](../models/llama.md) (Llama 3.1 70B Q4 ~40 GB; Llama 4 Scout Q4 ~55 GB), [DeepSeek](../models/deepseek.md) (R1-Distill-Llama-70B Q4 ~40 GB), [Command R](../models/command-r.md) (Command R 32B Q4 ~16 GB; Command R+ 104B Q4 ~52 GB), [Nemotron](../models/nemotron.md) (Nemotron-70B Q4 ~40 GB on 2× A100 80 GB), [Hunyuan](../models/hunyuan.md) (Hunyuan-A13B Q4_K_M ~49 GB on 2× 4090), [Falcon](../models/falcon.md) (Falcon-H1-34B Q4 ~17 GB; FP16 ~68 GB across GPUs)
- **Runtimes that target this tier:** [vLLM](../runtimes/vllm.md), [SGLang](../runtimes/sglang.md), [TGI](../runtimes/tgi.md), [llama.cpp](../runtimes/llama-cpp.md) (CPU offload)
