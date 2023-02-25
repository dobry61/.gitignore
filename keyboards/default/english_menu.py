from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

english_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="national food"),
            KeyboardButton(text="drinks")
        ],
        [
            KeyboardButton(text="burgers"),
            KeyboardButton("sweets")
        ],
        [
          KeyboardButton("back"),
          KeyboardButton("contact",request_contact=True)

        ],
        [
          KeyboardButton("location",request_location=True)
        ]
    ],
    resize_keyboard=True
)