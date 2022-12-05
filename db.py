import sqlite3


def is_active():
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT is_active FROM status WHERE id = 1")
    data = cursor.fetchone()[0]
    if data == 0:
        return False
    else:
        return True


def change_status():
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT is_active FROM status WHERE id = 1")
    data = cursor.fetchone()
    print(data)
    if data[0] == 0:
        cursor.execute("UPDATE status SET is_active = 1 WHERE id = 1")
        conn.commit()
        return 1
    else:
        cursor.execute("UPDATE status SET is_active = 0 WHERE id = 1")
        conn.commit()
        return 0



def is_auth(tg_id):
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE tg_id = ?", [str(tg_id)])
    data = cursor.fetchall()
    if not data:
        return False
    else:
        return True


def auth(tg_id):
    conn = sqlite3.connect("base.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users(tg_id) VALUES(?)", [str(tg_id)])
    conn.commit()
