# Lesson 1.05 — Moving Around in the Terminal

## The Big Idea

When you're in the terminal, you're always "somewhere" on your computer. Every command you run happens in that location — your current folder.

Think of it like a map pin. Before you do anything useful, you need to know where you are and how to move.

## Think About It This Way

Imagine your computer's folders are rooms in a house. When you open the terminal, you start in one specific room. If you want to do something in a different room, you have to walk there first.

The command for walking is `cd`. It stands for "change directory." Directory is just another word for folder.

## Where Are You Right Now?

Open your terminal (Win + R, type `cmd`, press Enter).

Look at the prompt. It shows something like:

```
C:\Users\YourName>
```

That path — `C:\Users\YourName` — is where you are. It's your home folder.

## Moving to Your Desktop

Your Desktop is a folder too. It lives inside your home folder. Let's go there.

**Step 1:** In the terminal, type this and press Enter:

```
cd Desktop
```

Your prompt should now show:

```
C:\Users\YourName\Desktop>
```

You moved. You're now "inside" the Desktop folder.

**Step 2:** Type `dir` and press Enter.

You should see all the files and folders on your Desktop listed out. If you have `hello.html` from earlier, it'll be in this list.

## Going Back Up

To go back to the folder above (your home folder), type:

```
cd ..
```

The `..` means "go up one level." Like taking an elevator up one floor.

Type it now and watch your prompt change back.

## A Few Useful Tips

- **Tab key:** Start typing a folder name and press Tab. The terminal will autocomplete it. This saves a lot of typing.
- **Up arrow:** Press the up arrow to repeat your last command. Press it again to go further back in your history.
- **Exact spelling:** Folder names must be spelled exactly right, including capital letters.

## Activity: Move Around and Look Around

Try this sequence:

1. `cd Desktop` — go to Desktop
2. `dir` — see what's there
3. `cd ..` — go back up
4. `dir` — see what's in your home folder

You just navigated your computer using only your keyboard. That is what developers do all day.

## Quick Recap

- You're always "somewhere" in the terminal. That's your current directory.
- `cd FolderName` moves you into a folder.
- `cd ..` moves you up one level.
- `dir` shows what's in the current folder.
- Tab autocompletes. Up arrow repeats commands.

Next up: Creating folders and files from the terminal — no mouse needed.

---

[< Previous: The Terminal: Your Secret Weapon](04-the-terminal-your-secret-weapon.md) | [Next: Making Things in the Terminal >](06-making-things-in-the-terminal.md)
