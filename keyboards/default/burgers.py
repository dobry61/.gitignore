from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

burger_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Hot Dog"),
            KeyboardButton(text="hamburger")
        ],
        [
            KeyboardButton(text="pizza"),
            KeyboardButton("chizburger")
        ],
        [
            KeyboardButton(text="back")
        ]
    ],
    resize_keyboard=True
)