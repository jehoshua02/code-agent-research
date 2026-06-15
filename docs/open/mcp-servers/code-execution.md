# Code Execution

_Last verified: 2026-06-14_

## 0. TL;DR

A code-execution [MCP](../GLOSSARY.md#mcp-model-context-protocol) server lets an agent run Python, JavaScript, or other code in a sandboxed environment and get back real output — useful for data analysis, math, or anything that's safer to compute than to reason about from memory. Use one when the agent needs to process files, generate charts, or verify calculations. The main catch: even sandboxed environments have escape risks; prefer cloud-managed sandboxes (E2B, etc.) over local subprocess runners when the agent's code is untrusted.

## 1. What It Is

MCP servers in this category run code in a sandboxed environment (Python, JavaScript, etc.) and return results. Agents need them for data analysis, math, and any task safer to compute than to reason about. Notable community: E2B Code Interpreter MCP, Pyodide-based browsers, and various Docker-sandboxed runners.

## 2. Capability

Exposes sandboxed code execution to the agent. Common tools across implementations:

- **run_code** / **execute_code** — submit a code string in a target language (Python, JavaScript, etc.) and receive stdout, stderr, and return value; some implementations also return rich output (images, dataframes) as artifacts
- **install_package** — install a library into the sandbox session (E2B and similar cloud-based runners)
- **upload_file** / **read_file** — transfer files into or out of the sandbox environment
- **list_sessions** / **kill_session** — manage long-lived sandbox sessions with state persistence between calls (E2B)

Implementations differ on isolation model: cloud sandboxes (E2B) run code in ephemeral remote VMs; local runners use Docker containers, Pyodide (WASM in-browser), or sub-processes with resource limits.

## 3. Install

No Anthropic reference implementation. E2B is the most common cloud-sandboxed option:

```
npx -y @e2b/mcp-server
```

Docker-based local runners typically require Docker to be installed and running on the host. Container deployment is strongly recommended for any local code-execution server to limit the blast radius of arbitrary code.

## 4. Transport

stdio for local implementations (Docker-based, Pyodide). Cloud-based servers such as E2B connect to a remote sandbox API; the MCP server itself is typically spawned locally via stdio and makes outbound HTTPS calls to the E2B API. Streamable HTTP transport is used by some hosted variants.

## 5. Auth

- **Cloud sandboxes (E2B)**: require an `E2B_API_KEY` environment variable; sign up on the E2B platform to obtain one
- **Local Docker runners**: no credential-based auth; isolation relies on container boundaries and Docker daemon permissions
- **Pyodide runners**: no auth; isolation relies on WASM sandbox

## 6. Security Considerations

**Sandbox strength is the critical variable.** Subprocess-based runners (no container) offer essentially no isolation — arbitrary code runs as the agent's OS user with full filesystem and network access. Always use a container (Docker, gVisor) or a cloud sandbox (E2B) for any untrusted code path.

**Network egress.** Even containerized runners allow outbound network by default. A piece of agent-generated code can exfiltrate data to an external host or download and execute a second-stage payload. Explicitly drop outbound network in the container network policy unless the use case requires it.

**Resource exhaustion.** Unbounded CPU loops, memory allocation, or fork bombs can bring down the host or adjacent workloads. Enforce per-execution CPU time limits, memory caps (`--memory` in Docker), and PID limits.

**Package installation as an escape hatch.** `install_package` tools let the agent pull arbitrary third-party libraries into the sandbox at runtime. A malicious or typosquatted package can bypass sandbox controls or phone home. Pin allowed packages or disable the tool when not needed.

## 7. Documented Strengths

- **Verifiable computation**: agents can run Python or JavaScript to confirm calculations, process data, and generate charts rather than reasoning about numbers from memory — eliminating a major source of LLM arithmetic errors ([E2B MCP server docs](https://e2b.dev/docs/mcp)).
- **E2B cloud sandboxes remove host risk**: E2B runs code in ephemeral remote micro-VMs with full isolation, meaning no local Docker setup, no host resource risk, and automatic teardown after each session — the leading option for production use cases.
- **Pyodide (WASM) as a zero-install option**: browser-side Pyodide runners execute Python in WebAssembly with no server process, OS permissions, or network access — a convenient, genuinely isolated choice for lightweight data tasks.
- **Stateful sessions**: E2B's session model persists installed packages and in-memory state across multiple `run_code` calls, enabling multi-step data analysis workflows without re-importing libraries each turn.

## 8. Documented Weaknesses

- **Cloud sandbox cost**: E2B bills per sandbox-second; an agentic loop running many code cells against a long-lived sandbox accumulates charges quickly, and there is no built-in per-session budget cap in the MCP server itself ([E2B pricing](https://e2b.dev/pricing)).
- **Subprocess-based local runners offer no real isolation**: without Docker or gVisor, `run_code` executes as the agent's OS user with full filesystem and network access — functionally equivalent to a shell server, despite the "code execution" framing.
- **Network egress enables data exfiltration**: even cloud sandboxes allow outbound network connections by default; agent-generated code can POST data to external endpoints unless the operator explicitly restricts egress at the network layer.
- **Package installation as a runtime escape hatch**: `install_package` tools pull arbitrary third-party libraries at runtime; a typosquatted or malicious package can introduce second-stage payloads that evade static review of the agent's code string.

## 9. Sources

- [PulseMCP — code execution servers](https://www.pulsemcp.com/servers?q=code) — observed 2026-06-14
