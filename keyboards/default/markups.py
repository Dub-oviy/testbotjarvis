from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from loader import languageMode

currentLanguage = languageMode.languageMode

Dall_e = KeyboardButton('Генерация изображений')
Trasnslator = KeyboardButton( 'Режим переводчика')
Cansel = KeyboardButton("Выход из режима")

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(Dall_e,Trasnslator)
secondMenu = ReplyKeyboardMarkup(resize_keyboard=True)
secondMenu.add(Cansel)



