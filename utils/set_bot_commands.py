from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("manual", "Инструкции по использованию"),
            types.BotCommand("balance", "Узнать баланс"),
            # types.BotCommand("pay", "Купить подписку"),
            # types.BotCommand("ref", "Программа рефера"),
            # types.BotCommand("image", "Сгенерировать фотографию"),

        ]
    )
