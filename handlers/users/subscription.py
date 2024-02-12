import logging
from aiogram import types
from loader import Users, dp,db
from keyboards.inline import inlinemarkups





@dp.callback_query_handler()
async def buy_subscription (callback : types.CallbackQuery):
    current_sub = db.get_user_subscription(callback.from_user.id)
    
    if callback.data == 'sub':
        await callback.message.answer(f'Ваша текущая подпика : {current_sub}\nЕсли желаете приобрести подписку нажмите на кнопку купить кнопку Приобрести подписку \nЕсли желаете узнать всю информацию о подписках нажмите Тарифы',
                            reply_markup=inlinemarkups.buyingSubscriptionMenu)
    elif callback.data == 'buy_sub':
        pass
    elif callback.data == 'rates':
        await callback.message.answer(f'Тарифы:\nStart(ChatGpt-3.5-turbo,Dall-E-2, переводчик)-выдаётся 1500 использований стоимость 5$\nStandard(ChatGpt-4,Dall-E-3 качество фото: обычное,переводчик)-выдаётся 2000 использований стоимость 8$\nAdvanced(ChatGpt-4-turbo,Dall-E-3 качество фото: HD,переводчик)-выдаётся 2500 использований стоимость 10$', reply_markup=inlinemarkups.buy_subscription)
    else:
        pass




