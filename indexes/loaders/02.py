from langchain.document_loaders import CSVLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

from dotenv import load_dotenv
load_dotenv(dotenv_path='../../.env')

loader = CSVLoader(file_path='../../data/MOCK_DATA.csv')

data = loader.load_and_split()

chat = ChatOpenAI()

embeddings = OpenAIEmbeddings()

db = Chroma.from_documents(data, embeddings)

retriever = db.as_retriever()

qa = RetrievalQA.from_chain_type(llm=chat, retriever=retriever)

query = "What airport is Kurt nearest to?"

result = qa.run(query)

print(result)