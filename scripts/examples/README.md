# Examples

Worked examples of the survey's query scripts in action. Each file shows a real scenario, the queries used to narrow the field, and the recommendation that fell out.

Output snapshots are dated and will drift as the survey changes — the value here is the **method** (queries, refinements, reasoning), not the specific picks. Rerun against the current survey for current results.

## Available

| File | Tool | Scenario |
|---|---|---|
| [pick-small-vram-coding.md](pick-small-vram-coding.md) | `pick.py` | 8 GB GPU, agentic coding, MCP-required, Apache 2.0 / MIT only |
| [query-small-vram-coding.md](query-small-vram-coding.md) | `query.py` (SQL) | Same scenario as above, worked via raw SQL |

## When to add a new example

When you (or a future contributor) work through a new scenario with one of the scripts and the queries are worth keeping, drop a file here. Suggested naming:

- `pick-<scenario-slug>.md` for `pick.py` walkthroughs
- `query-<scenario-slug>.md` for `query.py` / raw SQL walkthroughs

Include the constraints at the top, the queries with output, the final recommendation, and (optionally) a "what this tool gave us" reflection.

For your **personal** picking history — picks tied to your own machine, project goals, etc. — use `project/2-doing/002-local-agents-picks/` instead. Those are working notes; these are tool documentation.
