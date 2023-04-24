from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from loader import languageMode

currentLanguage = languageMode.languageMode
Chatgpt = KeyboardButton('Всезнайка' if currentLanguage == 'ru' else 'Wiki' )
Dall_e = KeyboardButton('Генерация изображений')
Text_generation = KeyboardButton('Генерация текста')
Trasnslator = KeyboardButton( 'Режим переводчика')
Cansel = KeyboardButton("Назад")

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(Chatgpt,Dall_e,Text_generation,Trasnslator,Cansel)



