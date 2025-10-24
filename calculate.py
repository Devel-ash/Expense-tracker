import sqlite3

connect = sqlite3.connect("database.db")
cursor = connect.cursor()

cursor.execute("SELECT Amount FROM finance")
amounts = [row[0] for row in cursor.fetchall()]

def cal (amounts):
    Income = []
    Expense = []
    for i in amounts:
        if i > 0:
            Income.append(i)
        else:
            Expense.append(i)

    sum_income = sum(Income)
    sum_expense = sum(Expense)
    average_income = sum_income/len(Income)
    average_expense = sum_expense/len(Expense)
    


    #print (average_income)
    #print (average_expense)


cal (amounts)