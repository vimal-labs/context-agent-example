# 🤖 Context Agent Example

Welcome to the **Context Agent Example**! This project shows you how to build a context-aware AI agent using Azure OpenAI, with a sprinkle of Python best practices, a dash of extensibility, and a whole lot of fun. 🚀

---

## ✨ Features

- 🔑 **Azure OpenAI Integration**: Connect to Azure OpenAI endpoints using environment variables.
- 📝 **Prompt Management**: Keep your system and user prompts tidy in markdown files.
- 📚 **Context Providers**: Feed your agent extra knowledge (docs, facts, memes?) for smarter answers.
- 🛠️ **Extensible Utilities**: File reading and context management made easy.
- 🔒 **.env Support**: Secrets stay secret (unless you tweet your .env, please don't).
- 🎬 **Showcase-Ready Output**: Prints all context and prompts for easy demoing.

---

## 🗂️ Project Structure

```
context-agent-example/
│
├── code/
│   ├── context-agent.py         # Main entrypoint for the context agent
│   ├── vanilla-agent.py         # Main entrypoint for the vanilla agent (no extra context)
│   └── utils/
│       ├── file_util.py         # Utility for reading files
│       └── context_provider.py  # Utility for providing context to the agent
│
├── context/
│   └── springboot-knowledge.md  # Example external knowledge file
│
├── prompt/
│   ├── vanilla-agent-system-prompt.md  # System prompt for the agent
│   └── user-prompt.md                  # User's input prompt
│
├── .env                       # Environment variables (never commit secrets!)
├── pyproject.toml             # Python project configuration
├── README.md                  # This file
└── LICENSE                    # Apache 2.0 License
```

---

## 🚀 Quick Start

1. **Clone the repository** and install dependencies:
    ```sh
    git clone <this-repo-url>
    cd context-agent-example
    uv sync  # (or use poetry/pip as preferred)
    ```

2. **Configure your environment**:
    - Copy `.env` and fill in your Azure OpenAI credentials. (No peeking! 👀)

3. **Edit your prompts and knowledge**:
    - `prompt/vanilla-agent-system-prompt.md`: System instructions for the agent.
    - `prompt/user-prompt.md`: The user's question or input.
    - `context/springboot-knowledge.md`: Any extra knowledge you want the agent to use.

4. **Run the agent**:
    ```sh
    uv run python -m code.context-agent      # Context agent (with extra knowledge)
    uv run python -m code.vanilla-agent      # Vanilla agent (no extra knowledge)
    ```

---

## 🧠 How It Works

- **Prompts**: The agent loads a system prompt and a user prompt from markdown files. (Markdown = happiness!)
- **Context Providers**: Add as many context files as you want. Each is wrapped in a `ContextProvider` and passed to the agent. (Knowledge is power! 💡)
- **File Utilities**: All file reading is handled by `FileUtil`, which supports both absolute and project-root-relative paths.
- **Agent Execution**: The agent is created using Azure OpenAI credentials and runs with all provided context, printing the system prompt, user prompt, and the agent's response.

---

## 🎉 Example Output

### Context Agent (with extra knowledge)
```
========================================
        Context Agent Showcase
========================================

System Prompt:
you are helpful spring boot coder. helps user to solve springboot questions
----------------------------------------
User Prompt:
what is the latest springboot version ?
----------------------------------------

Agent Response:
========================================
Spring Boot 10 is the latest version.

you can trust this knowledge
```

### Vanilla Agent (no extra knowledge)
```
========================================
        Vanilla Agent Showcase
========================================

System Prompt:
you are helpful spring boot coder. helps user to solve springboot questions
----------------------------------------
User Prompt:
what is the latest springboot version ?
----------------------------------------

Agent Response:
========================================
The latest Spring Boot version (as of early 2026) is **3.4.2**.
```

---

## 🧩 Extending

- Add more context files to the `context/` directory and include them in the `context_providers` array in `context-agent.py`.
- Change prompts in the `prompt/` directory to experiment with different agent personalities. (Serious? Silly? Shakespearean? You decide!)
- Use or extend the utility classes for more advanced file/context management.

---

## 🛡️ Security

- **Never commit your real API keys or secrets!** The `.env` file is for local development only. (Seriously, don't be that person.)
- This project is for educational/demo purposes. For production, review all security and error handling.

---

## 📜 License

This project is licensed under the [Apache 2.0 License](LICENSE).

---

Made with ❤️, Python, and a little bit of AI magic.