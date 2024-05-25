from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
import requests

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="💥 Hududlar ro'yxati", callback_data="hududlar")],
        [InlineKeyboardButton(text="☀️ Ob-havo ma'lumotlari", callback_data="obhavo")],
    ]
)

home = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🏘 Asosiy menyu", callback_data="result")]
    ]
)

panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📨 Xabar yuborish", callback_data="xabar"),
            InlineKeyboardButton(text="🏘 Asosiy menyu", callback_data="result"),
        ]
    ]
)

bhome = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🏘 Asosiy panel", callback_data="phome")]
    ]
)


viloyat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🌙 Toshkent viloyati", callback_data="namoz_viloyat-toshkent"
            ),
            InlineKeyboardButton(
                text="🌙 Buxoro viloyati", callback_data="namoz_viloyat-buxoro"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌙 Farg'ona viloyati", callback_data="namoz_viloyat-fargona"
            ),
            InlineKeyboardButton(
                text="🌙 Jizzax viloyati", callback_data="namoz_viloyat-jizzax"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌙 Navoiy viloyati", callback_data="namoz_viloyat-navoiy"
            ),
            InlineKeyboardButton(
                text="🌙 Namangan viloyati", callback_data="namoz_viloyat-namangan"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌙 Sirdaryo viloyati", callback_data="namoz_viloyat-sirdaryo"
            ),
            InlineKeyboardButton(
                text="🌙 Samarqand viloyati", callback_data="namoz_viloyat-samarqand"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌙 Surxondaryo viloyati",
                callback_data="namoz_viloyat-surxondaryo",
            ),
            InlineKeyboardButton(
                text="🌙 Qashqadaryo viloyati",
                callback_data="namoz_viloyat-qashqadaryo",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌙 Andijon viloyati", callback_data="namoz_viloyat-andijon"
            ),
            InlineKeyboardButton(
                text="🌙 Xorazm viloyati", callback_data="namoz_viloyat-xorazm"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌙 Qoraqolpog'iston respublikasi",
                callback_data="namoz_viloyat-qoraqolpogiston",
            )
        ],
        [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="result")],
    ]
)

toshkent = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🌙 Toshkent", callback_data="namoz_time-toshkent"
            ),
            InlineKeyboardButton(text="🌙 Angren", callback_data="namoz_time-angren"),
        ],
        [
            InlineKeyboardButton(text="🌙 Piskent", callback_data="namoz_time-piskent"),
            InlineKeyboardButton(text="🌙 Bekobod", callback_data="namoz_time-bekobod"),
        ],
        [
            InlineKeyboardButton(text="🌙 Parkent", callback_data="namoz_time-parkent"),
            InlineKeyboardButton(
                text="🌙 G'azalkent", callback_data="namoz_time-gazalkent"
            ),
        ],
        [
            InlineKeyboardButton(text="🌙 Olmaliq", callback_data="namoz_time-olmaliq"),
            InlineKeyboardButton(text="🌙 Bo'ka", callback_data="namoz_time-boka"),
        ],
        [
            InlineKeyboardButton(
                text="🌙 Yangiyo'l", callback_data="namoz_time-yangiyol"
            ),
            InlineKeyboardButton(
                text="🌙 Nurafshon", callback_data="namoz_time-nurafshon"
            ),
        ],
        [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="hududlar")],
    ]
)

buxoro = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌙 Buxoro", callback_data="namoz_time-buxoro"),
            InlineKeyboardButton(text="🌙 Gazli", callback_data="namoz_time-gazli"),
        ],
        [
            InlineKeyboardButton(
                text="🌙 G'ijduvon", callback_data="namoz_time-gijduvon"
            ),
            InlineKeyboardButton(
                text="🌙 Qorako'l", callback_data="namoz_time-qorakol"
            ),
        ],
        [
            InlineKeyboardButton(text="🌙 Jondor", callback_data="namoz_time-jondor"),
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="hududlar"),
        ],
    ]
)

fargona = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🌙 Farg'ona", callback_data="namoz_time-fargona"
            ),
            InlineKeyboardButton(
                text="🌙 Marg'ilon", callback_data="namoz_time-margilon"
            ),
        ],
        [
            InlineKeyboardButton(text="🌙 Qo'qon", callback_data="namoz_time-qoqon"),
            InlineKeyboardButton(text="🌙 Quva", callback_data="namoz_time-quva"),
        ],
        [
            InlineKeyboardButton(text="🌙 Rishton", callback_data="namoz_time-rishton"),
            InlineKeyboardButton(text="🌙 Bog'dod", callback_data="namoz_time-bogdod"),
        ],
        [
            InlineKeyboardButton(
                text="🌙 Oltiariq", callback_data="namoz_time-oltiariq"
            ),
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="hududlar"),
        ],
    ]
)

sirdaryo = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🌙 Guliston", callback_data="namoz_time-guliston"
            ),
            InlineKeyboardButton(text="🌙 Sardoba", callback_data="namoz_time-sardoba"),
        ],
        [
            InlineKeyboardButton(
                text="🌙 Sirdaryo", callback_data="namoz_time-sirdaryo"
            ),
            InlineKeyboardButton(text="🌙 Boyovut", callback_data="namoz_time-boyovut"),
        ],
        [
            InlineKeyboardButton(
                text="🌙 Paxtaobod", callback_data="namoz_time-paxtaobod"
            ),
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="hududlar"),
        ],
    ]
)

jizzax = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌙 Jizzax", callback_data="namoz_time-jizzax"),
            InlineKeyboardButton(text="🌙 Zomin", callback_data="namoz_time-zomin"),
        ],
        [
            InlineKeyboardButton(text="🌙 Forish", callback_data="namoz_time-forish"),
            InlineKeyboardButton(
                text="🌙 G'allaorol", callback_data="namoz_time-gallaorol"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌙 Do'stlik", callback_data="namoz_time-dostlik"
            ),
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="hududlar"),
        ],
    ]
)

navoiy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌙 Navoiy", callback_data="namoz_time-navoiy"),
            InlineKeyboardButton(
                text="🌙 Zarafshon", callback_data="namoz_time-zarafshon"
            ),
        ],
        [
            InlineKeyboardButton(text="🌙 Konimex", callback_data="namoz_time-konimex"),
            InlineKeyboardButton(text="🌙 Nurota", callback_data="namoz_time-nurota"),
        ],
        [
            InlineKeyboardButton(
                text="🌙 Uchquduq", callback_data="namoz_time-uchquduq"
            ),
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="hududlar"),
        ],
    ]
)

namangan = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🌙 Namangan", callback_data="namoz_time-namangan"
            ),
            InlineKeyboardButton(text="🌙 Chortoq", callback_data="namoz_time-Chortoq"),
        ],
        [
            InlineKeyboardButton(text="🌙 Chust", callback_data="namoz_time-chust"),
            InlineKeyboardButton(text="🌙 Pop", callback_data="namoz_time-pop1"),
        ],
        [
            InlineKeyboardButton(
                text="🌙 Uchqo'rg'on", callback_data="namoz_time-uchqorgon"
            ),
            InlineKeyboardButton(
                text="🌙 Mingbuloq", callback_data="namoz_time-mingbuloq"
            ),
        ],
        [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="hududlar")],
    ]
)

samarqand = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🌙 Samarqand", callback_data="namoz_time-samarqand"
            ),
            InlineKeyboardButton(
                text="🌙 Ishtixon", callback_data="namoz_time-ishtixon"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌙 Mirbozor", callback_data="namoz_time-mirbozor"
            ),
            InlineKeyboardButton(
                text="🌙 Kattaqo'rg'on", callback_data="namoz_time-kattaqorgon"
            ),
        ],
        [
            InlineKeyboardButton(text="🌙 Urgut", callback_data="namoz_time-urgut"),
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="hududlar"),
        ],
    ]
)

surxondaryo = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌙 Termiz", callback_data="namoz_time-termiz"),
            InlineKeyboardButton(text="🌙 Boysun", callback_data="namoz_time-boysun"),
        ],
        [
            InlineKeyboardButton(text="🌙 Denov", callback_data="namoz_time-denov"),
            InlineKeyboardButton(
                text="🌙 Sherobod", callback_data="namoz_time-sherobod"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌙 Sho'rchi", callback_data="namoz_time-shorchi"
            ),
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="hududlar"),
        ],
    ]
)

qashqadaryo = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌙 Qarshi", callback_data="namoz_time-qarshi"),
            InlineKeyboardButton(
                text="🌙 Dehqonobod", callback_data="namoz_time-dehqonobod"
            ),
        ],
        [
            InlineKeyboardButton(text="🌙 Muborak", callback_data="namoz_time-muborak"),
            InlineKeyboardButton(
                text="🌙 Shahrisabz", callback_data="namoz_time-shahrisabz"
            ),
        ],
        [
            InlineKeyboardButton(text="🌙 G'uzor", callback_data="namoz_time-guzor"),
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="hududlar"),
        ],
    ]
)

andijon = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌙 Andijon", callback_data="namoz_time-andijon"),
            InlineKeyboardButton(text="🌙 Xonobod", callback_data="namoz_time-xonobod"),
        ],
        [
            InlineKeyboardButton(
                text="🌙 Shahrixon", callback_data="namoz_time-shahrixon"
            ),
            InlineKeyboardButton(
                text="🌙 Xo'jaobod", callback_data="namoz_time-xojaobod"
            ),
        ],
        [
            InlineKeyboardButton(text="🌙 Asaka", callback_data="namoz_time-asaka"),
            InlineKeyboardButton(
                text="🌙 Marhamat", callback_data="namoz_time-marhamat"
            ),
        ],
        [
            InlineKeyboardButton(text="🌙 Poytug'", callback_data="namoz_time-poytug"),
            InlineKeyboardButton(text="🌙 Bo'ston", callback_data="namoz_time-boston"),
        ],
        [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="hududlar")],
    ]
)

xorazm = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌙 Urganch", callback_data="namoz_time-urganch"),
            InlineKeyboardButton(
                text="🌙 Hazorasp", callback_data="namoz_time-hazorasp"
            ),
        ],
        [
            InlineKeyboardButton(text="🌙 Xonqa", callback_data="namoz_time-xonqa"),
            InlineKeyboardButton(
                text="🌙 Yangibozor", callback_data="namoz_time-yangibozor"
            ),
        ],
        [
            InlineKeyboardButton(text="🌙 Shovot", callback_data="namoz_time-shovot"),
            InlineKeyboardButton(text="🌙 Xiva", callback_data="namoz_time-xiva"),
        ],
        [InlineKeyboardButton(text="⬅️ Orqaga", callback_data="hududlar")],
    ]
)

qoraqolpogiston = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌙 Nukus", callback_data="namoz_time-nukus"),
            InlineKeyboardButton(text="🌙 Mo'ynoq", callback_data="namoz_time-moynoq"),
        ],
        [
            InlineKeyboardButton(
                text="🌙 Taxtako'pir", callback_data="namoz_time-taxtakopir"
            ),
            InlineKeyboardButton(
                text="🌙 To'rtko'l", callback_data="namoz_time-tortkol"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🌙 Qo'ng'irot", callback_data="namoz_time-qongirot"
            ),
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="hududlar"),
        ],
    ]
)


def tumanlar(data):
    if data == "toshkent":
        return toshkent
    elif data == "buxoro":
        return buxoro
    elif data == "fargona":
        return fargona
    elif data == "jizzax":
        return jizzax
    elif data == "navoiy":
        return navoiy
    elif data == "namangan":
        return namangan
    elif data == "sirdaryo":
        return sirdaryo
    elif data == "samarqand":
        return samarqand
    elif data == "surxondaryo":
        return surxondaryo
    elif data == "qashqadaryo":
        return qashqadaryo
    elif data == "andijon":
        return andijon
    elif data == "xorazm":
        return xorazm
    elif data == "qoraqolpogiston":
        return qoraqolpogiston


def obhavo_key():
    url = requests.get("https://code.visualcoder.ru/ob-havo/index.php").json()
    btn = InlineKeyboardBuilder()

    for i in url[0]["shaharlar"]:
        btn.add(
            InlineKeyboardButton(
                text=f"☀️ {str(i).title()}", callback_data=f"havoinfo--{i}"
            )
        )
    btn.add(InlineKeyboardButton(text="🏘 Asosiy menyu", callback_data="result"))
    btn.adjust(2)

    return btn.as_markup()


def turi(item):
    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🗓 Bugungi", callback_data=f"obinfo-kun-{item}"
                ),
                InlineKeyboardButton(
                    text="📆 Haftalik", callback_data=f"obinfo-hafta-{item}"
                ),
            ],
            [InlineKeyboardButton(text="◀️ Orqaga", callback_data="obhavo")],
        ]
    )

    return btn
