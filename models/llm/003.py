from langchain.llms import OpenAI
from dotenv import load_dotenv

# Load environment variables with path to .env file
load_dotenv(dotenv_path='../../.env')

llm = OpenAI(model_name="text-curie-001", temperature=0.2)

token_count = llm.get_num_tokens("Write a poem about fire")
print(token_count)

