from aiogram import types
from keyboards.inline import inlinemarkups
from loader import dp,db


@dp.message_handler(commands=['balance'])
async def balance_getter(message : types.Message):
    
    userName =  db.get_user_name(message.from_user.id)
    userUserName =  db.get_user_userame(message.from_user.id)
    userId =  db.get_user_id(message.from_user.id)
    userBalance =  db.get_user_balance(message.from_user.id)
    


    await message.answer(
        f"Пользователь: {userName}\nИмя пользователя: @{userUserName}\nID: {userId}\nБaлaнc: {userBalance} ипользований",
        reply_markup= inlinemarkups.subscriptionMenu
    )
    

@dp.message_handler(commands=['manual'])
async def manual_getter(message: types.Message):
    # await message.answer('Инструкция по использованию после запуска бота вы можете выбрать один из режимов и так же воспользоваться режимом по умолчанию то есть задать вопросы ChatGpt(3.5 turbo) с помощью чата гпт вы мо ')
    await message.answer(   
        'Ниже приведена инструкция по использованию различных режимов ChatGPT:\n1. Режим ChatGPT (режим по умолчанию):\n Просто напишите что-то, не выбирая никаких опций. Бот будет использовать модель в зависимости от вашей подписки информация о подписках в разделе профиль, которая является одной из самых передовых моделей для генерации текста на рынке. Она способна предоставить высококачественные ответы на широкий спектр вопросов, которые вы ей зададите.\n\n'
        'Режим генерации изображений (DALL-E):\n В зависимости от вашей подписки. Выберите этот режим, а затем напишите запрос о том, что вы хотите увидеть на изображении. Бот будет использовать модель DALL-E, которая способна генерировать уникальные и красивые изображения на основе ваших запросов.\n\n'
        'Режим переводчика:\n3. Выберите этот режим, а затем напишите текст, который вы хотите перевести. Бот мгновенно выполнит перевод любого текста автоматически. Если вы написали текст на английском языке, бот переведет его на русский язык, а если текст на русском языке, бот переведет его на английский язык.'
    )