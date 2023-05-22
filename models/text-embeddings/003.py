from langchain.embeddings import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv(dotenv_path='../../.env')

embeddings = OpenAIEmbeddings()

text1 = 'I am a sentence.'
text2 = 'I like pizza.'

document_embeddings = embeddings.embed_documents([text1, text2])

print(document_embeddings)