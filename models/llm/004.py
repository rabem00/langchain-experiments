from langchain.llms import OpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from dotenv import load_dotenv

# Load environment variables with path to .env file
load_dotenv(dotenv_path='../../.env')

llm = OpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=0.0)

llm("Write a poem about fire")