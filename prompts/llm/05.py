from langchain import PromptTemplate, FewShotPromptTemplate
from dotenv import load_dotenv

load_dotenv(dotenv_path='../../.env')

examples = [
    {"animal": "bird", "home": "nest"},
    {"animal": "beaver", "home": "dam"},
]

example_template = """\
Animal: {animal}
Home: {home}\
"""

example_prompt = PromptTemplate(
    input_variables=["animal", "home"],
    template=example_template
)

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Identify the home for the given animal.",
    suffix="Animal: {animal}\nHome:",
    input_variables=["animal"],
    example_separator="\n\n"
)

formatted_prompt = few_shot_prompt.format(animal="clown fish")

print(formatted_prompt)