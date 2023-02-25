from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

taom_button = ReplyKeyboardMarkup(

keyboard=[
        [
            KeyboardButton(text="Osh"),
            KeyboardButton(text="Shorva")
        ],
        [
            KeyboardButton(text="Somsa"),
            KeyboardButton("Mastava")
        ],
        [
         KeyboardButton(text="chiqish")
        ]
    ],
resize_keyboard=True
)
