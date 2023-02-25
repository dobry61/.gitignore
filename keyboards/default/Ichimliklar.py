from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

ichimlik_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="cofe"),
            KeyboardButton(text="Choy")
        ],
        [
            KeyboardButton(text="Cola"),
            KeyboardButton("chiqish")
        ]
    ],
    resize_keyboard=True
)