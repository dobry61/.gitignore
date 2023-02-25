from aiogram import types
from aiogram.types import ContentTypes, InputFile

from loader import dp,bot


# Echo bot
@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await message.photo[-1].download()
    await message.answer(text="Rasm qabul qilindi")


@dp.message_handler(text=("Osh"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/16'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("Shorva"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/13'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("Somsa"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/14'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("Mastava"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/9'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("cofe"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/2'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("Choy"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/5'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("Cola"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/8'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("Hot-Dog"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/3'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("Gamburger"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/4'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("chizburger"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/6'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("pitsa"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/10'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("to'rt"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/15'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("pahlava"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/11'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("shokolad"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/12'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)


@dp.message_handler(text=("Muzqaymoq"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/7'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("Palow"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/16'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("Soop"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/13'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("Mastawa"))
async def bot_echo(message: types.Message):
    rasm_manzili ='Mastava'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("cofee"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/2'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("tea"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/5'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("cola"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/8'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("Hot Dog"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/3'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("hamburger"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/4'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)

@dp.message_handler(text=("pizza"))
async def bot_echo(message: types.Message):
    rasm_manzili = 'https://t.me/media_uchun596/10'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id, photo=rasm_manzili)

@dp.message_handler(text=("cake"))
async def bot_echo(message: types.Message):
    rasm_manzili ='https://t.me/media_uchun596/15'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili)


@dp.message_handler(text=("ice cream"))
async def bot_echo(message: types.Message):
    rasm_manzili = 'https://t.me/media_uchun596/7'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id, photo=rasm_manzili)


@dp.message_handler(text=("pahlawa"))
async def bot_echo(message: types.Message):
    rasm_manzili = 'https://t.me/media_uchun596/11'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id, photo=rasm_manzili,)


@dp.message_handler(text=("chocolate"))
async def bot_echo(message: types.Message):
    rasm_manzili = 'https://t.me/media_uchun596/12'
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id, photo=rasm_manzili)




