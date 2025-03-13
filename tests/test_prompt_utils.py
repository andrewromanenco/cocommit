from cocommit.prompt_utils import get_llm_prompt

def test_prompt():
    result = get_llm_prompt("message", template_name="test_prompt")
    expected = 'Commit message: message'
    assert result == expected
