import sqlite3 as db



con = db.connect("sms_db.db")
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS received_sms(sms_id INTEGER PRIMARY KEY AUTOINCREMENT, sender_num TEXT, rev_sms TEXT, rev_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
