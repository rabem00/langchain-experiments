from langchain.embeddings import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv(dotenv_path='../../.env')

embeddings = OpenAIEmbeddings()

text = 'I am a sentence and I want to be embedded.'

print(embeddings.embed_query(text))