from aiogram import executor
from loader import dp,db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from handlers.users.echo import bot_message
from handlers.users.subscription import buy_subscription

async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    dp.register_message_handler(bot_message)
    dp.register_callback_query_handler(buy_subscription)
    db.top_up_balance()

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup , timeout=None)



    