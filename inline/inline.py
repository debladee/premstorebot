from aiogram.utils.keyboard import InlineKeyboardBuilder
from db.sqlite_db import read_data

def inkb():
    inkb = InlineKeyboardBuilder()
    inkb.button(text='Русский', callback_data='RUS')
    inkb.button(text='English', callback_data='ENG')

    inkb.adjust(2)
    return inkb.as_markup()

def mainru():
    mainru = InlineKeyboardBuilder()
    mainru.button(text='Магазин🎮', callback_data='Магазин')
    mainru.button(text='Инструкция📝', callback_data='ЧаВо')
    mainru.button(text='Отзывы🧾', callback_data='Отзывы')
    mainru.button(text='Помощь👨‍🔧', callback_data='Помощь')
    mainru.button(text='English', callback_data='ENG')

    mainru.adjust(2, 2, 1)
    return mainru.as_markup()

def mainen():
    mainen = InlineKeyboardBuilder()
    mainen.button(text='Store🎮', callback_data='Store')
    mainen.button(text='Instruction📝', callback_data='FAQ')
    mainen.button(text='Reviews🧾', callback_data='Reviews')
    mainen.button(text='Support👨‍🔧', callback_data='Support')
    mainen.button(text='Русский', callback_data='RUS')

    mainen.adjust(2, 2, 1)
    return mainen.as_markup()

def store_ru():
    store_ru = InlineKeyboardBuilder()
    store_ru.button(text='Fortnite💻🎮', callback_data='Фортнайт')
    store_ru.button(text='Подписки💳', callback_data='Подписки')
    store_ru.button(text='Назад', callback_data='RUS')

    store_ru.adjust(2, 1)
    return store_ru.as_markup()

def store_en():
    store_en = InlineKeyboardBuilder()
    store_en.button(text='Fortnite💻🎮', callback_data='Fortnite')
    store_en.button(text='Subscriptions💳', callback_data='Subs')
    store_en.button(text='Back', callback_data='ENG')

    store_en.adjust(2, 1)
    return store_en.as_markup()

def fortnite_ru():
    fortnite_ru = InlineKeyboardBuilder()
    fortnite_ru.button(text='В-Баксы💲', callback_data='Вбаксы')
    fortnite_ru.button(text='Наборы💲🕺', callback_data='Наборы')
    fortnite_ru.button(text='Назад', callback_data='Магазин')

    fortnite_ru.adjust(2, 1)
    return fortnite_ru.as_markup()

def fortnite_en():
    fortnite_en = InlineKeyboardBuilder()
    fortnite_en.button(text='V-Bucks💲', callback_data='Vbucks')
    fortnite_en.button(text='Bundles💲🕺', callback_data='Bundles')
    fortnite_en.button(text='Back', callback_data='Store')

    fortnite_en.adjust(2, 1)
    return fortnite_en.as_markup()

def subscriptions_ru():
    subscriptions_ru = InlineKeyboardBuilder()
    subscriptions_ru.button(text='Spotify🟢', callback_data='Спотифай')
    subscriptions_ru.button(text='Xbox', callback_data='бокс')
    subscriptions_ru.button(text='Playstation', callback_data='пс')
    subscriptions_ru.button(text='Назад', callback_data='Магазин')

    subscriptions_ru.adjust(1, 2)
    return subscriptions_ru.as_markup() 

def subscriptions_en():
    subscriptions_en = InlineKeyboardBuilder()
    subscriptions_en.button(text='Spotify🟢', callback_data='Spotify')
    subscriptions_en.button(text='Xbox', callback_data='xbox')
    subscriptions_en.button(text='Playstation', callback_data='ps')
    subscriptions_en.button(text='Back', callback_data='Store')

    subscriptions_en.adjust(1, 2)
    return subscriptions_en.as_markup()

def spotify_ru():
    spotify_ru = InlineKeyboardBuilder()
    spotify_ru.button(text='Spotify Premium 1 месяц🟢', callback_data='Спотифай1')
    spotify_ru.button(text='Spotify Premium 3 месяца🟢', callback_data='Спотифай3')
    spotify_ru.button(text='Spotify Premium 6 месяцев🟢', callback_data='Спотифай6')
    spotify_ru.button(text='Spotify Premium 12 месяцев🟢', callback_data='Спотифай12')
    spotify_ru.button(text='Назад', callback_data='Подписки')

    spotify_ru.adjust(2, 2)
    return spotify_ru.as_markup()

def spotify_en():
    spotify_en = InlineKeyboardBuilder()
    spotify_en.button(text='Spotify Premium 1 month🟢', callback_data='Spotify1')
    spotify_en.button(text='Spotify Premium 3 months🟢', callback_data='Spotify3')
    spotify_en.button(text='Spotify Premium 6 months🟢', callback_data='Spotify6')
    spotify_en.button(text='Spotify Premium 12 months🟢', callback_data='Spotify12')
    spotify_en.button(text='Back', callback_data='Subs')

    spotify_en.adjust(2, 2, 1)
    return spotify_en.as_markup()

def xboxru():
    xboxru = InlineKeyboardBuilder()
    xboxru.button(text='ПК Game Pass', callback_data='пкгп')
    xboxru.button(text='Консольный Game Pass', callback_data='кгп')
    xboxru.button(text='Ultimate Game Pass', callback_data='угп')
    xboxru.button(text='Назад', callback_data='Подписки')

    xboxru.adjust(2, 1, 1)
    return xboxru.as_markup()

def xboxen():
    xboxen = InlineKeyboardBuilder()
    xboxen.button(text='PC Game Pass', callback_data='pcgp')
    xboxen.button(text='Console Game Pass', callback_data='cgp')
    xboxen.button(text='Ultimate Game Pass', callback_data='ugp')
    xboxen.button(text='Back', callback_data='Subs')

    xboxen.adjust(2, 1, 1)
    return xboxen.as_markup()

def table_selector(available_tables):
    table_selector = InlineKeyboardBuilder()

    for table_name in available_tables:
        table_selector.button(text=table_name, callback_data=f"select_table:{table_name}")

    table_selector.adjust(4, 4, 4)
    return table_selector.as_markup()

def gen_selection(table_name):
    gen_selection = InlineKeyboardBuilder()
    
    results = read_data(table_name)
    for product_name in results:
        product_name = product_name[0]
        gen_selection.button(text=product_name, callback_data=f"product:{product_name}")
    gen_selection.button(text='Назад', callback_data='Назад')

    gen_selection.adjust(4, 4, 4)
    return gen_selection.as_markup()

def yes_no():
    yes_no = InlineKeyboardBuilder()
    yes_no.button(text='Да', callback_data='Yes')
    yes_no.button(text='Нет', callback_data='No')

    yes_no.adjust(2)
    return yes_no.as_markup()