from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



Dall_e = KeyboardButton('Генерация изображений 🌄')
Trasnslator = KeyboardButton( 'Режим переводчика 📚')
ResetChatHistory = KeyboardButton('Очистить историю чата 🔄')
Cansel = KeyboardButton("Выход из режима 🔼")


mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(ResetChatHistory)
mainMenu.add(Dall_e,Trasnslator)
secondMenu = ReplyKeyboardMarkup(resize_keyboard=True)
secondMenu.add(Cansel)



