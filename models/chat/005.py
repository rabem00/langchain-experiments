from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, AIMessage, HumanMessage

from dotenv import load_dotenv

load_dotenv(dotenv_path='../../.env')

chat = ChatOpenAI(temperature=1)

result = chat.generate([[
    SystemMessage(content='Tell me 3 facts about the pacific ocean. Respond as a numbered list.'),
    HumanMessage(content='I am expert about the pacific ocean so make sure the fact is new to me.'),
    AIMessage(content='I will tell you a super unknown fact!')
]] * 2) # generate 2 responses


print(result.generations)
print(len(result.generations))