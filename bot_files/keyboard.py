from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, \
    InlineKeyboardButton, InlineKeyboardMarkup
import db


def main_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("Включить/Выключить сигнализацию")
    return kb
