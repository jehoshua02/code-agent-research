# Lesson 4.10 — Reading Code You Didn't Write

## The Big Idea

AI writes code fast. Sometimes too fast to understand.

You paste in a prompt, it generates 50 lines of code, and you copy it into your project without really knowing what it does.

That works until it breaks. Then you have no idea where to even start.

This lesson is about building the habit of understanding the code you use — even if you didn't write it.

---

## Do This First

Grab any piece of AI-generated code you've used recently. If you don't have one, ask the AI to generate a function right now.

Paste it into Claude or ChatGPT with this prompt:

> "Explain this code like I'm new to coding. Go section by section. After each section, check if I have questions before moving on."

Read the explanation. For each section, ask follow-up questions until you could explain that section yourself in one sentence.

---

## Why You Need to Understand Code You Didn't Write

**Reason 1: You have to maintain it.**
Code breaks. When it does, you need to know where to look. If the code is a black box, you're stuck.

**Reason 2: You have to modify it.**
Your app will grow. You'll need to add features, change behavior, connect new parts. You can't do that if you don't understand what's already there.

**Reason 3: Bugs hide in code that "looks fine."**
AI-generated code often looks clean and correct. The bugs are subtle. You won't catch them by just reading — you need to understand what each part is supposed to do.

---

## A Method That Works

When you get AI-generated code, do this:

1. **Read it once, top to bottom.** Don't worry about understanding it. Just see the shape.
2. **Identify the main sections.** Where does data come in? Where does it get processed? Where does it go out?
3. **Ask AI to label it.** "Add a comment above each section explaining what it does."
4. **Ask about anything that confuses you.** "What does this line do? Why is it needed?"
5. **Test your understanding.** Cover the code and explain it in plain English. If you can't, go back.

---

## What You're Actually Looking For

You don't need to understand every character. You need to understand:

- What goes in (inputs)
- What comes out (outputs)
- What changes happen in the middle (logic)
- What could go wrong (edge cases)

That's enough to use it, fix it, and modify it.

---

## You Don't Have to Be the One Who Writes Everything

Good developers read other people's code constantly. Libraries, frameworks, open source projects — almost no one writes everything from scratch.

The skill isn't memorizing syntax. It's reading code and quickly figuring out what it does. AI makes you faster at writing. Understanding makes you capable of debugging.

---

## Key Takeaway

Don't ship code you don't understand. Use AI to explain it to you. One section at a time is enough. The goal isn't mastery — it's knowing enough to fix it when it breaks.

---

[< Previous: MCP and Tool Use: Giving AI Superpowers](09-mcp-and-tool-use.md) | [Next: Final Project Kickoff: Pick Your Idea >](11-final-project-kickoff.md)
