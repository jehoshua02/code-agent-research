---
name: "Jan"
maker: "Menlo Research"
license: "AGPL-3.0"
license_category: "source-available"
status: "active"
url: "https://github.com/menloresearch/jan"
last_verified: "2026-06-14"
language: "TypeScript"
platforms: ["linux", "macos", "windows"]
gpu_backends: ["cuda", "rocm", "metal", "cpu", "vulkan"]
api_openai_compat: true
supports_mcp: "native"
formats: ["gguf", "mlx"]
notes: "Desktop chat app; GGUF-only for primary llama.cpp path; MLX backend added v0.7.7 for Apple Silicon."
---

# Jan

_Last verified: 2026-06-14_

## 0. TL;DR

Jan is a cross-platform desktop chat app — think a privacy-first, open-source alternative to ChatGPT that runs entirely on your own machine. Pick it if you want a polished GUI for chatting with local models on Mac, Windows, or Linux without touching the terminal. The catch is it's primarily a chat interface rather than a developer-facing API server, so it's less useful if you're building integrations or need programmatic access.

## 1. What It Is

Jan (menloresearch/jan) is an AGPL-3.0 TypeScript+Rust desktop application. Active. Cross-platform ChatGPT-style local interface that can run multiple inference backends under the hood; positioned as a privacy-first open alternative to commercial chat apps.

## 2. Install

Prebuilt installers from [jan.ai/download](https://jan.ai/download); no package manager.

- **macOS:** Universal `.dmg` (Apple Silicon and Intel).
- **Windows:** `.exe` installer, Windows 10+.
- **Linux:** `.AppImage` (portable, most distros) or `.deb` (Debian/Ubuntu); Flathub package available. No official `.rpm`.

System requirements: AVX2 CPU minimum (Haswell 2013+ / Excavator 2015+), 8 GB RAM and 6 GB VRAM minimum; 16 GB / 8 GB recommended; 32 GB+ with AVX512 optimal. Approx. 200 MB app + per-model storage.

## 3. Hardware Support

Primary engine is llama.cpp via a router process (v0.8.0+); other backends extend hardware coverage.

- **NVIDIA CUDA (Windows/Linux):** Driver ≥ 470.63.01, CUDA Toolkit 11.7+ (12.0 recommended, 13.x supported). AVX/AVX2/AVX512 llama.cpp builds. Cortex.TensorRT-LLM submodule available for high-throughput NVIDIA inference (CUDA 12.4.1, TensorRT 10.1.0).
- **AMD ROCm/HIP (Linux only, experimental):** Added in v0.8.2 (June 2026). Ranked above Vulkan when sufficient VRAM is detected. Windows ROCm/HIP not shipped.
- **Apple Metal:** Native via llama.cpp Metal build; **MLX backend** added in v0.7.7 for fully GPU-accelerated Apple Silicon inference. Unified memory allows 16 GB Macs to run 7B–13B models.
- **Vulkan:** Cross-platform fallback for AMD and Intel Arc on Windows/Linux.
- **CPU fallback:** Always available; AVX, AVX2, AVX512; broadest-compatibility build for non-AVX2 CPUs.
- **Multi-GPU:** llama.cpp layer-distribution; users supply a comma-separated device list to control GPU set and split.

## 4. Model Formats

- **GGUF (primary):** Only natively supported local format ("Local models are managed through Llama.cpp"). Supports all common quantizations (Q4_K_M, Q5_K_M, Q8_0, F16, …). MTP-capable models detected from GGUF metadata in v0.8.0+. Import via built-in Hub (HF-backed), Hugging Face repo ID, "Use this model" deep link, or local file.
- **MLX (Apple Silicon only):** MLX-Swift format via MLX backend; separate import path.
- **TensorRT-LLM (NVIDIA via Cortex.TensorRT-LLM):** Compiles LLM definitions into GPU-specific TRT engines; supports INT4/INT8 weights (FP16 activations) and SmoothQuant. Not a generic format importer.
- **safetensors:** Not directly loadable for inference; Hugging Face is used as a source for GGUF files. HF access token is configurable in settings.
- **Discovery UI:** Hub panel shows "Fits / May be slow / Won't fit" based on detected RAM/VRAM; pause/resume downloads (v0.8.2+).

## 5. API Surface

Local API server at `http://127.0.0.1:1337` described as "an OpenAI-compatible REST API."

- `POST /v1/chat/completions` — primary endpoint; streaming and tool/function calling.
- `GET /v1/models` — list available/loaded models.
- `POST /v1/messages` — Anthropic-compatible endpoint, auto-translated internally.
- `/v1/responses` — "Coming Soon."
- `/v1/completions`, `/v1/embeddings` — not documented.

**Tool / function calling:** On `/v1/chat/completions`. MCP tool calls executable server-side via "Execute Tools on Server" setting. **Vision (multimodal):** Image upload support added v0.6.9 ("Major multimodal support with image uploads"); Jan-v2-VL model in the hub; API-level details for multimodal inputs not spelled out. **Streaming:** Supported on `/v1/chat/completions` (SSE-style, per OpenAI compat). **Structured outputs:** JSON Schema File parameter (GBNF grammar constraint via llama.cpp); OpenAI-style `response_format: json_object` not explicitly called out. **Logprobs:** Not documented.

Sources: [api-server](https://jan.ai/docs/desktop/api-server), [api-preference](https://jan.ai/docs/desktop/api-preference), [model-parameters](https://jan.ai/docs/desktop/model-parameters).

## 6. Performance

Not benchmarked by maintainer. Jan's docs, README, and changelog contain no canonical tokens/sec, latency, or batch-size figures. The only performance-adjacent configuration exposed is GPU Layers, Context Length, a "Fit to Hardware" auto context optimization, and configurable Request Timeout — none constitute benchmark claims. Source: [model-parameters](https://jan.ai/docs/desktop/model-parameters).

## 7. Documented Strengths

- **Privacy-first, fully local:** "Everything runs locally when you want it to" — no data leaves the machine; no cloud account required. Source: [README](https://github.com/menloresearch/jan).
- **Polished cross-platform desktop GUI:** Native installers for Windows 10+, macOS 13.6+, and Linux (AppImage/deb/Flathub); UI includes "Fits / May be slow / Won't fit" VRAM guidance and pause/resume downloads. Source: [jan.ai/download](https://jan.ai/download).
- **Multiple hardware backends in one app:** llama.cpp (CPU/CUDA/ROCm/Metal/Vulkan), MLX (Apple Silicon), and Cortex.TensorRT-LLM (NVIDIA) all accessible through the same interface. Source: [Hardware docs](https://jan.ai/docs/desktop/).
- **OpenAI- and Anthropic-compatible local API:** `localhost:1337` exposes `/v1/chat/completions` and `/v1/messages` (auto-translated Anthropic format), enabling drop-in local use by any OpenAI-compatible client. Source: [api-server docs](https://jan.ai/docs/desktop/api-server).

## 8. Documented Weaknesses

- **GGUF-only local inference (primary path):** The llama.cpp backend accepts GGUF exclusively; safetensors, GPTQ, AWQ, and EXL2 are not directly loadable. Source: [README](https://github.com/menloresearch/jan).
- **Desktop app, not a production server:** No concurrent request batching or multi-user serving layer; designed for single-user interactive chat, not API throughput. Source: [README](https://github.com/menloresearch/jan).
- **Published security CVEs in 2025:** Four CVEs issued (CVE-2025-2446 path traversal, CVE-2025-2439 GGUF parser OOB read, CVE-2025-2445 Python engine command injection, CVE-2025-2447 missing CSRF). Source: [SecurityWeek, March 2025](https://www.securityweek.com/vulnerabilities-expose-jan-ai-systems-to-remote-manipulation/).
- **No GGUF validation on load:** Jan allows chatting with a partially downloaded model without error, causing hard-to-diagnose malfunctions. Source: [issue #5266](https://github.com/janhq/jan/issues/5266).

## 9. Sources

- [menloresearch/jan](https://github.com/menloresearch/jan) — observed 2026-06-14
