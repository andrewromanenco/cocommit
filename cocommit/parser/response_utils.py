import re

def get_text(llm_response, tag_name):
    match = re.search(rf"<{tag_name}>(.*?)</{tag_name}>", llm_response, re.DOTALL)
    return match.group(1) if match else None

def get_updated_commit_message(llm_response):
    return get_text(llm_response, "NEW-COMMIT-MESSAGE")

def get_summary(llm_response):
    return get_text(llm_response, "SUMMARY")

def get_list(llm_response, tag_name):
    match = re.search(rf"<{tag_name}>(.*?)</{tag_name}>", llm_response, re.DOTALL)
    if match:
        fixes_content = match.group(1).strip()
        return [line.strip() for line in fixes_content.split("\n") if line.strip()]
    return []

def get_list_of_recommendations(llm_response):
    return get_list(llm_response, "FIXES")

def get_list_of_strengths(llm_response):
    return get_list(llm_response, "STRENGTHS")

def get_list_of_improvements(llm_response):
    return get_list(llm_response, "IMPROVE")

