import json
import os
from PyQt5 import QtWidgets


class Ex7(QtWidgets.QDialog):
    def __init__(self, lst, parent=None):
        self.lst = lst
        self.i = 0
        QtWidgets.QWidget.__init__(self, parent)

        self.labelTask = QtWidgets.QLabel(
            'Write a remark or question for each of the following responses.')
        self.labelQuest = QtWidgets.QLabel(self.lst[self.i]['answer'])
        self.textEdit = QtWidgets.QLineEdit()
        self.btnCheck = QtWidgets.QPushButton("Check")
        self.btnBack = QtWidgets.QPushButton("<< &Back")
        self.btnForw = QtWidgets.QPushButton("&Forward >>")

        self.vboxLayout = QtWidgets.QVBoxLayout()
        self.vboxLayout.addWidget(self.labelTask)
        self.vboxLayout.addWidget(self.textEdit)
        self.vboxLayout.addWidget(self.labelQuest)

        self.hbox = QtWidgets.QHBoxLayout()
        self.hbox.addWidget(self.btnCheck)
        self.hbox.addWidget(self.btnBack)
        self.hbox.addWidget(self.btnForw)

        self.vboxLayout.addLayout(self.hbox)

        self.btnBack.clicked.connect(self.on_btnBack_clicked)
        self.btnForw.clicked.connect(self.on_btnForw_clicked)
        self.btnCheck.clicked.connect(self.on_btnCheck_clicked)

        self.setLayout(self.vboxLayout)
        self.setGeometry(400, 200, 200, 100)

    def on_btnCheck_clicked(self):
        # answer = self.textEdit.text()
        # if answer == self.lst[self.i]['response']:
        #     self.textEdit.clear()
        QtWidgets.QMessageBox.information(self, 'Possible answer',
                                          self.lst[self.i]['qst'])
        # else:
        #     QtWidgets.QMessageBox.information(self, 'Mesage', 'Try again!')

    def on_btnForw_clicked(self):
        if self.i < len(self.lst) - 1:
            self.i += 1
            self.labelQuest.setText(self.lst[self.i]['answer'])
            self.textEdit.clear()

    def on_btnBack_clicked(self):
        if self.i > 0:
            self.i -= 1
            self.labelQuest.setText(self.lst[self.i]['answer'])
            self.textEdit.clear()


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    with open(
         os.path.join(dirname, '../json/ex7.json'), encoding='utf-8') as f:
        data = json.load(f)
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ex7(data['test'])
    window.setWindowTitle("Ex7")
    window.show()
    sys.exit(app.exec_())
