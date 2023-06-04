import datetime
import logging
from datetime import date

import openai
import tiktoken 


GPT_3_MODELS = ("gpt-3.5-turbo", "gpt-3.5-turbo-0301")
GPT_4_MODELS = ("gpt-4", "gpt-4-0314")
GPT_4_32K_MODELS = ("gpt-4-32k", "gpt-4-32k-0314")
GPT_ALL_MODELS = GPT_3_MODELS + GPT_4_MODELS + GPT_4_32K_MODELS


class ChatGptMessageHandler:
    
    def __init__(self):
      self.conversations: dict[int: list] = {}  # {chat_id: history}
      self.last_updated: dict[int: datetime] = {}  # {chat_id: last_update_timestamp}
      self.system_prompt = 'You are the user assistant and answer all his questions in a friendly way'

    async def get_chatgpt_message(self, chat_id, prompt):
      print(prompt)
      try:  
        if chat_id not in self.conversations or self.__max_age_reached(chat_id):
            self.reset_chat_history(chat_id)

        self.last_updated[chat_id] = datetime.datetime.now()
        
        self.__add_to_history(chat_id, role = "user", content = prompt);
        

        token_count = self.__count_tokens(self.conversations[chat_id])
        print(token_count)
        exceeded_max_tokens = token_count + 2400 > 4096
        exceeded_max_history_size = len(self.conversations[chat_id]) > 15

        if exceeded_max_tokens or exceeded_max_history_size:
            logging.info(f'Chat history for chat ID {chat_id} is too long. Summarising...')
            try:
                summary = await self.__summarise(self.conversations[chat_id][:-1])
                logging.debug(f'Summary: {summary}')
                self.reset_chat_history(chat_id)
                self.__add_to_history(chat_id, role="assistant", content=summary)
                self.__add_to_history(chat_id, role="user", content = prompt)
            except Exception as e:
                logging.warning(f'Error while summarising chat history: {str(e)}. Popping elements instead...')
                self.conversations[chat_id] = self.conversations[chat_id][-15:]

        

        response = openai.ChatCompletion.create(
          model = "gpt-3.5-turbo" ,
          messages = self.conversations[chat_id],
          temperature = 0.4,
          max_tokens = 2400,
          n = 1, 
          top_p = 1.0,
          presence_penalty = 0.6,
          stop = ["You:"],
        )


        answer = response['choices'][0]['message']['content'].strip()
        self.__add_to_history(chat_id, role="assistant", content=answer)

        return answer
      

      except openai.error.RateLimitError as error:
        self.reset_chat_history(chat_id)
        self.get_chatgpt_message(chat_id, prompt)
        raise Exception() from error

    
    

    def __count_tokens(self, messages) -> int:
        model = "gpt-3.5-turbo"
        
        try:
            encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            encoding = tiktoken.get_encoding("gpt-3.5-turbo")

        if model in GPT_3_MODELS:
            tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
            tokens_per_name = -1  # if there's a name, the role is omitted
        elif model in GPT_4_MODELS + GPT_4_32K_MODELS:
            tokens_per_message = 3
            tokens_per_name = 1
        else:
            raise NotImplementedError(f"""num_tokens_from_messages() is not implemented for model {model}.""")
        num_tokens = 0
        for message in messages:
            num_tokens += tokens_per_message
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":
                    num_tokens += tokens_per_name
        num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
        return num_tokens
    

    def reset_chat_history(self, chat_id, content = ''):
      if content == '':
        content = self.system_prompt
      self.conversations[chat_id] = [{"role": "system", "content": content}]

    def __max_age_reached(self, chat_id) -> bool:
        """
        Checks if the maximum conversation age has been reached.
        :param chat_id: The chat ID
        :return: A boolean indicating whether the maximum conversation age has been reached
        """
        if chat_id not in self.last_updated:
            return False
        last_updated = self.last_updated[chat_id]
        now = datetime.datetime.now()
        max_age_minutes = 180
        return last_updated < now - datetime.timedelta(minutes=max_age_minutes)
    
    def __add_to_history(self, chat_id, role, content):
        """
        Adds a message to the conversation history.
        :param chat_id: The chat ID
        :param role: The role of the message sender
        :param content: The message content
        """

        self.conversations[chat_id].append({"role": role, "content": content})



    async def __summarise(self, conversation) -> str:

        messages = [
            {"role": "assistant", "content": "Summarize this conversation in 700 characters or less strictly"},
            {"role": "user", "content": str(conversation)}
        ]

        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.4,
        )
        return response.choices[0]['message']['content']  
    