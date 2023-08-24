from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admkb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='/Добавить'
        ),
        KeyboardButton(
            text='/Изменить'
        ),
        KeyboardButton(
            text='/Таблицы'
        )
    ],
    [
        KeyboardButton(
                text='/Удалить'
            ),
            KeyboardButton(
                text='/Отмена'
            )
    ]
], resize_keyboard=True)

admtbl = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='/Новая'
        ),
        KeyboardButton(
            text='/Стереть'
        ),
        KeyboardButton(
            text='/Назад'
        )
    ]    
], resize_keyboard=True)
