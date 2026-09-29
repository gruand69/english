from pathlib import Path
import json
import random

import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont, QTextCharFormat, QColor, QTextCursor

import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')
nltk.download('punkt_tab')

# Рекурсивный поиск файлов (во всех подпапках)
pathes = []
for file in Path('./bte_check').rglob('dialog*.json'):
    pathes.append(file.absolute())
task = {}
for path in pathes:
    with open(path, encoding='utf-8') as f:
        data = json.load(f)

        for i in range(0, len(data['test'])-1):
            sentences_rus = sent_tokenize(
                data['test'][i]['question'], language="russian")
            sentences_eng = sent_tokenize(
                data['test'][i]['response'], language="english")
            for k, v in zip(sentences_rus, sentences_eng):
                task[k] = v

random_keys = random.sample(list(task.keys()), 10)

random_pairs = [[key, task[key]] for key in random_keys]

# print(random_pairs)


class DiffWindow(QtWidgets.QDialog):
    def __init__(self, question, response, parent=None):
        self.question = question
        self.response = response
        QtWidgets.QWidget.__init__(self, parent)

        self.label_quest = QtWidgets.QLabel(self.question)
        self.label_quest.setWordWrap(True)
        self.label_quest.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_quest.setFont(QFont('Times', 14))
        self.label_quest.setStyleSheet(
            "border: 1px dashed black; border-radius: 10px;")

        self.label_ans = QtWidgets.QTextEdit(self.response + ' ')
        # self.label_ans.setWordWrap(True)
        # self.label_ans.setAlignment(
        #     QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_ans.setFont(QFont('Times', 14))
        self.label_ans.setStyleSheet(
            "border: 1px dashed black; border-radius: 10px;")

        self.compare()

        self.btnQuit = QtWidgets.QPushButton("&Close the window")

        self.vboxLabel = QtWidgets.QVBoxLayout()
        self.vboxLabel.addWidget(self.label_quest)
        self.vboxLabel.addWidget(self.label_ans)

        self.vboxNavBtn = QtWidgets.QHBoxLayout()

        self.vboxNavBtn.addWidget(self.btnQuit)

        self.vboxVert = QtWidgets.QVBoxLayout()
        self.vboxVert.addLayout(self.vboxLabel)
        self.vboxVert.addLayout(self.vboxNavBtn)

        self.setLayout(self.vboxVert)
        self.setGeometry(400, 200, 600, 300)

        # self.btnQuit.clicked.connect(QtWidgets.qApp.quit)
        self.btnQuit.clicked.connect(self.btnClosed)

    def btnClosed(self):
        self.close()

    def compare(self):
        if self.response:
            k = 0
            while self.response and self.response[k] == self.question[k]:
                if (k == len(self.response)-1) or (k == len(self.question)-1):
                    k += 1
                    break
                k += 1
            highlight_format = QTextCharFormat()
            highlight_format.setBackground(QColor("red"))
            cursor = QTextCursor(self.label_ans.textCursor())
            cursor.setPosition(k)
            cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor,
                                1)
            cursor.mergeCharFormat(highlight_format)


class CheckWindow(QtWidgets.QDialog):
    def __init__(self, lst, parent=None):
        self.lst = lst
        self.i = 0
        self.score = 0
        self.flag = True
        QtWidgets.QWidget.__init__(self, parent)

        self.labelRus = QtWidgets.QLabel(self.lst[self.i][0])
        self.labelRus.setWordWrap(True)
        self.labelRus.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelRus.setFont(QFont('Times', 14))
        self.labelRus.setStyleSheet(
            "border: 1px dashed black; border-radius: 10px;")

        self.textEdit = QtWidgets.QPlainTextEdit()
        self.textEdit.setFont(QFont('Times', 14))
        self.textEdit.setStyleSheet(
            "border: 1px dashed black; border-radius: 10px;")

        self.btnCheck = QtWidgets.QPushButton("Check")
        # self.btnBack = QtWidgets.QPushButton("<< &Back")
        self.btnForw = QtWidgets.QPushButton("&Forward >>")
        self.btnQuit = QtWidgets.QPushButton("&Close the window")

        self.vboxLabel = QtWidgets.QVBoxLayout()
        self.vboxLabel.addWidget(self.labelRus)
        self.vboxLabel.addWidget(self.textEdit)

        self.vboxNavBtn = QtWidgets.QHBoxLayout()
        self.vboxNavBtn.addWidget(self.btnCheck)
        # self.vboxNavBtn.addWidget(self.btnBack)
        self.vboxNavBtn.addWidget(self.btnForw)
        self.vboxNavBtn.addWidget(self.btnQuit)

        self.vboxVert = QtWidgets.QVBoxLayout()
        self.vboxVert.addLayout(self.vboxLabel)
        self.vboxVert.addLayout(self.vboxNavBtn)

        self.setLayout(self.vboxVert)
        self.setGeometry(400, 200, 600, 300)

        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)
        self.btnQuit.clicked.connect(self.btnClosed)
        self.btnCheck.clicked.connect(self.on_btnCheck_clicked)
        # self.btnBack.clicked.connect(self.on_btnBack_clicked)
        self.btnForw.clicked.connect(self.on_btnForw_clicked)

    def on_btnForw_clicked(self):
        if self.i < len(self.lst) - 1:
            self.flag = True
            self.i += 1
            self.labelRus.setText(self.lst[self.i][0])
            self.textEdit.clear()
            # self.labelEng.setText(self.lst[self.i]['response'])
        else:
            QtWidgets.QMessageBox.information(self, 'Mesage', f'Your result: {self.score} from 10.')

    def on_btnBack_clicked(self):
        if self.i > 0:
            self.i -= 1
            self.labelRus.setText(self.lst[self.i][0])
            self.textEdit.clear()
            # self.labelEng.setText(self.lst[self.i]['response'])

    def on_btnCheck_clicked(self):
        answer = self.textEdit.toPlainText()
        if answer == self.lst[self.i][1]:
            QtWidgets.QMessageBox.information(self, 'Mesage', 'Excellent!')
            if self.flag:
                self.score += 1
        # else:
        elif answer:
            # self.textEdit.clear()
            self.flag = False
            dialog = DiffWindow(self.lst[self.i][1],
                                self.textEdit.toPlainText())
            self.textEdit.clear()
            dialog.exec_()
            # QtWidgets.QMessageBox.information(self, 'Mesage', "You're wrong!")
            # for i in range(len(self.response)-1):
            #     if self.response[i] != answer[i]:
            #         QtWidgets.QMessageBox.information(
            #             self, 'Mesage', self.response[i])
            #         break
        else:
            QtWidgets.QMessageBox.information(self, 'Mesage', 'Print something, please!')

    def btnClosed(self):
        self.close()


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = CheckWindow(random_pairs)
    window.setWindowTitle("OOP-style creating the window")
    # window.resize(300, 70)
    window.show()
    sys.exit(app.exec_())
