import asyncio
import signal
import imports
import logging
import handlers.clientprem
import handlers.adminprem
import db.sqlite_db 
from aiogram import Bot, Dispatcher
from aiogram.filters import Command

    #Запуск SQLite
print('Бот онлайн')
sqlite_db.sql_start()

    #Стартовая функция и логирование
async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=imports.TOKEN)

    dp = Dispatcher()

    #Регистрация обработчиков и коллбеков
    dp.message.register(clientprem.startup, Command(commands=['start', 'help']))
    dp.message.register(adminprem.op, Command(commands='op'))
    dp.message.register(adminprem.add, Command(commands='Добавить'))
    dp.message.register(sqlite_db.sql_get_tables, Command(commands='Показать таблицы'))
    dp.message.register(adminprem.cancel, Command(commands='Отмена'))
    dp.message.register(adminprem.load_photo, UPD.photo)
    dp.message.register(adminprem.load_name, UPD.name)
    dp.message.register(adminprem.load_description, UPD.description)
    dp.message.register(adminprem.load_price, UPD.price)
    dp.callback_query.register(clientprem.russian, lambda c: c.data.startswith('RUS'))
    dp.callback_query.register(clientprem.english, lambda c: c.data.startswith('ENG'))
    dp.callback_query.register(clientprem.store, lambda c: c.data.startswith('Магазин'))
    dp.callback_query.register(clientprem.faq, lambda c: c.data.startswith('ЧаВо'))
    dp.callback_query.register(clientprem.reviews, lambda c: c.data.startswith('Отзывы'))
    dp.callback_query.register(clientprem.support, lambda c: c.data.startswith('Помощь'))
    dp.callback_query.register(clientprem.store_en, lambda c: c.data.startswith('Store'))
    dp.callback_query.register(clientprem.faq_en, lambda c: c.data.startswith('FAQ'))
    dp.callback_query.register(clientprem.reviews_en, lambda c: c.data.startswith('Reviews'))
    dp.callback_query.register(clientprem.support_en, lambda c: c.data.startswith('Support'))
    dp.callback_query.register(clientprem.fortnite, lambda c: c.data.startswith('Фортнайт'))
    dp.callback_query.register(clientprem.fortnite_en, lambda c: c.data.startswith('Fortnite'))
    dp.callback_query.register(clientprem.vbucks, lambda c: c.data.startswith('Вбаксы'))
    dp.callback_query.register(clientprem.vbucks_en, lambda c: c.data.startswith('Vbucks'))
    dp.callback_query.register(clientprem.bunldes, lambda c: c.data.startswith('Наборы'))
    dp.callback_query.register(clientprem.bunldes_en, lambda c: c.data.startswith('Bundles'))
    dp.callback_query.register(clientprem.subs, lambda c: c.data.startswith('Подписки'))
    dp.callback_query.register(clientprem.subs_en, lambda c: c.data.startswith('Subs'))
    dp.callback_query.register(clientprem.spotify, lambda c: c.data.startswith('Спотифай'))
    dp.callback_query.register(clientprem.spotify_en, lambda c: c.data.startswith('Spotify'))
    dp.callback_query.register(clientprem.xbox, lambda c: c.data.startswith('бокс'))
    dp.callback_query.register(clientprem.xbox_en, lambda c: c.data.startswith('xbox'))


    #Старт поллинга, потом поменяется на хуки
    try:                                                       
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

    #Обработка SIGTERM
    def handle_sigterm(signum, frame):              
        loop = asyncio.get_event_loop()
        tasks = asyncio.all_tasks(loop)
        for task in tasks:
            task.cancel()
    
    def setup_signals():
        signal.signal(signal.SIGTERM, handle_sigterm)


if __name__ == "__main__":
    asyncio.run(start())
