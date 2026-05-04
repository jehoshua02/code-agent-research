# Lesson 3.15 — Push Your App to GitHub

## What You'll Learn

Your app works. But right now it only exists on your computer. If your hard drive fails, it's gone. If you want to show it to someone, you'd have to email them a file.

GitHub solves this. It stores your code online. It tracks every change you make. And it gives you a link you can share with anyone.

You learned the basics of Git in Module 1. This lesson puts it all together for a real project.

---

## Do This First

**Step 1 — Initialize Git in your project (if not already done)**

Open the terminal in VS Code. Run:

```
git init
```

If you already did this in Module 1, skip this step.

**Step 2 — Stage your files**

```
git add app.py idea.md
```

Add any other files you created for your app too.

**Step 3 — Commit**

```
git commit -m "Add my first AI-built app"
```

**Step 4 — Create a new repo on GitHub**

1. Go to [github.com](https://github.com) and log in.
2. Click the **+** button in the top right and select **New repository**.
3. Name it something like `my-first-ai-app`.
4. Leave it public so you can share the link.
5. Do NOT check "Initialize with README" — your project already exists.
6. Click **Create repository**.

**Step 5 — Connect and push**

GitHub will show you commands. Run them. They'll look like this:

```
git remote add origin https://github.com/yourusername/my-first-ai-app.git
git branch -M main
git push -u origin main
```

---

## Share the Link

Once pushed, your repo is live. Go to `github.com/yourusername/my-first-ai-app` and copy the URL. Send it to someone. You just shipped something.

---

## Why This Matters

Every project you build from now on should live on GitHub. It's your portfolio. It's your backup. It's proof that you made something real.

Recruiters look at GitHub. Collaborators work through GitHub. The entire open-source world lives on GitHub.

Starting now, every project gets pushed.

---

## Module 3 Complete

Look at what you just did across this module:

- Used chat AI to write and fix code
- Set up a real code editor with AI built in
- Tried four different AI tools and compared them
- Generated a UI from a text description
- Planned, built, and polished a complete app
- Pushed it to GitHub

That's not beginner stuff. That's how actual developers work today. You're doing it already.


---

[< Previous: Your First AI-Built App (Part 3: Fix and Polish)](14-first-ai-app-fix-and-polish.md) | [Next: Module 4 >](../module-4/01-prompts-are-programs.md)