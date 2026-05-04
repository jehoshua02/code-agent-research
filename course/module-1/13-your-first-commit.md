# Lesson 1.13 — Your First Commit

## The Big Idea

A commit is a saved snapshot of your project. Like saving a game at a checkpoint. Once you commit, you can always come back to that exact moment.

## Think About It This Way

Imagine you're writing an essay. You save a copy every time you finish a section. If you accidentally delete everything, you can load the last saved version.

A commit is that save. The difference is Git saves the entire project — every file — not just the one you're working on.

## Three Commands You Need

Here's the Git workflow, every time:

1. `git init` — start tracking a project (do this once per project)
2. `git add .` — tell Git which files to include in the next snapshot
3. `git commit -m "message"` — take the snapshot, with a note describing what changed

Let's do all three.

## Activity: Make Your First Commit

**Step 1:** Open a terminal (Win + R, type `cmd`, Enter).

**Step 2:** Navigate to your project folder:

```
cd Desktop\myproject
```

**Step 3:** Start Git tracking in this folder:

```
git init
```

You should see: `Initialized empty Git repository in ...`

Git is now watching this folder. Every file inside is being tracked.

**Step 4:** Stage all your files — tell Git to include them in the next snapshot:

```
git add .
```

The `.` means "everything in this folder." No output means it worked.

**Step 5:** Take the snapshot. This is the commit:

```
git commit -m "first save"
```

The `-m` flag means "message." The message in quotes is your note about what changed. You should see output listing the files that were saved.

## What Just Happened

Git took a snapshot of your entire `myproject` folder — including `index.html` and anything else inside. That snapshot is stored permanently in a hidden folder called `.git` inside your project.

You can make a hundred more changes, and you can always come back to this exact state.

## Commit Messages Matter

Get into the habit of writing clear commit messages. "first save" is fine for now. But in real projects, you'll write things like:

- `"add navigation menu"`
- `"fix broken link on homepage"`
- `"change background color to dark blue"`

Future you will be very grateful when you can read the history and understand what happened.

## Quick Recap

- `git init` — start tracking a new project (once).
- `git add .` — stage all files for the next commit.
- `git commit -m "message"` — save the snapshot.
- Write clear commit messages — they're notes to yourself.

Next up: Sending your project to GitHub.

---

[< Previous: Installing Git](12-installing-git.md) | [Next: Pushing to GitHub >](14-pushing-to-github.md)
