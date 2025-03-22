import warnings

# Suppress the specific DeprecationWarning from pydantic.v1.typing
# Remove after langchain upgrades their dependency
warnings.filterwarnings(
    "ignore",
    category=DeprecationWarning,
    module="pydantic.v1.typing"
)

import pytest
from click.testing import CliRunner
from cocommit.cocommit import main
from unittest.mock import MagicMock, patch

from cocommit.shortcuts import shortcuts

@pytest.fixture
def runner():
    return CliRunner()

@patch('cocommit.cocommit.is_git_repo')
@patch('cocommit.cocommit.cli_ui')
def test_running_outside_of_git(mock_cli_ui, mock_is_git_repo, runner):
    mock_is_git_repo.return_value = False
    result = runner.invoke(main, ['--shortcut', 'bedrock-claude37'])
    mock_is_git_repo.assert_called_once()
    mock_cli_ui.not_a_git_repo.assert_called_once()

@patch('cocommit.cocommit.is_git_repo')
@patch('cocommit.cocommit.cli_ui')
def test_show_shortcuts(mock_cli_ui, mock_is_git_repo, runner):
    mock_is_git_repo.return_value = True
    result = runner.invoke(main, ['--show-shortcuts'])
    mock_is_git_repo.assert_called_once()
    mock_cli_ui.show_shortcuts.assert_called_once()
    assert result.exit_code == 0

@patch('cocommit.cocommit.is_git_repo')
def test_shortcut_no_name(mock_is_git_repo, runner):
    mock_is_git_repo.return_value = True
    result = runner.invoke(main, ['--shortcut'])
    mock_is_git_repo.assert_not_called()
    assert result.exit_code == 2
    assert "Option '--shortcut' requires an argument" in result.output

@patch('cocommit.cocommit.is_git_repo')
@patch('cocommit.cocommit.cli_ui')
def test_non_existing_shortcut(mock_cli_ui, mock_is_git_repo, runner):
    mock_is_git_repo.return_value = True
    result = runner.invoke(main, ['--shortcut', 'non_exsiting_shortcut'])
    assert result.exit_code == 0
    mock_cli_ui.no_such_shortcut.assert_called_once()

@patch('cocommit.cocommit.is_git_repo')
@patch('cocommit.cocommit.get_last_commit_message')
@patch('cocommit.cocommit.get_llm_prompt')
@patch('cocommit.cocommit.get_llm_reply')
@patch('cocommit.cocommit.looks_like_good_llm_response')
@patch('cocommit.cocommit.LLMReply')
@patch('cocommit.cocommit.ask_and_amend')
@patch('cocommit.cocommit.cli_ui')
def test_bedrock_shortcut(
        mock_cli_ui,
        mock_ask_and_amend,
        mock_LLMReply,
        mock_looks_like_good_llm_response,
        mock_get_llm_reply,
        mock_get_llm_prompt,
        mock_get_last_commit_message,
        mock_is_git_repo,
        runner):
    end_to_end(
        mock_cli_ui,
        mock_ask_and_amend,
        mock_LLMReply,
        mock_looks_like_good_llm_response,
        mock_get_llm_reply,
        mock_get_llm_prompt,
        mock_get_last_commit_message,
        mock_is_git_repo,
        runner,
        ['--shortcut', 'bedrock-claude37'])
    mock_get_llm_reply.assert_called_once_with('prompt', shortcuts['bedrock-claude37'])
    mock_cli_ui.print_llm_prompt.assert_not_called()
    mock_cli_ui.print_llm_reply.assert_not_called()

@patch('cocommit.cocommit.is_git_repo')
@patch('cocommit.cocommit.get_last_commit_message')
@patch('cocommit.cocommit.get_llm_prompt')
@patch('cocommit.cocommit.get_llm_reply')
@patch('cocommit.cocommit.looks_like_good_llm_response')
@patch('cocommit.cocommit.LLMReply')
@patch('cocommit.cocommit.ask_and_amend')
@patch('cocommit.cocommit.cli_ui')
def test_bedrock_shortcut_with_debug(
        mock_cli_ui,
        mock_ask_and_amend,
        mock_LLMReply,
        mock_looks_like_good_llm_response,
        mock_get_llm_reply,
        mock_get_llm_prompt,
        mock_get_last_commit_message,
        mock_is_git_repo,
        runner):
    end_to_end(
        mock_cli_ui,
        mock_ask_and_amend,
        mock_LLMReply,
        mock_looks_like_good_llm_response,
        mock_get_llm_reply,
        mock_get_llm_prompt,
        mock_get_last_commit_message,
        mock_is_git_repo,
        runner,
        ['--shortcut', 'bedrock-claude37','--show-llm-prompt', '--show-llm-reply'])
    mock_get_llm_reply.assert_called_once_with('prompt', shortcuts['bedrock-claude37'])
    mock_cli_ui.print_llm_prompt.assert_called_once()
    mock_cli_ui.print_llm_reply.assert_called_once()

@patch('cocommit.cocommit.is_git_repo')
@patch('cocommit.cocommit.get_last_commit_message')
@patch('cocommit.cocommit.get_llm_prompt')
@patch('cocommit.cocommit.get_llm_reply')
@patch('cocommit.cocommit.looks_like_good_llm_response')
@patch('cocommit.cocommit.LLMReply')
@patch('cocommit.cocommit.ask_and_amend')
@patch('cocommit.cocommit.cli_ui')
def test_model_params_from_cli(
        mock_cli_ui,
        mock_ask_and_amend,
        mock_LLMReply,
        mock_looks_like_good_llm_response,
        mock_get_llm_reply,
        mock_get_llm_prompt,
        mock_get_last_commit_message,
        mock_is_git_repo,
        runner):
    mock_cli_ui.get_dynamic_options.return_value= {
        'model': 'some-model',
        'provider': 'some-provider'
    }
    end_to_end(
        mock_cli_ui,
        mock_ask_and_amend,
        mock_LLMReply,
        mock_looks_like_good_llm_response,
        mock_get_llm_reply,
        mock_get_llm_prompt,
        mock_get_last_commit_message,
        mock_is_git_repo,
        runner,
        ['--model', 'some-model','--provider', 'some-provider'])
    mock_cli_ui.get_dynamic_options.assert_called_once()
    call_args = mock_cli_ui.get_dynamic_options.call_args
    assert 'langchain_options' in call_args[0][0]
    mock_get_llm_reply.assert_called_once_with('prompt',
                                               {
                                                   'model': 'some-model',
                                                   'provider': 'some-provider'
                                               })
    mock_cli_ui.print_llm_prompt.assert_not_called()
    mock_cli_ui.print_llm_reply.assert_not_called()

def end_to_end(
        mock_cli_ui,
        mock_ask_and_amend,
        mock_LLMReply,
        mock_looks_like_good_llm_response,
        mock_get_llm_reply,
        mock_get_llm_prompt,
        mock_get_last_commit_message,
        mock_is_git_repo,
        runner,
        args):
    mock_is_git_repo.return_value = True
    mock_get_last_commit_message.return_value = 'last-commit'
    mock_get_llm_prompt.return_value = 'prompt'
    mock_get_llm_reply.return_value = 'llm-reply'
    mock_looks_like_good_llm_response.return_value = True
    llm_reply = MagicMock()
    llm_reply.commit_message = 'amended commit message'
    mock_LLMReply.get.return_value = llm_reply
    result = runner.invoke(main, args)
    mock_is_git_repo.assert_called_once_with('.')
    mock_get_last_commit_message.assert_called_once_with('.')
    mock_get_llm_prompt.assert_called_once_with('last-commit')
    mock_looks_like_good_llm_response.assert_called_once_with('llm-reply')
    mock_LLMReply.get.assert_called_once_with('llm-reply')
    mock_ask_and_amend.assert_called_once_with('amended commit message')
    assert result.exit_code == 0
