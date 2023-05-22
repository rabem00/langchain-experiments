from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv
load_dotenv(dotenv_path='../../.env')

chat = ChatOpenAI(temperature=0)

parser = CommaSeparatedListOutputParser()

system_template = "Provide 3 solutions to the user's problem.\n{format_instructions}\n"
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

human_template = "{problem}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

user_query = "My tire is flat."

messages = chat_prompt.format_prompt(problem=user_query, format_instructions=parser.get_format_instructions()).to_messages()
print(messages[0].content)

result = chat(messages)

parsed_result = parser.parse(result.content)
print(parsed_result)
print(len(parsed_result))