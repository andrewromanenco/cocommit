import click
import time

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
    click.echo(llm_reply.summary)
    click.echo("\n")
    _print_list("Strengths", llm_reply.strengths_list)
    _print_list("Improvements", llm_reply.improvements_list)
    commit_header = " Amended git message: "
    click.echo(('*'*10) + commit_header + ("*"*20))
    click.echo(llm_reply.commit_message)
    click.echo("*"*(10 + 20 + len(commit_header)))
    _print_list("Fixes", llm_reply.recommendations_list)

