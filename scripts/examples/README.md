# Examples

Worked examples of `scripts/query.py` in action. Each file shows a real scenario, the queries used to narrow the field, and the recommendation that fell out.

Output snapshots are dated and will drift as the survey changes — the value here is the **method** (queries, refinements, reasoning), not the specific picks. Rerun against the current survey for current results.

## Available

| File | Scenario |
|---|---|
| [query-small-vram-coding.md](query-small-vram-coding.md) | 8 GB GPU, agentic coding, MCP-required, Apache 2.0 / MIT only |

## When to add a new example

When you (or a future contributor) work through a new scenario and the queries are worth keeping, drop a file here. Suggested naming: `query-<scenario-slug>.md`.

Include the constraints at the top, the queries with output, the final recommendation, and (optionally) a "what SQL gave us" reflection.

For your **personal** picking history — picks tied to your own machine, project goals, etc. — use `project/2-doing/002-local-agents-picks/` instead. Those are working notes; these are tool documentation.
