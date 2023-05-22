from langchain.embeddings import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv(dotenv_path='../../.env')

embeddings = OpenAIEmbeddings()

print(embeddings)