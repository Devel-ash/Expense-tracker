# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QStatusBar, QTabWidget, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 791, 531))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.pushButton_5 = QPushButton(self.tab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(170, 410, 100, 32))
        self.dateEdit_3 = QDateEdit(self.tab)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setGeometry(QRect(80, 260, 91, 22))
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 320, 71, 16))
        self.lineEdit_3 = QLineEdit(self.tab)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(30, 80, 271, 21))
        self.comboBox_5 = QComboBox(self.tab)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setGeometry(QRect(110, 310, 103, 41))
        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 260, 58, 16))
        self.label_14 = QLabel(self.tab)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(30, 40, 58, 16))
        self.label_15 = QLabel(self.tab)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(30, 140, 58, 16))
        self.pushButton_6 = QPushButton(self.tab)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(30, 410, 100, 32))
        self.comboBox_6 = QComboBox(self.tab)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setGeometry(QRect(30, 190, 271, 41))
        self.tableView_3 = QTableView(self.tab)
        self.tableView_3.setObjectName(u"tableView_3")
        self.tableView_3.setGeometry(QRect(390, 100, 351, 341))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 40, 81, 16))
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 100, 111, 16))
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 160, 58, 16))
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 220, 71, 16))
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 270, 81, 16))
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 330, 71, 16))
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 380, 58, 16))
        self.pushButton = QPushButton(self.tab_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(49, 420, 111, 32))
        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(190, 420, 111, 32))
        self.lineEdit = QLineEdit(self.tab_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 40, 113, 21))
        self.lineEdit_2 = QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(170, 100, 113, 21))
        self.lineEdit_4 = QLineEdit(self.tab_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(170, 270, 111, 21))
        self.dateEdit = QDateEdit(self.tab_2)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(170, 160, 121, 22))
        self.comboBox = QComboBox(self.tab_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(170, 330, 121, 32))
        self.spinBox = QSpinBox(self.tab_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(170, 380, 42, 22))
        self.tableView = QTableView(self.tab_2)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(400, 40, 321, 401))
        self.radioButton = QRadioButton(self.tab_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(170, 220, 21, 16))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(290, 40, 221, 91))
        font = QFont()
        font.setFamilies([u"Arial Rounded MT Bold"])
        font.setPointSize(36)
        font.setBold(False)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_8.setStyleSheet(u"")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.summaryContainer = QWidget(self.tab_3)
        self.summaryContainer.setObjectName(u"summaryContainer")
        self.summaryContainer.setGeometry(QRect(30, 150, 721, 271))
        self.boxNecessary = QWidget(self.summaryContainer)
        self.boxNecessary.setObjectName(u"boxNecessary")
        self.boxNecessary.setGeometry(QRect(30, 0, 151, 271))
        self.boxNecessary.setStyleSheet(u"QWidget { background-color: rgba(210, 255, 210, 180); \n"
"border: 1px solid rgba(120, 200, 120, 200); \n"
"border-radius: 8px; } \n"
"")
        self.label_9 = QLabel(self.boxNecessary)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 30, 131, 101))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setWeight(QFont.DemiBold)
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"QLabel {\n"
"    color: #2E7D32;\n"
"    font-weight: 600;\n"
"    font-size: 12pt;\n"
"}")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_10 = QLabel(self.boxNecessary)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 210, 58, 16))
        self.label_10.setStyleSheet(u"QLabel {\n"
"    color: #1B5E20;\n"
"    font-weight: bold;\n"
"    font-size: 18pt;\n"
"}")
        self.boxUnnecessary = QWidget(self.summaryContainer)
        self.boxUnnecessary.setObjectName(u"boxUnnecessary")
        self.boxUnnecessary.setGeometry(QRect(200, 0, 161, 271))
        self.boxUnnecessary.setStyleSheet(u"QWidget { background-color: rgba(255, 220, 220, 180); \n"
"border: 1px solid rgba(220, 150, 150, 200); \n"
"border-radius: 8px; } \n"
"")
        self.label_16 = QLabel(self.boxUnnecessary)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(50, 210, 58, 16))
        self.label_16.setStyleSheet(u"QLabel {\n"
"    color: #C62828;\n"
"    font-weight: bold;\n"
"    font-size: 18pt;\n"
"}")
        self.label_19 = QLabel(self.boxUnnecessary)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 30, 141, 101))
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"QLabel {\n"
"    color: #B71C1C;\n"
"    font-weight: 600;\n"
"    font-size: 12pt;\n"
"}")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.boxRevenue = QWidget(self.summaryContainer)
        self.boxRevenue.setObjectName(u"boxRevenue")
        self.boxRevenue.setGeometry(QRect(380, 0, 161, 271))
        self.boxRevenue.setStyleSheet(u"QWidget { background-color: rgba(210, 235, 255, 180); \n"
"border: 1px solid rgba(140, 180, 220, 200);\n"
"border-radius: 8px; } \n"
"")
        self.label_17 = QLabel(self.boxRevenue)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(50, 210, 58, 16))
        self.label_17.setStyleSheet(u"QLabel {\n"
"    color: #0D47A1;\n"
"    font-weight: bold;\n"
"    font-size: 18pt;\n"
"}")
        self.label_20 = QLabel(self.boxRevenue)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 30, 141, 101))
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"QLabel {\n"
"    color: #1565C0;\n"
"    font-weight: 600;\n"
"    font-size: 12pt;\n"
"}")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.boxTotalSpending = QWidget(self.summaryContainer)
        self.boxTotalSpending.setObjectName(u"boxTotalSpending")
        self.boxTotalSpending.setGeometry(QRect(560, 0, 161, 271))
        self.boxTotalSpending.setStyleSheet(u"QWidget { background-color: rgba(240, 240, 240, 170); \n"
"border: 1px solid rgba(200, 200, 200, 200); \n"
"border-radius: 8px; } \n"
"")
        self.label_18 = QLabel(self.boxTotalSpending)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(50, 210, 58, 16))
        self.label_18.setStyleSheet(u"QLabel {\n"
"    color: #212121;\n"
"    font-weight: bold;\n"
"    font-size: 18pt;\n"
"}")
        self.label_21 = QLabel(self.boxTotalSpending)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 30, 141, 101))
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"QLabel {\n"
"    color: #424242;\n"
"    font-weight: 600;\n"
"    font-size: 12pt;\n"
"}")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 38))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Necessity:", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Amount:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Bank:", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Add Record", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Income / Expense", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bank Name:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Deposit Amount:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Gets APR?", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"APR Rate:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"APR Type:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Days:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add Bank", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Update Balances", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Monthly", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Annually", None))

        self.radioButton.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Bank Accounts", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Summary", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Total </p><p>Necessary </p><p>Spending</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"$0.00 (PlaceHolder)", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"$0.00 (PlaceHolder)", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Total </p><p>Unnecessary </p><p>Spending</p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"$0.00 (PlaceHolder)", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Total </p><p>Revenue</p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"$0.00 (PlaceHolder)", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Total</p><p>Spending</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Summary", None))
    # retranslateUi

