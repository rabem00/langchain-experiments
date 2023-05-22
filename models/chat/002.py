from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage

from dotenv import load_dotenv

load_dotenv(dotenv_path='../../.env')

chat = ChatOpenAI(temperature=0.4)

result = chat([
    SystemMessage(content='Hello, how are you?')
])

print(result)

print(result.content)