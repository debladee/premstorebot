import sqlite3 as sq
import imports
from aiogram import Bot
global base, cur
bot = Bot(token=imports.TOKEN)

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

async def sql_add_vbucks(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO vbucks VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_add_vbucksen(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO vbucksEN VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_add_bundles(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO bundles VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_add_bundlesen(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO bundlesEN VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_add_spot(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO spotify VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_add_spoten(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO spotifyEN VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_add_xbox(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO xboxRU VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_add_xboxen(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO xboxEN VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read_vbucks(message):
    for ret in cur.execute('SELECT * FROM vbucks').fetchall():
        await bot.send_message(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')

async def sql_read_vbucksen(message):
    for ret in cur.execute('SELECT * FROM vbucksEN').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nDescription: {ret[2]}\nPrice: {ret[-1]}')

async def sql_read_bundles(message):
    for ret in cur.execute('SELECT * FROM bundles').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')

async def sql_read_bundlesen(message):
    for ret in cur.execute('SELECT * FROM bundlesEN').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nDescription: {ret[2]}\nPrice: {ret[-1]}')

async def sql_read_spot(message):
    for ret in cur.execute('SELECT * FROM spotify').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')

async def sql_read_spoten(message):
    for ret in cur.execute('SELECT * FROM spotEN').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nDescription: {ret[2]}\nPrice: {ret[-1]}')

async def sql_read_xbox(message):
    for ret in cur.execute('SELECT * FROM xboxRU').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')

async def sql_read_xboxen(message):
    for ret in cur.execute('SELECT * FROM xboxEN').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nDescription: {ret[2]}\nPrice: {ret[-1]}')


