import sqlite3

connect = sqlite3.connect("database.db")
cursor = connect.cursor()

cursor.execute("SELECT Amount, Nec FROM finance")
amounts = [row for row in cursor.fetchall()]

def arrange (amounts):
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

def cal (data):
    result = {}
    for key, value in data.items():
        total = sum(value)
        avrage = total/len(value) if value else 0
        result[key] = {"total": total, "average": avrage}
    result["all"] = {
        "total": sum([sum(v) for v in data.values()]),
        "average": sum([sum(v) for v in data.values()]) / sum([len(v) for v in data.values()]) if sum([len(v) for v in data.values()]) > 0 else 0}
    return result


Income , Expense = arrange(amounts)
Income_cal = cal(Income)
Expense_cal = cal(Expense)
print(Income_cal)
print(Expense_cal)
