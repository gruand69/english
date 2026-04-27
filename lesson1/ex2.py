import os
import json
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont

sign = ('Match each remark in the first column with an appropriate ' +
        'response from the second column. Note: Some remarks ' +
        'have more than one appropriate response.')


class Ex2(QtWidgets.QDialog):
    def __init__(self, lst, sign, parent=None):
        self.lst = lst
        self.i = 0
        self.sign = sign
        QtWidgets.QWidget.__init__(self, parent)

        self.labelTask = QtWidgets.QLabel(self.sign)
        self.labelTask.setWordWrap(True)
        self.labelTask.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelTask.setFont(QFont('Times', 14))
        self.labelTask.setStyleSheet(
            "border: 1px dashed black; border-radius: 10px;")

        self.labelQst = QtWidgets.QLabel(self.lst['question'][self.i])
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
        self.btns = []
        for resp in self.lst['response']:
            btn = QtWidgets.QCheckBox(resp)
            self.radBtn.addWidget(btn)
            self.btns.append(btn)

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
        spisok = []
        for item in self.btns:
            if item.isChecked():
                spisok.append(self.btns.index(item)+1)
        word = self.lst['correct'][self.i]
        numbers = [ord(c) - 64 for c in word.upper()]
        result = [x for x in spisok if x in numbers]
        if (spisok == numbers):
            QtWidgets.QMessageBox.information(self, 'Message', 'Excellent!')
        elif not result:
            QtWidgets.QMessageBox.information(
                self, 'Message', 'Not exactly, Try again!')
        else:
            corr_ans = [self.lst['response'][x-1] for x in result]

            dialog = DiffWindow(corr_ans)
            dialog.exec_()

    def cleanData(self):
        self.labelQst.setText(self.lst['question'][self.i])

    def on_btnNext_clicked(self):
        if self.i < len(self.lst['question']) - 1:
            self.i += 1
            self.cleanData()

    def on_btnBack_clicked(self):
        if self.i > 0:
            self.i -= 1
            self.cleanData()


class DiffWindow(QtWidgets.QDialog):
    def __init__(self, ans, parent=None):
        self.ans = ans
        QtWidgets.QWidget.__init__(self, parent)

        self.label_quest = QtWidgets.QLabel("Your correct choises:")
        self.label_quest.setWordWrap(True)
        self.label_quest.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_quest.setFont(QFont('Times', 14))
        self.btnQuit = QtWidgets.QPushButton("&Close the window")

        self.vboxLabel = QtWidgets.QVBoxLayout()
        self.vboxLabel.addWidget(self.label_quest)
        for resp in self.ans:
            btn = QtWidgets.QLabel(resp)
            btn.setWordWrap(True)
            btn.setAlignment(
                QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            btn.setFont(QFont('Times', 14))

            self.vboxLabel.addWidget(btn)

        self.vboxLabel.addWidget(self.btnQuit)

        self.setLayout(self.vboxLabel)
        self.setGeometry(400, 200, 600, 300)

        self.btnQuit.clicked.connect(self.btnClosed)

    def btnClosed(self):
        self.close()


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    with open(
         os.path.join(dirname, '../json/ex2.json'), encoding='utf-8') as f:
        data = json.load(f)
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ex2(data['test'], sign)
    window.setWindowTitle("Ex2")
    window.show()
    sys.exit(app.exec_())
