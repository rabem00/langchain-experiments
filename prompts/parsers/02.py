from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv
load_dotenv(dotenv_path='../../.env')

chat = ChatOpenAI(temperature=0)

response_schemas = [
  ResponseSchema(name="question", description="the user's question"),
  ResponseSchema(name="answer", description="the answer to the user's question")
]

parser = StructuredOutputParser.from_response_schemas(response_schemas)

system_template = "Answer the user's question.\n{format_instructions}\n"
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

human_template = "{question}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

user_query = "What is the most popular sport in the world?"

messages = chat_prompt.format_prompt(question=user_query, format_instructions=parser.get_format_instructions()).to_messages()
print(messages[0].content)

result = chat(messages)

parsed_result = parser.parse(result.content)
print(parsed_result)