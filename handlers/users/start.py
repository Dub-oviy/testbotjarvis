from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import markups
from loader import dp,bot,hellophoto


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await bot.send_photo(message.chat.id , photo=hellophoto ,caption =f"Привет, {message.from_user.full_name}! это телеграмм бот с разными фунциями , нажми на одну из них и давай начинать",
                         reply_markup=markups.mainMenu)
