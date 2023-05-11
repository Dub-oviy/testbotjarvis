from loader import dp
from aiogram import types
from states.states import chatgpt_handler, dall_e_handler
from keyboards.default import markups

from keyboards.inline import inlinemarkups
# import profanity_check
dp.register_message_handler(chatgpt_handler, state='chatgpt')
dp.register_message_handler(dall_e_handler ,state='dall_e')

@dp.message_handler(content_types=['text'])
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        # Проверяем текущее состояние пользователя
        state = dp.current_state(user=message.from_user.id)
        if message.text == 'Генерация изображений':
            # Если пользователь выбрал другой режим, сбрасываем текущее состояние на "dall_e"
            await state.set_state('dall_e')
            await message.reply('Это режим генерации изображений, тут вы можете написать, что вы хотите увидеть, а потом бот сгенерирует вам изображение',
                                reply_markup=markups.secondMenu)
            await dall_e_handler(message)

        elif message.text == 'Режим переводчика':
            # Если пользователь выбрал другой режим, сбрасываем текущее состояние на "translate"
            await message.reply('Вы вошли в режим переводчика, при написании текста на английском языке, бот автоматически переведет его на Русский.', reply_markup=inlinemarkups.language)

        else:
            if await state.get_state() != 'chatgpt':
            # Если состояние пользователя не "chatgpt", то сбрасываем его на "chatgpt"
                await state.set_state('chatgpt')
                await message.answer('Это режим Всезнайка, здесь вы можете задавать вопросы ChtGpt')
                await chatgpt_handler(message)