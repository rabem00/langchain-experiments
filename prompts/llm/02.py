from langchain import PromptTemplate
from dotenv import load_dotenv

load_dotenv(dotenv_path='../../.env')

simple_template = "This is my template."

prompt = PromptTemplate(
    input_variables=[],
    template=simple_template
)

formatted_prompt = prompt.format()

print(formatted_prompt)