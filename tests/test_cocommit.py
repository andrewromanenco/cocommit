import pytest
from click.testing import CliRunner
from cocommit.cocommit import main
from unittest.mock import MagicMock, patch

from cocommit.shortcuts import shortcuts

@pytest.fixture
def runner():
    return CliRunner()

@patch('cocommit.cocommit.is_git_repo')
def test_runnin_outside_of_git(mock_is_git_repo, runner):
    mock_is_git_repo.return_value = False
    result = runner.invoke(main, ['--shortcut', 'bedrock_claud37'])
    mock_is_git_repo.assert_called_once()
    assert 'You must be in the root directory of a Git repository' in result.output

def test_show_shortcuts(runner):
    result = runner.invoke(main, ['--show-shortcuts'])
    assert result.exit_code == 0
    assert 'Available CLI parameter presets' in result.output

def test_shortcut_no_name(runner):
    result = runner.invoke(main, ['--shortcut'])
    assert result.exit_code == 2
    assert "Option '--shortcut' requires an argument" in result.output

def test_non_existing_shortcut(runner):
    result = runner.invoke(main, ['--shortcut', 'non_exsiting_shortcut'])
    assert result.exit_code == 0
    assert "Unknown shortcut 'non_exsiting_shortcut'" in result.output

@patch('cocommit.cocommit.is_git_repo')
@patch('cocommit.cocommit.get_last_commit_message')
@patch('cocommit.cocommit.get_llm_prompt')
@patch('cocommit.cocommit.get_llm_reply')
@patch('cocommit.cocommit.looks_like_good_llm_response')
@patch('cocommit.cocommit.LLMReply')
@patch('cocommit.cocommit.ask_and_amend')
def test_bedrock_shortcut(
        mock_ask_and_amend,
        mock_LLMReply,
        mock_looks_like_good_llm_response,
        mock_get_llm_reply,
        mock_get_llm_prompt,
        mock_get_last_commit_message,
        mock_is_git_repo,
        runner):
    mock_is_git_repo.return_value = True
    mock_get_last_commit_message.return_value = 'last-commit'
    mock_get_llm_prompt.return_value = 'prompt'
    mock_get_llm_reply.return_value = 'llm-reply'
    mock_looks_like_good_llm_response.return_value = True
    llm_reply = MagicMock()
    llm_reply.commit_message = 'amended commit message'
    mock_LLMReply.get.return_value = llm_reply

    result = runner.invoke(main, ['--shortcut', 'bedrock_claud37'])
    mock_is_git_repo.assert_called_once_with('.')
    mock_get_last_commit_message.assert_called_once_with('.')
    mock_get_llm_prompt.assert_called_once_with('last-commit')
    mock_get_llm_reply.assert_called_once_with('prompt', shortcuts['bedrock_claud37'])
    mock_looks_like_good_llm_response.assert_called_once_with('llm-reply')
    mock_LLMReply.get.assert_called_once_with('llm-reply')
    mock_ask_and_amend.assert_called_once_with('amended commit message')
    assert "Calling with: --model_provider bedrock --model us.anthropic.claude-3-7-sonnet-20250219-v1:0 --region_name us-east-1" in result.output
