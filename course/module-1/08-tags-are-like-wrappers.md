# Lesson 1.08 — Tags Are Like Wrappers

## The Big Idea

HTML tags wrap content. The tag goes around the text, and whatever tag you use changes how that content looks and what it means.

It's like gift wrapping. The gift inside is the same. But a fancy box says "important." A plain bag says "casual." The wrapper changes how people see it.

## Tags You'll Use All the Time

Here are the most common ones:

| Tag | What It Does |
|-----|--------------|
| `<h1>` | Big heading (most important) |
| `<h2>` | Smaller heading |
| `<p>` | Paragraph of text |
| `<b>` | Bold text |
| `<a>` | A link |
| `<img>` | An image |

You don't have to memorize all of these. You'll learn them by using them.

## Tags Can Nest

You can put tags inside other tags. Like a gift inside a gift inside a gift.

```html
<p>This is <b>really important</b> stuff.</p>
```

The `<b>` is nested inside the `<p>`. The word "really important" will be bold. The rest of the sentence won't.

The rule: the tag you open last, you close first. If you open `<p>` and then `<b>`, close `<b>` first, then `</p>`.

## Activity: Add a Paragraph to Your Page

**Step 1:** Open `index.html` from your `myproject` folder in Notepad.

**Step 2:** Under your `<h1>` line, add this:

```html
<p>This is my first webpage. I made it myself.</p>
```

Your full file should now look like:

```html
<h1>Hello World</h1>
<p>This is my first webpage. I made it myself.</p>
```

**Step 3:** Save with Ctrl + S.

**Step 4:** Go to your browser. The page is probably still open. Press Ctrl + R to refresh it.

You should see your heading and then a paragraph of text below it. The browser automatically added some spacing between them.

## Try This Too

Add one more line to make some text bold:

```html
<p>My name is <b>Alex</b> and I am learning to code.</p>
```

(Replace Alex with your actual name.)

Save, refresh. "Alex" should appear bold. Everything else in that line should be normal weight.

## Quick Recap

- Tags wrap content and change how it looks or what it means.
- `<p>` for paragraphs, `<b>` for bold, `<h1>` for headings.
- Tags can nest — but close them in reverse order.
- Save the file and refresh the browser to see changes.

Next up: Variables — the most important idea in all of programming.
