# Lesson 4.07 — When AI Gets It Wrong: Debugging AI Output

## The Big Idea

AI makes mistakes. Confidently, smoothly, with perfect grammar.

That's what makes it dangerous. It doesn't say "I'm not sure." It just gives you wrong code that looks right.

The skill isn't avoiding AI mistakes — that's impossible. The skill is catching them fast and fixing them efficiently.

---

## Do This First

Ask ChatGPT or Claude to write a small Python function — something like:

> "Write a Python function that takes a list of numbers and returns the average."

Copy the code into your editor or Replit. Run it. Check if it actually works.

If it works, try to break it. What happens if you pass an empty list? Does it crash?

Tell the AI exactly what happened:

> "When I pass an empty list, I get this error: ZeroDivisionError. Fix it."

Let it fix the code. Run it again.

---

## The Most Common AI Code Mistakes

**Wrong logic**
The code runs but gives the wrong answer. Classic example: off-by-one errors, wrong math, bad conditions.

**Outdated information**
AI was trained on data up to a certain date. It might use an old API that no longer works, or a library that changed its syntax.

**Misunderstood requirements**
You asked for one thing, the AI built something similar but different. Not a lie — it just interpreted your prompt differently than you intended.

**Made-up functions**
Sometimes AI invents function names that sound real but don't exist. This is called a "hallucination." Running the code immediately reveals this.

---

## The Debugging Loop

When AI output doesn't work:

1. **Run it.** Don't just read it. Running code finds bugs that reading misses.
2. **Copy the exact error.** Don't paraphrase. Give the AI the full error message.
3. **Tell it what you expected vs. what happened.** "I expected X, but I got Y."
4. **Ask it to fix it.** Watch what it changes and why.
5. **Run again.** Repeat until it works.

---

## Your Job in This Loop

You are not a passive receiver of AI output. You are the tester.

AI generates. You run. You report. AI fixes.

This loop is basically how professional developers work with AI too. The human provides feedback; the AI adjusts. Neither one is doing it alone.

---

## A Useful Prompt for Debugging

> "This code throws [exact error] when I run it. Here's the code: [paste code]. What's wrong and how do I fix it?"

Specific error + code + question = fast fix.

---

## Key Takeaway

Never trust AI code without running it. Errors are normal. Your job is to run, report, and iterate — not to find AI that never makes mistakes.
