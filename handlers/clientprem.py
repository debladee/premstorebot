from aiogram import types, Bot, Dispatcher
from inline import inline
import imports
from db.sqlite_db import read_vbucks
bot = Bot(token=imports.TOKEN)
dp = Dispatcher()

    # Функция старта, потом идут соответсвующие функции получаемые после выбора из первой

async def startup(message: types.Message, bot: Bot):
    await message.answer('Добрый день, пожалуйста выберите предпочитаемый язык, заметье от языка зависит валюта и доступные методы оплаты. Welcome, please select preffered language take a notice that this will change available payment options and currency.', reply_markup=inline.inkb())

async def russian(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'RUS':
        new_message = await callback.message.answer('Вы выбрали русский язык', reply_markup=inline.mainru())
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

async def english(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'ENG':
        new_message = await callback.message.answer("You've selected English language", reply_markup=inline.mainen())
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

async def store(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'Магазин':
        new_message = await callback.message.answer('Выберите категорию товаров', reply_markup=inline.store_ru())
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

async def faq(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'ЧаВо':
        new_message = await callback.message.answer('Вот небольшая инструкция что вы хотели бы сделать перед заказом: вставить ссылку')
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

async def reviews(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'Отзывы':
        new_message = await callback.message.answer('Ознакомиться с отзывами вы можете в нашем телеграм канале с отзывами: вставить ссылку')
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

async def support(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'Помощь':
        new_message = await callback.message.answer('Напишите о вашей проблеме или вопросе нам: @')
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

async def store_en(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'Store':
        new_message = await callback.message.answer('Select category', reply_markup=inline.store_en())
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

async def faq_en(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'FAQ':
        new_message = await callback.message.answer("Here's a quick guide on what you want to do before you order: ")
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

async def reviews_en(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'Reviews':
        new_message = await callback.message.answer('You can read all the reviews here: ')
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

async def support_en(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'Support':
        new_message = await callback.message.answer('Message us here @')
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

async def fortnite(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'Фортнайт':
        new_message = await callback.message.answer('Выберите категорию', reply_markup=inline.fortnite_ru())
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

async def fortnite_en(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'Fortnite':
        new_message = await callback.message.answer('Select category', reply_markup=inline.fortnite_en())
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

async def vbucks(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'Вбаксы':
        new_message = await callback.message.answer('В-Баксы на ваш аккаунт Epic Games, Xbox или Playstation. Внимание! В-баксы не доступны на Nintendo')
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await sqlite
        await callback.answer()
        return

async def vbucks_en(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'Vbucks':
        new_message = await callback.message.answer('V-Bucks for your Epic Games, Xbox or Playstation account. Warning! V-Bucks are not available on Nintendo')
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

async def bunldes(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'Наборы':
        new_message = await callback.message.answer('Наборы на ваш аккаунт Epic Games, Xbox или Playstation. Внимание! В-баксы не доступны на Nintendo')
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

async def bunldes_en(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'Bundles':
        new_message = await callback.message.answer('Bundles for your Epic Games, Xbox or Playstation account. Warning! V-Bucks are not available on Nintendo')
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

async def subs(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'Подписки':
        new_message = await callback.message.answer('Премиальные подписки на онлайн-сервисы', reply_markup=inline.subscriptions_ru())
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

async def subs_en(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'Subs':
        new_message = await callback.message.answer('Premium subscriptions on online services', reply_markup=inline.subscriptions_en())
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

async def spotify(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'Спотифай':
        new_message = await callback.message.answer('Подписка на Spotify Премиум по выгодной цене. Выберите тип подписки', reply_markup=inline.spotify_ru())
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

async def spotify_en(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'Spotify':
        new_message = await callback.message.answer('Spotify Premium subscription. Please select subscription type', reply_markup=inline.spotify_en())
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

async def xbox(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'бокс':
        new_message = await callback.message.answer('Подписка на Xbox Game Pass на твой ПК, консоль или то и другое вместе', reply_markup=inline.xboxru())
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

async def xbox_en(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'xbox':
        new_message = await callback.message.answer('Xbox Game Pass subscription for your PC, console or both at once', reply_markup=inline.xboxen())
        await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
        await callback.answer()
        return

