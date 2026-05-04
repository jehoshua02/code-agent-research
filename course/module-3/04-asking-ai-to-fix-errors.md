# Lesson 3.04 — Asking AI to Fix Your Errors

## What You'll Learn

Every coder sees error messages. Even professionals. The skill isn't avoiding errors — it's knowing how to fix them fast.

AI is incredibly good at reading error messages and explaining what went wrong.

---

## Do This First

Take your working Python code from Replit:

```python
name = input("What's your name? ")
print("Hello, " + name + "!")
```

Now break it on purpose. Delete one character — like remove the closing parenthesis from the first line:

```python
name = input("What's your name? "
print("Hello, " + name + "!")
```

Hit **Run**.

You'll get an error. It'll look something like:

```
  File "main.py", line 2
    print("Hello, " + name + "!")
    ^^^^^
SyntaxError: invalid syntax
```

---

## Now Ask AI to Fix It

1. Copy the error message.
2. Go to ChatGPT (or Claude).
3. Paste this:

```
I got this error in my Python code. What does it mean and how do I fix it?

[paste your error here]

Here's my code:
[paste your code here]
```

4. Read what it says. Then apply the fix.

---

## Why This Works

Error messages are written for computers, not humans. They're accurate but confusing. AI is trained on millions of examples of errors and fixes, so it can translate that message into plain English and tell you exactly what to change.

It's like having a tutor on call 24/7.

---

## What to Do When AI Gets It Wrong

Sometimes the AI fix doesn't work. That's okay. Just paste the new error back in and say:

```
That didn't work. Here's the new error:
[paste error]
```

Keep going. Most bugs get solved in 2-3 rounds.

---

## What's Next

So far you've been chatting with AI in a browser. Next, you'll set up a tool that brings AI right into your code editor — so it can help you as you type.
