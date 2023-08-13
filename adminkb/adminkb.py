from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admkb = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Добавить'
        ),
        KeyboardButton(
            text='Изменить'
        ),
        KeyboardButton(
            text='Показать таблицы'
        )
    ],
    [
        KeyboardButton(
                text='Удалить'
            ),
            KeyboardButton(
                text='Отмена'
            )
    ]
], resize_keyboard=True)


