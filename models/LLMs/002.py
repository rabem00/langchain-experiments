from langchain.llms import OpenAI
from dotenv import load_dotenv

# Load environment variables with path to .env file
load_dotenv(dotenv_path='../../.env')

llm = OpenAI(model_name="text-curie-001", temperature=0.2)

result = llm.generate([
    "Write a poem about fire",
    "Write a poem about water"
])

print(result.generations)
print(len(result.generations))

print(result.generations[0][0])

print(result.generations[0][0].text)

print(result.llm_output)