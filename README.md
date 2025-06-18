# 🤖 Clang + GenAI Pull Request Reviewer for LLVM

An automated LLVM pull request review tool that combines the power of:

- `clang-format` → Code formatting checks
- `clang-tidy` → Static analysis and warnings
- 💡 **GenAI (LLMs)** → Human-like review comments, improvement suggestions, and code critiques

> 📄 Generates consolidated markdown reports from GitHub PRs.  
> 🧠 Saves developer time while improving code quality.

---

## 🚀 Features

- 🔍 **Fetch LLVM PR Patch** from GitHub
- 📄 Parse diffs and detect modified lines
- 🧪 Run `clang-format` and `clang-tidy` locally
- 🧠 Use **LLMs (like GPT/Groq)** to generate:
  - Code readability feedback
  - Bug-prone logic hints
  - Alternative suggestions
- 📜 Save reviews in Markdown format
- 🌐 Includes a **Streamlit Web UI**

---

## 📸 Demo

| Terminal CLI Review | Streamlit App |
|---------------------|---------------|
| ![cli demo](docs/cli_demo.png) | ![web demo](docs/web_demo.png) |

---

## 🛠️ Installation

> ⚠️ Requires Python 3.10+ and tools like `clang-format`, `clang-tidy`.

```bash
git clone https://github.com/<your-username>/clang-genai-review.git
cd clang-genai-review
pip install -r requirements.txt
