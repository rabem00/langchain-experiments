from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader

from dotenv import load_dotenv
load_dotenv(dotenv_path='../../.env')

loader = TextLoader('../../data/ai.txt')

documents = loader.load()

text_splitter = CharacterTextSplitter(
    separator = "\n\n",
    chunk_size = 1000,
    chunk_overlap = 100
)

texts = text_splitter.split_documents(documents)

print(texts[0])