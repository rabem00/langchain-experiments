from langchain import PromptTemplate
from dotenv import load_dotenv

load_dotenv(dotenv_path='../../.env')
complex_template = """
{name} is {age} years old and enjoys {hobby}.
"""

prompt = PromptTemplate(
    input_variables=["name", "age", "hobby"],
    template=complex_template
)

formatted_prompt = prompt.format(name="Elon", age="51", hobby="rockets")

print(formatted_prompt)