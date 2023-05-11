from googletrans import Translator

translator = Translator()

async def translate_mode(text):
    lang = translator.detect(text).lang
    if lang == 'en':
        translation = translator.translate(text, dest='ru').text
    elif lang == 'ru':
        translation = translator.translate(text, dest='en').text
    else:
        translation = "Я не могу определить язык сообщения."
    
    answer = translation
    return answer