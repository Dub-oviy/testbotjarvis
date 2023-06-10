import logging
from loader import Admins, Users, dp,bot
from aiogram import types
from states.states import *
from keyboards.default import markups
from images import *
from keyboards.inline import inlinemarkups

# import profanity_check
dp.register_message_handler(chatgpt_handler, state='chatgpt',content_types=['text'])
dp.register_message_handler(dall_e_handler ,state='dall_e',content_types=['text'])
dp.register_message_handler(translator_handler ,state='translator',content_types=['text'])

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        # Проверяем текущее состояние пользователя
        state = dp.current_state(user=message.from_user.id)
        if message.text == 'Генерация изображений 🌄':
            with open('images/textimage.png','rb') as photo1:
                await bot.send_photo(message.chat.id,photo=photo1 , caption ='Это режим генерации изображений, тут вы можете написать, что вы хотите увидеть, а потом бот сгенерирует вам изображение',
                                reply_markup=markups.secondMenu)
            await state.set_state('dall_e')
            await dall_e_handler(message)

        elif message.text == 'Режим переводчика 📚':
            with open('images/Translate.png','rb') as photo2:
                await bot.send_photo(message.chat.id,photo=photo2 , caption ='Это режим переводчика, при написании текста на английском языке, бот автоматически переведет его на Русский.',
                                reply_markup=markups.secondMenu)
            await state.set_state('translator')
            await translator_handler(message)
        elif message.text in [ 'Отправить сообщение' ,'Статистика за неделю' ,'Статистика за месяц']:
            if message.from_user.id  in [int(admin_id) for admin_id in Admins]:
                if message.text == 'Отправить сообщение':
                    await message.answer(f'Введите тект рассылки')
                    await bot_mailing.text.set()
                elif message.text == 'Статистика за неделю':
                    stats_week_message = db.get_weekly_statistics()
                    await message.answer(stats_week_message)
                elif message.text == 'Статистика за месяц':
                    stats_mounth_message =  db.get_mounthly_statistics()
                    await message.answer(stats_mounth_message)
            else:
                pass
        else: 
            if await state.get_state() != 'chatgpt':
            # Если состояние пользователя не "chatgpt", то сбрасываем его на "chatgpt"
                await state.set_state('chatgpt')
                await message.answer('Это режим Всезнайка, здесь вы можете задавать вопросы ChtGpt')
                await chatgpt_handler(message)
            