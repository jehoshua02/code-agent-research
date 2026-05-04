# Lesson 1.06 — Making Things in the Terminal

## The Big Idea

You don't need a mouse to create files and folders. The terminal can do it in one line. Once you get used to this, it's way faster than right-clicking and navigating menus.

## Think About It This Way

Right-clicking to create a folder is like going to a restaurant, looking at the menu, flagging down a waiter, reading out your order, waiting for them to write it down, and then getting your food.

Typing a command is like walking into the kitchen and making it yourself. Faster. More direct.

## Making a Folder

The command is `mkdir`. It stands for "make directory" — which means make a folder.

**Step 1:** Open your terminal (Win + R, type `cmd`, Enter).

**Step 2:** Navigate to your Desktop:

```
cd Desktop
```

**Step 3:** Create a new folder called `myproject`:

```
mkdir myproject
```

**Step 4:** Check that it worked:

```
dir
```

You should see `myproject` in the list with `<DIR>` next to it. Go look at your Desktop — the folder is there.

## Moving Into Your New Folder

**Step 5:** Move into the folder:

```
cd myproject
```

Your prompt now shows:

```
C:\Users\YourName\Desktop\myproject>
```

You're inside your new project folder. This is where your code will live.

## Creating a File

Now let's create a file from the terminal. On Windows, the easiest way is:

```
type nul > index.html
```

This creates an empty file called `index.html`. The command is a bit weird-looking — don't worry about what it means right now. Just know it creates an empty file.

**Step 6:** Run that command, then type `dir` to confirm the file appeared.

## A Note on Naming

When naming files and folders in code projects:

- **No spaces.** Use dashes or underscores instead. `my-project` not `my project`.
- **Lowercase.** Keeps things consistent and avoids headaches later.
- **Descriptive.** `myproject` is fine for now. Real projects get more specific.

## Quick Recap

- `mkdir foldername` creates a new folder.
- `cd foldername` moves you into it.
- `type nul > filename.ext` creates an empty file on Windows.
- No spaces in file or folder names for code projects.

You now have a project folder (`myproject`) with a file (`index.html`) inside it. In the next lesson, you'll put something in that file.

---

[< Previous: Moving Around in the Terminal](05-moving-around-in-the-terminal.md) | [Next: Your First HTML Page >](07-your-first-html-page.md)
