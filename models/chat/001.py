from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv

load_dotenv(dotenv_path='../../.env')

chat = ChatOpenAI(temperature=0.5) # default to gpt-3.5-turbo

print(chat)