import click
import time

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

def timed_llm_call(fn, *args, **kwargs):
    start_time = time.time()
    click.echo("Calling LLM....")
    result = fn(*args, **kwargs)
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
    click.echo(llm_reply.summary)
    click.echo("\n")
    _print_list("Strengths", llm_reply.strengths_list)
    _print_list("Improvements", llm_reply.improvements_list)
    commit_header = " Amended git message: "
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
