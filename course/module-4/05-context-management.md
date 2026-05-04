# Lesson 4.05 — Context Management: What to Include and What to Cut

## The Big Idea

More isn't always better.

When you dump everything into a prompt — your whole codebase, three paragraphs of background, every requirement you can think of — the AI gets overwhelmed. Important stuff gets buried. You get worse output.

A lean, focused prompt almost always beats a bloated one.

---

## Do This First

Find a long prompt you've written, or write one that's clearly too long. Something like:

> "I'm building a to-do app for my school project and it needs to let users add tasks and delete them and mark them done and also filter by category and search and maybe have a dark mode and I'm using React and also I want it to look good and I'm not sure what to use for the database but maybe localStorage for now and also I need help with the login page..."

Now cut it in half. Keep only the most important thing you actually need right now:

> "I'm building a to-do app in React. Help me write the component for adding a new task. It should have an input field and a submit button."

Run both. The shorter one probably gives you something you can actually use.

---

## What Just Happened

The long version asked the AI to hold too many things at once. It didn't know what to focus on, so it either:
- Gave you a generic overview of everything
- Prioritized the wrong part
- Got confused and produced messy output

The short version gave the AI one clear job. It did that job well.

---

## The Rule: One Prompt, One Job

Think of each prompt like a single function in code. A function that does fifteen things is a bad function. A function that does one thing well is a good function.

Same with prompts.

---

## What to Cut

When trimming a prompt, remove:

- Background info the AI doesn't need to do this specific task
- Future requirements that aren't relevant yet
- Vague goals ("make it good", "make it professional")
- Redundant sentences that say the same thing twice
- Anything you included "just in case"

---

## What to Keep

Keep:

- The exact task you need done right now
- The format you want the output in
- Any constraints that would change the answer (language, library, etc.)
- One or two examples if the format matters

---

## When More Context Does Help

Sometimes context matters. If you're debugging a specific bug, paste the relevant code. If you're working with a specific library, name it.

The goal isn't to always write short prompts. It's to cut the stuff that doesn't help.

---

## Key Takeaway

When the AI gives you a bad response, your instinct might be to add more explanation. Often the real fix is to cut what's distracting it. One job per prompt.
