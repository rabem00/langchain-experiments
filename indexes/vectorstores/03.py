from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader

from dotenv import load_dotenv
load_dotenv(dotenv_path='../../.env')

loader = TextLoader('../../data/ai.txt')

documents = loader.load()
  
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

persist_directory = 'db'

db = Chroma.from_documents(texts, embeddings, persist_directory=persist_directory)

db.persist()

query = "When was AI founded as a discipline?"

docs = db.similarity_search(query)

print(docs)

# KEEP BELOW COMMENTED UNTIL PERSISTED

# persist_directory = 'db'

# embeddings = OpenAIEmbeddings()

# vectordb_persisted = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

# query = "When was AI founded as a discipline?"

# docs = vectordb_persisted.similarity_search(query)

# print(docs)