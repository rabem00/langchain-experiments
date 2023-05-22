from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser, RetryWithErrorOutputParser
from pydantic import BaseModel, Field, validator
from dotenv import load_dotenv
load_dotenv(dotenv_path='../../.env')

chat = ChatOpenAI(temperature=0.0)

class QA(BaseModel):
  question: str = Field(description="the user's question")
  answer: str = Field(description="the answer to the user's question")

  @validator('question')
  def question_ends_with_question_mark(field):
      if field[-1] != '?':
        raise ValueError("Question must end with a question mark.")
      return field
        
parser = PydanticOutputParser(pydantic_object=QA)

user_query = "What is the most popular sport in the world?"

system_template = "Answer the user's question.\n{format_instructions}\n"
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

human_template = "{question}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

formatted_prompt = chat_prompt.format_prompt(format_instructions=parser.get_format_instructions(), question=user_query)

bad_response = '{"question": "What is the most popular sport'

# parser.parse(bad_response)

retry_parser = RetryWithErrorOutputParser.from_llm(parser=parser, llm=chat)

fixed_result = retry_parser.parse_with_prompt(bad_response, formatted_prompt)
print(fixed_result)