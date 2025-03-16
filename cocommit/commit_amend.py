import cocommit.cli_ui as cli_ui
from cocommit.git_utils import get_amend_last_commit_message

def ask_and_amend(commit_message):
    stripped_message = commit_message.strip()
    should_amend = cli_ui.ask_if_do_amend()
    if should_amend:
        previous_message = get_amend_last_commit_message(".", stripped_message)
        cli_ui.confirm_amend(previous_message)
