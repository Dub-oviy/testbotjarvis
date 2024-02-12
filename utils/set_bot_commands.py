from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("manual", "Инструкции по использованию"),
            types.BotCommand("profile", "Профиль,сведение о подписке"),
            # types.BotCommand("pay", "Купить подписку"),
            # types.BotCommand("ref", "Программа рефера"),
            # types.BotCommand("image", "Сгенерировать фотографию"),

        ]
    )
