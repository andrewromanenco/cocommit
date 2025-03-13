from cocommit.bedrock import call_bedrock_claude_3_7
from cocommit.git_utils import get_last_commit_message, is_git_repo
from cocommit.prompt_utils import get_llm_prompt
from cocommit.response_utils import get_list_of_improvements, get_list_of_recommendations, get_list_of_strengths, get_summary, get_updated_commit_message

def main():
    path = "."
    if not is_git_repo(path):
        print("Not in a git repo")
        return
    last_commit_message = get_last_commit_message('.')
    llm_prompt = get_llm_prompt(last_commit_message)
    result = call_bedrock_claude_3_7(llm_prompt)
    print_results(result)
    print("All done!")

def print_results(result):
    print("Full promt (for debug)")
    print(result)
    print("EndOfResult")
    print("\n"*5)

    print(get_summary(result))
    print()
    
    print("Strengths:")
    for line in get_list_of_strengths(result):
        print(f"\t * {line}")
    print()
    
    print("Areas for improvement:")
    for line in get_list_of_improvements(result):
        print(f"\t * {line}")
    print()
    
    new_commit_message = get_updated_commit_message(result)
    if new_commit_message:
        print("\t***Proposed commit message***\n\n")
        print(new_commit_message)
        print("\n\n\t***End of commit message***")
    else:
        print("\tNo commit message is available\n\n")
    
    recommendations = get_list_of_recommendations(result)
    if len(recommendations) > 0:
        print("Recommended fixes:")
        for r in recommendations:
            print(f" - {r}")

if __name__ == "__main__":
    main()