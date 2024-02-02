import logging
from aiogram import types
from aiogram.dispatcher import FSMContext
from states import bot_mailing
from loader import Users, dp,bot
from keyboards.inline import inlinemarkups


@dp.message_handler(state=bot_mailing.text)
async def mailing_text(message : types.Message , state : FSMContext):
    answer = message.text
    await state.update_data(text=answer)
    await message.answer(text=answer , reply_markup=inlinemarkups.addphotomenu)
    await bot_mailing.state.set()

@dp.callback_query_handler(state=bot_mailing.state,text = 'next')
async def start_without_photo(call:types.CallbackQuery,state:FSMContext):
    data = await state.get_data()
    text = data.get('text')
    await state.finish()
    for user_id in Users:
        try:
            await bot.send_message(chat_id=user_id,text=text)
        except Exception as e:
                    logging.exception(f"Error sending message to user {user_id}: {e}")
                    await call.message.answer('Произошла ошибка')
    await call.message.answer(f"Сообщение отправлено {len(Users)} пользователям")

@dp.callback_query_handler(text='add_photo',state=bot_mailing.state)
async def add_photo(call : types.CallbackQuery):
    await call.message.answer('Пришлите фотографию')
    await bot_mailing.photo.set()


@dp.message_handler(state=bot_mailing.photo , content_types=types.ContentType.PHOTO)
async def mailing_photo(message : types.Message , state : FSMContext):
    photo_file_id =message.photo[-1].file_id
    await state.update_data(photo=photo_file_id)
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')
    await message.answer_photo(photo=photo , caption=text,reply_markup=inlinemarkups.quitphotomenu)

@dp.callback_query_handler(state=bot_mailing.photo,text='next')
async def start(call:types.CallbackQuery,state:FSMContext):
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')
    await state.finish()
    for user_id in Users:
        try:
            await bot.send_photo(photo=photo,chat_id=user_id,caption=text)
        except Exception as e:
                    logging.exception(f"Error sending message to user {user_id}: {e}")
                    await call.message.answer('Произошла ошибка')
    await call.message.answer(f"Сообщение отправлено {len(Users)} пользователям")

@dp.message_handler(state=bot_mailing.photo)
async def no_photo(message: types.Message):
    await message.answer('Пришлите фотографию ',reply_markup=inlinemarkups.quitbtn)


@dp.callback_query_handler(state=[bot_mailing.text , bot_mailing.photo,bot_mailing.state],text = 'quit')
async def quit(call: types.CallbackQuery,state= FSMContext):
    await state.finish()
    await call.message.answer('Рассылка отменена ')