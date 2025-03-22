# Cocommit Version 2 Overview

Cocommit Version 1 focused on improving commit messages. Version 2 expands this mission to enhance entire commits—including both the commit message and the code changes themselves.

Version 2 not only improves your own commits but also helps you review code changes contributed by others more effectively.

### Key Enhancements in Version 2

Version 2 introduces a new abstraction that maps a Git commit to a Large Language Model (LLM) prompt. Unlike Version 1, which only processed commit messages, this new layer incorporates both the commit message and the related code changes to provide the LLM with a more comprehensive context. This results in a more insightful and effective commit process.

### Benefits of Version 2

With this enhanced approach, Version 2 will:

-   Generate better commit messages with deeper context.
-   Provide insights into the **code review experience**, such as identifying overly large changes.
-   Highlight potential **inefficiencies** in the commit that may be worth addressing.
-   Suggest **improvements** to keep the codebase cleaner and more maintainable.
    

### Backward Compatibility

Version 2 is fully backward compatible with Version 1. Users have full control over how prompts are generated—they can choose to include only the commit message (as in Version 1) or enrich the prompt with code context for deeper analysis.