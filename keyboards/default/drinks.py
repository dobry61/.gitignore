from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

drink_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="cofee"),
            KeyboardButton(text="tea")
        ],
        [
            KeyboardButton(text="cola"),
            KeyboardButton(text="back")
        ]
    ],
    resize_keyboard=True
)