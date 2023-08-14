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

selector = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='/Вбаксы'
        ),
        KeyboardButton(
            text='/vbucks'
        )
    ]
])
