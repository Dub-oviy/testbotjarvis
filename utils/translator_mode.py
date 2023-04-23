from loader import dp
from aiogram import types
from language_mode import language_mode

@dp.callback_query_handler()
async def transalor_mode(callback : types.CallbackQuery):
    if callback.data == 'ru':
        language_mode = 'ru'
        await callback.answer(text='Вы перешли в русский режим ')
        await callback.answer(text=language_mode)

    elif callback.data == 'eng':
        language_mode = 'eng'
        await callback.answer(text='You switched to english mode ')
        await callback.answer(text=language_mode)
