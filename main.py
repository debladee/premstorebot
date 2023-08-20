import asyncio
import signal
import imports
import logging
import handlers.clientprem
import handlers.adminprem
import db.sqlite_db 
from aiogram import Bot, Dispatcher
from aiogram.filters import Command

    # Запуск SQLite
print('Бот онлайн')
db.sqlite_db.sql_start()

    # Стартовая функция и логирование
async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=imports.TOKEN)

    dp = Dispatcher()

    # Регистрация обработчиков и коллбеков
    dp.message.register(handlers.clientprem.startup, Command(commands=['start', 'help', 'начать', 'Начать', 'привет', 'Привет']))
    dp.message.register(handlers.adminprem.op, Command(commands='op'))
    dp.message.register(db.sqlite_db.get_tables, Command(commands='Таблицы'))
    dp.message.register(handlers.adminprem.add, Command(commands='Добавить'))
    dp.message.register(handlers.adminprem.cancel, Command(commands='Отмена'))
    dp.message.register(handlers.adminprem.load_photo, handlers.adminprem.UPD.photo)
    dp.message.register(handlers.adminprem.load_name, handlers.adminprem.UPD.name)
    dp.message.register(handlers.adminprem.load_description, handlers.adminprem.UPD.description)
    dp.message.register(handlers.adminprem.load_price, handlers.adminprem.UPD.price)
    dp.callback_query.register(handlers.adminprem.select_table, handlers.adminprem.UPD.table_select)
    # dp.message.register(db.sqlite_db.add_vbucks, Command(commands='Вбаксы'))
    # dp.message.register(db.sqlite_db.save_data, Command(commands='Vbucks'))
    dp.callback_query.register(handlers.clientprem.russian, lambda c: c.data.startswith('RUS'))
    dp.callback_query.register(handlers.clientprem.english, lambda c: c.data.startswith('ENG'))
    dp.callback_query.register(handlers.clientprem.store, lambda c: c.data.startswith('Магазин'))
    dp.callback_query.register(handlers.clientprem.faq, lambda c: c.data.startswith('ЧаВо'))
    dp.callback_query.register(handlers.clientprem.reviews, lambda c: c.data.startswith('Отзывы'))
    dp.callback_query.register(handlers.clientprem.support, lambda c: c.data.startswith('Помощь'))
    dp.callback_query.register(handlers.clientprem.store_en, lambda c: c.data.startswith('Store'))
    dp.callback_query.register(handlers.clientprem.faq_en, lambda c: c.data.startswith('FAQ'))
    dp.callback_query.register(handlers.clientprem.reviews_en, lambda c: c.data.startswith('Reviews'))
    dp.callback_query.register(handlers.clientprem.support_en, lambda c: c.data.startswith('Support'))
    dp.callback_query.register(handlers.clientprem.fortnite, lambda c: c.data.startswith('Фортнайт'))
    dp.callback_query.register(handlers.clientprem.fortnite_en, lambda c: c.data.startswith('Fortnite'))
    dp.callback_query.register(handlers.clientprem.vbucks, lambda c: c.data.startswith('Вбаксы'))
    dp.callback_query.register(handlers.clientprem.vbucks_en, lambda c: c.data.startswith('Vbucks'))
    dp.callback_query.register(handlers.clientprem.bunldes, lambda c: c.data.startswith('Наборы'))
    dp.callback_query.register(handlers.clientprem.bunldes_en, lambda c: c.data.startswith('Bundles'))
    dp.callback_query.register(handlers.clientprem.subs, lambda c: c.data.startswith('Подписки'))
    dp.callback_query.register(handlers.clientprem.subs_en, lambda c: c.data.startswith('Subs'))
    dp.callback_query.register(handlers.clientprem.spotify, lambda c: c.data.startswith('Спотифай'))
    dp.callback_query.register(handlers.clientprem.spotify_en, lambda c: c.data.startswith('Spotify'))
    dp.callback_query.register(handlers.clientprem.xbox, lambda c: c.data.startswith('бокс'))
    dp.callback_query.register(handlers.clientprem.xbox_en, lambda c: c.data.startswith('xbox'))


    # Старт поллинга, потом поменяется на хуки
    try:                                                       
        await dp.start_polling(bot)
    finally:
        print("Завершаю работу...")
        await bot.session.close()

    # Обработка SIGTERM
def handle_sigterm(signum, frame):              
    loop = asyncio.get_event_loop()
    tasks = asyncio.all_tasks(loop)
    for task in tasks:
        task.cancel()
    
def setup_signals():
    signal.signal(signal.SIGTERM, handle_sigterm)


if __name__ == "__main__":
    setup_signals()

    asyncio.run(start())
