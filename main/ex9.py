import json
import os
from PyQt5 import QtWidgets


class Ex9(QtWidgets.QDialog):
    def __init__(self, lst, sign, parent=None):
        self.lst = lst
        self.i = 0
        self.sign = sign
        QtWidgets.QWidget.__init__(self, parent)

        # self.labelTask = QtWidgets.QLabel(
        #     'Fill each blank with the correct form of the indicated verb.')
        self.labelTask = QtWidgets.QLabel(
            self.sign)

        self.labelBegin = QtWidgets.QLabel(self.lst[self.i]['begin'])
        self.textEdit = QtWidgets.QLineEdit()
        self.labelEnd = QtWidgets.QLabel(self.lst[self.i]['end'])
        self.btnCheck = QtWidgets.QPushButton("Check")
        self.btnBack = QtWidgets.QPushButton("<< &Back")
        self.btnForw = QtWidgets.QPushButton("&Forward >>")

        self.hboxLayout1 = QtWidgets.QHBoxLayout()
        self.hboxLayout1.addWidget(self.labelBegin)
        self.hboxLayout1.addWidget(self.textEdit)
        self.hboxLayout1.addWidget(self.labelEnd)

        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addWidget(self.btnCheck)
        self.hbox.addWidget(self.btnBack)
        self.hbox.addWidget(self.btnForw)

        self.vboxLayout = QtWidgets.QVBoxLayout()
        self.vboxLayout.addWidget(self.labelTask)
        self.vboxLayout.addLayout(self.hboxLayout1)
        self.vboxLayout.addLayout(self.hbox)

        self.btnBack.clicked.connect(self.on_btnBack_clicked)
        self.btnForw.clicked.connect(self.on_btnForw_clicked)
        self.btnCheck.clicked.connect(self.on_btnCheck_clicked)

        self.setLayout(self.vboxLayout)
        self.setGeometry(400, 200, 200, 100)

    def on_btnCheck_clicked(self):
        answer = self.textEdit.text()
        if answer == self.lst[self.i]['correct']:
            self.textEdit.clear()
            QtWidgets.QMessageBox.information(self, 'Mesage', 'Excellent!')
        else:
            QtWidgets.QMessageBox.information(self, 'Mesage', 'Try again!')

    def on_btnForw_clicked(self):
        if self.i < len(self.lst) - 1:
            self.i += 1
            self.labelBegin.setText(self.lst[self.i]['begin'])
            self.labelEnd.setText(self.lst[self.i]['end'])
            self.textEdit.setText('')

    def on_btnBack_clicked(self):
        if self.i > 0:
            self.i -= 1
            self.labelBegin.setText(self.lst[self.i]['begin'])
            self.labelEnd.setText(self.lst[self.i]['end'])
            self.textEdit.setText('')


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    with open(
         os.path.join(dirname, '../json/lesson2/ex2.json'), encoding='utf-8') as f:
        data = json.load(f)
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ex9(data['test'], 'Fill in each blank with the correct form of say, speak, or tell, as appropriate.')
    window.setWindowTitle("Ex8")
    window.show()
    sys.exit(app.exec_())
