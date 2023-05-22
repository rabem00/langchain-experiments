from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader

from dotenv import load_dotenv
load_dotenv(dotenv_path='../../.env')

loader = TextLoader('../../data/ai.txt')

documents = loader.load()
  
text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=0)

texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

db = Chroma.from_documents(texts, embeddings)

query = "When was AI founded as a discipline?"

docs = db.similarity_search_with_score(query, k=1)

print(docs[0][1])