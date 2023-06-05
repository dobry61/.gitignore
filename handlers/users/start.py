import datetime

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, KeyboardButton, ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup

from keyboards.default.menu_uchun import menu_button
from keyboards.default.milliy_taom import taom_button

from keyboards.inline.tillar_uchun import till_button


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
        korzinka = base.select_maxsulot_from_korzinka(nomi=max_nomi,tg_id=user_id)
        print(korzinka)
        if korzinka:
            max_soni = korzinka.soni+1
        base.maxsulot_qoshish_to_korzinka(nomi=max_nomi,tg_id=user_id,narxi=max_narxi,rasm=max_rasmi,turi=max_turi,soni=max_soni,malumot=max_malumot,username=user_name,date=date,status=True)

        await xabar.message.answer(f"Maxsulot Korzinkaga joylandi ! ")

@dp.message_handler(text="Korzinka")
async def bot_start (message: types.Message):
    user_id = message.from_user.id
    user_maxsulotlar = base.select_maxsulotlar_from_korzinka(tg_id=user_id)

    for maxsulot in user_maxsulotlar:
        # 1, 'Osh', 20000, 'https://t.me/media_uchun596/16', 'Toshkent Oshi', 'Milliy taomlar', 1, 6206058862, '2023-06-05 13:51:23.593051', 1, 'Dobry_one'
        max_id = maxsulot[0]
        max_nomi = maxsulot[1]
        max_narxi = maxsulot[2]
        max_rasmi = maxsulot[3]
        max_soni = maxsulot[6]
        user_id = message.from_user.id
        await bot.send_photo(chat_id=user_id, photo=max_rasmi, caption=f"Nomi :{max_nomi}\n"
                                                                       f"Narxi : {max_narxi}",
                             reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text="-", callback_data=f"min {max_id}"),
                                     InlineKeyboardButton(text=f"{max_soni}", callback_data=f"number {max_id}"),
                                     InlineKeyboardButton(text="+", callback_data=f"plus {max_id}"),


                                 ]
                             ]
                             )

                             )

    await message.answer(f"Birinchi taomni tanlang, {message.from_user.full_name}!", reply_markup=taom_button)
