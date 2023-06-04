from aiogram import types
from aiogram.types import ContentTypes, InputFile

from loader import dp,bot,base



menular = base.select_all_menu()
@dp.message_handler(text=("Osh"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/16'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="To'y oshi - 18000")






