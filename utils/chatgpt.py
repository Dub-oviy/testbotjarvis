import openai 
from data.config import OPENAI_API
from language_mode import language_mode

openai.api_key = OPENAI_API
print(language_mode) 
if language_mode == 'ru':
  system_prompt= 'You are the assistant to the user and answer all his questions in a friendly way, and also answer questions only in Russion.'
elif language_mode == 'eng':
  system_prompt = 'You are the assistant to the user and answer all his questions in a friendly way, and also answer questions only in English.'
else:
  system_prompt = 'You are the user assistant and answer all his questions in a friendly way'


async def get_chatgpt_message(prompt):
    response = openai.ChatCompletion.create(
       model = "gpt-3.5-turbo" ,
       messages = [
         {'role':'system','content':system_prompt},
         {"role":"user","content": prompt }],
       temperature = 0.9,
       max_tokens = 3000,
       top_p = 1.0,
       presence_penalty = 0.6,
       stop = ["You:"]
    )

    return response['choices'][0]['message']['content']