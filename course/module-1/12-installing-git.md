# Lesson 1.12 — Installing Git

## The Big Idea

Git is a tool you install once and use on every project, forever. Let's get it set up.

## Download Git

**Step 1:** Open your browser and go to:

```
https://git-scm.com
```

**Step 2:** Click the big download button. It should detect Windows automatically and offer you the right version.

**Step 3:** Run the installer file that downloads. It's a normal Windows installer — click through it.

**The installer will ask a lot of questions.** Most of them are fine on their defaults. Here are the ones to pay attention to:

- "Choosing the default editor used by Git" — pick Notepad if you see it as an option, or just leave the default. We'll change this later.
- "Adjusting the name of the initial branch" — select "Override the default branch name for new repositories" and type `main`. (GitHub uses `main` as the default now, and you want them to match.)
- Everything else — leave on default.

**Step 4:** Finish the install.

## Confirm It Worked

After installing, you need to open a fresh terminal. If you had one open already, close it — Git won't show up in old terminals.

**Step 5:** Press Win + R, type `cmd`, press Enter.

**Step 6:** Type this and press Enter:

```
git --version
```

You should see something like:

```
git version 2.44.0.windows.1
```

The exact number doesn't matter. If you see a version number, Git is installed and working.

## One-Time Setup: Tell Git Who You Are

Git tracks who made each change. So you need to tell it your name and email once.

**Step 7:** Type these two commands, one at a time. Replace the name and email with yours:

```
git config --global user.name "Your Name"
```

```
git config --global user.email "your@email.com"
```

Use the same email you used for your GitHub account. This connects your Git activity to your GitHub profile.

**Step 8:** Confirm it saved:

```
git config --global user.name
```

It should print back your name.

## Quick Recap

- Download Git from git-scm.com.
- During install: set the default branch name to `main`.
- After install: confirm with `git --version`.
- Run `git config` to set your name and email — do this once.

Next up: Making your first commit — saving a snapshot of your project.
