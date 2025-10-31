import sqlite3
from data_collect import income_collect
from data_collect import bank_collect
from calculate import cal_bank


connect1 = sqlite3.connect("database.db")
cursor1 = connect1.cursor()

cursor1.execute(""" CREATE TABLE IF NOT EXISTS finance (Id INTEGER PRIMARY KEY AUTOINCREMENT, Bank_Name TEXT NOT NULL, Amount REAL NOT NULL, Date TEXT NOT NULL, Nec INTEGER NOT NULL)""")
connect1.commit()

connect2 = sqlite3.connect("banks.db")
cursor2 = connect2.cursor()

cursor2.execute(""" CREATE TABLE IF NOT EXISTS bank (Id INTEGER PRIMARY KEY AUTOINCREMENT, Bank_Name TEXT NOT NULL, Deposit REAL NOT NULL, Gets_APR INTEGER NOT NULL, Rate REAL, Rate_Type TEXT, Days INTEGER)""")
connect2.commit()


def Import_income_expense():
    Amount, name, Date, Nec = income_collect()
    cursor1.execute(""" INSERT INTO finance (Amount, Bank_Name, Date, Nec) VALUES (?, ?, ?, ?)""", (Amount, name, Date, 1 if Nec else 0))
    connect1.commit()
    cal_bank ()

        

def Import_bank():
    Bank_Name, Deposit, Gets_APR, Rate, Rate_Type, Days = bank_collect()
    cursor2.execute(""" INSERT INTO bank (Bank_Name, Deposit, Gets_APR, Rate, Rate_Type, Days) VALUES (?, ?, ?, ?, ?, ?)""", (Bank_Name, Deposit, 1 if Gets_APR else 0, Rate, Rate_Type, Days))
    connect2.commit()
    print("ثبت شد.")


try:
    #Import_bank()
    Import_income_expense()
except Exception as e:
    print("خطا:", e)

connect1.close()
connect2.close()
