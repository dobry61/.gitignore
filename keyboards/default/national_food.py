from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

food_button = ReplyKeyboardMarkup(

keyboard=[
        [
            KeyboardButton(text="Palow"),
            KeyboardButton(text="Soop")
        ],
        [
            KeyboardButton(text="Somsa"),
            KeyboardButton("Mastawa")
        ],
        [
         KeyboardButton(text="back")
        ]
    ],
resize_keyboard=True
)