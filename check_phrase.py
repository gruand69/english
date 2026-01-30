import difflib
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont, QTextCharFormat, QColor, QTextCursor


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

        self.label_ans = QtWidgets.QTextEdit(self.response)
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

        s = difflib.SequenceMatcher(None,
                                    self.question,
                                    self.response)
        # for tag, i1, i2, j1, j2 in s.get_opcodes():
        #     print(f"{tag} a[{i1}:{i2}] b[{j1}:{j2}]")
        # print(s.get_opcodes()[1][3], s.get_opcodes()[1][4])
        start = s.get_opcodes()[1][3]
        finish = s.get_opcodes()[1][4]
        if start == finish:
            finish += 1
            self.label_ans.setPlainText(self.response + ' ')
        # print(start)
        # print(finish)
        highlight_format = QTextCharFormat()
        highlight_format.setBackground(QColor("red"))

        cursor = QTextCursor(self.label_ans.textCursor())
        # cursor = QTextCursor(self.label_ans.setCursor())

        cursor.setPosition(start)
        # print(cursor.position())
        cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor,
                            finish-start)
        print(cursor.position())
        cursor.mergeCharFormat(highlight_format)
        # self.label_ans.setText(self.)


class CheckWindow(QtWidgets.QDialog):
    def __init__(self, question, response, parent=None):
        self.question = question
        self.response = response
        QtWidgets.QWidget.__init__(self, parent)

        self.labelRus = QtWidgets.QLabel(self.question)
        self.labelRus.setWordWrap(True)
        self.labelRus.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelRus.setFont(QFont('Times', 14))
        self.labelRus.setStyleSheet(
            "border: 1px dashed black; border-radius: 10px;")

        self.textEdit = QtWidgets.QPlainTextEdit()
        # self.labelEng.size()
        # self.labelEng.setWordWrap(True)
        # self.labelEng.setAlignment(
        #     QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.textEdit.setFont(QFont('Times', 14))
        self.textEdit.setStyleSheet(
            "border: 1px dashed black; border-radius: 10px;")

        self.btnCheck = QtWidgets.QPushButton("Check")
        self.btnQuit = QtWidgets.QPushButton("&Close the window")

        self.vboxLabel = QtWidgets.QVBoxLayout()
        self.vboxLabel.addWidget(self.labelRus)
        self.vboxLabel.addWidget(self.textEdit)

        self.vboxNavBtn = QtWidgets.QHBoxLayout()
        self.vboxNavBtn.addWidget(self.btnCheck)
        self.vboxNavBtn.addWidget(self.btnQuit)

        self.vboxVert = QtWidgets.QVBoxLayout()
        self.vboxVert.addLayout(self.vboxLabel)
        self.vboxVert.addLayout(self.vboxNavBtn)

        self.setLayout(self.vboxVert)
        self.setGeometry(400, 200, 600, 300)

        # self.btnQuit.clicked.connect(QtWidgets.qApp.quit)
        self.btnQuit.clicked.connect(self.btnClosed)
        self.btnCheck.clicked.connect(self.on_btnCheck_clicked)

    def on_btnCheck_clicked(self):
        answer = self.textEdit.toPlainText()
        if answer == self.response:
            QtWidgets.QMessageBox.information(self, 'Mesage', 'Excellent!')
        else:
            self.textEdit.clear()
            dialog = DiffWindow(self.response,
                                self.textEdit.toPlainText())
            dialog.exec_()
            # QtWidgets.QMessageBox.information(self, 'Mesage', "You're wrong!")
            # for i in range(len(self.response)-1):
            #     if self.response[i] != answer[i]:
            #         QtWidgets.QMessageBox.information(
            #             self, 'Mesage', self.response[i])
            #         break

    def btnClosed(self):
        self.close()


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = DiffWindow('Correct! I just got in last night.',
                        'Correct!I just get in last night.')
    window.setWindowTitle("OOP-style creating the window")
    # window.resize(300, 70)
    window.show()
    sys.exit(app.exec_())
