from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="milliy taomlar"),
            KeyboardButton(text="Ichimliklar")
        ],
        [
            KeyboardButton(text="fast food"),
            KeyboardButton(text="Shirinliklar")
        ],
        [
          KeyboardButton(text="chiqish"),
          KeyboardButton(text="kontakt",request_contact=True)

        ],

        [
          KeyboardButton(text="lokatsiya",request_location=True),
            KeyboardButton(text="ingliz tili")
        ],



    ],
    resize_keyboard=True
)
tasdiqlash_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="tasdiqlash"),
            KeyboardButton(text="bekor qilish"),
        ],




    ],
    resize_keyboard=True
)