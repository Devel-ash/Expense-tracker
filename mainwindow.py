import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Qt, QAbstractTableModel, QDate
from ui_form import Ui_MainWindow


class SQLiteTableModel(QAbstractTableModel):
    def __init__(self, data, headers):
        super().__init__()
        self._data = data
        self._headers = headers

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return str(self._data[index.row()][index.column()])
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._headers[section]
            else:
                return section + 1


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.add_income_expense_button.clicked.connect(self.goto_income_expense)
        self.ui.add_bank_account_button.clicked.connect(self.goto_bank_account)
        self.ui.back_to_summary_bank_account_button.clicked.connect(self.goto_summary)
        self.ui.back_to_summary_income_expense_button.clicked.connect(self.goto_summary)


        self.ui.add_record_button.clicked.connect(self.add_finance_record)
        self.ui.add_bank_button.clicked.connect(self.add_bank_record)

        self.load_finance_data()
        self.load_bank_data()
        self.load_banks_into_combobox()

    def goto_income_expense(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.income_expense)

    def goto_bank_account(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.bank_account)

    def goto_summary(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.summary)

    def load_banks_into_combobox(self):
        try:
            conn = sqlite3.connect("banks.db")
            cur = conn.cursor()
            cur.execute("SELECT bank_name FROM bank")
            banks = cur.fetchall()
            conn.close()

            self.ui.bank_choose_field.clear()
            for bank in banks:
                self.ui.bank_choose_field.addItem(bank[0])
        except Exception as e:
            print("خطا در بارگذاری بانک‌ها:", e)

    def load_finance_data(self):
        try:
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM finance")
            rows = cur.fetchall()
            headers = [desc[0] for desc in cur.description]
            conn.close()

            model = SQLiteTableModel(rows, headers)
            self.ui.sql_tableview.setModel(model)
        except Exception as e:
            print("خطا در بارگذاری database.db:", e)

    def add_finance_record(self):
        amount = self.ui.amount_entry_field.text().strip()
        bank = self.ui.bank_choose_field.currentText()
        date = self.ui.date_selector_income_expense.date().toString("yyyy-MM-dd")
        necessity = self.ui.necessity_choose_field.currentText()

        if not amount or not bank:
            QMessageBox.warning(self, "خطا", "لطفاً همه فیلدها را پر کنید.")
            return

        try:
            connect1 = sqlite3.connect("database.db")
            cursor1 = connect1.cursor()
            cursor1.execute(""" CREATE TABLE IF NOT EXISTS finance (Id INTEGER PRIMARY KEY AUTOINCREMENT, Bank_Name TEXT NOT NULL, Amount REAL NOT NULL, Date TEXT NOT NULL, Nec INTEGER NOT NULL, Done INTEGER NOT NULL DEFAULT 0)""")
            cursor1.execute(""" INSERT INTO finance (Amount, Bank_Name, Date, Nec) VALUES (?, ?, ?, ?)""", (amount, bank, date, 1 if necessity else 0))
            connect1.commit()
            import calculate
            calculate.cal_bank()
            connect1.close()

            QMessageBox.information(self, "ثبت موفق", "رکورد جدید با موفقیت افزوده شد.")
            self.load_finance_data()
            self.clear_inputs()

        except Exception as e:
            QMessageBox.critical(self, "خطا در درج داده", str(e))

    def clear_inputs(self):
        self.ui.amount_entry_field.clear()
        self.ui.bank_choose_field.setCurrentIndex(0)
        self.ui.necessity_choose_field.setCurrentIndex(0)
        self.ui.date_selector_income_expense.setDate(QDate.currentDate())


    #next_page


    def add_bank_record(self):
        name = self.ui.bank_name_entry_field.text().strip()
        deposit = self.ui.deposit_amount_entry_field.text().strip()
        date = self.ui.date_selector_bank.date().toString("yyyy-MM-dd")
        gets_apr = 1 if self.ui.apr_radio_button.isChecked() else 0
        apr_rate = self.ui.apr_rate_entry_field.text().strip()
        apr_type = self.ui.apr_choose_field.currentText()
        days = self.ui.days_spinbox.value()

        if not name or not deposit:
            QMessageBox.warning(self, "خطا", "نام بانک و مبلغ سپرده الزامی است.")
            return

        try:
            deposit = float(deposit)
        except ValueError:
            QMessageBox.warning(self, "خطا", "لطفاً مبلغ سپرده را به عدد وارد کنید.")
            return
        

        try:
            connect2 = sqlite3.connect("banks.db")
            cursor2 = connect2.cursor()
            cursor2.execute(""" CREATE TABLE IF NOT EXISTS bank (Id INTEGER PRIMARY KEY AUTOINCREMENT, Bank_Name TEXT NOT NULL, Deposit REAL NOT NULL, Date TEXT NOT NULL, Gets_APR INTEGER NOT NULL, Rate REAL, Rate_Type TEXT, Days INTEGER)""")
            cursor2.execute(""" INSERT INTO bank (Bank_Name, Deposit, Date, Gets_APR, Rate, Rate_Type, Days) VALUES (?, ?, ?, ?, ?, ?, ?)""", (name, deposit, date, 1 if gets_apr else 0, apr_rate, apr_type, days))
            connect2.commit()
            import calculate
            calculate.cal_rate()
            connect2.close()

            QMessageBox.information(self, "ثبت موفق", "بانک جدید با موفقیت ثبت شد.")
            self.load_bank_data()
            self.load_banks_into_combobox()
            self.clear_bank_inputs()

        except Exception as e:
            QMessageBox.critical(self, "خطا در ثبت بانک", str(e))

    def load_bank_data(self):
        try:
            conn = sqlite3.connect("banks.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM bank")
            rows = cur.fetchall()
            headers = [desc[0] for desc in cur.description]
            conn.close()

            model = SQLiteTableModel(rows, headers)
            self.ui.tableView_6.setModel(model)
        except Exception as e:
            print("خطا در بارگذاری banks.db:", e)

    def clear_bank_inputs(self):
        self.ui.bank_name_entry_field.clear()
        self.ui.deposit_amount_entry_field.clear()
        self.ui.apr_rate_entry_field.clear()
        self.ui.apr_radio_button.setChecked(False)
        self.ui.apr_choose_field.setCurrentIndex(0)
        self.ui.days_spinbox.setValue(0)
        self.ui.date_selector_bank.setDate(QDate.currentDate())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
