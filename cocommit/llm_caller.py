from langchain.chat_models import init_chat_model

def call_llm(prompt, **kwargs):
    chat_model = init_chat_model(**kwargs)
    response = chat_model.invoke(prompt)
    return response.content

def looks_like_good_llm_response(llm_response):
    if not isinstance(llm_response, str):
        return False
    return 'NEW-COMMIT-MESSAGE' in llm_response
