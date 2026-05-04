# Lesson 1.09 — What Is a Variable?

## The Big Idea

A variable is a named box that holds a value.

That's it. Give the box a name. Put something inside. Use the name later to get the thing back out.

## Think About It This Way

Imagine you have a labeled drawer in your room. The label says "charger." Inside the drawer is your phone charger.

Whenever you need your charger, you don't describe where it is every time. You just say "the charger drawer." The label points to the thing.

Variables work the same way. Instead of writing the actual value every time, you give it a name and use that name.

## Why Variables Matter

Imagine you're writing a game. The player's score shows up in ten different places on the screen. Without variables, you'd have to update all ten places every time the score changes.

With a variable, you change it once. The name `score` always points to the current value. Every place that uses `score` automatically gets the new number.

## What a Variable Looks Like

In most programming languages, creating a variable looks like this:

```
username = "Alex"
score = 0
lives = 3
```

- The part on the left is the name (like the drawer label).
- The `=` means "store this value."
- The part on the right is the value being stored.

Notice: `"Alex"` has quotes around it because it's text. `0` and `3` don't have quotes because they're numbers. This distinction matters and we'll come back to it.

## Activity: Write Variables on Paper (Or in Notepad)

Let's practice the concept before we write real code.

**Step 1:** Open Notepad.

**Step 2:** Write out three variables for a made-up game character:

```
username = "Alex"
score = 0
lives = 3
```

(Use your real name if you want.)

**Step 3:** Now "update" the score. Change it to `150` — just edit the number.

**Step 4:** Save the file as `notes.txt` somewhere you can find it.

You just wrote your first variables. They don't run yet — we don't have Python set up. But you understand the concept. A name. An equals sign. A value.

## One Rule: Names Can't Have Spaces

Variable names can't have spaces. If you want two words, connect them:

- `high_score` (underscore, very common in Python)
- `highScore` (capital letter, common in JavaScript)
- `highscore` (just mash them together, works but harder to read)

## Quick Recap

- A variable is a named box that holds a value.
- You create one with: `name = value`
- Text values need quotes. Number values don't.
- Variable names can't have spaces.

Next up: Time to write real code — in Python.
