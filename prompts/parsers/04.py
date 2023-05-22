from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, validator
from langchain.output_parsers import OutputFixingParser

from dotenv import load_dotenv
load_dotenv(dotenv_path='../../.env')


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

misformatted = "{'question': 'What is the most popular sport in the world?', 'answer': 'soccer'}"

# parser.parse(misformatted)

fixing_parser = OutputFixingParser.from_llm(parser=parser, llm=ChatOpenAI())
print(fixing_parser)

fixed_result = fixing_parser.parse(misformatted)
print(fixed_result)