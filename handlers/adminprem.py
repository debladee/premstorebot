from db import sqlite_db
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import types, Bot, Dispatcher
from adminkb.adminkb import admkb
from inline import inline
from imports import ADMIN, TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher()

    # Машина состояний
class UPD(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()
    table_select = State()

    # Включение клавиатуры администратора
async def op(message: types.Message, bot: Bot):
    if message.from_user.id == ADMIN:
        await message.answer('Добро пожаловать в админ-меню, воспользуйтесь клавиатурой для совершения действий', reply_markup=admkb)
    else:
        await bot.send_message(message.from_user.id, 'Вы не являетесь администратором')

    # Функция отмены добавления
async def cancel(message: types.Message, state: FSMContext, bot: Bot):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer('Изменения отменены')

    # Начало машины состояний, доп. проверка ID администратора, добавление картинки и перевод в состояние UPD.photo
async def add(message: types.Message, state: FSMContext, bot: Bot):
    if message.from_user.id == ADMIN: 
        await message.answer('Добавьте картинку, обратите внимание на язык, который вы собираетесь добавить')
        await state.set_state(UPD.photo)
    else:
        await bot.send_message(message.from_user.id, 'Вы не можете выполнить данное действие, так как не являетесь администратором')

    # Обновление данных о фото за счёт API телеграм в файл для записи в базу данных, перевод в состояние UPD.name
async def load_photo(message: types.Message, state: FSMContext, bot: Bot):
    await state.update_data(photo=message.photo[-1].file_id)
    await state.set_state(UPD.name)
    await message.answer("Введите название товара")


    # Обновление данных для имени, перевод состояния в UPD.description
async def load_name(message: types.Message, state : FSMContext, bot: Bot):
    await state.update_data(name=message.text)
    await state.set_state(UPD.description)
    await message.answer("Введите описание")


    # Обновление данных для описания, перевод состояния в UPD.price
async def load_description(message: types.Message, state : FSMContext, bot: Bot):
    await state.update_data(description=message.text)
    await state.set_state(UPD.price)
    await message.answer("Укажите цену в RUB или USD")


    # Обновление данных для цены, перевод состояния в UPD.table_select
async def load_price(message: types.Message, state : FSMContext, bot: Bot):
    await state.update_data(price=float(message.text))
    await state.set_state(UPD.table_select)
    available_tables = await sqlite_db.get_tables()
    await message.answer('Теперь выберете таблицу для записи данных:', reply_markup=inline.table_selector(available_tables))


    # Выбор таблицы, возврат полученных в этом состоянии данных
async def select_table(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    selected_table = callback.data.split(":")[1]

    await callback.message.answer('Таблица выбрана. Данные записаны.')

    data = await state.get_data()
    data_tuple = tuple(data.values())

    await sqlite_db.save_data(selected_table, data_tuple)
    await callback.answer()
    await state.clear()