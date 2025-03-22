# Cocommit: A Copilot for Git

[![image](https://img.shields.io/pypi/v/cocommit.svg)](https://pypi.python.org/pypi/cocommit)
[![image](https://img.shields.io/pypi/l/cocommit.svg)](https://github.com/andrewromanenco/cocommit/blob/main/LICENSE.txt)
[![image](https://img.shields.io/pypi/pyversions/cocommit.svg)](https://pypi.python.org/pypi/cocommit)

Cocommit is a command-line tool that works with your HEAD commit and leverages an LLM of your choice to enhance commit quality.

A good commit consists of multiple elements, but at a minimum, it should have a well-crafted commit message. Cocommit analyzes the message from the last (HEAD) commit and suggests improvements, highlighting both strengths and areas for enhancement.

Cocommit v2 is currently in development and will introduce many new features—see the [v2 documentation](https://github.com/andrewromanenco/cocommit/blob/main/docs/cocommit-v2.md) for details.

Cocommit utilizes [LangChain](https://github.com/langchain-ai/langchain) as an abstraction layer to access various Large Language Models (LLMs).

## Why Use Cocommit?
- Works with the LLM of your choice
- Provides a simple foundation for building custom AI-powered tools
- Easily integrates into your development workflow
- Allows customization of the LLM experience to fit your project needs

## Table of Contents

- [Example CLI Session](#example-cli-session)
- [Installation](#installation)
- [Usage](#usage)
  - [Example: Using OpenAI](#example-using-openai)
  - [Simplifying OpenAI Usage with Shortcuts](#simplifying-openai-usage-with-shortcuts)
  - [Example: Using Claude 3.7 on Bedrock](#example-using-claude-37-on-bedrock)
  - [Simplifying Bedrock Claude 3.7 Usage with Shortcuts](#simplifying-bedrock-claude-37-usage-with-shortcuts)
  - [Viewing Available Shortcuts](#viewing-available-shortcuts)
  - [Using Other LLMs](#using-other-llms)
  - [Useful CLI Options](#useful-cli-options)
- [Contributing](#contributing)
- [License](#license)

## Example CLI Session

### Session Start
```sh
git add .
git commit
cocommit -s bedrock-claude37
```

### Execution Output
```
Calling with: --model_provider bedrock --model us.anthropic.claude-3-7-sonnet-20250219-v1:0 --region_name us-east-1
Calling LLM....
Done in 9.6 seconds.

About your commit:
This is a good quality commit message that follows most best practices. It has a clear, concise title in imperative mood and a brief explanation of why the change was made.

Strengths:
  - Concise first line under 80 characters
  - Uses imperative mood correctly ("Add" not "Added")
  - Provides context in the description about why the change was made
  - Clearly specifies what was changed
  - Follows proper structure with title, blank line, and description

Improvements:
  - The description could be slightly more specific about which Python versions are now supported

********** Proposed Git Message: ********************

Add Python version classifiers to project metadata

This change lists supported Python versions for better visibility on PyPI.

****************************************************

Fixes:
  - Consider specifying which Python versions are now supported in the description for more detail

Amend the commit message? [Y/n]: y
********** Previous Message **********
Add Python version classifiers metadata

Lists supported Python versions for PyPI.
**************************************
Amend ... done!
```

## Installation

To install Cocommit, run:

```sh
pip install cocommit
```

### Installing from Source
You can also install Cocommit from the source code, which allows for customization. For details, see the [Contributing Guide](https://github.com/andrewromanenco/cocommit/blob/main/docs/CONTRIBUTING.md).

### Handling on-demand Dependencies
When calling a specific LLM, you may encounter a message like this:

```sh
cocommit --model llama3-8b-8192 --model_provider groq
```

```sh
Unable to import langchain_groq. Please install with `pip install -U langchain-groq`
```

To resolve this, execute the suggested `pip install` command. Since Cocommit supports a wide variety of LLMs, dependencies are installed only when needed.

## Usage

Cocommit interacts with Large Language Models (LLMs) through an abstraction layer provided by [LangChain](https://github.com/langchain-ai/langchain). This allows you to use any LLM provider supported by LangChain’s `init_chat_model` [function](https://python.langchain.com/api_reference/langchain/chat_models/langchain.chat_models.base.init_chat_model.html).

### Example: Using OpenAI
To use OpenAI, set your API key as the `OPENAI_API_KEY` environment variable. Alternatively, you can provide the key via the command line using the `--api_key <your key>` option:  

```sh
cocommit --model_provider openai --model gpt-4o
```

Note: On the first run, you may need to install additional dependencies by running: `pip install -U langchain-openai`.

### Simplifying OpenAI Usage with Shortcuts
Cocommit provides shortcuts for common LLM providers and models, allowing you to avoid specifying every parameter manually.

Ensure your chosen LLM provider is authorized (e.g., OpenAI API key or AWS credentials).

Run:
```sh
cocommit -s NAME
```

For example, if OPENAI_API_KEY is set:

```sh
cocommit -s gpt-4o
```

This command is equivalent to the full OpenAI GPT-4o example above.

### Example: Using Claude 3.7 on Bedrock
Before using Amazon Bedrock, ensure that:
- The Claude 3.7 model is enabled in your AWS account (region: `us-east-1`)
- You have valid credentials to access the model (typically configured in `~/.aws/credentials` or via environment variables; refer to AWS documentation for details)

To analyze and enhance the last commit message in a Git repository, run:

```sh
cocommit --model_provider bedrock --model us.anthropic.claude-3-7-sonnet-20250219-v1:0 --region us-east-1
```

To simplify execution for future use, save the above command in a shell script.

### Simplifying Bedrock Claude 3.7 Usage with Shortcuts

If AWS credentials are configured and Claude 3.7 is enabled in us-east-1, run:

```sh
cocommit -s bedrock-claude37
```

This command is equivalent to the previous Bedrock example.

### Viewing Available Shortcuts
To see all available shortcuts, run:

```sh
cocommit --show-shortcuts
```

If a shortcut you need is missing, consider contributing! See the [Contributing Guide](https://github.com/andrewromanenco/cocommit/blob/main/docs/CONTRIBUTING.md) for details.

### Using Other LLMs
Cocommit leverages LangChain’s `init_chat_model` function to call different LLMs. Command-line arguments map directly to its parameters.

- The `--model` parameter corresponds to the `model` argument in `init_chat_model`. It's the first positional parameter in LangChain's documentation.
- Other command-line parameters are passed directly to `init_chat_model` (ensure you use `_` instead of `-` when required by LangChain’s documentation).

**Recommended usage:** Always specify `--model` and `--model_provider` explicitly, unless using a shortcut.

- [init_chat_model documentation](https://python.langchain.com/api_reference/langchain/chat_models/langchain.chat_models.base.init_chat_model.html)
- [models](https://python.langchain.com/docs/integrations/chat/) (certain examples demonstrate the use of  init_chat_model  with its required parameters)

### Useful CLI Options
Cocommit supports debugging features, including:
- Viewing the raw LLM prompt
- Displaying the raw LLM response

To explore available options, run:

```sh
cocommit --help
```

## Contributing

Contributions are appreciated! If you'd like to get started, please review the [contributing guidelines](https://github.com/andrewromanenco/cocommit/blob/main/docs/CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](https://github.com/andrewromanenco/cocommit/blob/main/LICENSE.txt).
