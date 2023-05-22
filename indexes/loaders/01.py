from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

from dotenv import load_dotenv
load_dotenv(dotenv_path='../../.env')

loader = PyPDFLoader("../../data/attention-all-you-need.pdf")

pages = loader.load_and_split()

chat = ChatOpenAI()

embeddings = OpenAIEmbeddings()

db = Chroma.from_documents(pages, embeddings)

retriever = db.as_retriever()

qa = RetrievalQA.from_chain_type(llm=chat, retriever=retriever)

query = "What last question was asked?"

result = qa.run(query)

print(result)