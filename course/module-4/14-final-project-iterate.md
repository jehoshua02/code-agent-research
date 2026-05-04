# Lesson 4.14 — Final Project: Iterate and Improve

## The Big Idea

No app is done after the first version. Every app you've ever used went through hundreds of rounds of "build, test, fix, repeat."

This process is called **iteration**. And it's not a sign that you failed the first time — it's literally how software development works.

Your job this lesson: use what's broken to make it better.

---

## Do This First

Open your app. Use it like a real user would. Try to break it.

Write down every problem you notice. Don't fix anything yet — just list them. Aim for at least 5 things:

1. [Something that's wrong or missing]
2. [Something that's wrong or missing]
3. [Something that's wrong or missing]
4. [Something that's wrong or missing]
5. [Something that's wrong or missing]

Now pick 3 of them to fix. Not all 5. Just 3.

For each one, write a prompt and fix it with AI. When each fix is done, document what prompt worked.

---

## What "Using It Like a Real User" Means

Don't just click the happy path — the perfect scenario where everything goes right.

Try the messy paths:

- What happens if you submit an empty form?
- What if the text is really long?
- What if you click fast multiple times?
- What happens on a small phone screen?
- What if you refresh the page mid-task?

Real users do all of these things. If your app breaks on them, that's a bug worth fixing.

---

## How to Write a Good Fix Prompt

Bad: "Fix the bug."

Good: "When I submit the form with an empty input, the app crashes with this error: [error]. The expected behavior is that nothing happens and I see a message that says 'Please enter a task.' Fix only this issue."

Specific problem + specific expected behavior + "fix only this" = cleaner fixes, less chance of breaking other things.

---

## Document What Worked

This is the part most people skip. Don't skip it.

Keep a simple log as you go:

| Problem | Prompt Used | Did It Work? |
|---------|-------------|--------------|
| Empty form crashes | "When I submit empty..." | Yes |
| Button invisible on mobile | "On small screens, the button..." | Took 2 tries |
| Data resets on refresh | "Store tasks in localStorage..." | Yes |

This log teaches you which prompting patterns work. Next project, you'll be faster.

---

## The Temptation to Add Features

When you're iterating, it's easy to get excited and start adding new features instead of fixing existing problems.

Resist this. Fix what's broken first. Then, after your 3 fixes are done, you can add one new thing if you have time.

Finished and working beats fancy and broken.

---

## What Good Enough Looks Like

You don't need to fix everything. You need to reach the point where:

- The main feature works reliably
- The app doesn't crash on normal use
- It looks like something you'd be okay showing to someone

That's good enough to ship. Perfect is for later.

---

## Key Takeaway

Iteration is not optional — it's the job. Use your app, find 5 problems, fix 3 of them using well-crafted prompts, and document what worked. Real development is this loop, repeated until it's good enough.

---

[< Previous: Final Project: Build with AI](13-final-project-build.md) | [Next: Final Project: Ship It >](15-final-project-ship-it.md)
