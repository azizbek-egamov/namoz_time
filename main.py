# START CODING

from functions import *


@dp.message(CommandStart())
async def startbot(message: Message):
    await message.answer(
        text=f"""<b>👋 Salom {message.chat.full_name}.

<i>🤖 Bu bot orqali siz o'zingiz yashab turgan shahar yoki tumanning namoz vaqti va ob-havo ma'lumotlarini bilib borishingiz mumkin.</i></b>""",
        reply_markup=menu,
    )


@dp.callback_query(F.data == "result")
async def res(callback: CallbackQuery):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
        text=f"""<b>👋 Salom {callback.message.chat.full_name}.

<i>🤖 Bu bot orqali siz o'zingiz yashab turgan shahar yoki tumanning namoz vaqti va ob-havo ma'lumotlarini bilib borishingiz mumkin.</i></b>""",
        reply_markup=menu,
    )


@dp.callback_query(F.data == "obhavo")
async def ob(callback: CallbackQuery):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
        text="<b>💥 Marhamat, hududingizni tanlang.</b>", reply_markup=obhavo_key()
    )


@dp.callback_query(F.data.startswith("havoinfo--"))
async def info_(callback: CallbackQuery):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
        text="<b>🪐 Yo'nalishni tanlang.</b>",
        reply_markup=turi(callback.data.split("--")[1]),
    )


@dp.callback_query(F.data.startswith("obinfo-"))
async def info_(callback: CallbackQuery):
    action = callback.data.split("-")
    tur = action[1]
    sh = action[2]
    mes = await callback.message.answer("🙂 1 soniya, ma'lumotlarni yuklayabman.")
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    a = requests.get(f"https://code.visualcoder.ru/ob-havo/index.php?city={sh}").json()
    url = a[0]

    bugun = url["bugun"]
    shahar = bugun["shahar"]
    bugun_sana = bugun["bugun"]
    tavsif = bugun["tavsif"]
    bugun_harorat = bugun["harorat"]
    tong_harorati = bugun["tong"]
    kun_harorati = bugun["kun"]
    oqshom_harorati = bugun["oqshom"]
    namlik = bugun["namlik"]
    shamol = bugun["shamol"]
    bosim = bugun["bosim"]
    oy = bugun["oy"]
    quyosh_chiqishi = bugun["quyosh_chiqishi"]
    quyosh_botishi = bugun["quyosh_botishi"]
    soat = bugun["soat"]
    sana = bugun["sana"]

    haftalik = url["haftalik"]
    ertaga = haftalik["ertaga"]
    ertaga_kun = ertaga["kun"]
    ertaga_sana = ertaga["sana"]
    ertaga_harorat = ertaga["harorat"]
    ertaga_tavsif = ertaga["tavsif"]

    kun2 = haftalik["kun2"]
    kun2_kun = kun2["kun"]
    kun2_sana = kun2["sana"]
    kun2_harorat = kun2["harorat"]
    kun2_tavsif = kun2["tavsif"]

    kun3 = haftalik["kun3"]
    kun3_kun = kun3["kun"]
    kun3_sana = kun3["sana"]
    kun3_harorat = kun3["harorat"]
    kun3_tavsif = kun3["tavsif"]

    kun4 = haftalik["kun4"]
    kun4_kun = kun4["kun"]
    kun4_sana = kun4["sana"]
    kun4_harorat = kun4["harorat"]
    kun4_tavsif = kun4["tavsif"]

    kun5 = haftalik["kun5"]
    kun5_kun = kun5["kun"]
    kun5_sana = kun5["sana"]
    kun5_harorat = kun5["harorat"]
    kun5_tavsif = kun5["tavsif"]

    kun6 = haftalik["kun6"]
    kun6_kun = kun6["kun"]
    kun6_sana = kun6["sana"]
    kun6_harorat = kun6["harorat"]
    kun6_tavsif = kun6["tavsif"]

    kun7 = haftalik["kun7"]
    kun7_kun = kun7["kun"]
    kun7_sana = kun7["sana"]
    kun7_harorat = kun7["harorat"]
    kun7_tavsif = kun7["tavsif"]

    await bot.delete_message(callback.message.chat.id, mes.message_id)

    if str(tur) == "kun":
        await callback.message.answer(
            text=f"""<b>💥 {shahar} uchun bugungi ob-havo ma'lumotlari:</b>
<i>
🗓 {bugun_sana}
🕔 Soat: {soat}
💫 Harorat: {bugun_harorat}
🌔 Tong harorati: {tong_harorati}
🌕 Kun harorati: {kun_harorati}
🌒 Oqshom harorati: {oqshom_harorati}
ℹ️ Tavsif: {tavsif}
💧 {namlik}
💨 {shamol}
🌫 {bosim}
🌙 {oy}

🌔 {quyosh_chiqishi}
🌒 {quyosh_botishi}
</i>""",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="◀️ Orqaga", callback_data=f"havoinfo--{sh}"
                        )
                    ]
                ]
            ),
        )
    elif tur == "hafta":
        await callback.message.answer(
            text=f"""<b>💥 {shahar} uchun haftalik ob-havo ma'lumotlari:</b>
<i>
#bugun
📆 {bugun_sana}
💫 Harorat: {bugun_harorat}
ℹ️ Tavsif: {tavsif}

#{ertaga_kun}
📆 {ertaga_sana}
💫 Harorat: {ertaga_harorat}
ℹ️ Tavsif: {ertaga_tavsif}

#{kun2_kun}
📆 {kun2_sana}
💫 Harorat: {kun2_harorat}
ℹ️ Tavsif: {kun2_tavsif}

#{kun3_kun}
📆 {kun3_sana}
💫 Harorat: {kun3_harorat}
ℹ️ Tavsif: {kun3_tavsif}

#{kun4_kun}
📆 {kun4_sana}
💫 Harorat: {kun4_harorat}
ℹ️ Tavsif: {kun4_tavsif}

#{kun5_kun}
📆 {kun5_sana}
💫 Harorat: {kun5_harorat}
ℹ️ Tavsif: {kun5_tavsif}

#{kun6_kun}
📆 {kun5_sana}
💫 Harorat: {kun6_harorat}
ℹ️ Tavsif: {kun6_tavsif}

#{kun7_kun}
📆 {kun7_sana}
💫 Harorat: {kun7_harorat}
ℹ️ Tavsif: {kun7_tavsif}
</i><b>
🕔 Soat: {soat}
📆 Sana: {sana} 
</b>
""",
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text="◀️ Orqaga", callback_data=f"havoinfo--{sh}"
                        )
                    ]
                ]
            ),
        )


@dp.callback_query(F.data == "hududlar")
async def hududlar(callback: CallbackQuery):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
        text="<b>💥 Marhamat, hududingizni tanlang.</b>", reply_markup=viloyat
    )


@dp.callback_query(F.data.startswith("namoz_viloyat-"))
async def hududlar(callback: CallbackQuery):
    data = callback.data.split("-")[1]
    btn = tumanlar(str(data))
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
        text="<b>💥 Marhamat, shahar yoki tumaningizni tanlang.</b>", reply_markup=btn
    )


@dp.callback_query(F.data.startswith("namoz_time-"))
async def hududlar(callback: CallbackQuery):
    data = callback.data.split("-")[1]
    mes = await callback.message.answer("🙂 1 soniya, ma'lumotlarni yuklayabman.")
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)

    url = requests.get(
        f"https://code.visualcoder.ru/namoz/index.php?city={str(data)}"
    ).json()
    res = url[0]["result"]
    time = res["current_time"]
    city = res["city"]
    bomdod = res["bomdod"]
    quyosh = res["quyosh"]
    peshin = res["peshin"]
    asr = res["asr"]
    shom = res["shom"]
    xufton = res["xufton"]
    await bot.delete_message(callback.message.chat.id, mes.message_id)
    await callback.message.answer(
        text=f"""<b>🌙 {city} uchun namoz vaqtlari:
        
🕰 Bomdod   -  {bomdod}
🕰 Quyosh   -  {quyosh}
🕰 Peshin   -  {peshin}
🕰 Asr      -  {asr}
🕰 Shom     -  {shom}
🕰 Xufton   -  {xufton}

🕐 Soat: {time}</b>""",
        reply_markup=home,
    )


# ADMIN PANEL


@dp.message(Command("panel"))
async def apanel(message: Message, state: FSMContext):
    if str(message.from_user.id) == admin:
        await message.answer(text="<b>Admin paneldasiz.</b>", reply_markup=panel)
        await state.clear(None)


@dp.callback_query(F.data == "phome")
async def wpanel(callback: CallbackQuery, state: FSMContext):
    if str(callback.message.chat.id) == admin:
        await callback.message.answer(
            text="<b>Admin paneldasiz.</b>", reply_markup=panel
        )
        await state.set_state(None)



@dp.callback_query(F.data == "xabar")
async def xabar(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="Foydalanuvchilarga yuboriladigan xabar matnini kiritng:",
        reply_markup=bhome,
    )
    await state.set_state(xabars.text)


@dp.message(xabars.text)
async def yuborish(message: Message, state: FSMContext):
    r = select_info("users")
    for i in r:
        try:
            await bot.send_message(chat_id=f"{i[1]}", text=f"{message.text}")
        except:
            continue
    await message.answer(
        text="<b>Xabar barcha foydalanuvchilarga muvaffaqiyatli yuborildi.</b>",
        reply_markup=panel,
    )
    await state.clear()


async def main() -> None:
    dp.message.middleware.register(ThrottlingMiddleware())
    # dp.update.middleware.register(joinchat())
    dp.update.middleware.register(check())
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except:
        print("Jarayon yakunlandi")
