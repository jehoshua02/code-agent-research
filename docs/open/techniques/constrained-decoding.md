# Constrained decoding (JSON mode, grammar)

_Last verified: 2026-06-14_

## 1. What It Is

Constrained decoding masks token logits at each generation step to enforce a grammar or schema (JSON, regex, context-free grammar), guaranteeing parseable output. Implemented in llama.cpp grammars, dottxt/Outlines, vLLM's structured output, and OpenAI Structured Outputs.

## 2. Problem It Solves

LLMs generate free-form text that may not conform to required schemas. Even with explicit JSON instructions in the prompt, models occasionally produce malformed JSON (missing braces, trailing commas, invalid escape sequences) or deviate from the required field names and value types. Downstream code that parses the output then fails at runtime, requiring expensive retry logic or manual error handling.

## 3. How It Works

At each token generation step, a logit processor computes which tokens are valid continuations of the output so far under a formal grammar (JSON schema, regex, context-free grammar). Invalid tokens have their logits set to negative infinity before sampling, so they can never be selected. The result is guaranteed to be a valid instance of the grammar by construction. Formalized by Willard & Louf 2023 (Outlines paper).

```
grammar = JSONSchema(schema_definition)
logits_processor = GrammarLogitsProcessor(grammar)
tokens = []
while not grammar.is_complete(tokens):
    logits = model.forward(tokens)
    logits = logits_processor.mask(logits, tokens)  # zero out invalid tokens
    token = sample(logits)
    tokens.append(token)
```

## 4. When To Use

Use constrained decoding when the output must conform to a schema consumed by code — API responses, structured extraction into typed data, SQL generation, function call arguments. It eliminates a class of parse errors and removes the need for retry-on-parse-failure logic.

## 5. When Not To Use

Avoid constrained decoding for open-ended creative tasks where the grammar is too restrictive and would force unnatural word choices. If the target model already has native JSON mode (e.g., OpenAI `response_format: json_object`), the provider's implementation is usually simpler to use than a custom grammar layer. Constrained decoding adds overhead to each token generation step.

## 6. Implementations

- **Outlines** (`dottxt-ai/outlines`) — Python library; JSON schema, regex, and CFG constraints; works with Transformers, llama.cpp, vLLM backends
- **llama.cpp** — `--grammar-file` flag accepts GBNF grammar files; built into the inference runtime
- **guidance** (Microsoft) — interleaved generation and constraint language; supports handlebars-style templates
- **vLLM** — `guided_decoding` parameter with JSON schema, regex, or grammar; uses Outlines under the hood
- **SGLang** — structured generation with regex and JSON schema constraints built into the serving runtime

## 7. Sources

- [OpenAI Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) — observed 2026-06-14
