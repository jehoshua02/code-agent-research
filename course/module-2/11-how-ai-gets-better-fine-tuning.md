# Lesson 2.11 — How AI Gets Better: Fine-Tuning

## Try this first

If you have access to GitHub Copilot (or can use it through GitHub's free tier), open it and type a comment in a code file:

```
# function that adds two numbers
```

Watch what it suggests.

Then ask regular ChatGPT the same thing. Compare how they respond.

Notice that Copilot feels more "in the zone" for code? That's because it was fine-tuned.

---

## Starting from a base

Every AI model starts as a **base model** — trained on a massive mix of text. Wikipedia, news, books, forums, all of it.

The base model is pretty good at everything. But "pretty good at everything" isn't always what you need.

Sometimes you need "really good at one specific thing."

---

## What is fine-tuning?

Fine-tuning is a second round of training.

You take a base model and train it again — but this time on a smaller, focused dataset.

- Want a coding AI? Train it more on code.
- Want a customer service bot? Train it on customer conversations.
- Want a medical AI? Train it on medical journals.

The model starts knowing a lot. Fine-tuning makes it expert-level in a specific area.

---

## The athlete analogy

Think of the base model like a great all-around athlete. Decent at every sport.

Fine-tuning is like specializing. That athlete picks basketball and trains every day for two years.

They're still athletic in general. But now they're really good at basketball.

---

## Real examples

- **GitHub Copilot** — fine-tuned on millions of code repos. It "thinks" in code.
- **Medical AI tools** — fine-tuned on clinical notes and research papers.
- **Customer service bots** — fine-tuned on support ticket conversations.

Each one started from a strong base and got specialized.

---

## The key idea

> Fine-tuning trains a model further on specific data — turning a generalist into a specialist.

It doesn't replace the base training. It builds on top of it.

---

## Activity

Ask regular ChatGPT to autocomplete this code comment:

```
# function to reverse a string in Python
```

Then if you have Copilot access, try the same thing there.

If you don't have Copilot, ask ChatGPT: "How does GitHub Copilot differ from you? Why is it better at code?"

**Write down the biggest difference you noticed (or what ChatGPT said about it).**

---

[< Previous: Models Are Like Different Brains](10-models-are-like-different-brains.md) | [Next: What Is RAG? (Retrieval-Augmented Generation) >](12-what-is-rag.md)
