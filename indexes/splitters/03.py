from langchain.text_splitter import TokenTextSplitter
from langchain.document_loaders import TextLoader

from dotenv import load_dotenv
load_dotenv(dotenv_path='../../.env')

loader = TextLoader('../../data/ai.txt')

documents = loader.load()

text_splitter = TokenTextSplitter(
    chunk_size = 10,
    chunk_overlap = 0
)

texts = text_splitter.split_documents(documents)

print(texts[0])