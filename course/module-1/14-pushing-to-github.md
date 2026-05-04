# Lesson 1.14 — Pushing to GitHub

## The Big Idea

So far your commits only live on your computer. If your hard drive dies, they're gone.

Pushing sends your code to GitHub. Now it's backed up online and you can share it with anyone.

## Think About It This Way

Your Git commits are like photos on your phone. They exist, but they're only on one device. Pushing to GitHub is like uploading them to the cloud. Now they're safe. Now you can show people.

## Step 1: Create a Repo on GitHub

A repository (repo) is a project on GitHub. You need to create one to push to.

1. Go to [github.com](https://github.com) and log in.
2. Click the `+` icon in the top right corner.
3. Select "New repository."
4. Name it `myproject` (match your folder name).
5. Leave everything else on the defaults.
6. Click "Create repository."

## Step 2: Read the Instructions GitHub Gives You

After creating the repo, GitHub shows you a page with commands to run. Look for the section that says:

**"...or push an existing repository from the command line"**

It will look something like this (with your actual username):

```
git remote add origin https://github.com/yourusername/myproject.git
git branch -M main
git push -u origin main
```

Copy those three lines. You're about to paste them into your terminal.

## Step 3: Run the Commands

1. Open your terminal (Win + R, type `cmd`, Enter).
2. Navigate to your project: `cd Desktop\myproject`
3. Paste and run each command, one at a time.

The first command connects your local folder to GitHub. The second renames your branch to `main`. The third sends your code up.

When you run `git push`, Git might ask for your GitHub username and password. Use the email and password from your GitHub account.

Note: GitHub may ask you to use a Personal Access Token instead of your password. If it does, go to GitHub > Settings > Developer Settings > Personal Access Tokens > Generate new token. Give it full repo access and use that token as your password.

## Step 4: Verify It Worked

Go back to your repo page on GitHub and refresh it. You should see your `index.html` file listed there.

Click on it. GitHub shows you the contents. Your code is on the internet.

## Quick Recap

- Create a repo on GitHub first.
- GitHub gives you the exact commands to connect and push.
- `git push` sends your committed code to GitHub.
- Your code is now backed up and shareable.

Next up: The final lesson — you're already a developer.
