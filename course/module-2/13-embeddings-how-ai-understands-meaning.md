# Lesson 2.13 — Embeddings: How AI Understands Meaning

## Try this first

Ask ChatGPT:

**"What's more similar to 'dog' — 'puppy' or 'bark'? Explain why."**

Read the answer carefully. Notice it's not just comparing the words — it's comparing what they mean.

Now ask: **"What's more similar to 'cold' — 'freezing' or 'ice cream'?"**

The AI reasons about meaning, not just spelling or letters.

---

## Words as locations

Here's a mind-bending idea.

Imagine every word had a location in space. Words with similar meanings are close together. Words with very different meanings are far apart.

- "happy" and "joyful" would be near each other.
- "dog" and "puppy" would be close.
- "dog" and "algebra" would be far apart.

This is basically what an **embedding** is.

---

## What is an embedding?

An embedding is a list of numbers that represents the meaning of a word or sentence.

Those numbers act like coordinates — a position in meaning-space.

When AI needs to compare two pieces of text, it converts them to embeddings and measures how close the numbers are.

Close numbers = similar meaning.

---

## Why is this useful?

Because searching by meaning is way more powerful than searching by exact words.

Normal search: "dog care tips" only finds pages with those exact words.

Embedding search: also finds pages about "puppy health" and "pet grooming" — because those are close in meaning-space.

---

## Where you've already seen this

Search engines, recommendation systems, and chatbots all use embeddings behind the scenes.

- When YouTube recommends videos you'd like, it's comparing the embeddings of what you watched.
- When Gmail suggests "Did you mean?" — embeddings.
- When AI understands that "car" and "automobile" mean the same thing — embeddings.

---

## You don't need to do the math

You won't be writing embedding code today. This is just about understanding what's happening.

The key idea is: AI doesn't just match words. It matches meaning.

---

## The key idea

> Embeddings let AI compare meaning, not just words. "Happy" and "joyful" are similar in meaning-space, so the AI knows they're related even if the letters are different.

---

## Activity

Ask ChatGPT these questions:

- "Which is more similar to 'run' — 'sprint' or 'walk'?"
- "Which is more similar to 'enormous' — 'huge' or 'tiny'?"
- "Which is more similar to 'sad' — 'unhappy' or 'raincoat'?"

**Look at how it explains the reasoning. Does it reference meaning, feeling, or context?**

---

[< Previous: What Is RAG? (Retrieval-Augmented Generation)](12-what-is-rag.md) | [Next: Review: Talking to AI Smarter >](14-review-talking-to-ai-smarter.md)
