import aiogram
from loader import dp,bot,textphoto,translatephoto
from aiogram import types
from utils import chatgpt,dall_e,translator_mode
from keyboards.inline import inlinemarkups
from keyboards.default import markups




async def chatgpt_handler(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    if message.text == 'Генерация изображений🌄' or message.text == 'Режим переводчика📚':
        # Удаляем обработчик сообщений Всезнайка
        await dp.current_state(user=message.from_user.id).set_state(None)
        await message.answer('Вы вышли из режим Всезнайка',reply_markup=markups.mainMenu)
        if message.text == 'Генерация изображений🌄':
            await dp.current_state(user=message.from_user.id).set_state('dall_e')
            await bot.send_photo(message.chat.id , photo=textphoto ,caption ='Это режим генерации изображений, тут вы можете написать, что вы хотите увидеть, а потом бот сгенерирует вам изображение',
                                reply_markup=markups.secondMenu)
            await dall_e_handler(message)
        elif message.text == 'Режим переводчика📚':
            await bot.send_photo(message.chat.id , photo=translatephoto ,caption ='Вы вошли в режим переводчика, при написании текста на английском языке, бот автоматически переведет его на Русский.',
                                reply_markup=markups.secondMenu)
            await dp.current_state(user=message.from_user.id).set_state('translator')
            await translator_handler(message)
    else:
        await bot.send_chat_action(message.chat.id, "typing")
        response = await chatgpt.get_chatgpt_message(message.text)
        await bot.send_message(chat_id=message.chat.id, text=response, reply_to_message_id=message.message_id)

async def dall_e_handler(message: types.Message):
    # await message.answer( 'Интересный запрос , подождите немного и бот скинет изображение')
    if message.text == 'Выход из режима🔼':
        # Удаляем обработчик сообщений Всезнайка
        await dp.current_state(user=message.from_user.id).reset_state()
        await message.reply('Вы вышли из режим Генерация изображений',reply_markup=markups.mainMenu)
    else:
        if message.text == 'Генерация изображений🌄':
            pass
        else:
            await message.answer( 'Интересный запрос , подождите немного и бот скинет изображение')
            response = await dall_e.generate_image(message.text)
            await bot.send_chat_action(message.chat.id, "upload_photo")
            await bot.send_chat_action(message.chat.id, aiogram.types.ChatActions.UPLOAD_PHOTO)
            await bot.send_photo(chat_id=message.chat.id, photo=response, reply_to_message_id=message.message_id)

async def translator_handler(message: types.Message):
    if message.text == 'Выход из режима🔼':
        await dp.current_state(user=message.from_user.id).reset_state()
        await message.reply('Вы вышли из режим переводчика',reply_markup=markups.mainMenu)
    else:
        if message.text == 'Режим переводчика📚':
            pass
        else:
            await bot.send_chat_action(message.chat.id, "typing")
            answer = await translator_mode.translate_mode(message.text)
            await bot.send_chat_action(message.chat.id, aiogram.types.ChatActions.TYPING)
            await bot.send_message(chat_id=message.chat.id, text=answer, reply_to_message_id=message.message_id)