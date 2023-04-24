from loader import dp, languageMode
from aiogram import types


@dp.callback_query_handler()
async def transalor_mode(callback : types.CallbackQuery):
    if callback.data == 'ru':
        languageMode.languageMode = 'ru'
        await callback.answer(text='Вы перешли в русский режим')
        await callback.answer(text=languageMode.languageMode)

    elif callback.data == 'eng':
        languageMode.languageMode = 'eng'
        await callback.answer(text='You switched to english mode')
        await callback.answer(text=languageMode.languageMode)
