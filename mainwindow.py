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

        self.load_finance_data()
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
            cursor1.execute(""" INSERT INTO finance (Amount, Bank_Name, Date, Nec) VALUES (?, ?, ?, ?)""", (amount, bank, date, 1 if necessity else 0))
            connect1.commit()
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
