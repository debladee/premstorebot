import sqlite3 as sq
import imports
from aiogram import Bot, types
from inline import inline
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

# def sql_start():
#     global base, cur
#     base = sq.connect('premstore.db')
#     cur = base.cursor()
#     if base:
#         print ('База данных подключена!')
    
#     table_definitions = {
#         'vbucks': ['img TEXT', 'name TEXT PRIMARY KEY', 'description TEXT', 'price TEXT'],
#         'bundles': ['img TEXT', 'name TEXT PRIMARY KEY', 'description TEXT', 'price TEXT'],
#         'spotify': ['img TEXT', 'name TEXT PRIMARY KEY', 'description TEXT', 'price TEXT'],
#         'subs': ['img TEXT', 'name TEXT PRIMARY KEY', 'description TEXT', 'price TEXT'],
#         'xboxRU': ['img TEXT', 'name TEXT PRIMARY KEY', 'description TEXT', 'price TEXT'],
#         'vbucksEN': ['img TEXT', 'name TEXT PRIMARY KEY', 'description TEXT', 'price TEXT'],
#         'bundlesEN': ['img TEXT', 'name TEXT PRIMARY KEY', 'description TEXT', 'price TEXT'],
#         'spotifyEN': ['img TEXT', 'name TEXT PRIMARY KEY', 'description TEXT', 'price TEXT'],
#         'xboxEN': ['img TEXT', 'name TEXT PRIMARY KEY', 'description TEXT', 'price TEXT'],
#     }

#     for table_name, columns in table_definitions.items():
#         colums_str = ', '.join(columns)
#         base.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})')
    
#     base.commit()

    # Функция получения таблиц базы данных
async def get_tables():
    cur.execute('SELECT name FROM sqlite_master WHERE type = "table"')
    tables = cur.fetchall()
    tables_list = [table[0] for table in tables]
    return tables_list

    # Сохранение данных в выбранную таблицу из callback_data в модуле adminprem
async def save_data(selected_table, data_tuple):
    cur.execute(f'INSERT INTO {selected_table} VALUES (?, ?, ?, ?)', data_tuple)
    base.commit()

    # Чтение данных из таблицы соответствующей выбору пользователя
def read_data(table_name):
    cur.execute(f'SELECT name, price FROM {table_name}')
    results = cur.fetchall()
    return results

def read_data_delete(table_name):
    cur.execute(f'SELECT name FROM {table_name}')
    results = cur.fetchall()
    return results

async def del_table(selected_table):
    cur.execute(f'DROP TABLE IF EXISTS {selected_table}')
    base.commit()

async def del_data(table_name, product_id):
    cur.execute(f'DELETE FROM {table_name} WHERE name = ?', (product_id,))
    base.commit()

async def product_output(product_id):
    cur.execute(f'')