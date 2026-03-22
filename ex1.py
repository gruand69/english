import random
import os
import json
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont


class MyWindow(QtWidgets.QDialog):
    def __init__(self, lst, parent=None):
        self.lst = lst
        self.i = 0
        QtWidgets.QWidget.__init__(self, parent)

        self.labelTask = QtWidgets.QLabel(
            'Choose the most appropriate short answer for each question.')
        self.labelTask.setWordWrap(True)
        self.labelTask.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelTask.setFont(QFont('Times', 14))
        self.labelTask.setStyleSheet(
            "border: 1px dashed black; border-radius: 10px;")

        self.labelQst = QtWidgets.QLabel(self.lst[self.i]['question'])
        self.labelQst.setWordWrap(True)
        self.labelQst.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelQst.setFont(QFont('Times', 14))
        self.labelQst.setStyleSheet(
            "border: 1px dashed black; border-radius: 10px;")

        self.btnCheck = QtWidgets.QPushButton("&Check")
        self.btnNext = QtWidgets.QPushButton("&Next >>")
        self.btnBack = QtWidgets.QPushButton("<< &Back")

        self.radBtn = QtWidgets.QVBoxLayout()
        self.radBtn_group = QtWidgets.QButtonGroup()
        self.btns = []
        for resp in self.lst[self.i]['response']:
            btn = QtWidgets.QRadioButton(resp)
            self.radBtn.addWidget(btn)
            self.radBtn_group.addButton(btn)
            self.btns.append(btn)
        self.btns[random.randint(
            0, len(self.lst[self.i]['response'])-1)].setChecked(True)

        self.hboxQstResp = QtWidgets.QHBoxLayout()
        self.hboxQstResp.addWidget(self.labelQst)
        self.hboxQstResp.addLayout(self.radBtn)

        self.hboxNavBtn = QtWidgets.QHBoxLayout()
        self.hboxNavBtn.addWidget(self.btnCheck)
        self.hboxNavBtn.addWidget(self.btnBack)
        self.hboxNavBtn.addWidget(self.btnNext)

        self.vboxVert = QtWidgets.QVBoxLayout()
        self.vboxVert.addWidget(self.labelTask)
        self.vboxVert.addLayout(self.hboxQstResp)
        self.vboxVert.addLayout(self.hboxNavBtn)

        self.setLayout(self.vboxVert)
        self.setGeometry(400, 200, 600, 300)

        self.btnCheck.clicked.connect(self.on_btnCheck_clicked)
        self.btnNext.clicked.connect(self.on_btnNext_clicked)
        self.btnBack.clicked.connect(self.on_btnBack_clicked)

    def on_btnCheck_clicked(self):
        n = self.radBtn_group.checkedButton().text()
        if n == self.lst[self.i]['response'][self.lst[self.i]['correct']-1]:
            QtWidgets.QMessageBox.information(self, 'Message', 'Excellent!')
        else:
            QtWidgets.QMessageBox.information(
                self, 'Message', 'Not exactly, Try again!')

    def cleanData(self):
        self.labelQst.setText(self.lst[self.i]['question'])
        while self.radBtn.count():
            item = self.radBtn.takeAt(0)  # Берем первый элемент
            widget = item.widget()   # Получаем виджет
            if widget is not None:
                widget.deleteLater()  # Удаляем виджет
        for i in self.radBtn_group.buttons():
            i.deleteLater()

        self.btns.clear()
        for resp in self.lst[self.i]['response']:
            btn = QtWidgets.QRadioButton(resp)
            self.radBtn.addWidget(btn)
            self.radBtn_group.addButton(btn)
            self.btns.append(btn)
        self.btns[random.randint(
            0, len(self.lst[self.i]['response'])-1)].setChecked(True)

    def on_btnNext_clicked(self):
        if self.i < len(self.lst) - 1:
            self.i += 1
            self.cleanData()

    def on_btnBack_clicked(self):
        if self.i > 0:
            self.i -= 1
            self.cleanData()


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, 'json/ex1.json'), encoding='utf-8') as f:
        data = json.load(f)

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow(data['test'])
    window.setWindowTitle("Ex1")
    window.show()
    sys.exit(app.exec_())
