import openai
from data.config import OPENAI_API
from language_mode import language_mode

openai.api_key = OPENAI_API

if language_mode == 'ru':
  system_prompt = 'You are a bot that generates text by the name of the text and always write the text in Russian'
elif language_mode == 'eng':
  system_prompt = 'You are a bot that generates text by the name of the text and always write the text in English'
else:
  system_prompt = 'You are a bot that generates text by Text Name if the text name is in Russian then the text will be in Russian if the text name is in English then the text will be in English'




async def text_generator(prompt):
    # await message.reply( 'Интересный текст подождите немного пожалуйста')
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
    # print(response['choices'][0]['message']['content'])
    return response['choices'][0]['message']['content']
    








