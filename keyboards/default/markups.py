from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



Dall_e = KeyboardButton('Генерация изображений 🌄')
Trasnslator = KeyboardButton( 'Режим переводчика 📚')
Cansel = KeyboardButton("Выход из режима 🔼")

Allusersmessage = KeyboardButton('Отправить сообщение')
WeekUsers = KeyboardButton('Статистика за неделю')
MounthUsers = KeyboardButton('Статистика за месяц')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(Dall_e,Trasnslator)
secondMenu = ReplyKeyboardMarkup(resize_keyboard=True)
secondMenu.add(Cansel)
AdminMenu = ReplyKeyboardMarkup(resize_keyboard=True)
AdminMenu.add(Allusersmessage,WeekUsers,MounthUsers,Dall_e,Trasnslator)



