from aiogram import types
from aiogram.types import ContentTypes

from loader import dp
from filters.guruh_uchun import Guruh


# Echo bot
@dp.message_handler(Guruh(),commands="start")
async def bot_echo(message: types.Message):
    await message.answer(text=f" salom {message.from_user.full_name}")

@dp.message_handler(Guruh(),content_types=ContentTypes.NEW_CHAT_MEMBERS )
async def bot_echo(message: types.Message):
    ism = message.new_chat_members[0].full_name
    await message.answer(text=f"Guruhga xush kelibsiz {ism}")

@dp.message_handler(Guruh(),content_types=ContentTypes.LEFT_CHAT_MEMBER )
async def bot_echo(message: types.Message):
    ism = message.left_chat_members[0].full_name
    chat_id = message.migrate_to_chat_id
    await message.answer(text=f" {ism} gurhni tark etdi ")


