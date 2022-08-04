from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='10'),
            KeyboardButton(text='11'),
        ],
        [
            KeyboardButton(text='subscribe'),
            KeyboardButton(text='unsubscribe'),
            KeyboardButton(text='inline_menu'),
        ]
    ],
    resize_keyboard=True
)