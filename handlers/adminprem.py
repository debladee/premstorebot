from db import sqlite_db
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import types, Bot, Dispatcher
from adminkb.adminkb import admkb, admtbl
from inline import inline
from imports import ADMIN, TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher()

    # Включение клавиатуры администратора
async def op(message: types.Message, bot: Bot):
    if message.from_user.id == ADMIN:
        await message.answer('Добро пожаловать в админ-меню, воспользуйтесь клавиатурой для совершения действий', reply_markup=admkb)
    else:
        await bot.send_message(message.from_user.id, 'Вы не являетесь администратором')

    # Функция отмены добавления
async def cancel(message: types.Message, state: FSMContext, bot: Bot):
    if message.from_user.id == ADMIN:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.clear()
        await message.answer('Изменения отменены')
    else:
        await bot.send_message(message.from_user.id, 'Вы не являетесь администратором')

    # Машина состояний добавления товара
class UPD(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()
    table_select = State()

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

    # Машина состояний удаление товара
class DEL(StatesGroup):
    select = State()
    delete = State()

async def delete_data_select_table(message: types.Message, state: FSMContext, bot: Bot):
    if message.from_user.id == ADMIN:
        available_tables = await sqlite_db.get_tables()
        await message.answer('Выберите таблицу из которой вы хотите удалить данные', reply_markup=inline.table_selector(available_tables))
        await state.set_state(DEL.select)
    else:
        await bot.send_message(message.from_user.id, 'Вы не являетесь администратором')

async def delete_data_select_product(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    table_name = callback.data.split(":")[1]
    await callback.message.answer('Выберите позицию которую вы хотите удалить.', reply_markup=inline.gen_selection_for_deletion(table_name))
    await state.update_data(table_name=table_name)
    await state.set_state(DEL.delete)
    await callback.answer()

async def delete_selected(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
    data = await state.get_data()
    product_id = callback.data.split(":")[1]
    table_name = data.get('table_name')
    await sqlite_db.del_data(table_name, product_id)
    updated_keyboard_markup = inline.gen_selection_for_deletion(table_name)
    await bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=updated_keyboard_markup)
    await callback.answer()

    # Когда-нибудь здесь будет редактирование данных, но не сейчас
# class EDIT(StatesGroup):
#     photo = State()
#     name = State()
#     description = State()
#     price = State()

# async def edit_data(message: types.Message, state: FSMContext, bot: Bot):
#     if message.from_user.id == ADMIN:
#         available_tables = await sqlite_db.get_tables()
#         await message.answer('Выберите таблицу в которой вы хотите изменить позицию', reply_markup=sqlite_db.table_selector(available_tables))
#     else:
#         await bot.send_message(message.from_user.id, 'Вы не можете выполнить данное действие, так как не являетесь администратором')

# async def select_row(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
#     table_name = callback.data.split(":")[0]




    # Смена клавиатуры
async def changekb(message: types.Message, state : FSMContext, bot: Bot):
    if message.from_user.id == ADMIN:
        await message.answer('Переключаюсь клавиатуру на управление таблицами', reply_markup=admtbl)
    else:
        await bot.send_message(message.from_user.id, 'Вы не можете выполнить данное действие, так как не являетесь администратором')

    # Создание новых таблиц
class TBL(StatesGroup):
    table_name = State()

async def new_table(message: types.Message, state: FSMContext, bot: Bot):
    await message.answer('Введите имя новой таблицы:')
    await state.set_state(TBL.table_name)

async def create_table(message: types.Message, state: FSMContext, bot: Bot):
    table_name = message.text
    columns = ['img TEXT', 'name TEXT PRIMARY KEY', 'description TEXT', 'price TEXT']

    sqlite_db.base.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({", ".join(columns)})')
    sqlite_db.base.commit()

    await message.answer(f'Таблица {table_name} успешно добавлена!')
    await state.clear()
    
# class TBLDEL(StatesGroup):
#     confirm_prompt = State()
#     handle_confirm = State()

    # Удаление таблиц
# async def delete_table(message: types.Message, state: FSMContext, bot: Bot):
#     available_tables = await sqlite_db.get_tables()

#     await message.answer('Внимание! Удаление таблицы приводит к полной потери данных, действуйте на своё усмотрение!', reply_markup=inline.table_selector(available_tables))
#     await state.set_state(TBLDEL.confirm_prompt)

# async def confirmation_prompt(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
#     selected_table = callback.data.split(":")[1]
#     await state.update_data(selected_table=selected_table)

#     new_message = await callback.message.answer(f'Вы действительно хотите удалить таблицу {selected_table}', reply_markup=inline.yes_no())
#     await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)

#     await state.set_state(TBLDEL.handle_confirm)
#     await callback.answer()

# async def handle_confirmation(callback: types.CallbackQuery, state: FSMContext, bot: Bot):
#     data = await state.get_data()
#     selected_table = data.get("selected_table")

#     if callback.data == "Yes":
#         await sqlite_db.del_table(selected_table)
#         new_message = await callback.message.answer(f'Таблица {selected_table} успешно удалена!')
#         await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
#     else:
#         await callback.message.edit_text('Удаление таблицы отменено.')

#     await state.clear()
#     await callback.answer()