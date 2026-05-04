# Lesson 3.07 — Copilot in Action: Let It Code for You

## What You'll Learn

Copilot doesn't just complete code — it can read a comment you wrote in plain English and write the whole function for you.

A comment is a line that starts with `#` in Python. The computer ignores it. But Copilot reads it and uses it to figure out what you want.

---

## Do This First

1. Open VS Code.
2. Create a new file called `birthday.py` in your project.
3. Type this comment — and then stop typing:

```python
# ask the user for their age and tell them what year they were born
```

4. Press **Enter** after the comment.
5. Wait one or two seconds.

You should see Copilot's suggestion appear in gray text. It might look like:

```python
age = int(input("How old are you? "))
birth_year = 2024 - age
print("You were born in", birth_year)
```

6. Press **Tab** to accept it.
7. Open the terminal and run: `python birthday.py`

---

## What Just Happened

You wrote one sentence in plain English. Copilot wrote three lines of working code.

That's the power of autocomplete AI. It doesn't just finish your words — it finishes your ideas.

---

## Tips for Getting Better Suggestions

- Be specific in your comments. "ask for age" gives worse suggestions than "ask the user for their age as a number."
- If the suggestion is wrong, press **Escape** to dismiss it and try rewriting your comment.
- You can accept part of a suggestion by pressing `Ctrl+Right` to accept one word at a time.

---

## Copilot Is a Starting Point, Not the Final Answer

Copilot guesses based on patterns. It's usually pretty close, but not always right. Always read what it wrote before you run it.

Think of it like autocorrect on your phone. Usually helpful. Sometimes hilariously wrong.

---

## What's Next

Copilot works inside editors. But what if you want AI to design an entire UI — a real-looking interface — just from a description? That's next.
