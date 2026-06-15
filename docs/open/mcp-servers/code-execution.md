# Code Execution

_Last verified: 2026-06-14_

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

Documented strengths from maintainer docs or community reports. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker or community reports. Cite source.

## 9. Sources

- [PulseMCP — code execution servers](https://www.pulsemcp.com/servers?q=code) — observed 2026-06-14
