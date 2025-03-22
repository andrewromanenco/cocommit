import click
import json
import time

from cocommit.shortcuts import shortcuts

from cocommit.dogs_vs_cats import generate_ascii_pet

def not_a_git_repo():
    click.echo("You must be in the root directory of a Git repository (where the .git folder is located).")

def print_llm_prompt(prompt):
    click.echo("Prompt sent to LLM:")
    click.echo("-"*30)
    click.echo(prompt)
    click.echo("-"*30)
    click.echo("\tEnd of Prompt")
    click.echo("\n"*3)

def print_llm_reply(prompt):
    click.echo("Text received from LLM:")
    click.echo("-"*30)
    click.echo(prompt)
    click.echo("-"*30)
    click.echo("\tEnd of LLM reply")
    click.echo("\n"*3)

def timed_llm_call(fn):
    start_time = time.time()
    click.echo("Calling LLM....")
    result = fn()
    end_time = time.time()
    execution_time = end_time - start_time
    click.echo(f"Done in {execution_time:.1f} seconds.")
    return result

def _print_list(name, items):
    click.echo(f"{name}:")
    for item in items:
        click.echo(f"\t - {item}")
    click.echo("\n")

def print_result(llm_reply):
    click.echo("V"*40)
    generate_ascii_pet()
    click.echo("\n")
    click.echo("About your commit:")
    click.echo(llm_reply.summary)
    click.echo("\n")
    _print_list("Strengths", llm_reply.strengths_list)
    _print_list("Improvements", llm_reply.improvements_list)
    commit_header = " Proposed git message: "
    click.echo(('*'*10) + commit_header + ("*"*20))
    click.echo(llm_reply.commit_message)
    click.echo("*"*(10 + 20 + len(commit_header)))
    _print_list("Fixes", llm_reply.recommendations_list)

def ask_if_do_amend():
    valid_answers = {"yes": True, "y": True, "no": False, "n": False}
    question = "Amend the commit message?"
    prompt = " [Y/n]: "
    default = "yes"

    while True:
        user_input = input(question + prompt).strip().lower()
        if not user_input:  # If user presses Enter, use default
            return valid_answers[default]
        if user_input in valid_answers:
            return valid_answers[user_input]
        click.echo("Invalid response. Please enter 'yes' or 'no' (or 'y'/'n').")

def confirm_amend(previous_commit):
    header = "*" * 10 + " Previous message " + "*" * 10
    click.echo(header)
    click.echo(previous_commit.strip())
    click.echo("*" * len(header))
    click.echo("Amend ... done!")

def get_dynamic_options(options):
    if 'langchain_options' in options:
        dynamic_options = options.pop('langchain_options')
        it = iter(dynamic_options)
        extra_dict = {}
        for arg in it:
            if arg.startswith("--"):
                key = arg.lstrip("-")
                try:
                    value = next(it)
                    if value.startswith("--"):
                        extra_dict[key] = True
                        it = iter([value] + list(it))
                    else:
                        extra_dict[key] = value
                except StopIteration:
                    extra_dict[key] = True
        return extra_dict
    return {}

def no_model_parameters():
    click.echo("It looks like no model selection options were provided.")
    click.echo("Use --help for more information,")
    click.echo("or run --show-shortcuts to view available presets.")

def bad_llm_response():
    click.echo("Got a bad response back from the LLM!")
    click.echo("Try running with --show-llm-reply to view the raw reply.")
    click.echo("Use --show-llm-prompt to inspect the actual prompt.")

def show_shortcuts():
    click.echo("Available CLI parameter presets. Use 'cocommit --shortcut <NAME>' to apply a preset.")
    click.echo("You may be prompted to install specific LLM dependencies. Run 'pip install <LIB>' to install them.")
    click.echo()
    for name, details in shortcuts.items():
        click.echo(f"--shortcut {name}")
        click.echo(json.dumps(details, indent=4))
        click.echo()

def selected_shortcut(options):
    formatted_options = [f"--{key} {value}" for key, value in options.items()]
    cli = " ".join(formatted_options)
    click.echo(f"Calling with: {cli}")

def no_such_shortcut(name):
    click.echo(f"Error: Unknown shortcut '{name}'")
    click.echo("Please run 'cocommit --show-shortcuts' to view the available presets.")
