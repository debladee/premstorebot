import asyncio
import imports
import logging
from handlers.clientprem import startup, russian, english, store, faq, reviews, support, store_en, faq_en, reviews_en, support_en, fortnite, fortnite_en, vbucks, vbucks_en, bunldes, bunldes_en, subs, subs_en, spotify, spotify_en, xbox_en, xbox
from handlers.adminprem import op, add, cancel, load_name, load_description, load_photo, load_price, UPD
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from db import sqlite_db

print('Бот онлайн')
sqlite_db.sql_start()

async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=imports.TOKEN)

    dp = Dispatcher()
    dp.message.register(startup, Command(commands=['start', 'help']))
    dp.message.register(op, Command(commands='op'))
    dp.message.register(add, Command(commands='Добавить'))
    dp.message.register(cancel, Command(commands='Отмена'))
    dp.message.register(load_photo, UPD.photo)
    dp.message.register(load_name, UPD.name)
    dp.message.register(load_description, UPD.description)
    dp.message.register(load_price, UPD.price)
    dp.callback_query.register(russian, lambda c: c.data.startswith('RUS'))
    dp.callback_query.register(english, lambda c: c.data.startswith('ENG'))
    dp.callback_query.register(store, lambda c: c.data.startswith('Магазин'))
    dp.callback_query.register(faq, lambda c: c.data.startswith('ЧаВо'))
    dp.callback_query.register(reviews, lambda c: c.data.startswith('Отзывы'))
    dp.callback_query.register(support, lambda c: c.data.startswith('Помощь'))
    dp.callback_query.register(store_en, lambda c: c.data.startswith('Store'))
    dp.callback_query.register(faq_en, lambda c: c.data.startswith('FAQ'))
    dp.callback_query.register(reviews_en, lambda c: c.data.startswith('Reviews'))
    dp.callback_query.register(support_en, lambda c: c.data.startswith('Support'))
    dp.callback_query.register(fortnite, lambda c: c.data.startswith('Фортнайт'))
    dp.callback_query.register(fortnite_en, lambda c: c.data.startswith('Fortnite'))
    dp.callback_query.register(vbucks, lambda c: c.data.startswith('Вбаксы'))
    dp.callback_query.register(vbucks_en, lambda c: c.data.startswith('Vbucks'))
    dp.callback_query.register(bunldes, lambda c: c.data.startswith('Наборы'))
    dp.callback_query.register(bunldes_en, lambda c: c.data.startswith('Bundles'))
    dp.callback_query.register(subs, lambda c: c.data.startswith('Подписки'))
    dp.callback_query.register(subs_en, lambda c: c.data.startswith('Subs'))
    dp.callback_query.register(spotify, lambda c: c.data.startswith('Спотифай'))
    dp.callback_query.register(spotify_en, lambda c: c.data.startswith('Spotify'))
    dp.callback_query.register(xbox, lambda c: c.data.startswith('бокс'))
    dp.callback_query.register(xbox_en, lambda c: c.data.startswith('xbox'))


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())
