import json
import random
import os
import sys
from PyQt5 import QtWidgets

from dialog import MyWindow
from ex1 import Ex1
from ex2 import Ex2
from ex3 import Ex3

i = 1
max_ex = 10


class MyLesson(QtWidgets.QDialog):
    def __init__(self, i, max_ex, parent=None):
        self.i = i
        self.max_ex = max_ex
        QtWidgets.QWidget.__init__(self, parent)

        self.hboxMain = QtWidgets.QHBoxLayout()
        self.vbox1 = QtWidgets.QVBoxLayout()
        self.vbox2 = QtWidgets.QVBoxLayout()
        self.vbox3 = QtWidgets.QVBoxLayout()

        self.btnDialog = QtWidgets.QPushButton("&Dialog")
        self.btnEx = QtWidgets.QPushButton("&StartEx")
        self.vbox2.addWidget(self.btnDialog)
        self.vbox2.addWidget(self.btnEx)

        self.radBtn_group = QtWidgets.QButtonGroup()
        self.btns = []
        for i in range(1, self.max_ex+1, 1):
            btn = QtWidgets.QRadioButton(f'ex {i}')
            self.vbox1.addWidget(btn)
            self.radBtn_group.addButton(btn)
            self.btns.append(btn)
        self.btns[random.randint(
            0, self.max_ex-1)].setChecked(True)

        self.hboxMain.addLayout(self.vbox1)
        self.hboxMain.addLayout(self.vbox2)
        self.hboxMain.addLayout(self.vbox3)

        self.setLayout(self.hboxMain)
        self.setGeometry(400, 200, 250, 175)

        self.btnDialog.clicked.connect(self.on_btnDialog_clicked)
        self.btnEx.clicked.connect(self.on_btnEx_clicked)

    def on_btnEx_clicked(self):
        n = self.btns.index(self.radBtn_group.checkedButton()) + 1
        dirname = os.path.dirname(__file__)
        if n == 1:
            with open(os.path.join(
                 dirname, '../json/ex1.json'), encoding='utf-8') as f:
                data = json.load(f)
            window = Ex1(data['test'])
            window.setWindowTitle("Ex1")
            window.exec_()
        elif n == 2:
            with open(os.path.join(
                 dirname, '../json/ex2.json'), encoding='utf-8') as f:
                data = json.load(f)
            window = Ex2(data['test'])
            window.setWindowTitle("Ex2")
            window.exec_()
        elif n == 3:
            with open(
                 os.path.join(
                     dirname, '../json/ex3.json'), encoding='utf-8') as f:
                data = json.load(f)
            window = Ex3(data['test'])
            window.setWindowTitle("Ex3")
            window.exec_()
        else:
            pass

    def on_btnDialog_clicked(self):
        dirname = os.path.dirname(__file__)
        with open(os.path.join(
             dirname, '../json/dialog1.json'), encoding='utf-8') as f:
            data = json.load(f)
        dialog = MyWindow(data['test'])
        dialog.setWindowTitle("Dialog 1")
        dialog.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyLesson(i, max_ex)
    window.setWindowTitle("Lesson1")
    window.show()
    sys.exit(app.exec_())
