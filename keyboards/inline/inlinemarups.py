from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

ru = InlineKeyboardButton('русский' , callback_data='ru')
eng = InlineKeyboardButton('english' , callback_data='eng')

language = InlineKeyboardMarkup(row_width=1)
language.add(ru,eng)
