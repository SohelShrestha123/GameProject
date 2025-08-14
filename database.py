import sqlite3

conn=sqlite3.connect('game.db')
cursor=conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS player(
 sn INTEGER PRIMARY KEY AUTOINCREMENT,
 firstname TEXT NOT NULL,
 lastname TEXT NOT NULL,
 username TEXT NOT NULL,
 address TEXT NOT NULL,
 email TEXT NOT NULL,
 newpassword TEXT NOT NULL,
 confirmpassword TEXT NOT NULL,
 gender TEXT,
 dob TEXT NOT NULL,
 birthtime TEXT NOT NULL
)
''')
conn.commit()
conn.close()