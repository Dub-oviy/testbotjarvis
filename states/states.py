from loader import dp,bot
from aiogram import types
from utils import chatgpt,dall_e,text_generate,translator_mode
from keyboards.inline import inlinemarups
from keyboards.default import markups




async def chatgpt_handler(message: types.Message):
    if message.text == 'Выход из режима':
        # Удаляем обработчик сообщений Всезнайка
        await dp.current_state(user=message.from_user.id).reset_state()
        await message.answer('Вы вышли из режим Всезнайка',reply_markup=markups.mainMenu)
    else:
        response = await chatgpt.get_chatgpt_message(message.text)
        await bot.send_message(chat_id=message.chat.id, text=response, reply_to_message_id=message.message_id)

async def dall_e_handler(message: types.Message):
    # await message.answer( 'Интересный запрос , подождите немного и бот скинет изображение')
    if message.text == 'Выход из режима':
        # Удаляем обработчик сообщений Всезнайка
        await dp.current_state(user=message.from_user.id).reset_state()
        await message.reply('Вы вышли из режим Генерация изображений',reply_markup=markups.mainMenu)
    else:
        if message.text == 'Генерация изображений':
            pass
        else:
            response = await dall_e.generate_image(message.text)
            await bot.send_photo(chat_id=message.chat.id, photo=response, reply_to_message_id=message.message_id)

async def text_generator_handler(message: types.Message):

    # await message.answer('Интересный запрос , подождите немного и бот скинет текст ')
    if message.text == 'Выход из режима':

        await dp.current_state(user=message.from_user.id).reset_state()
        await message.reply('Вы вышли из режим Генерация текста',reply_markup=markups.mainMenu)
    else:
        response = await text_generate.text_generator(message.text)
        await bot.send_message(chat_id=message.chat.id, text=response, reply_to_message_id=message.message_id)

