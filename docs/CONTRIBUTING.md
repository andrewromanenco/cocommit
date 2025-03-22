# Contributing to cocommit

Welcome, and thank you for your contribution! For minor changes, feel free to create a pull request. For larger updates, please open an issue or reach out to the maintainers directly.

## Contribute to UX
Cocommit is a user-friendly tool designed to simplify interactions with Large Language Models (LLMs). However, configuring the right combination of command-line options for a chosen LLM can be challenging, often requiring users to reference LangChain documentation ([here](https://python.langchain.com/api_reference/langchain/chat_models/langchain.chat_models.base.init_chat_model.html) and [here](https://python.langchain.com/docs/integrations/chat/)).

To make usage easier, Cocommit supports **shortcuts** — named sets of command-line options. Instead of manually entering these options, users can invoke a shortcut, which automatically applies the required settings.

You can list all available shortcuts by running and run them:

```sh
cocommit --show-shortcuts
cocommit -s shortcut_name
```

If you have access to an LLM supported by LangChain and no shortcut exists yet, your contribution is highly welcomed.

### How to contribute a shortcut

Follow these steps to add a new shortcut:

1. Check if a shortcut for your LLM already exists (or if an existing one could be improved).
2. Set up a local development environment (see instructions below).
3. Add your shortcut and test it.
4. Submit a pull request.

## More Complex Contributions

Cocommit v2 is currently under development. See the [cocommit-v2](https://github.com/andrewromanenco/cocommit/blob/main/docs/cocommit-v2.md) for details. If you have ideas for new features or improvements, feel free to:

- Open an issue on GitHub.
- Contact the project maintainer directly.

## Local Development

Cocommit is a Python project that uses Poetry for dependency management. To set up a development environment:

1. Clone the repository:
   ```sh
   git clone https://github.com/andrewromanenco/cocommit.git
   cd cocommit
   ```
2. Install dependencies:
   ```sh
   poetry install
   ```
3. Run tests to ensure everything works:
   ```sh
   poetry run test
   ```
4. Check code quality with the linter:
   ```sh
   poetry run ruff check .
   ```
5. Execute Cocommit from your local copy:
   ```sh
   poetry run cocommit <options>
   ```

If you want to install Cocommit from the source:

```sh
poetry run test
poetry build
pip install dist/cocommit-VERSION.whl
```

---

## Adding a Shortcut

To add a new shortcut:

1. Edit the `cocommit/shortcuts.py` file.
2. Run:
   ```sh
   poetry run cocommit -s <shortcut-name>
   ```

---

## Editing the LLM Prompt

To modify the LLM prompt (you may want to add your project-specific instructions):

1. Edit the prompt file:
   ```sh
   nano cocommit/llm_prompts/prompt.llm
   ```
2. Run tests to verify your changes:
   ```sh
   poetry run test
   ```
