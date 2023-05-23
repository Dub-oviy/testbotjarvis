from aiogram import types
from loader import dp,db


@dp.message_handler(commands=['balance'])
async def balance_getter(message : types.Message):
    await message.answer(
        f"Пользователь: {db.get_user_name(message.from_user.id)}\nИмя пользователя: @{db.get_user_userame(message.from_user.id)}\nID: {db.get_user_id(message.from_user.id)}\nБaлaнc: {db.get_user_balance(message.from_user.id)} ипользований"
    )
    print(type(db.get_user_balance(message.from_user.id)))

@dp.message_handler(commands=['manual'])
async def manual_getter(message: types.Message):
    # await message.answer('Инструкция по использованию после запуска бота вы можете выбрать один из режимов и так же воспользоваться режимом по умолчанию то есть задать вопросы ChatGpt(3.5 turbo) с помощью чата гпт вы мо ')
    await message.answer(   
        'Инструкция по использованию \nРежим ChatGpt (режим по умолчанию):\n Просто напишите что-то, не выбирая никаких опций. Бот будет использовать модель ChatGpt 3.5 turbo, которая является самой продвинутой моделью генерации текста на рынке. Она может генерировать высококачественные ответы на любые вопросы, которые вы ей зададите.\n\n'
        'Режим генерации изображений (DALL-E):\nВыберите этот режим. Затем напишите запрос того, что вы хотите увидеть на изображении. Бот будет использовать модель DALL-E, которая может генерировать уникальные и красивые изображения на основе ваших запросов.\n\n'
        'Режим переводчика:\nВыберите этот режим. Затем напишите текст, который вы хотите перевести. Бот очень быстро переведет любой текст автоматически. Если вы написали текст на английском языке, бот переведет его на русский язык, а если текст на русском языке, бот переведет его на английский язык.'
    )