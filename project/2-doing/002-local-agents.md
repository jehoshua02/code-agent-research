# Local AI Agents — Survey, Setup, Harness

## Abstract

Run AI agents at home on owned hardware, free, for coding + research/web + writing + personal automation + data analysis. Survey the landscape, stand up a working stack, and benchmark agents head-to-head before committing to one.

## Priority: 2

- Value: 7/10 — Reduces reliance on paid APIs; reusable infra for everything downstream.
- Momentum: 1/10 — Brand new work, no prior local-stack experience.
- Effort: 8/10 — Broad survey + new stack + harness over 2-4 weeks.
- Risk: 4/10 — Hardware ceiling (8GB VRAM) constrains which models can actually be run/benchmarked locally, but does **not** constrain survey breadth.

## Timeline

- Captured: 2026-06-13
- Refined: 2026-06-13
- Started:
- Verified:
- Done:

Horizon: 2-4 weeks.

## Details

### Motivation

Frustrated with paid model token limits while a capable home PC sits idle. Want to test multiple agents/models on owned hardware without optimizing for any single variable yet — gather unbiased breadth first, then decide.

### Hardware and current environment

- Home PC: RTX 3070 (8GB VRAM). Upgrade only if proven necessary.
- Current preferred deployment for the running stack: Linux (bare-metal, WSL2 on Windows, OrbStack on Mac, or cloud Linux). Open to changing this if the model or runtime worth running requires another platform (e.g. macOS for MLX).
- Survey scope (deliverable 1) is **not** bound by current hardware or current environment — covers everything regardless of fit.

### Access

Remote access is required — not tethered to the PC. SSH and/or web UI. The more access methods, the better.

### Scope of tasks

Beyond coding, agents should handle:

- Research / web browsing
- Writing / content
- Personal automation (files, scripts, scheduling)
- Data analysis

### Constraints

- Fully offline — no paid APIs, including for grading.
- MCP-compatible only — agents must speak MCP for tool use.
- Reproducible — pinned versions, seeds, deterministic where possible.

### Deliverables (in order)

1. **Survey doc** — broad survey of every open-weight model and self-hostable component that meets the [inclusion criteria](../../docs/open/README.md#22-inclusion-criteria), including ones that don't fit on the 3070. Breadth before depth. Lives in this repo. Multi-dimensional:
   - By layer: models / runtimes / agent frameworks / MCP servers / techniques (plus applications as a non-layer category)
   - By task: coding / research / writing / automation / data
   - By hardware tier: 8 / 12 / 16 / 24 / 24+ GB (filters fit, doesn't bound scope)
2. **Working local stack** — pick something from the survey that fits the 3070, install, get something running end-to-end. Stack choice is hardware-bound; survey is not.
3. **Test harness** — public benchmarks only (SWE-bench, GAIA, MMLU, HumanEval, etc.), programmatic grading only.

### Priorities for picking what to test

Unbiased breadth. Not optimizing for tool-use quality, output quality, speed, or ecosystem fit yet — gather data across all dimensions before narrowing.

## Verification

- Survey doc covers all three dimensions (layer, task, hardware tier).
- Local stack runs at least one agent against at least one benchmark task.
- Harness produces reproducible, programmatically-graded results for 2+ agents on 2+ benchmarks.
