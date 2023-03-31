from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu_uchun import menu_button
from keyboards.default.fast_food import fast_button
from keyboards.default.Ichimliklar import ichimlik_button
from keyboards.default.milliy_taom import taom_button
from keyboards.default.shirinlik_uchun import shirinlik_button
from keyboards.inline.tillar_uchun import till_button
from aiogram.types import  CallbackQuery
from keyboards.default.english_menu import english_menu
from keyboards.default.drinks import drink_button
from keyboards.default.burgers import burger_button
from keyboards.default.national_food import food_button
from keyboards.default.sweets import sweet_button
from filters.shaxsiy_uchun import Shaxsiy




from loader import dp,bot,base


@dp.message_handler(Shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    ism = message.from_user.first_name
    fam = message.from_user.last_name
    user_id = message.from_user.id
    try:
     base.user_qoshish(ism=ism,fam=fam,tg_id=user_id)
    except Exception as xatolik:
        print(xatolik)
    await message.answer(f"salom, {message.from_user.full_name}!",reply_markup=till_button)

@dp.callback_query_handler(text="www")
async def bot_start( xabar : CallbackQuery):
    await xabar.message.answer(f"bot qayta ishga tushdi",reply_markup=till_button)


@dp.callback_query_handler(text="til1")
async def bot_start(xabar : CallbackQuery):
    await xabar.message.answer(f"O'zbek tili tanlandi",reply_markup=menu_button)


@dp.message_handler(text="milliy taomlar")
async def bot_start(message: types.Message):
    await message.answer(f"Taomlarni tanlang, {message.from_user.first_name}!",reply_markup=taom_button)

@dp.message_handler(text="fast food")
async def bot_start(message: types.Message):
    await message.answer(f"fast food tanlang, {message.from_user.full_name}!",reply_markup=fast_button)

@dp.message_handler(text="Ichimliklar")
async def bot_start(message: types.Message):
    await message.answer(f"ichimlik tanlang, {message.from_user.full_name}!", reply_markup=ichimlik_button)

@dp.message_handler(text="Shirinliklar")
async def bot_start(message: types.Message):
    await message.answer(f"shirinlik tanlang, {message.from_user.full_name}!", reply_markup=shirinlik_button)

@dp.message_handler(text="chiqish")
async def bot_start(message: types.Message):
    await message.answer(f"ortga, {message.from_user.full_name}!",reply_markup=menu_button)

@dp.callback_query_handler(text="til2")
async def bot_start(xabar : CallbackQuery):
    await xabar.message.answer(f"ingliz tili tanlandi",reply_markup=english_menu)

@dp.message_handler(text="back")
async def bot_start(message: types.Message):
    await message.answer(f"back, {message.from_user.full_name}!",reply_markup=english_menu)

@dp.message_handler(text="national food")
async def bot_start(message: types.Message):
    await message.answer(f"choose a national dish, {message.from_user.full_name}!",reply_markup=food_button)

@dp.message_handler(text="burgers")
async def bot_start(message: types.Message):
    await message.answer(f"choose a burgers, {message.from_user.full_name}!",reply_markup=burger_button)

@dp.message_handler(text="sweets")
async def bot_start(message: types.Message):
    await message.answer(f"choose a sweets, {message.from_user.full_name}!",reply_markup=sweet_button)

@dp.message_handler(text="drinks")
async def bot_start(message: types.Message):
    await message.answer(f"choose a drinks, {message.from_user.full_name}!",reply_markup=drink_button)

@dp.message_handler(text="ingliz tili")
async def bot_start(message: types.Message):
    await message.answer(f"english menu, {message.from_user.full_name}!",reply_markup=english_menu)

@dp.message_handler(text="Uzbek langulange")
async def bot_start(message: types.Message):
    await message.answer(f"O'zbek tili tanlandi, {message.from_user.full_name}!",reply_markup=menu_button)


@dp.message_handler(commands="reklama",chat_id = '5003220187')
async def bot_start(message: types.Message):
    userlar =  base.select_all_users()
    print(userlar)
    for user in userlar:

        await bot.send_message(chat_id=user[2],text=f" Bizning kanallar : @rasmlar_moshinalar \n @dasturlash_boylab \n @bellingam_saka_mount \n admin: @dobry_team , @dobry_one" )




