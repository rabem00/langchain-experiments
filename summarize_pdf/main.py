from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain

from dotenv import load_dotenv

# Load environment variables with path to .env file
load_dotenv(dotenv_path='../.env')

loader = PyPDFLoader('../assets/attention-all-you-need.pdf')
data = loader.load()

text_splitter = TokenTextSplitter(model_name='gpt-3.5-turbo', chunk_size=4000, chunk_overlap=200)
docs = text_splitter.split_documents(data)

llm = ChatOpenAI(temperature=0.3, model_name='gpt-3.5-turbo')

sum_chain = load_summarize_chain(llm, chain_type="refine", verbose=True)

summary = sum_chain.run(docs)


