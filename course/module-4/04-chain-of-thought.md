# Lesson 4.04 — Chain of Thought: Make AI Show Its Work

## The Big Idea

AI sometimes gives wrong answers confidently. Like that one person in class who raises their hand fast but guesses wrong.

There's a simple fix: make the AI think out loud before answering.

This is called **chain of thought prompting**. You ask the AI to walk through its reasoning step by step. When it does that, it catches its own mistakes — and you catch them too.

---

## Do This First

Try this math problem with ChatGPT or Claude.

**Version 1 — just ask:**
> "A store sells apples for $1.20 each. You buy 7. You pay with a $10 bill. How much change do you get?"

**Version 2 — ask it to think:**
> "A store sells apples for $1.20 each. You buy 7. You pay with a $10 bill. How much change do you get? Think through this step by step."

Compare the answers. Version 2 should show its work. Check if it's right.

---

## What Just Happened

When you add "think step by step," the AI slows down (metaphorically). It:

1. Calculates the total cost first
2. Then subtracts from $10
3. Then gives the answer

When it just blurts an answer, it skips steps — and that's where errors sneak in.

---

## Why Thinking Out Loud Helps

Your math teacher makes you show your work for the same reason. When you write out each step, you catch mistakes you'd miss if you just tried to do it in your head.

AI has the same problem. It predicts words one at a time. If it jumps to the answer too fast, it's guessing based on pattern — not actually calculating.

Forcing it to write the steps forces it to actually do the work.

---

## When to Use This

Use chain of thought when:

- The problem involves multiple steps (math, logic, planning)
- The AI keeps giving you wrong or weird answers
- You need to trust the answer (so you need to verify the reasoning)
- You're debugging something and want to understand the AI's logic

You don't need it for simple questions. "What's the capital of France?" doesn't need step-by-step reasoning.

---

## Phrases That Trigger It

These all work:

- "Think step by step."
- "Walk me through your reasoning."
- "Show your work."
- "Before you answer, reason through it carefully."

---

## Key Takeaway

When accuracy matters, make the AI show its work. One short phrase can cut errors dramatically on anything involving logic, math, or multi-step reasoning.
