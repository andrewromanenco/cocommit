from langchain.chat_models import init_chat_model

def call_llm(prompt, **kwargs):
    chat_model = init_chat_model(**kwargs)
    response = chat_model.invoke(prompt)
    return response.content
