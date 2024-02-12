import logging
import tempfile
import openai
import requests
import base64
import io
from data.config import OPENAI_API

openai.api_key = OPENAI_API



async def generate_image(prompt,user_db):
    current_sub = user_db

    try:
        if current_sub == 'Start':
            model_ver = "dall-e-2"
        elif current_sub == 'Standard':
            model_ver ='dall-e-3'
            image_quality = 'standard'
        elif current_sub == 'Advanced':
            model_ver = 'dall-e-3'
            image_quality = 'hd'

        else:
            pass
    except Exception as e:
        logging.warning(f'Error in getting chatgpt model {str(e)}')
    print(model_ver+image_quality)
    # Generating the image with the DALL-E API
    response = openai.Image.create(
        model=model_ver,
        prompt=prompt,
        n=1,
        size= '1024x1024',
        quality=image_quality,
    )


# standard or hd 
    

    # Get the URL of the generated image
    image_url = response.data[0].url

    # Download the image content
    image_content = requests.get(image_url).content

        # Send the photo to the user using the file path
    with tempfile.NamedTemporaryFile(delete=False) as temp_image:
        temp_image.write(image_content)
        temp_image.flush()

        # Send the photo to the user using the file path
        image = open(temp_image.name, "rb")
        return image

# async def generate_image(prompt):
#         # Отправляем текст в DALL-E для генерации изображения
#     response = requests.post(
#         "https://api.openai.com/v1/images/generations",
#         headers={
#             "Content-Type": "application/json",
#             "Authorization": f"Bearer {openai.api_key}",
#         },
#         json={
#             "prompt": prompt,
#             "num_images": 1,
#             "size": "512x512",
#             "response_format": "b64_json",
#         },
#     )
#     if response.json() != None:
            
#         image_data = response.json()['data'][0]['b64_json']
#         image_binary = base64.b64decode(image_data)
#         image_file = io.BytesIO(image_binary)
#         return image_file
#     else:
#         print('error')
#         return None