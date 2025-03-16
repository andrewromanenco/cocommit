import json
from langchain_aws import ChatBedrock

def call_bedrock_claude_3_7(prompt):
    llm = ChatBedrock(
        model="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
        region="us-east-1"
        )
    response = llm.invoke(prompt)
    return response.content
