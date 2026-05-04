# Lesson 4.13 — Final Project: Build with AI

## The Big Idea

You have a spec. Now you build.

This is where everything comes together — role prompting, context management, few-shot examples, chain of thought. You're going to use your AI tools to generate a real working app from a real document you wrote.

The goal of this lesson: get your app running, even if it's rough.

---

## Do This First

Take the spec you wrote in Lesson 4.12 and paste it into your AI tool of choice — Cursor, Replit, v0.dev, or Claude.

Use a prompt like this:

> "You are a senior web developer. I'm a beginner. Based on this spec, build me a working first version of this app. Use simple, readable code. Explain what you're building as you go. Here is the spec: [paste your spec]"

Let it generate. Read what it produces. Then get it running.

---

## Getting It Running

Depending on your tool:

- **Replit** — paste the code into a new project, hit Run
- **Cursor** — open a new folder, let Cursor generate files, run with the terminal
- **v0.dev** — paste your spec and let it generate a React component you can preview instantly

If you hit errors, go back to Lesson 4.07 (debugging AI output). Copy the exact error. Tell the AI what broke. Let it fix it.

Don't stop until the app actually opens and the main thing works.

---

## Build in Layers, Not All at Once

Don't try to build every feature in one prompt.

**Layer 1 — Core only.** Get the main feature working. For a to-do app, that's adding a task and seeing it in a list. Nothing else.

**Layer 2 — Add one feature at a time.** Once Layer 1 works, pick the next most important thing. One prompt per feature.

**Layer 3 — Polish.** Once it works, make it look better and handle edge cases.

This is how real apps are built. Not all at once — layer by layer.

---

## What to Do When the AI Gets It Wrong

This will happen. Here's the response:

1. Run it anyway. See exactly what breaks.
2. Tell the AI: "This broke. Here's the error: [paste error]. Here's what I expected: [explain]. Fix it."
3. Run again.

Don't rewrite the whole prompt. Target the specific broken piece.

---

## What "Running" Means

For this lesson, "running" means:

- The app opens without crashing
- The main feature works at least once
- You can click through it and show someone what it does

It doesn't mean it's perfect. It means it exists and works.

---

## Prompts That Help During Building

- "This isn't working. Here's the error: [error]. Fix just this part."
- "Add a [feature] to the existing app. Don't change anything else."
- "Explain what this section of code does before changing it."
- "The button isn't doing anything when I click it. What's wrong?"

---

## Key Takeaway

Feed your spec to the AI, get a first version running, then fix it layer by layer. Your goal today is a working app — not a perfect one. It will be rough. Ship rough.

---

[< Previous: Final Project: Spec It Out](12-final-project-spec.md) | [Next: Final Project: Iterate and Improve >](14-final-project-iterate.md)
