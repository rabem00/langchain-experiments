from langchain import PromptTemplate

from dotenv import load_dotenv
load_dotenv(dotenv_path='../../.env')

similar_word_template = """"
I'm going to give you a word, and I want you to give me a word that is similar to it.

Word: {word}
Similar word:
"""

prompt = PromptTemplate(
  input_variables=['word'],
  template=similar_word_template,

)

formatted_prompt = prompt.format(word='dog')

print(formatted_prompt)