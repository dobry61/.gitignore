from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

shirinlik_button = ReplyKeyboardMarkup(

keyboard=[
        [
            KeyboardButton(text="to'rt"),
            KeyboardButton(text="pahlava")
        ],
        [
            KeyboardButton(text="shokolad"),
            KeyboardButton("Muzqaymoq")
        ],
        [
         KeyboardButton(text="chiqish")
        ]
    ],
resize_keyboard=True
)