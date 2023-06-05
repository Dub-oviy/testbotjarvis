from aiogram import executor
from loader import dp,db,scheduler
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from handlers.users.echo import bot_message

async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    dp.register_message_handler(bot_message, content_types=['text'])
    db.top_up_balance()
    scheduler.add_job(db.top_up_balance, 'cron', hour=0)
    scheduler.start()

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup , timeout=None)