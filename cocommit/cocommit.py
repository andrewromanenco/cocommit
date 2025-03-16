import click
import cocommit.cli_ui as cli_ui

from cocommit.bedrock import call_bedrock_claude_3_7
from cocommit.git_utils import get_last_commit_message, is_git_repo
from cocommit.prompt_utils import get_llm_prompt
from cocommit.parser.llm_reply import LLMReply

@click.command()
@click.option('--show-llm-prompt', is_flag=True, help='Show the prompt sent out to the LLM')
@click.option('--show-llm-reply', is_flag=True, help='Show the raw reply from the LLM')
@click.pass_context
def main(ctx, **kwargs):
    options = ctx.params
    path = "."
    if not is_git_repo(path):
        cli_ui.not_a_git_repo()
        return
    last_commit_message = get_last_commit_message(path)
    llm_prompt = get_llm_prompt(last_commit_message)
    if options.get('show_llm_prompt'):
        cli_ui.print_llm_prompt(llm_prompt)
    llm_txt_reply = cli_ui.timed_llm_call(call_bedrock_claude_3_7, llm_prompt)
    if options.get('show_llm_reply'):
        cli_ui.print_llm_reply(llm_txt_reply)
    llm_reply = LLMReply.get(llm_txt_reply)
    cli_ui.print_result(llm_reply)

if __name__ == "__main__":
    main()
