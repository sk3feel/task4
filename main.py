import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPainter, QColor
import sqlite3

ui_file = 'main.ui'


class Taskform(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.load_table()
        self.btn_reload.clicked.connect(self.load_table)

    def load_table(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        value = f"""SELECT * FROM sorts"""
        datas = cur.execute(value).fetchall()
        self.tablewg.setRowCount(len(datas))
        tablerow = 0
        print(datas)
        for date in datas:
            for i in range(6):
                self.tablewg.setItem(tablerow, i, QtWidgets.QTableWidgetItem(str(date[i + 1])))
            tablerow += 1


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Taskform()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
