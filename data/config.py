from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env() 

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
OPENAI_API = env.str("OPENAI_API")
# OPENAI_API = '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'
# ADMINS = [1133571937]  # Тут у нас будет список из админов
# BOT_TOKEN = '6163546129:AAH66Ep47nFkQzolqsq-cD4xbvvew6saVg4'  # Забираем значение типа str

