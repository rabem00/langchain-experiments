from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, AIMessage, HumanMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from dotenv import load_dotenv

load_dotenv(dotenv_path='../../.env')

chat = ChatOpenAI(streaming=True,callbacks=[StreamingStdOutCallbackHandler()] ,temperature=0.4)

result = chat([
    SystemMessage(content='Tell me 3 facts about the pacific ocean. Respond as a numbered list.'),
    HumanMessage(content='I am expert about the pacific ocean so make sure the fact is new to me.'),
    AIMessage(content='I will tell you a super unknown fact!')
])