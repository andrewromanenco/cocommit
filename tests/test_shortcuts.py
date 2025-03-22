from cocommit.shortcuts import shortcuts, get_shortcut

def test_dictionary_smoke_test():
    assert shortcuts['bedrock-claude37']

def test_get_shortcut():
    cli_params = get_shortcut('bedrock-claude37')
    assert cli_params['model_provider'] == 'bedrock'
    assert cli_params['model'] == 'us.anthropic.claude-3-7-sonnet-20250219-v1:0'
    assert cli_params['region_name'] == 'us-east-1'
