from langchain.document_loaders import WebBaseLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

from dotenv import load_dotenv
load_dotenv(dotenv_path='../../.env')

loader = WebBaseLoader("https://en.wikipedia.org/wiki/Steve_Jobs")

pages = loader.load_and_split()

chat = ChatOpenAI()

embeddings = OpenAIEmbeddings()

db = Chroma.from_documents(pages, embeddings)

retriever = db.as_retriever()

qa = RetrievalQA.from_chain_type(llm=chat, chain_type="stuff", retriever=retriever)

query = "What did he do between 1985–1997?"

result = qa.run(query)

print(result)