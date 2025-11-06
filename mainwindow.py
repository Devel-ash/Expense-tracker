import sys
import sqlite3

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QAbstractTableModel

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

        #########################
        self.load_bank_data()
        self.load_finance_data()

    def load_bank_data(self):
        try:
            conn = sqlite3.connect("banks.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM bank")
            rows = cur.fetchall()
            headers = [desc[0] for desc in cur.description]
            conn.close()

            model = SQLiteTableModel(rows, headers)
            self.ui.tableView.setModel(model)
        except Exception as e:
            print("خطا در بارگذاری banks.db:", e)

    def load_finance_data(self):
        try:
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM finance")
            rows = cur.fetchall()
            headers = [desc[0] for desc in cur.description]
            conn.close()

            model = SQLiteTableModel(rows, headers)
            self.ui.tableView_3.setModel(model)
        except Exception as e:
            print("خطا در بارگذاری database.db:", e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
