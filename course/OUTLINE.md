# Zero to Hero AI Coding

## Module 1: Code Basics

**What code is, how computers think, and your first tools.**

### Lesson 1.01 — Computers Are Dumb (On Purpose)
- **Learn:** Computers do exactly what you tell them — nothing more, nothing less.
- **Do:** Open Notepad, type your name, save it. You just created a file a computer can read.

### Lesson 1.02 — What Is Code?
- **Learn:** Code is just instructions written in a language computers understand.
- **Do:** Open the Notepad file you saved. Rename it to `hello.txt`. Notice the `.txt` — that's the file type.

### Lesson 1.03 — File Types Are Like Costumes
- **Learn:** The extension (`.txt`, `.py`, `.html`) tells the computer what to do with a file.
- **Do:** Rename `hello.txt` to `hello.html`, then double-click it. It opens in a browser.

### Lesson 1.04 — The Terminal: Your Secret Weapon
- **Learn:** The terminal lets you control your computer by typing instead of clicking.
- **Do:** Press `Win + R`, type `cmd`, hit Enter. You're in the terminal. Type `dir` and press Enter.

### Lesson 1.05 — Moving Around in the Terminal
- **Learn:** The terminal has a "you are here" location, just like a map pin.
- **Do:** Type `cd Desktop` to move to your Desktop. Type `dir` again. See your files listed.

### Lesson 1.06 — Making Things in the Terminal
- **Learn:** You can create folders and files without ever touching your mouse.
- **Do:** Type `mkdir myproject` to create a folder. Then `cd myproject`. You're inside it.

### Lesson 1.07 — Your First HTML Page
- **Learn:** HTML is the skeleton of every website you've ever visited.
- **Do:** Create `index.html` in your folder. Add `<h1>Hello World</h1>`. Open it in a browser.

### Lesson 1.08 — Tags Are Like Wrappers
- **Learn:** HTML tags wrap content to give it meaning — like putting text in bold or making it a heading.
- **Do:** Add `<p>This is my page.</p>` under your heading. Refresh the browser.

### Lesson 1.09 — What Is a Variable?
- **Learn:** A variable is a named box that holds a value — like a labeled drawer.
- **Do:** In a new file `notes.txt`, write `username = "Alex"`. You just invented a variable on paper.

### Lesson 1.10 — Your First Real Code (Python)
- **Learn:** Python is a beginner-friendly language that reads almost like English.
- **Do:** Go to python.org/shell, type `print("Hello!")`, press Enter.

### Lesson 1.11 — What Is Git?
- **Learn:** Git is like "undo history" for your entire project — even weeks later.
- **Do:** Go to github.com, create a free account. This is where your code will live.

### Lesson 1.12 — Installing Git
- **Learn:** Git is a tool you install once and use forever.
- **Do:** Download Git from git-scm.com, install it, open a new terminal, type `git --version`.

### Lesson 1.13 — Your First Commit
- **Learn:** A commit is a snapshot of your code at a moment in time — like saving a game.
- **Do:** In your project folder, run `git init`, then `git add .`, then `git commit -m "first save"`.

### Lesson 1.14 — Pushing to GitHub
- **Learn:** Pushing sends your code to GitHub so it's backed up and shareable.
- **Do:** Create a new repo on GitHub, copy the commands it gives you, paste them in your terminal.

### Lesson 1.15 — Review: You Are Now a Developer
- **Learn:** Recap of what you can do: terminal, HTML, Python, Git, GitHub.
- **Do:** Write one sentence in your repo's README.md describing your project. Commit and push it.

---

## Module 2: How AI Works

**What's actually happening inside ChatGPT and tools like it.**

### Lesson 2.01 — AI Is Not Magic (It's Math)
- **Learn:** AI doesn't think — it predicts the next most likely word, over and over.
- **Do:** Go to ChatGPT, type "The sky is" — notice it completes it. That's prediction in action.

### Lesson 2.02 — What Is a Language Model?
- **Learn:** A language model is trained on billions of sentences and learned patterns from all of them.
- **Do:** Ask ChatGPT: "Complete this like a pirate: The sky is..." Compare to the default answer.

### Lesson 2.03 — Tokens: How AI Reads
- **Learn:** AI doesn't read words — it reads chunks called tokens. "unbelievable" might be two tokens.
- **Do:** Go to platform.openai.com/tokenizer, paste a sentence, see it split into tokens.

### Lesson 2.04 — Context Window: AI's Working Memory
- **Learn:** AI can only "remember" a limited amount of text at once — like RAM, not a hard drive.
- **Do:** Start a new ChatGPT chat. Tell it your name. After 20 messages, ask if it remembers.

### Lesson 2.05 — What Is a Prompt?
- **Learn:** A prompt is everything you send to an AI — your question, your instructions, your examples.
- **Do:** Ask ChatGPT "Explain gravity" then ask "Explain gravity like I'm 8." Compare both answers.

### Lesson 2.06 — System Prompts: The Hidden Instructions
- **Learn:** Behind most AI tools is a hidden message shaping how it behaves.
- **Do:** Ask ChatGPT "What are your instructions?" Watch how it responds.

### Lesson 2.07 — Temperature: How Random Is the AI?
- **Learn:** Temperature controls how creative (or boring) the AI's answers are.
- **Do:** Ask the same question in two separate chats. Notice the answers differ slightly each time.

### Lesson 2.08 — Training vs. Knowing
- **Learn:** AI was trained up to a cutoff date — it doesn't know what happened yesterday.
- **Do:** Ask ChatGPT about a very recent event. Notice it either refuses or gets it wrong.

### Lesson 2.09 — Hallucinations: When AI Makes Stuff Up
- **Learn:** AI will confidently say false things — because it's predicting words, not checking facts.
- **Do:** Ask ChatGPT to cite a source for a claim. Then Google that source. It may not exist.

### Lesson 2.10 — Models Are Like Different Brains
- **Learn:** GPT-4, Claude, Gemini — each model has different strengths, speeds, and costs.
- **Do:** Ask the same coding question on ChatGPT and on claude.ai. Compare answers.

### Lesson 2.11 — How AI Gets Better: Fine-Tuning
- **Learn:** Fine-tuning trains a model further on specific data — like teaching a generalist to specialize.
- **Do:** Notice how GitHub Copilot "knows" code better than regular ChatGPT — it was fine-tuned on code.

### Lesson 2.12 — What Is RAG? (Retrieval-Augmented Generation)
- **Learn:** RAG lets AI look things up before answering — like giving it Google access.
- **Do:** Use perplexity.ai to ask something recent. Notice it cites real sources.

### Lesson 2.13 — Embeddings: How AI Understands Meaning
- **Learn:** Embeddings let AI compare meaning, not just words — "happy" and "joyful" end up close together.
- **Do:** Ask ChatGPT: "What's more similar to 'dog' — 'puppy' or 'bark'? Explain why."

### Lesson 2.14 — Review: Talking to AI Smarter
- **Learn:** You now understand what's really happening when you type a prompt.
- **Do:** Write the best prompt you can to get ChatGPT to explain a topic you care about. Save it.

---

## Module 3: AI Coding Tools

**Trying real tools, building your first AI-assisted app.**

### Lesson 3.01 — The AI Coding Landscape
- **Learn:** There are tools for chatting, autocomplete, code generation, and full app building.
- **Do:** Search "AI coding tools" — skim the results and write down 5 tool names you see.

### Lesson 3.02 — Chat-Based Coding: Using ChatGPT to Write Code
- **Learn:** You can just ask ChatGPT to write code — no setup required.
- **Do:** Ask ChatGPT: "Write Python code that asks my name and says hello." Copy and run it on replit.com.

### Lesson 3.03 — Replit: Your Browser-Based Coding Home
- **Learn:** Replit lets you run code in the browser — no installs, no setup.
- **Do:** Create a free Replit account. Fork the Python project you pasted. Hit "Run."

### Lesson 3.04 — Asking AI to Fix Your Errors
- **Learn:** When code breaks, paste the error into ChatGPT. It usually knows what went wrong.
- **Do:** Delete one character from your working code. Run it. Paste the error into ChatGPT and ask for a fix.

### Lesson 3.05 — GitHub Copilot: AI That Lives in Your Editor
- **Learn:** Copilot watches what you type and suggests the next lines of code automatically.
- **Do:** Sign up for GitHub Copilot (free for students). Install VS Code. Install the Copilot extension.

### Lesson 3.06 — VS Code: The Editor Pros Use
- **Learn:** VS Code is a free code editor that most real developers use — with AI built in.
- **Do:** Open your `myproject` folder in VS Code. Notice the file tree, terminal, and editor panes.

### Lesson 3.07 — Copilot in Action: Let It Code for You
- **Learn:** Just write a comment describing what you want — Copilot writes the code.
- **Do:** In a `.py` file, type `# ask the user for their age and tell them what year they were born`. Watch Copilot suggest code.

### Lesson 3.08 — v0 by Vercel: Describe a UI, Get a Website
- **Learn:** v0 takes a text description and generates a working UI — design by talking.
- **Do:** Go to v0.dev, type "a to-do list app with a dark theme," see what it builds.

### Lesson 3.09 — Cursor: An Editor Built Around AI
- **Learn:** Cursor is VS Code rebuilt with AI at the center — you can chat with your codebase.
- **Do:** Download cursor.sh, open your project, press `Ctrl+K`, ask it to change your HTML heading.

### Lesson 3.10 — Claude for Coding: Long Context, Careful Answers
- **Learn:** Claude handles large chunks of code well and explains things clearly.
- **Do:** Paste your entire HTML file into Claude. Ask: "What does each line do?"

### Lesson 3.11 — Comparing Tools: Same Task, Different Tools
- **Learn:** Every AI tool has trade-offs — speed, cost, accuracy, personality.
- **Do:** Give the same task to ChatGPT, Claude, and Copilot. Write one sentence about each result.

### Lesson 3.12 — Your First AI-Built App (Part 1 — Plan)
- **Learn:** A real app starts with a clear description of what it should do.
- **Do:** Write a 3-sentence description of a simple app you want to build. Save it as `idea.md`.

### Lesson 3.13 — Your First AI-Built App (Part 2 — Build)
- **Learn:** Give your description to an AI tool and let it generate the starting code.
- **Do:** Paste your `idea.md` into Cursor or ChatGPT. Ask for the full code. Run it.

### Lesson 3.14 — Your First AI-Built App (Part 3 — Fix and Polish)
- **Learn:** Real apps never work perfectly on the first try — iteration is the job.
- **Do:** Find one thing broken or missing. Ask AI to fix it. Repeat until it works.

### Lesson 3.15 — Push Your App to GitHub
- **Learn:** Saving your app to GitHub makes it permanent and shareable.
- **Do:** Commit your app files and push to a new GitHub repo. Share the link with someone.

---

## Module 4: Going Deeper

**Prompt engineering, choosing the right tools, and building a real project.**

### Lesson 4.01 — Prompts Are Programs
- **Learn:** A well-written prompt controls AI output like code controls a computer.
- **Do:** Rewrite an old prompt with a role, a goal, and a format instruction. Compare outputs.

### Lesson 4.02 — Role Prompting: Give the AI a Job
- **Learn:** Telling AI "you are a..." shapes its tone, depth, and style dramatically.
- **Do:** Ask ChatGPT to review your code "as a senior developer." Then "as a teacher for beginners." Compare.

### Lesson 4.03 — Few-Shot Prompting: Show, Don't Just Tell
- **Learn:** Giving AI examples of what you want works better than describing it in words.
- **Do:** Give ChatGPT two examples of the output format you want, then a new input. See if it follows the pattern.

### Lesson 4.04 — Chain of Thought: Make AI Show Its Work
- **Learn:** Asking AI to "think step by step" increases accuracy on hard problems.
- **Do:** Ask a math or logic problem normally. Then add "think step by step." Compare accuracy.

### Lesson 4.05 — Context Management: What to Include and What to Cut
- **Learn:** Stuffing too much into a prompt confuses the AI — lean context gets better results.
- **Do:** Take a long prompt and cut it in half. Run both. Often the shorter one wins.

### Lesson 4.06 — Choosing the Right Model
- **Learn:** Speed, cost, and intelligence trade off against each other.
- **Do:** Make a simple table: list 3 models, their rough cost (free/cheap/expensive), and what they're best at.

### Lesson 4.07 — When AI Gets It Wrong: Debugging AI Output
- **Learn:** AI errors fall into patterns — wrong logic, outdated info, misunderstood requirements.
- **Do:** Find an AI-generated code bug by running it. Tell the AI exactly what went wrong. Let it fix it.

### Lesson 4.08 — Agents: AI That Takes Actions
- **Learn:** An AI agent doesn't just answer — it uses tools, browses the web, writes files, and loops until done.
- **Do:** Try perplexity.ai with a research question. Notice it searches and synthesizes automatically.

### Lesson 4.09 — MCP and Tool Use: Giving AI Superpowers
- **Learn:** AI can be connected to tools — calendars, databases, GitHub — through tool use.
- **Do:** Ask Claude or ChatGPT to describe what it could do if it had access to your file system.

### Lesson 4.10 — Reading Code You Didn't Write
- **Learn:** AI generates code you need to understand — even partially — to use and fix it.
- **Do:** Paste any AI-generated code into Claude. Ask: "Explain this like I'm new to coding, one section at a time."

### Lesson 4.11 — Final Project Kickoff: Pick Your Idea
- **Learn:** The final project should solve a real problem you actually have or care about.
- **Do:** Write down 3 app ideas. For each, write who would use it and why. Pick your favorite.

### Lesson 4.12 — Final Project: Spec It Out
- **Learn:** A spec is a short document describing what your app does before you build it.
- **Do:** Write a one-page spec: what the app does, what pages it has, what happens when you click things.

### Lesson 4.13 — Final Project: Build with AI
- **Learn:** Use AI tools to generate your app from the spec.
- **Do:** Feed your spec into your chosen AI tool. Generate the first version. Get it running.

### Lesson 4.14 — Final Project: Iterate and Improve
- **Learn:** Real development is a loop — build, test, break, fix, repeat.
- **Do:** List 5 things to improve. Fix at least 3 using AI. Document what prompts worked.

### Lesson 4.15 — Final Project: Ship It
- **Learn:** "Shipping" means making your project available to real users — even just one.
- **Do:** Push to GitHub. Deploy on vercel.com or Replit. Share the live link.
