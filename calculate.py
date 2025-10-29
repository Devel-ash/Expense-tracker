import sqlite3

connect = sqlite3.connect("database.db")
cursor = connect.cursor()

cursor.execute("SELECT Amount, Nec FROM finance")
amounts = [row for row in cursor.fetchall()]

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


#def cal_bank ():







Income , Expense = arrange_income(amounts)
Income_cal = cal_income(Income)
Expense_cal = cal_income(Expense)
#print(Income_cal)
#print(Expense_cal)

banks = arrange_banks (rows2, columns2)
reserve = cal_reserve(banks, Income_cal, Expense_cal)
print(banks)
print(reserve)
