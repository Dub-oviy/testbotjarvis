from aiogram import types
from keyboards.default import markups
from loader import dp,bot,db,Admins
from images import *



@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    if (not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id ,message.from_user.full_name,message.from_user.username)
    else:
        pass
    if message.from_user.id  in [int(admin_id) for admin_id in Admins]:
        print(Admins)
        with open('images/Hello.png','rb') as photo:
            await bot.send_photo(message.chat.id , photo=photo ,caption =f"Привет, {message.from_user.full_name}! это телеграмм бот с разными фунциями , нажми на одну из них и давай начинать",
                            reply_markup=markups.AdminMenu)
    else:
        with open('images/Hello.png','rb') as photo:
            await bot.send_photo(message.chat.id , photo=photo ,caption =f"Привет, {message.from_user.full_name}! это телеграмм бот с разными фунциями , нажми на одну из них и давай начинать",
                            reply_markup=markups.mainMenu)

