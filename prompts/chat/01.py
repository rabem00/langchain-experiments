from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from dotenv import load_dotenv
load_dotenv(dotenv_path='../../.env')

system_template = "Help me learn about {subject}. I will tell you what specific topic I want to learn about."
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

human_template = "I want to learn about {topic}."
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

messages = chat_prompt.format_prompt(subject="math", topic="trigonometry").to_messages()

print(messages)

chat = ChatOpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=0.5)

chat(messages)