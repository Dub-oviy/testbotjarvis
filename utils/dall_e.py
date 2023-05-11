import openai
import requests
import base64
import io
from data.config import OPENAI_API

openai.api_key = OPENAI_API


# system_prompt = 'As a non-commercial DALL-E message handler, my task is to process messages for grammar and improve requests to produce realistic and colorful pictures. I will not ask for any clarification or additional details, but will simply accept the request for improvement and pass it on to DALL-E. Please note that I will not write anything other than the answer given for DALL-E, and I will not ask any questions. Thank you.'

    
async def generate_image(prompt):
#     print(prompt)
#     responses = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {'role': 'system', 'content': system_prompt},
#             {'role': 'user', 'content': prompt},
#         ],
#         temperature=0.9,
#         max_tokens=3000,
#         top_p=1.0,
#         presence_penalty=0.6,
#         stop=["\n"],
#     )

#     if responses is None:
#             return None
#     else:
#             print(responses['choices'][0]['message']['content'])
#             text = responses['choices'][0]['message']['content']

        # Отправляем текст в DALL-E для генерации изображения
    response = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai.api_key}",
        },
        json={
            "prompt": prompt,
            "num_images": 1,
            "size": "512x512",
            "response_format": "b64_json",
        },
    )
    if response.json() != None:
            
        image_data = response.json()['data'][0]['b64_json']
        image_binary = base64.b64decode(image_data)
        image_file = io.BytesIO(image_binary)
        return image_file
    else:
        print('error')
        return None