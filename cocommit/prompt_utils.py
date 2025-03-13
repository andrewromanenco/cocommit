import importlib.resources
from string import Template

def load_template(filename):
    package = __package__ or "cocommit"
    with importlib.resources.files(package + ".llm_prompts").joinpath(filename).open("r", encoding="utf-8") as f:
        return f.read()

def get_llm_prompt(commit_message, template_name="prompt"):
    template_content = load_template(f"{template_name}.llm")
    template = Template(template_content)
    return template.safe_substitute(commit_message=commit_message)
