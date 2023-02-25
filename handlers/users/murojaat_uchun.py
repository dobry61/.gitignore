from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default .menu_uchun import tasdiqlash_buttons,menu_button
from loader import dp,bot
from states.holatlar import Forma


# Echo bot
@dp.message_handler(text="Adminga murojaat")
async def bot_echo(message: types.Message):
    await message.answer(text="Ismni kiriting")
    await Forma.ism_qabul_qilish.set()

@dp.message_handler(state=Forma.ism_qabul_qilish,commands='start')
async def bot_echo(message: types.Message,state:FSMContext):
    await message.answer(text="bosh menu ",reply_markup=menu_button)
    await state.finish()

@dp.message_handler(state=Forma.ism_qabul_qilish)
async def bot_echo(message: types.Message,state:FSMContext):
    ism = message.text
    await state.update_data({'name':ism})
    await message.answer(text="Familyani kiriting")
    await Forma.fam_qabul_qilish.set()

@dp.message_handler(state=Forma.fam_qabul_qilish)
async def bot_echo(message: types.Message, state: FSMContext):
    fam = message.text
    await state.update_data({'familya': fam})
    await message.answer(text="telefon raqamni kiriting")
    await Forma.tel_qabul_qilish.set()

@dp.message_handler(state=Forma.tel_qabul_qilish)
async def bot_echo(message: types.Message, state: FSMContext):
    tel = message.text
    await state.update_data({'nomer': tel})
    await message.answer(text="manzilni  kiriting")
    await Forma.manzil_qabul_qilish.set()

@dp.message_handler(state=Forma.manzil_qabul_qilish)
async def bot_echo(message: types.Message, state: FSMContext):
    manzil = message.text
    await state.update_data({'lokatsiya': manzil})
    await message.answer(text="yoshni kiriting")
    await Forma.yosh_qabul_qilish.set()

@dp.message_handler(state=Forma.yosh_qabul_qilish)
async def bot_echo(message: types.Message, state: FSMContext):
    yosh = message.text
    await state.update_data({'age': yosh})
    await message.answer(text="murojaatni kiriting")
    await Forma.murojaat_qabul_qilish.set()

@dp.message_handler(state=Forma.murojaat_qabul_qilish)
async def bot_echo(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({'matn': text})
    malumotlar = await state.get_data()
    user_ismi = malumotlar.get('name')
    user_fami = malumotlar.get('familya')
    user_teli = malumotlar.get('nomer')
    user_manzili = malumotlar.get('lokatsiya')
    user_yoshi = malumotlar.get('ager')
    user_murojaati = malumotlar.get('matn')

    about = f"Ism : {user_ismi}\n" \
            f"Familya : {user_fami}\n" \
            f"Telefon raqam : {user_teli}\n" \
            f"Manzil : {user_manzili}\n" \
            f"Yosh : {user_yoshi}\n" \
            f"Murojaat : {user_murojaati}\n"

    await message.answer(text=about,reply_markup=tasdiqlash_buttons)
    await Forma.tasdiqlash_holat.set()

@dp.message_handler(state=Forma.tasdiqlash_holat,text="tasdiqlash")
async def bot_echo(message: types.Message, state: FSMContext):
    malumotlar = await state.get_data()
    user_ismi = malumotlar.get('name')
    user_fami = malumotlar.get('familya')
    user_teli = malumotlar.get('nomer') 
    user_manzili = malumotlar.get('lokatsiya')
    user_yoshi = malumotlar.get('ager')
    user_murojaati = malumotlar.get('matn')

    about = f"Ushbu {message.from_user.first_name} foydalanuvchi murojaati :\n\n"\
            f"Ism : {user_ismi}\n" \
            f"Familya : {user_fami}\n" \
            f"Telefon raqam : {user_teli}\n" \
            f"Manzil : {user_manzili}\n" \
            f"Yosh : {user_yoshi}\n" \
            f"Murojaat : {user_murojaati}\n"
    await bot.send_message(chat_id='5003220187',text=about)
    await message.answer(text="Adminga yuborildi",reply_markup=menu_button)
    await state.finish()




@dp.message_handler(state=Forma.murojaat_qabul_qilish, text="bekor qilish")
async def bot_echo(message: types.Message, state: FSMContext):

    await message.answer(text="Bekor qilindi",reply_markup=menu_button)
    await state.finish()

