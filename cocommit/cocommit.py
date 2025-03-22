import click
import cocommit.cli_ui as cli_ui

from cocommit.commit_amend import ask_and_amend
from cocommit.git_utils import get_last_commit_message, is_git_repo
from cocommit.llm_caller import call_llm, looks_like_good_llm_response
from cocommit.prompt_utils import get_llm_prompt
from cocommit.parser.llm_reply import LLMReply
from cocommit.shortcuts import get_shortcut

@click.command(context_settings=dict(
    ignore_unknown_options=True,
    allow_extra_args=True
))
@click.option('--show-llm-prompt', is_flag=True, help='Show the prompt sent out to the LLM')
@click.option('--show-llm-reply', is_flag=True, help='Show the raw reply from the LLM')
@click.option('--show-shortcuts', is_flag=True, help='Display available presets for CLI parameters.')
@click.option('-s', '--shortcut', type=str, help='Predefined CLI parameters for common models')
@click.argument("langchain_options", nargs=-1, type=click.UNPROCESSED)
@click.pass_context
def main(ctx, **kwargs):
    path = "."
    if not is_git_repo(path):
        cli_ui.not_a_git_repo()
        return

    options = ctx.params
    if options.get('show_shortcuts'):
        cli_ui.show_shortcuts()
        return

    dynamic_options = get_llm_calling_options(ctx, options)
    if not dynamic_options:
        cli_ui.no_model_parameters()
        return

    last_commit_message = get_last_commit_message(path)
    llm_prompt = get_llm_prompt(last_commit_message)
    if options.get('show_llm_prompt'):
        cli_ui.print_llm_prompt(llm_prompt)

    llm_txt_reply = get_llm_reply(llm_prompt, dynamic_options)

    if not looks_like_good_llm_response(llm_txt_reply):
        cli_ui.bad_llm_response()
        return

    if options.get('show_llm_reply'):
        cli_ui.print_llm_reply(llm_txt_reply)
    llm_reply = LLMReply.get(llm_txt_reply)
    cli_ui.print_result(llm_reply)

    ask_and_amend(llm_reply.commit_message)

def get_llm_calling_options(ctx, options):
    if options.get('shortcut'):
        dynamic_options = get_shortcut(options.get('shortcut'))
        if not dynamic_options:
            cli_ui.no_such_shortcut(options.get('shortcut'))
            return
        cli_ui.selected_shortcut(dynamic_options)
    else:
        dynamic_options = cli_ui.get_dynamic_options(ctx.params)
    return dynamic_options

def get_llm_reply(llm_prompt, dynamic_options):
    return cli_ui.timed_llm_call(lambda: call_llm(llm_prompt, **dynamic_options))

if __name__ == "__main__":
    main()
