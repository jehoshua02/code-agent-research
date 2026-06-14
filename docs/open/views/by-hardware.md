# View — By Hardware

What fits at each VRAM tier. Tier descriptions are rough rules of thumb — exact fit depends on quantization, context length, KV cache, and concurrent processes. System RAM matters when offloading.

## 1. 8 GB

_RTX 3070 / 4060 / 4060 Ti 8GB-class. 7B Q4_K_M fits with room for context. 13B is tight and may require heavy quant or partial offload._

## 2. 12 GB

_RTX 3060 12G / 4070 / 5070-class. 13B Q4 fits. 14B is feasible at smaller context._

## 3. 16 GB

_RTX 4080 / 4070 Ti Super / pro 16G. ~20B Q4 fits. MoE starts to make sense — active params determine compute, total params determine VRAM, so MoE only helps if total fits._

## 4. 24 GB

_RTX 3090 / 4090. 30–34B Q4 comfortable. 70B requires heavy quant (Q2/Q3) and CPU offload — workable but slower._

## 5. 24 GB+ multi-GPU

_2× 3090 / single 5090 / pro cards. 70B Q4 comfortable. 100B+ MoE feasible with enough system RAM for offload._
