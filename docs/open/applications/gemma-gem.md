# Gemma Gem

_Last verified: 2026-06-14_

> **Borderline inclusion.** ★930 as of 2026-06-14 (under the ★1,000 adoption threshold) but distinct contribution: runs Gemma 4 entirely on-device via WebGPU. Revisit in 3 months.

## 0. TL;DR

Gemma Gem is a browser extension that runs Google's Gemma 4 [model](../GLOSSARY.md#model) entirely on-device via WebGPU — no install, no API key, no data leaving your machine, just load the extension in Chrome or Edge and the model runs in your browser tab. Pick it when you want a completely offline, zero-trust AI assistant and your browser supports WebGPU; it is best for privacy-sensitive tasks or environments where you cannot install local software. Being niche and early-stage (★930 as of 2026-06-14), the model choices are limited to Gemma variants and WebGPU support is still browser-dependent, so expect occasional compatibility gaps.

## 1. What It Is

Gemma Gem (kessler/gemma-gem) is an Apache 2.0 TypeScript application. Active. Runs Google's Gemma 4 model entirely on-device via WebGPU — no API keys, no cloud, no data leaving the machine. Model-specific by design.

## 2. Install

Platform: Chrome (113+) or Edge (113+) with WebGPU enabled. Requires `pnpm`.

```bash
pnpm install
pnpm build
```

Load the unpacked extension from `.output/chrome-mv3-dev/` via `chrome://extensions` (developer mode). Model weights (~500 MB for E2B, ~1.5 GB for E4B) are cached locally on first run. See [../README.md](../README.md#4-deployment-notes) for general reader-facing deployment context.

## 3. Interfaces

Browser extension (Chrome/Edge MV3). Injects a shadow-DOM chat overlay on any page (toggle via `Alt+G`). No standalone web UI, CLI, or API surface.

## 4. Model Compatibility

Bundled Gemma 4 via `@huggingface/transformers` + WebGPU (ONNX, q4f16 quantization, 128K context). Two variants: E2B (`onnx-community/gemma-4-E2B-it-ONNX`, ~500 MB) and E4B (`onnx-community/gemma-4-E4B-it-ONNX`, ~1.5 GB). Model-specific — Gemma 4 only, no external API or provider support.

## 5. Capabilities

General chat and coding assistance in any language Gemma 4 supports, running fully on-device via WebGPU. Because it is a browser extension, it has passive access to the current page (shadow-DOM overlay) but no active browser-automation, shell, file-system, or vision tool. Data analysis is limited to what the model can reason about from pasted text.

## 6. MCP Support

Not supported. Gemma Gem is a browser extension with no network egress or plugin protocol; MCP would require a local server bridge that is not implemented.

## 7. Extensibility

No plugin or skill system. The extension is intentionally minimal; all logic lives in the TypeScript source under `src/` (content script, service worker, popup). Customisation requires forking and rebuilding the MV3 extension.

## 8. Documented Strengths

Documented strengths from maintainer docs, benchmarks, or independent reviews. Cite source.

## 9. Documented Weaknesses

Documented limitations from issue tracker, docs, or community reports. Cite source.

## 10. Sources

- [kessler/gemma-gem](https://github.com/kessler/gemma-gem) — observed 2026-06-14
