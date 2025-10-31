import sqlite3

connect1 = sqlite3.connect("database.db")
cursor1 = connect1.cursor()

cursor1.execute("SELECT Amount, Nec FROM finance")
amounts = [row for row in cursor1.fetchall()]

connect2 = sqlite3.connect("banks.db")
cursor2 = connect2.cursor()

cursor2.execute("SELECT * FROM bank")
rows2 = cursor2.fetchall()
columns2 = [description[0] for description in cursor2.description]

def arrange_income (amounts):
    Income = {"Necessary": [], "Not_Necessary": []}
    Expense = {"Necessary": [], "Not_Necessary": []}
    for amount, nec in amounts:
        if amount > 0:
            if nec == 1:
                Income["Necessary"].append(amount)
            else:
                Income["Not_Necessary"].append(amount)
        else:
            if nec == 1:
                Expense["Necessary"].append(amount)
            else:
                Expense["Not_Necessary"].append(amount)
    return Income, Expense



def arrange_banks (rows2, columns2):
    banks = {}
    for row in rows2:
        row_dict = dict(zip(columns2, row))
        row_id = row_dict['Id']
        banks[row_id] = row_dict
    return banks


def cal_income (data):
    result = {}
    for key, value in data.items():
        total = sum(value)
        avrage = total/len(value) if value else 0
        result[key] = {"total": total, "average": avrage}
    result["all"] = {
        "total": sum([sum(v) for v in data.values()]),
        "average": sum([sum(v) for v in data.values()]) / sum([len(v) for v in data.values()]) if sum([len(v) for v in data.values()]) > 0 else 0}
    return result


def cal_reserve(banks, Income_cal, Expense_cal):
    reserve = sum(row['Deposit'] for row in banks.values()) + Income_cal['all']['total'] + Expense_cal['all']['total']
    return reserve


def cal_bank ():
    cursor1.execute("SELECT Amount, Bank_Name FROM finance ORDER BY id DESC LIMIT 1")
    last_row = cursor1.fetchone()
    if not last_row:
        print("⚠️ هیچ تراکنشی در جدول وجود ندارد.")
    amount, bank_name= last_row

    cursor2.execute("SELECT Deposit FROM bank WHERE Bank_Name = ?", (bank_name,))
    bank = cursor2.fetchone()
    if bank:
        new_deposit = bank[0] + amount
        cursor2.execute("UPDATE bank SET Deposit = ? WHERE Bank_Name = ?", (new_deposit, bank_name))
        print(f"موجودی {bank_name} به {new_deposit} تغییر یافت.")
    else:
        print("بانک وجود ندارد")

    connect2.commit()

Income , Expense = arrange_income(amounts)
Income_cal = cal_income(Income)
Expense_cal = cal_income(Expense)
#print(Income_cal)
#print(Expense_cal)

banks = arrange_banks (rows2, columns2)
reserve = cal_reserve(banks, Income_cal, Expense_cal)
#print(banks)
#print(reserve)
