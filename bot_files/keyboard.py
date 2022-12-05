from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, \
    InlineKeyboardButton, InlineKeyboardMarkup
import db


def main_kb():
    kb = ReplyKeyboardMarkup()
    if db.is_active():
        kb.add(KeyboardButton("❌ Отключить отправку"))
    else:
        kb.add(KeyboardButton("✅ Включить отправку"))
