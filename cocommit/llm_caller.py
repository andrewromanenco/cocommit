from langchain.chat_models import init_chat_model

def call_llm(prompt):
    chat_model = init_chat_model(
        model="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
        model_provider="bedrock",
        region_name="us-east-1")
    response = chat_model.invoke(prompt)
    return response.content
