from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

ru = InlineKeyboardButton('русский' , callback_data='ru')
eng = InlineKeyboardButton('english' , callback_data='eng')

addphoto = InlineKeyboardButton('Добавить фотографию' ,callback_data='add_photo')
next = InlineKeyboardButton('Далее' ,callback_data='next')
quitbtn = InlineKeyboardButton('Отменить',callback_data='quit')

subscription = InlineKeyboardButton('Купить подписку' ,callback_data='sub')
buy_subscription = InlineKeyboardButton('Приобрести подписку',callback_data='buy_sub')
rates = InlineKeyboardButton('Тарифы', callback_data='rates')

language = InlineKeyboardMarkup(row_width=1)
language.add(ru,eng)

addphotomenu = InlineKeyboardMarkup(row_width=2)
addphotomenu.add(addphoto,next,quitbtn)

quitphotomenu= InlineKeyboardMarkup(row_width=2)
quitphotomenu.add(next,quitbtn)

subscriptionMenu = InlineKeyboardMarkup(row_width=2)
subscriptionMenu.add(subscription)

buyingSubscriptionMenu = InlineKeyboardMarkup(row_width=2)
buyingSubscriptionMenu.add(buy_subscription,rates)