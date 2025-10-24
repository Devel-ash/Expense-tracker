import sqlite3

connect = sqlite3.connect("database.db")
cursor = connect.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS finance (Id INTEGER PRIMARY KEY AUTOINCREMENT, Amount REAL NOT NULL, Date TEXT NOT NULL, Nec INTEGER NOT NULL)""")
connect.commit()

def Import(Amount, Date, Nec):
    cursor.execute(""" INSERT INTO finance (Amount, Date, Nec) VALUES (?, ?, ?)""", (Amount, Date, 1 if Nec else 0))
    connect.commit()
    print("ثبت شد.")