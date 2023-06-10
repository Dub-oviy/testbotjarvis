import logging
import aiogram
import asyncio
import telegram
from loader import Admins, Users, dp,bot,db,chatGPTMessageHandler
from aiogram import types
from states.mailing_state import bot_mailing
from utils import dall_e,translator_mode
from keyboards.default import markups
from images import *
from handlers.users.start import bot_start
from handlers.users.help import bot_help
from handlers.users.commands import manual_getter,balance_getter

commandlist = ['/start' ,'/help','/balance','/manual']
adminmenu = [ 'Отправить сообщение' ,'Статистика за неделю' ,'Статистика за месяц']
usermenu = ['Генерация изображений 🌄','Режим переводчика 📚' ]


async def chatgpt_handler(message: types.Message):
    user_id = message.from_user.id
    try:
        if message.text in usermenu:
            # Удаляем обработчик сообщений Всезнайка
            await dp.current_state(user=user_id).set_state(None)
            if user_id in [int(admin_id) for admin_id in Admins]:
                await message.answer('Вы вышли из режим Всезнайка',reply_markup=markups.AdminMenu)
            else:
                await message.answer('Вы вышли из режим Всезнайка',reply_markup=markups.mainMenu)
            if message.text == 'Генерация изображений 🌄':
                await dp.current_state(user=user_id).set_state('dall_e')
                with open('images/textimage.png','rb') as photo1:
                    await bot.send_photo(message.chat.id,photo=photo1 , caption ='Это режим генерации изображений, тут вы можете написать, что вы хотите увидеть, а потом бот сгенерирует вам изображение',
                                    reply_markup=markups.secondMenu)
                await dall_e_handler(message)
            elif message.text == 'Режим переводчика 📚':
                with open('images/textimage.png','rb') as photo2:
                    await bot.send_photo(message.chat.id,photo=photo2 , caption ='Это режим переводчика, при написании текста на английском языке, бот автоматически переведет его на Русский.',
                                    reply_markup=markups.secondMenu)
                await dp.current_state(user=user_id).set_state('translator')
                await translator_handler(message)
        elif message.text in commandlist:
            if message.text == '/start':
                await dp.current_state(user=user_id).reset_state()
                await bot_start(message)
            elif message.text == '/help':
                await bot_help(message)
            elif message.text == '/balance':
                await balance_getter(message)
            elif message.text == '/manual':
                await manual_getter(message)
        elif message.text in adminmenu and user_id in [int(admin_id) for admin_id in Admins]:
            if message.text == 'Отправить сообщение':
                await dp.current_state(user=user_id).reset_state()
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
            if (db.get_user_balance(user_id=user_id) == "0"):
                await message.answer('У вас закончились попытки пожалуйста поплните их')
            else:
                db.decrease_user_balance(user_id=user_id,amount=1)
                await bot.send_chat_action(message.chat.id, "typing")
                print(message.text)
                response = await chatGPTMessageHandler.get_chatgpt_message(message.text)
                await bot.send_message(chat_id=message.chat.id, text=response, reply_to_message_id=message.message_id)
    except Exception as e:
        await dp.current_state(user=user_id).reset_state()
        await bot_start(message)
        
async def dall_e_handler(message: types.Message):
    user_id = message.from_user.id
    if message.text == 'Выход из режима 🔼':
        await dp.current_state(user=user_id).reset_state()
        if user_id  in [int(admin_id) for admin_id in Admins]:
            await message.reply('Вы вышли из режима Генерация изображений',reply_markup=markups.AdminMenu)
        else:
            await message.reply('Вы вышли из режима Генерация изображений',reply_markup=markups.mainMenu)

    else:
        if message.text == 'Генерация изображений 🌄':
            pass
        elif message.text in commandlist:
            if message.text == '/start':
                await dp.current_state(user=user_id).reset_state()
                await bot_start(message)
            elif message.text == '/help':
                await bot_help(message)
            elif message.text == '/balance':
                await balance_getter(message)
            elif message.text == '/manual':
                await manual_getter(message)
        else:
            try:
                if (db.get_user_balance(user_id=user_id) == "0"):
                    await message.answer('У вас закончились попытки пожалуйста поплните их')
                else:
                    db.decrease_user_balance(user_id=user_id,amount=1)
                    await message.answer( 'Интересный запрос , подождите немного и бот отправит изображение')
                    await bot.send_chat_action(message.chat.id, "upload_photo")
                    response = await dall_e.generate_image(message.text)
                    await bot.send_chat_action(message.chat.id, aiogram.types.ChatActions.UPLOAD_PHOTO)
                    await bot.send_photo(chat_id=message.chat.id, photo=response, reply_to_message_id=message.message_id)
            except Exception as e:
                await dp.current_state(user=user_id).reset_state()
                await bot_start(message)
                
async def translator_handler(message: types.Message):
    user_id = message.from_user.id
    if message.text == 'Выход из режима 🔼':
        await dp.current_state(user=user_id).reset_state()
        if user_id  in [int(admin_id) for admin_id in Admins]:
            await message.reply('Вы вышли из режим переводчика',reply_markup=markups.AdminMenu)

        else:
            await message.reply('Вы вышли из режим переводчика',reply_markup=markups.mainMenu)

    else:
        if message.text == 'Режим переводчика 📚':
            pass
        elif  message.text in commandlist:
            if message.text == '/start':
                await dp.current_state(user=user_id).reset_state()
                await bot_start(message)
            elif message.text == '/help':
                await bot_help(message)
            elif message.text == '/balance':
                await balance_getter(message)
            elif message.text == '/manual':
                await manual_getter(message)
        else:
            try:
                if (db.get_user_balance(user_id=user_id) == "0"):
                    await message.answer('У вас закончились попытки пожалуйста поплните их')
                else:
                    db.decrease_user_balance(user_id=user_id,amount=1)
                    await bot.send_chat_action(message.chat.id, "typing")
                    answer = await translator_mode.translate_mode(message.text)
                    await bot.send_chat_action(message.chat.id, aiogram.types.ChatActions.TYPING)
                    await bot.send_message(chat_id=message.chat.id, text=answer, reply_to_message_id=message.message_id)
            except Exception as e:
                    await dp.current_state(user=user_id).reset_state()
                    await bot_start(message)
