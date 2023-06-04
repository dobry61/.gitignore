import datetime

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, KeyboardButton, ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup

from keyboards.default.menu_uchun import menu_button
# from keyboards.default.taomlar_uchun import taomlar_buttun
# from keyboards.default.ichimliklar_uchun import ichimliklar_buttun
# from keyboards.default.alkagollar_uchun import alkagollar_buttun
# from keyboards.default.salqin_ichimliklar_uchun import salqin_ichimliklar_buttun
# from keyboards.default.taomlar2_uchun import taomlar2_buttun
# from keyboards.default.taomlar1_uchun import taomlar1_buttun

from keyboards.inline.tillar_uchun import till_button

# #english
# from keyboards.default.menu_en import menu_buttun_en
# from keyboards.default.foods import foods_uchun
# from keyboards.default.foods1 import foods1_buttun
# from keyboards.default.foods2 import foods2_buttun
# from keyboards.default.drinks import drinkss_buttun
# from keyboards.default.cool_ichimliklar import sovuq_ichimliklar_buttun
# from keyboards.default.alcahol import alcahols_buttun

from loader import dp, base, bot


#Menu
# azolarni qabul qilish
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    ism = message.from_user.first_name
    fam = message.from_user.last_name
    user_id = message.from_user.id
    try:
        base.user_qoshish(ism=ism,fam=fam,username=message.from_user.username,tg_id=user_id)
    except Exception:
        pass
    await message.answer(f"Salom, Tillarni tanlang  {message.from_user.full_name}!",reply_markup=till_button)

# tillar uchun
@dp.callback_query_handler(text="til1")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Taomlarni tanlang ",reply_markup=menu_button)




#Taomlar bo'limi buttonlar
menular = base.select_all_menu()
@dp.message_handler(text=[menu[1] for menu in menular])
async def bot_start(message: types.Message):
    typee =message.text
    maxsulotlar = base.select_maxsulotlar(turi=typee)

    index = 0
    i = 0
    royxat = []
    for menu in maxsulotlar:
        if i % 2 == 0 and i != 0:
            index += 1
        if i % 2 == 0:
            royxat.append([KeyboardButton(text=menu[1])])
        else:
            royxat[index].append(KeyboardButton(text=menu[1]))
        i += 1

    royxat.append([KeyboardButton(text="Orqaga")])
    maxsulotlar_buttun = ReplyKeyboardMarkup(keyboard=royxat, resize_keyboard=True)

    await message.answer(f"Maxsulotlarni tanlang, {message.from_user.full_name}!",reply_markup=maxsulotlar_buttun)

#maxsulotlar
menular = base.select_all_maxsulotlar()
@dp.message_handler(text=[menu[1] for menu in menular])
async def bot_start(message: types.Message):
    typee = message.text
    maxsulot = base.select_maxsulotlar(nomi=typee)[0]
    print(maxsulot,'++++++++++++++++++++++')
    #print(maxsulot)
    #(1, 'Osh', 20000, 'https://t.me/meningkanalim1898/2', None, 'Taomlar')
    max_id = maxsulot[0]
    max_nomi = maxsulot[1]
    max_narxi = maxsulot[5]
    max_rasmi = maxsulot[2]
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=max_rasmi,caption=f"Nomi :{max_nomi}\n"
                                                                 f"Narxi : {max_narxi}",
                         reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                             [
                             InlineKeyboardButton(text="Sotib olish",callback_data=f"buy {max_id}")
                             ]
                         ]
                         )

                         )

#orqaga
@dp.message_handler(text="Orqaga")
async def bot_start(message: types.Message):
    await message.answer(f"Taomlarni  tanlang, {message.from_user.full_name}!", reply_markup=menu_button)


@dp.callback_query_handler()
async def bot_start(xabar: CallbackQuery):
    data = xabar.data.split()
    if data[0] == 'buy':
        maxsulot_id = data[1]
        maxsulot=base.select_maxsulot(id=maxsulot_id)

        max_nomi = maxsulot[1]
        max_narxi = maxsulot[5]
        max_rasmi = maxsulot[2]
        max_malumot = maxsulot[3]
        max_turi = maxsulot[4]
        max_soni = 1
        user_id = xabar.from_user.id
        user_name=xabar.from_user.username
        date = datetime.datetime.now()
        base.maxsulot_qoshish_to_korzinka(nomi=max_nomi,tg_id=user_id,narxi=max_narxi,rasm=max_rasmi,turi=max_turi,soni=max_soni,malumot=max_malumot,username=user_name,date=date,status=True)


        await xabar.message.answer(f"Maxsulot Korzinkaga joylandi ! ")


# @dp.message_handler(text="1 - Taomlar")
# async def bot_start(message: types.Message):
#     await message.answer(f"Birinchi taomni tanlang, {message.from_user.full_name}!", reply_markup=taomlar1_buttun)
#
# @dp.message_handler(text="2 - Taomlar")
# async def bot_start(message: types.Message):
#     await message.answer(f"Ikkinchi taomni tanlang, {message.from_user.full_name}!", reply_markup=taomlar2_buttun)
#
#
#
#
# #Ichimliklar bo'limi
# @dp.message_handler(text="Ichimliklar")
# async def bot_start(message: types.Message):
#     await message.answer(f"Ichimliklarni tanlang, {message.from_user.full_name}!", reply_markup=ichimliklar_buttun)
#
#
#
# @dp.message_handler(text="Salqin ichimliklar")
# async def bot_start(message: types.Message):
#     await message.answer(f"Salqin ichimliklarni tanlang, {message.from_user.full_name}!", reply_markup=salqin_ichimliklar_buttun)
#
# @dp.message_handler(text="Alkagollar")
# async def bot_start(message: types.Message):
#     await message.answer(f"Alkagollarni tanlang, {message.from_user.full_name}!", reply_markup=tillar_buttun)
#
#
# @dp.message_handler(text="Orqaga")
# async def bot_start(message: types.Message):
#     await message.answer(f"Taomlarni  tanlang, {message.from_user.full_name}!", reply_markup=menu_buttun)
#
# # English
#
# @dp.callback_query_handler(text="til2")
# async def bot_start(xabar: CallbackQuery):
#     await xabar.message.answer(f" Choose foods ",reply_markup=menu_buttun_en)
#
# @dp.message_handler(text="Foods")
# async def bot_start(message: types.Message):
#     await message.answer(f"Choose foods, {message.from_user.full_name}!",reply_markup=foods_uchun)
#
# @dp.message_handler(text="1 - Food")
# async def bot_start(message: types.Message):
#     await message.answer(f"Choose the first dish, {message.from_user.full_name}!", reply_markup=foods1_buttun)
#
# @dp.message_handler(text="2 - Food")
# async def bot_start(message: types.Message):
#     await message.answer(f"Choose the first dish, {message.from_user.full_name}!", reply_markup=foods2_buttun)
#
#
# # Drinks
#
# @dp.message_handler(text="Drinks")
# async def bot_start(message: types.Message):
#     await message.answer(f"Choose drinks , {message.from_user.full_name}!", reply_markup=drinkss_buttun)
#
# @dp.message_handler(text="Cool drinks")
# async def bot_start(message: types.Message):
#     await message.answer(f"Cool drinks choose , {message.from_user.full_name}!", reply_markup=sovuq_ichimliklar_buttun)
#
#
# @dp.message_handler(text="Alcohols")
# async def bot_start(message: types.Message):
#     await message.answer(f"Alcohols choose, {message.from_user.full_name}!", reply_markup=tillar_buttun)
#
#
# @dp.message_handler(text="Back")
# async def bot_start(message: types.Message):
#     await message.answer(f"Choose foods, {message.from_user.full_name}!", reply_markup=menu_buttun_en)
#
#
# @dp.callback_query_handler(text="www")
# async def bot_start(xabar:CallbackQuery):
#     await xabar.message.answer(f"Qayta ishga tushirish",reply_markup=menu_buttun)
#
# #reklama jo'natish
# @dp.message_handler(commands="reklama",chat_id= '1961871634')
# async def bot_start(message: types.Message):
#     userlar= base.select_all_users()
#     for user in userlar:
#          await bot.send_message(chat_id=user[4],text=f"Assalomu alaykum bu reklama, {message.from_user.full_name}!")
