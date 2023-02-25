from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

sweet_button = ReplyKeyboardMarkup(

keyboard=[
        [
            KeyboardButton(text="cake"),
            KeyboardButton(text="pahlawa")
        ],
        [
            KeyboardButton(text="chocolate"),
            KeyboardButton(text="ice cream")
        ],
        [
         KeyboardButton(text="back")
        ]
    ],
resize_keyboard=True
)