import json
import boto3

def call_bedrock_claude_3_7(prompt):
    client = boto3.client("bedrock-runtime", region_name="us-east-1")

    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 2000
    }

    response = client.invoke_model(
        modelId="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
        contentType="application/json",
        accept="application/json",
        body=json.dumps(payload)
    )

    result = json.loads(response["body"].read())
    return result["content"][0]["text"]
