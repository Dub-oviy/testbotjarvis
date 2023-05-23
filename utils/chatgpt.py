import openai 
from data.config import OPENAI_API


openai.api_key = OPENAI_API

class ChatGptMessageHandler:
    def __init__(self) -> None:
       pass


    async def get_chatgpt_message(self,prompt):

      system_prompt = 'You are the user assistant and answer all his questions in a friendly way'

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
    

