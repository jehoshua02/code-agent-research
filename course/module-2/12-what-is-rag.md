# Lesson 2.12 — What Is RAG? (Retrieval-Augmented Generation)

## Try this first

Go to **perplexity.ai** (free, no account needed).

Ask it: "What happened in the news this week?"

Look at the answer. Notice the little numbered citations? Click one.

It links to a real article. That's not how regular ChatGPT works.

---

## The problem with base AI

Remember the training cutoff from Lesson 2.08?

Base AI models don't know about recent events. They can't browse the internet. Their knowledge is frozen.

That's a problem for anything time-sensitive.

**RAG** is one way to fix it.

---

## What does RAG stand for?

**Retrieval-Augmented Generation.**

That's a mouthful. Here's what it means:

- **Retrieval** — go look something up first
- **Augmented** — add that info to the prompt
- **Generation** — now generate an answer using that info

In short: the AI searches for relevant information, reads it, and uses it to answer your question.

---

## Like an open-book test

Normal AI answers from memory. That's a closed-book test.

RAG is an open-book test. Before answering, the AI gets to look things up.

The "looking up" part can mean:
- Searching the web
- Searching a database
- Searching a document you uploaded

Then it uses what it found to give you a better, more accurate answer.

---

## Why does this matter?

RAG lets AI:

- Answer questions about recent events
- Reference real documents and cite them
- Work with your own private data (like a company's internal files)

It's one of the main ways businesses use AI in production — connecting it to their actual information, not just general training data.

---

## The key idea

> RAG lets AI look things up before answering. It gets current information, reads it, and uses it to generate a better response.

This is why Perplexity can cite real sources and base ChatGPT often can't.

---

## Activity

Go to **perplexity.ai** and ask:

**"What are some AI tools released in the last 6 months?"**

Look at the citations. Click at least two to verify they're real articles.

Then ask the same thing on regular ChatGPT.

**What was different about the two answers? Which one did you trust more and why?**

---

[< Previous: How AI Gets Better: Fine-Tuning](11-how-ai-gets-better-fine-tuning.md) | [Next: Embeddings: How AI Understands Meaning >](13-embeddings-how-ai-understands-meaning.md)
