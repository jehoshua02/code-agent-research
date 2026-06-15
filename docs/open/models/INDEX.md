# Models — Index

One row per family. Click through for variant details.

| Family | Maker | Sizes | License | Context | Notes |
|---|---|---|---|---|---|
| [Command R](command-r.md) | Cohere | Command-R-35B, Command-R-32B, Command-R+-104B, Command-R7B-7B, Command-A-111B | CC-BY-NC 4.0 | 262K | CC-BY-NC license blocks production use without a separate Cohere commercial agreement |
| [DBRX](dbrx.md) | Databricks | DBRX-Base, DBRX-Instruct | Databricks Open Model License | 32K | No updates since March 2024; largely superseded by Llama 3 and Qwen 2.5 class models |
| [DeepSeek](deepseek.md) | DeepSeek AI | V2, V2.5, V3, V3-0324, R1, R1-0528, R1-Distill-Qwen-1.5B, R1-Distill-Qwen-7B, R1-Distill-Qwen-14B, R1-Distill-Qwen-32B, R1-Distill-Llama-8B, R1-Distill-Llama-70B | MIT | 131K | V3/R1 weight license is DeepSeek (not MIT); R1 distill variants are MIT; tool calling added in R1-0528 |
| [Falcon](falcon.md) | TII | Falcon-7B, Falcon-40B, Falcon-180B, Falcon3-1B, Falcon3-3B, Falcon3-7B, Falcon3-10B, Falcon-H1-0.5B, Falcon-H1-1.5B, Falcon-H1-3B, Falcon-H1-7B, Falcon-H1-34B, Falcon-H1R-7B | Apache-2.0 | 262K | Falcon-180B uses TII Falcon License (non-Apache); Falcon 1 series limited to 2K context — effectively obsolete |
| [Gemma](gemma.md) | Google | 1B, 2B, 4B, 7B, 9B, 12B, 27B, E2B, E4B, 26B-A4B, 31B | Gemma Terms of Use | 262K | Gemma 1–3 require license-acceptance gating; Gemma 4 is Apache 2.0 and ungated |
| [Granite](granite.md) | IBM | Granite-3.1-1B-A400M, Granite-3.1-2B, Granite-3.1-3B-A800M, Granite-3.1-8B, Granite-3.3-2B, Granite-3.3-8B | Apache-2.0 | 131K | Tops out at 8B; explicit data provenance documentation makes it suitable for regulated industries |
| [Hermes](hermes.md) | Nous Research | Hermes-3-8B, Hermes-3-70B, Hermes-3-405B | Llama Community License | 131K | Fine-tune of Llama 3.1; inherits Llama 700M MAU cap; trained at 8K context so long-context quality may degrade |
| [Hunyuan](hunyuan.md) | Tencent | Hunyuan-Large-389B, Hunyuan-A13B-Pretrain, Hunyuan-A13B-Instruct, Hunyuan-A13B-Instruct-FP8, Hunyuan-A13B-Instruct-GPTQ-Int4 | Tencent Hunyuan License | 262K | Proprietary Tencent license — not Apache 2.0; minimum 2× RTX 4090 even at Q4 |
| [Llama](llama.md) | Meta | 1B, 3B, 8B, 70B, 405B, Scout-17B-16E, Maverick-17B-128E | Llama Community License | 128K | Broadest ecosystem support; community-license restricts apps over 700M MAU |
| [Mistral](mistral.md) | Mistral AI | 7B, Mixtral-8x7B, Mixtral-8x22B, NeMo-12B, Large-2407, Codestral-22B, Small-3.1-24B, Large-3-675B | Apache-2.0 | 262K | Codestral v0.1 and Large-2407 are non-commercial; check license per variant |
| [Nemotron](nemotron.md) | NVIDIA | Nemotron-4-340B-Base, Nemotron-4-340B-Instruct, Nemotron-4-340B-Reward, Llama-3.1-Nemotron-70B-Instruct, Llama-3.1-Nemotron-70B-Reward | NVIDIA Open Model License | 131K | Nemotron-4-340B has only 4K context; Llama-3.1-Nemotron-70B inherits 128K from Llama 3.1 |
| [OLMo](olmo.md) | Allen Institute for AI | OLMo-2-7B, OLMo-2-7B-SFT, OLMo-2-7B-DPO, OLMo-2-7B-Instruct, OLMo-2-13B, OLMo-2-13B-SFT, OLMo-2-13B-DPO, OLMo-2-13B-Instruct | Apache-2.0 | 4K | Full pipeline open (weights + data + training code); English-only; 4K context is a hard limitation |
| [Phi](phi.md) | Microsoft | Phi-3-mini-3.8B, Phi-3-small-7B, Phi-3-medium-14B, Phi-3.5-mini-3.8B, Phi-3.5-MoE-42B, Phi-3.5-Vision-4.2B, Phi-4-14B, Phi-4-mini-3.8B, Phi-4-multimodal-5.6B, Phi-4-reasoning-14B, Phi-4-reasoning-vision-15B | MIT | 131K | Phi-4 has only 16K native context; family is English-first despite some multilingual support |
| [Qwen](qwen.md) | Alibaba | 0.6B, 1.7B, 4B, 8B, 14B, 32B, 30B-A3B, 72B, 235B-A22B | Apache-2.0 | 131K | Qwen2.5 uses a proprietary Alibaba license; Qwen3 is Apache 2.0 |
| [SmolLM](smollm.md) | HuggingFace | SmolLM2-135M, SmolLM2-135M-Instruct, SmolLM2-360M, SmolLM2-360M-Instruct, SmolLM2-1.7B, SmolLM2-1.7B-Instruct | Apache-2.0 | 8K | English-only; 135M/360M are too small for instruction following; designed for on-device edge deployment |
| [StarCoder2](starcoder2.md) | BigCode | 3B, 7B, 15B | BigCode OpenRAIL-M | 16K | Base model only — no instruction tuning; largely superseded by Qwen2.5-Coder and DeepSeekCoder-V2 |
| [Yi](yi.md) | 01.AI | Yi-6B, Yi-6B-Chat, Yi-9B, Yi-9B-200K, Yi-34B, Yi-34B-Chat, Yi-34B-200K, Yi-1.5-6B, Yi-1.5-9B, Yi-1.5-34B, Yi-VL-6B, Yi-VL-34B | Apache-2.0 | 200K | Largely superseded by Qwen3 and Llama 3 as of mid-2025; no native tool-calling format |
