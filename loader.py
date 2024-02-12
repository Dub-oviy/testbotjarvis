from aiogram import Bot, Dispatcher, types
from apscheduler.schedulers.background import BackgroundScheduler
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config
from data import *
import openai
from language_mode import LanguageMode
from utils.misc.db import Database

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
scheduler = BackgroundScheduler()
dp = Dispatcher(bot, storage=storage)
db = Database('data/database.db')
openai.api_key = config.OPENAI_API
languageMode = LanguageMode('default')
Admins = config.ADMINS
Users = db.get_all_userid()
# hellophoto = 'images/Hello.png'
# textphoto = InputFile('images/textimage.png')
# translatephoto = InputFile('images/Translate.png')