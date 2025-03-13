import re

def get_updated_commit_message(llm_response):
    match = re.search(r"<NEW-COMMIT-MESSAGE>(.*?)</NEW-COMMIT-MESSAGE>", llm_response, re.DOTALL)
    return match.group(1) if match else None

def get_list_of_recommendations(llm_response):
    match = re.search(r"<FIXES>(.*?)</FIXES>", llm_response, re.DOTALL)
    if match:
        fixes_content = match.group(1).strip()
        return [line.strip() for line in fixes_content.split("\n") if line.strip()]
    return []
