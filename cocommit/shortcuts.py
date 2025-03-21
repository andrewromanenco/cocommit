shortcuts = {
    'bedrock_claud37': {
        "model_provider": "bedrock",
        "model": "us.anthropic.claude-3-7-sonnet-20250219-v1:0",
        "region_name": "us-east-1"
    }
}

def get_shortcut(name):
    return shortcuts.get(name, {})
    