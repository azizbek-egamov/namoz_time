from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from bs4 import BeautifulSoup as X
import requests
from googletrans import Translator

tr = Translator()

TOKEN = '6742690139:AAFOEPW3xYSWkcvnYA3nup1bW_1yyPTFhI4'

channel = "@walpapersUz"
admin = "5668945618"
bot_user = "Prayertime_uzbot"
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
