import sqlite3 as sq
import imports
from aiogram import Bot, types
from handlers.adminprem import select_table
global base, cur
bot = Bot(token=imports.TOKEN)

    # Функция старта базы данных
def sql_start():
    global base, cur
    base = sq.connect('premstore.db')
    cur = base.cursor()
    if base:
        print ('База данных подключена!')
    base.execute('CREATE TABLE IF NOT EXISTS vbucks(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS bundles(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS spotify(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS vbucksEN(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS bundlesEN(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS spotifyEN(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS xboxRU(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS xboxEN(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()

    # Функция получения таблиц базы данных (Лол, а зачем она нужна по итогу?)
async def get_tables(message: types.Message, bot: Bot):
    cur.execute('SELECT name FROM sqlite_master WHERE type = "table"')
    tables = cur.fetchall()
    tables_str = ', '.join([table[0] for table in tables])
    await message.answer(f"Таблицы в базе данных: {tables_str}")

    # Сохранение данных в выбранную таблицу из callback_data в модуле adminprem
async def save_data(selected_table, data_tuple):
    cur.execute(f'INSERT INTO {selected_table} VALUES (?, ?, ?, ?)', data_tuple)
    base.commit()

    # Чтение данных из таблицы соответствующей выбору пользователя
async def read_vbucks(message):
    for ret in cur.execute('SELECT * FROM vbucks').fetchall():
        await bot.send_message(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')

async def read_vbucksen(message):
    for ret in cur.execute('SELECT * FROM vbucksEN').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nDescription: {ret[2]}\nPrice: {ret[-1]}')

async def read_bundles(message):
    for ret in cur.execute('SELECT * FROM bundles').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')

async def read_bundlesen(message):
    for ret in cur.execute('SELECT * FROM bundlesEN').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nDescription: {ret[2]}\nPrice: {ret[-1]}')

async def read_spot(message):
    for ret in cur.execute('SELECT * FROM spotify').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')

async def read_spoten(message):
    for ret in cur.execute('SELECT * FROM spotEN').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nDescription: {ret[2]}\nPrice: {ret[-1]}')

async def read_xbox(message):
    for ret in cur.execute('SELECT * FROM xboxRU').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')

async def read_xboxen(message):
    for ret in cur.execute('SELECT * FROM xboxEN').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nDescription: {ret[2]}\nPrice: {ret[-1]}')


