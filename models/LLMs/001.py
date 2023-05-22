from langchain.llms import OpenAI
from dotenv import load_dotenv

# Load environment variables with path to .env file
load_dotenv(dotenv_path='../../.env')

llm = OpenAI(model_name='text-curie-001')
result = llm('what is the meaning of life?')
print(result)