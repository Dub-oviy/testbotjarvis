from loader import dp,bot,textphoto,translatephoto
from aiogram import types
from states.states import chatgpt_handler, dall_e_handler,translator_handler
from keyboards.default import markups

from keyboards.inline import inlinemarkups
# import profanity_check
dp.register_message_handler(chatgpt_handler, state='chatgpt')
dp.register_message_handler(dall_e_handler ,state='dall_e')
dp.register_message_handler(translator_handler ,state='translator')


@dp.message_handler(content_types=['text'])
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        # Проверяем текущее состояние пользователя
        state = dp.current_state(user=message.from_user.id)
        if message.text == 'Генерация изображений 🌄':
            # Если пользователь выбрал другой режим, сбрасываем текущее состояние на "dall_e"
            await state.set_state('dall_e')
            await bot.send_photo(message.chat.id , photo=textphoto ,caption ='Это режим генерации изображений, тут вы можете написать, что вы хотите увидеть, а потом бот сгенерирует вам изображение',
                                reply_markup=markups.secondMenu)
            await dall_e_handler(message)

        elif message.text == 'Режим переводчика 📚':
            await state.set_state('translator')
            await bot.send_photo(message.chat.id , photo=translatephoto ,caption ='Вы вошли в режим переводчика, при написании текста на английском языке, бот автоматически переведет его на Русский.',
                                reply_markup=markups.secondMenu)
            await translator_handler(message)

        else:
            if await state.get_state() != 'chatgpt':
            # Если состояние пользователя не "chatgpt", то сбрасываем его на "chatgpt"
                await state.set_state('chatgpt')
                await message.answer('Это режим Всезнайка, здесь вы можете задавать вопросы ChtGpt')
                await chatgpt_handler(message)