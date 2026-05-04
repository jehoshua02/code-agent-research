# Lesson 2.03 — Tokens: How AI Reads

## Try this first

Go to: **platform.openai.com/tokenizer**

Paste this sentence: `I am unbelievably happy today`

Look at how it splits up. Notice anything weird?

"unbelievably" probably splits into pieces. "I" is one token. "am" is one token. "today" is one token.

---

## AI doesn't read words

You read word by word. Or even letter by letter when you were learning.

AI reads in **tokens**.

A token is a chunk of text — could be a whole word, could be part of a word, could be punctuation.

---

## What counts as a token?

Here are some examples:

| Text | Tokens |
|------|--------|
| `cat` | 1 token |
| `unbelievable` | 2-3 tokens |
| `ChatGPT` | 2 tokens |
| ` hello` (with space) | 1 token |
| `!?!` | 3 tokens |

Common short words are usually one token. Rare or long words get split up.

---

## Why does this matter?

Two reasons.

**Reason 1: Cost.** AI services charge by the token. More tokens = more money. If you're building something with AI, keeping prompts short saves cash.

**Reason 2: Limits.** AI can only handle a certain number of tokens at once. If you go over the limit, it starts forgetting things or cuts you off.

You'll learn more about that limit in the next lesson.

---

## The emoji example

Paste an emoji into the tokenizer.

One emoji might be 2-3 tokens. That's why AI sometimes gets weird with emojis — it's reading them in chunks, not as a single character.

---

## The key idea

> AI doesn't read words. It reads tokens — chunks of text that can be whole words, parts of words, or single characters.

Understanding tokens helps you write better prompts and understand why AI sometimes stumbles on unusual words.

---

## Activity

Go to **platform.openai.com/tokenizer** and test these:

- Your full name
- A word from another language
- A made-up word like "flibbertigibbet"
- A few emojis

**Count how many tokens your full name takes. Write it down.**

---

[< Previous: What Is a Language Model?](02-what-is-a-language-model.md) | [Next: Context Window: AI's Working Memory >](04-context-window-ais-working-memory.md)
