# Cloud APIs

_Last verified: 2026-06-14_

## 0. TL;DR

A cloud-API [MCP](../GLOSSARY.md#mcp-model-context-protocol) server lets an agent interact with AWS, GCP, Azure, or Cloudflare resources — listing buckets, querying logs, deploying functions — through natural language instead of raw CLI commands. Use one when building DevOps agents that need to inspect or manage cloud infrastructure. The main catch: write operations are real and often irreversible, so gate destructive actions behind explicit confirmation steps and use least-privilege IAM roles.

## 1. What It Is

MCP servers in this category wrap cloud-provider APIs (AWS, GCP, Azure) to expose resources, run commands, or query telemetry. Agents need them for cloud operations, cost analysis, and infrastructure-as-code workflows. Notable community: AWS MCP, GCP MCP, Azure MCP, and Cloudflare's official MCP servers.

## 2. Capability

Exposes cloud-provider resource management and query operations. Tools vary by provider but commonly include:

- **list_resources** / **describe_resource** — enumerate or inspect cloud resources (EC2 instances, S3 buckets, GCS objects, Azure VMs, etc.)
- **run_query** / **execute_command** — invoke a provider CLI or SDK call and return structured output
- **get_logs** / **query_metrics** — retrieve CloudWatch, Cloud Logging, or Azure Monitor data
- **deploy** / **update_resource** — create or modify infrastructure resources (often gated behind explicit write-mode flags)
- **list_deployments** / **rollback** — manage deployments or release history

Cloudflare's official servers expose Workers, KV, R2, D1, and AI Gateway operations. AWS community servers wrap the AWS SDK or CLI. GCP and Azure servers similarly wrap their respective SDKs.

## 3. Install

No single reference implementation; each provider has its own package. Examples:

Cloudflare (official, Node.js):

```
npx -y @cloudflare/mcp-server-cloudflare
```

AWS community servers are typically Node.js or Python:

```
npx -y @aws-mcp/mcp-server-aws
```

```
uvx awslabs.core-mcp-server
```

Host install is standard when using ambient credentials (AWS profile, gcloud ADC, Azure CLI login). Container deployment is viable if credentials are injected via environment variables or mounted credential files.

## 4. Transport

stdio for locally spawned servers (the most common pattern for CLI/SDK-based servers). Cloudflare's hosted MCP servers use streamable HTTP with OAuth 2.1, accessible directly from MCP clients without a local process. AWS and GCP remote variants also use streamable HTTP when offered as hosted endpoints.

## 5. Auth

Credentials are passed via environment variables or ambient SDK credential chains — not through MCP protocol-level auth:

- **AWS**: `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` / `AWS_SESSION_TOKEN`, or ambient `~/.aws/credentials` / instance role
- **GCP**: Application Default Credentials (`gcloud auth application-default login`) or `GOOGLE_APPLICATION_CREDENTIALS` pointing to a service account JSON
- **Azure**: Azure CLI login (`az login`) or `AZURE_CLIENT_ID` / `AZURE_CLIENT_SECRET` / `AZURE_TENANT_ID`
- **Cloudflare remote servers**: OAuth 2.1 authorization code flow; the MCP client handles the browser-based consent prompt

## 6. Security Considerations

**Credential scope — least-privilege IAM is mandatory.** Ambient credentials (instance roles, `gcloud` ADC, `~/.aws/credentials`) typically carry broad permissions. An agent with `AdministratorAccess` can delete all resources or exfiltrate secrets. Create a dedicated IAM role or service account scoped to only the resources and actions the agent needs.

**Blast radius of irreversible mutations.** Write tools like `delete_bucket`, `terminate_instances`, or `destroy_stack` can cause instant, hard-to-reverse outages. Gate destructive tools behind an explicit confirmation step or disable them when only read/query access is needed.

**Cost runaway via runaway provisioning.** An agent in a loop can spin up thousands of compute instances or storage objects before a human notices. Set provider-level budget alerts and quotas; consider read-only mode for exploratory or analytical agent tasks.

**Cross-account access.** Servers configured with role-assumption or organization-level credentials can accidentally touch accounts other than the intended target. Scope credentials to a single account and verify `sts:GetCallerIdentity` / equivalent at startup.

## 7. Documented Strengths

Documented strengths from maintainer docs or community reports. Cite source.

## 8. Documented Weaknesses

Documented limitations from issue tracker or community reports. Cite source.

## 9. Sources

- [PulseMCP — cloud provider servers](https://www.pulsemcp.com/servers?q=cloud) — observed 2026-06-14
