import random
import os
import json
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont


class Ex2(QtWidgets.QDialog):
    def __init__(self, lst, parent=None):
        self.lst = lst
        self.i = 0
        QtWidgets.QWidget.__init__(self, parent)

        self.labelTask = QtWidgets.QLabel(
            'Match each remark in the first column with an appropriate response from the second column. Note: Some remarks have more than one appropriate response.')
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
        # self.radBtn_group = QtWidgets.QButtonGroup()
        self.btns = []
        for resp in self.lst['response']:
            btn = QtWidgets.QCheckBox(resp)
            self.radBtn.addWidget(btn)
            # self.radBtn_group.addButton(btn)
            self.btns.append(btn)
        # self.btns[random.randint(
        #     0, len(self.lst[self.i]['response'])-1)].setChecked(True)

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
        # print(result)
        # print(self.i, spisok, numbers)
        if (spisok == numbers):
            QtWidgets.QMessageBox.information(self, 'Message', 'Excellent!')
        elif not result:
            QtWidgets.QMessageBox.information(
                self, 'Message', 'Not exactly, Try again!')
        else:
            corr_ans = [self.lst['response'][x-1] for x in result]

            dialog = DiffWindow(corr_ans)
            dialog.exec_()

        # n = self.radBtn_group.checkedButton().text()
        # if n == self.lst[self.i]['response'][self.lst[self.i]['correct']-1]:
        #     QtWidgets.QMessageBox.information(self, 'Message', 'Excellent!')
        # else:
        #     QtWidgets.QMessageBox.information(
        #         self, 'Message', 'Not exactly, Try again!')

    def cleanData(self):
        self.labelQst.setText(self.lst['question'][self.i])
        # while self.radBtn.count():
        #     item = self.radBtn.takeAt(0)  # Берем первый элемент
        #     widget = item.widget()   # Получаем виджет
        #     if widget is not None:
        #         widget.deleteLater()  # Удаляем виджет
        # for i in self.radBtn_group.buttons():
        #     i.deleteLater()

        # self.btns.clear()
        # for resp in self.lst[self.i]['response']:
        #     btn = QtWidgets.QRadioButton(resp)
        #     self.radBtn.addWidget(btn)
        #     self.radBtn_group.addButton(btn)
        #     self.btns.append(btn)
        # self.btns[random.randint(
        #     0, len(self.lst[self.i]['response'])-1)].setChecked(True)

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
        # self.label_quest.setStyleSheet(
        #     "border: 1px dashed black; border-radius: 10px;")

        # self.label_ans = QtWidgets.QTextEdit(self.response + ' ')
        # self.label_ans.setWordWrap(True)
        # self.label_ans.setAlignment(
        #     QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        # self.label_ans.setFont(QFont('Times', 14))
        # self.label_ans.setStyleSheet(
        #     "border: 1px dashed black; border-radius: 10px;")

        # self.compare()

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
        # self.vboxLabel.addWidget(self.label_ans)

        # self.vboxNavBtn = QtWidgets.QHBoxLayout()

        self.vboxLabel.addWidget(self.btnQuit)

        # self.vboxVert = QtWidgets.QVBoxLayout()
        # self.vboxVert.addLayout(self.vboxLabel)
        # self.vboxVert.addLayout(self.vboxNavBtn)

        self.setLayout(self.vboxLabel)
        self.setGeometry(400, 200, 600, 300)

        # self.btnQuit.clicked.connect(QtWidgets.qApp.quit)
        self.btnQuit.clicked.connect(self.btnClosed)

    def btnClosed(self):
        self.close()

    # def compare(self):
    #     if self.response:
    #         k = 0
    #         while self.response and self.response[k] == self.question[k]:
    #             if (k == len(self.response)-1) or (k == len(self.question)-1):
    #                 k += 1
    #                 break
    #             k += 1
    #         highlight_format = QTextCharFormat()
    #         highlight_format.setBackground(QColor("red"))
    #         cursor = QTextCursor(self.label_ans.textCursor())
    #         cursor.setPosition(k)
    #         cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor,
    #                             1)
    #         cursor.mergeCharFormat(highlight_format)


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, '../json/ex2.json'), encoding='utf-8') as f:
        data = json.load(f)
    # print(data['test'])
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ex2(data['test'])
    window.setWindowTitle("Ex2")
    window.show()
    sys.exit(app.exec_())


