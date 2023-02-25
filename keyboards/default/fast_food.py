from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

fast_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Hot-Dog"),
            KeyboardButton(text="Gamburger")
        ],
        [
            KeyboardButton(text="pitsa"),
            KeyboardButton("chizburger")
        ],
        [
            KeyboardButton(text="chiqish")
        ]
    ],
    resize_keyboard=True
)