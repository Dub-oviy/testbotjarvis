from aiogram import types
# from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import markups
from loader import dp,bot,db
from images import *



@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    if (not db.user_exists):
        db.add_user(message.from_user.id ,message.from_user.full_name,message.from_user.username)
    else:
        pass
    with open('images/Hello.png','rb') as photo:
        await bot.send_photo(message.chat.id , photo=photo ,caption =f"Привет, {message.from_user.full_name}! это телеграмм бот с разными фунциями , нажми на одну из них и давай начинать",
                         reply_markup=markups.mainMenu)

