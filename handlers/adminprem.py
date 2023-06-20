from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import types, Bot, Dispatcher
from adminkb.adminkb import admkb
from imports import ADMIN, TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher()

class UPD(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()
    table_select = State()
   # vru = State()
  #  ven = State()
   # bru = State()
  #  sru = State()
  #  sen = State()
  #  xru = State()
  #  xen = State()



async def op(message: types.Message, bot: Bot):
    if message.from_user.id == ADMIN:
        await message.answer('Добро пожаловать в админ-меню, воспользуйтесь клавиатурой для совершения действий', reply_markup=admkb)
    else:
        await bot.send_message(message.from_user.id, 'Вы не являетесь администратором')

async def add(message: types.Message, state: FSMContext, bot: Bot):
    if message.from_user.id == ADMIN:
        await message.answer('Добавьте картинку, обратите внимание на язык, который вы собираетесь добавить')
        await state.set_state(UPD.photo)
    else:
        await bot.send_message(message.from_user.id, 'Вы не являетесь администратором')

async def cancel(message: types.Message, state: FSMContext, bot: Bot):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer('Изменения отменены')

async def load_photo(message: types.Message, state: FSMContext, bot: Bot):
    await state.update_data(photo=message.photo[-1].file_id)
    await state.set_state(UPD.name)
    await message.answer("Введите название товара")

async def load_name(message: types.Message, state : FSMContext, bot: Bot):
    await state.update_data(name=message.text)
    await state.set_state(UPD.description)
    await message.answer("Введите описание")

async def load_description(message: types.Message, state : FSMContext, bot: Bot):
    await state.update_data(description=message.text)
    await state.set_state(UPD.price)
    await message.answer("Укажите цену в RUB или USD")

async def load_price(message: types.Message, state : FSMContext, bot: Bot):
    await state.update_data(price=float(message.text))
    await state.set_state(UPD.table_select)
    await message.answer('Выберите таблицу для добавление записи: ')

#async def table_select(message: types.Message, state : FSMContext):

#async def vru (message: types.Message, state : FSMContext):
 #   if message.from_user.id == ADMIN:
  #      await state.set_state()
  #  await sqlite_db.sql_add_vbucks(state)
  #  await message.answer('Добавлено в таблицу В-баксы (RUB)')
  #  await state.finish()

# async def ven (message: types.Message, state : FSMContext):
#     if message.from_user.id == ADMIN:
#         await state.set_state()
#     await sqlite_db.sql_add_vbucksen(state)
#     await message.answer('Добавлено в таблицу В-баксы (USD)')
#     await state.finish()
#
# async def bru (message: types.Message, state : FSMContext):
#     if message.from_user.id == ADMIN:
#         await state.set_state()
#     await sqlite_db.sql_add_bundles(state)
#     await message.answer('Добавлено в таблицу Наборы (RUB)')
#     await state.finish()
#
# async def ben (message: types.Message, state : FSMContext):
#     if message.from_user.id == ADMIN:
#         await state.set_state()
#     await sqlite_db.sql_add_bundlesen(state)
#     await message.answer('Добавлено в таблицу Наборы (USD)')
#     await state.finish()
#
# async def sru (message: types.Message, state : FSMContext):
#     if message.from_user.id == ADMIN:
#         await state.set_state()
#     await sqlite_db.sql_add_spot(state)
#     await message.answer('Добавлено в таблицу Spotify (RUB)')
#     await state.finish()
#
# async def sen (message: types.Message, state : FSMContext):
#     if message.from_user.id == ADMIN:
#         await state.set_state()
#     await sqlite_db.sql_add_spoten(state)
#     await message.answer('Добавлено в таблицу Spotify (USD)')
#     await state.finish()
#
# async def xru (message: types.Message, state : FSMContext):
#     if message.from_user.id == ADMIN:
#         await state.set_state()
#     await sqlite_db.sql_add_xbox(state)
#     await message.answer('Добавлено в таблицу Xbox (USD)')
#     await state.finish()
#
# async def xen (message: types.Message, state : FSMContext):
#     if message.from_user.id == ADMIN:
#         await state.set_state()
#     await sqlite_db.sql_add_xboxen(state)
#     await message.answer('Добавлено в таблицу В-баксы (USD)')
#     await state.()
#
