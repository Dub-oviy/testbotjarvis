from loader import dp
from aiogram import types
from states.states import chatgpt_handler, dall_e_handler, text_generator_handler

from keyboards.inline import inlinemarups
from utils import chatgpt,dall_e,text_generate
# import profanity_check
dp.register_message_handler(chatgpt_handler, state='chatgpt')
dp.register_message_handler(dall_e_handler ,state='dall_e')
dp.register_message_handler(text_generator_handler,state='text_generator')






@dp.message_handler(content_types=['text'])
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'Всезнайка':
            await message.reply('Это режим Всезнайка тут вы задаете вопросы ChtGpt') 
            await dp.current_state(user=message.from_user.id).set_state('chatgpt')
            await chatgpt_handler(message)
            # response = await chatgpt.get_chatgpt_message(message.text)
        if message.text == 'Генерация изображений':
            await message.reply('Это режим генерации изображений, тут вы можете написать что вы хотите увидеть а потои бот с генерирует вам изображеие') 
            await dp.current_state(user=message.from_user.id).set_state('dall_e')
            await dall_e_handler(message)
            # response = await dall_e.generate_image(message.text)
        elif message.text == 'Генерация текста':
            await message.reply('Это режим Генерации текста тут вы пишите название или короткий текст и ИИ сам за вас всё допишет и напишет') 
            await dp.current_state(user=message.from_user.id).set_state('text_generator')
            await text_generator_handler(message) 
            # response = await text_generate.text_generator(message.text)
        elif message.text == 'Режим переводчика':
            await message.reply('Это режим переводчика тут вы выбираете язык на котором бот булет вам писать , можно не трогать этот режим и бот будет работать в обынчом режиме',
                                reply_markup=inlinemarups.language)
            # while != 'Назад':
            #     await message.reply('Выход из режим',)
                

