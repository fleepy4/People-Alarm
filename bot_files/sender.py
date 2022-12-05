import telebot
import sqlite3

bot = telebot.TeleBot('5537898680:AAHYtK67uW1aui_dvM5P6mA7G2v8wc1Pc2Y')


def sender():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("SELECT tg_id FROM users")
    data = cursor.fetchall()
    print(data)
    for tg_id in data:
        bot.send_photo(
            tg_id[0],
            open('bot_files/temp/save.png', 'rb'),
            "Ктото был замечен в вашем доме! Прикрепляю фото!"
        )
