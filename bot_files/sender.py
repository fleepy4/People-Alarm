import telebot
import sqlite3

bot = telebot.TeleBot('TOKEN')


def sender():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("SELECT tg_id FROM users")
    data = cursor.fetchall()
    print(data)
    for tg_id in data:
        try:
            bot.send_photo(
                tg_id[0],
                open('bot_files/temp/save.png', 'rb'),
                "Ктото был замечен в вашем доме! Прикрепляю фото!"
            )
        except:
            pass
