import sys
import re
import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Qt, QAbstractTableModel, QDate
from ui_form import Ui_MainWindow

connect1 = sqlite3.connect("database.db")
cursor1 = connect1.cursor()

cursor1.execute(""" CREATE TABLE IF NOT EXISTS finance (Id INTEGER PRIMARY KEY AUTOINCREMENT, Bank_Name TEXT NOT NULL, Amount REAL NOT NULL, Date TEXT NOT NULL, Nec INTEGER NOT NULL, Done INTEGER NOT NULL DEFAULT 0)""")
connect1.commit()

connect2 = sqlite3.connect("banks.db")
cursor2 = connect2.cursor()

cursor2.execute(""" CREATE TABLE IF NOT EXISTS bank (Id INTEGER PRIMARY KEY AUTOINCREMENT, Bank_Name TEXT NOT NULL, Deposit REAL NOT NULL, Date TEXT NOT NULL, Gets_APR INTEGER NOT NULL, Rate REAL, Rate_Type TEXT, Days INTEGER)""")
connect2.commit()


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
        amount_pattern = re.compile(r'^-?\d+(\.\d+)?$')
        #date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
        #nec_pattern = re.compile(r'^(yes|no|y|n)$', re.IGNORECASE)

        amount = self.ui.amount_entry_field.text().strip()
        bank = self.ui.bank_choose_field.currentText()
        date = self.ui.date_selector_income_expense.date().toString("yyyy-MM-dd")
        necessity = self.ui.necessity_choose_field.currentText()

        if not amount or not bank:
            QMessageBox.warning(self, "خطا", "لطفاً همه فیلدها را پر کنید.")
            return
        if not amount_pattern.match(amount):
            QMessageBox.warning(self, "Invalid amount format!")
            return
        try:
            amount = float(amount)
        except ValueError:
            QMessageBox.warning(self, "خطا", "مبلغ را به عدد وارد کنید.")
            return
        if amount == 0:
            QMessageBox.warning(self, "Amount cannot be zero.")
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

            if amount > 0:
                QMessageBox.information(self, "ثبت موفق", "درآمد جدید با موفقیت ثبت شد.")
            else:
                QMessageBox.information(self, "ثبت موفق", "هزینه جدید با موفقیت ثبت شد.")
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
        bank_pattern = re.compile(r'^[A-Za-z ]+$')
        number_pattern = re.compile(r'^\d+(\.\d+)?$')
        #date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')

        name = self.ui.bank_name_entry_field.text().strip()
        deposit = self.ui.deposit_amount_entry_field.text().strip()
        date = self.ui.date_selector_bank.date().toString("yyyy-MM-dd")
        gets_apr = 1 if self.ui.yesradio.isChecked() else 0
        if gets_apr == 1:
            apr_rate = self.ui.apr_rate_entry_field.text().strip()
            apr_type = self.ui.apr_choose_field.currentText()
            days = self.ui.days_spinbox.value()
            if not number_pattern.match(apr_rate):
                QMessageBox.warning(self, "Invalid APR format! Please enter a number.")
                return
            try:
                apr_rate = float(apr_rate)
            except ValueError:
                QMessageBox.warning(self, "APR must be greater than zero.")
                return
            if apr_rate <= 0:
                QMessageBox.warning(self, "APR must be greater than zero.")
                return
            if days <= 0:
                QMessageBox.warning(self, "Days must be greater than zero.")
                return
        else:
            apr_rate = None
            apr_type = None
            days = None

        if not name or not deposit or not gets_apr:
            QMessageBox.warning(self, "خطا", "نام بانک و مبلغ سپرده و داشتن یا نداشتن سود الزامی است.")
            return
        if not bank_pattern.match(name):
            QMessageBox.warning(self, "Bank name can only contain letters and spaces.")
            return
        if not number_pattern.match(deposit):
            QMessageBox.warning(self, "Invalid amount format! Please enter a number.")
            return
        try:
            deposit = float(deposit)
        except ValueError:
            QMessageBox.warning(self, "خطا", "لطفاً مبلغ سپرده را به عدد وارد کنید.")
            return
        if deposit <= 0:
            QMessageBox.warning(self, "Amount must be greater than zero.")
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
            self.ui.bank_account_tableView.setModel(model)
        except Exception as e:
            print("خطا در بارگذاری banks.db:", e)

    def clear_bank_inputs(self):
        self.ui.bank_name_entry_field.clear()
        self.ui.deposit_amount_entry_field.clear()
        self.ui.apr_rate_entry_field.clear()
        self.ui.yesradio.setChecked(False)
        self.ui.noradio.setChecked(False)
        self.ui.apr_choose_field.setCurrentIndex(0)
        self.ui.days_spinbox.setValue(0)
        self.ui.date_selector_bank.setDate(QDate.currentDate())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
