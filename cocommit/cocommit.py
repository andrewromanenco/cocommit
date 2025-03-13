from cocommit.git_utils import get_last_commit_message, is_git_repo
from cocommit.prompt_utils import get_llm_prompt

def main():
    path = "."
    if not is_git_repo(path):
        print("Not in a git repo")
        return
    last_commit_message = get_last_commit_message('.')
    llm_prompt = get_llm_prompt(last_commit_message)
    print(llm_prompt)

if __name__ == "__main__":
    main()