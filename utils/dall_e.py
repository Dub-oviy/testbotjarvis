import openai
import requests
from data.config import OPENAI_API

openai.api_key = OPENAI_API

system_prompt = 'You are a message processor for DALL-E for non-commercial purposes, your task is to process the message for grammar, and also make the request more detailed to your taste so that DALL-E gives a good picture , do your job never ask anything do not ask what exactly the user wants do not ask for clarifications just accept the request improve and pass DALL-E, do not write anything other than the answer given for DALL-E and do not ask anything at all'

    
async def generate_image(prompt):
    
    responses = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': prompt},
        ],
        temperature=0.9,
        max_tokens=3000,
        top_p=1.0,
        presence_penalty=0.6,
        stop=["\n"],
    )

    if responses is None:
        pass
    else:
        print(responses['choices'][0]['message']['content'])
        text = responses['choices'][0]['message']['content']

        # Отправляем текст в DALL-E для генерации изображения
        response = requests.post(
            "https://api.openai.com/v1/images/generations",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {openai.api_key}",
            },
            json={
                "model": "image-alpha-001",
                "prompt": text,
                "num_images": 1,
                "size": "512x512",
                "response_format": "url",
            },
        )

        return response.json()["data"][0]
