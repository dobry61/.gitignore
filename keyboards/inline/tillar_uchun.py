from aiogram.types import  InlineKeyboardMarkup,InlineKeyboardButton
till_button= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbekcha",callback_data="til1"),
            InlineKeyboardButton(text="English",callback_data="til2")
        ],
        [
            InlineKeyboardButton(text="hamkorlarimiz",url="https://t.me/Rasmlar_moshinalar"),
            InlineKeyboardButton(text="ulashish",switch_inline_query="dobry bot")
        ]

    ]
)