# Lesson 4.03 — Few-Shot Prompting: Show, Don't Just Tell

## The Big Idea

Describing what you want in words is hard. Showing an example is easy.

This is true for humans. It's also true for AI.

"Few-shot prompting" just means giving the AI a few examples of the output you want before asking for the real thing. It learns the pattern from your examples way faster than from your description.

---

## Do This First

Ask ChatGPT or Claude this:

> "Convert these to a fun product description.
>
> Input: Blue hoodie, size M, $29
> Output: Stay cozy in this ocean-blue hoodie. Soft, casual, and perfect for any weather. Grab yours for just $29.
>
> Input: Red sneakers, size 10, $65
> Output: These fire-red sneakers are built for heads that want to stand out. Cushioned, bold, and worth every dollar at $65.
>
> Input: Black backpack, 30L, $45
> Output:"

See what it gives you. It should follow the exact same style and energy as your examples.

---

## What Just Happened

You didn't have to write a long description like: "Make it casual, punchy, enthusiastic, two sentences, mention the price at the end..."

You just showed it twice. The AI figured out the pattern.

This is called "few-shot" because you give it a few examples (shots) before the real request.

---

## Why This Works Better Than Describing

Imagine teaching someone to draw a cartoon face. You could spend ten minutes explaining proportions, or you could just show them three examples.

The examples communicate faster than words.

AI is the same. It's been trained on patterns. Give it a pattern to follow, and it snaps right into it.

---

## How Many Examples Do You Need?

- **Zero examples** (zero-shot) — works for simple, clear tasks
- **One example** — helps a lot already
- **Two or three examples** — usually enough to lock in the pattern
- **More than five** — often not worth it; you're burning prompt space

Start with two. Add more only if the output is still off.

---

## Where This Is Useful

- Formatting data (turning messy input into clean output)
- Writing in a specific style or tone
- Generating structured content like lists, cards, or summaries
- Any time you keep getting the wrong format back

---

## Key Takeaway

When you can't describe what you want, show it. Two examples beat two paragraphs of instructions almost every time.

---

[< Previous: Role Prompting: Give the AI a Job](02-role-prompting.md) | [Next: Chain of Thought: Make AI Show Its Work >](04-chain-of-thought.md)
