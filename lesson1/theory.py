import os
import json
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont


class Theory(QtWidgets.QDialog):
    def __init__(self, lst, parent=None):
        self.lst = lst
        self.i = 0
        QtWidgets.QWidget.__init__(self, parent)

        self.labelTitle = QtWidgets.QLabel(self.lst[self.i]['title'])
        self.labelTitle.setWordWrap(True)
        self.labelTitle.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelTitle.setFont(QFont('Times', 14))
        self.labelTitle.setStyleSheet(
            "border: 1px dashed black; border-radius: 10px;")

        self.labelInform = QtWidgets.QLabel(self.lst[self.i]['inform'])
        self.labelInform.setWordWrap(True)
        self.labelInform.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelInform.setFont(QFont('Times', 14))
        self.labelInform.setStyleSheet(
            "border: 1px dashed black; border-radius: 10px;")

        self.labelExample = QtWidgets.QLabel(self.lst[self.i]['example'])
        self.labelExample.setWordWrap(True)
        self.labelExample.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelExample.setFont(QFont('Times', 14))
        self.labelExample.setStyleSheet(
            "border: 1px dashed black; border-radius: 10px;")

        self.btnNext = QtWidgets.QPushButton("&Next >>")
        self.btnBack = QtWidgets.QPushButton("<< &Back")

        self.hboxQstResp = QtWidgets.QVBoxLayout()
        self.hboxQstResp.addWidget(self.labelTitle)
        self.hboxQstResp.addWidget(self.labelInform)
        self.hboxQstResp.addWidget(self.labelExample)

        self.hboxNavBtn = QtWidgets.QHBoxLayout()
        self.hboxNavBtn.addWidget(self.btnBack)
        self.hboxNavBtn.addWidget(self.btnNext)

        self.vboxVert = QtWidgets.QVBoxLayout()
        self.vboxVert.addLayout(self.hboxQstResp)
        self.vboxVert.addLayout(self.hboxNavBtn)

        self.setLayout(self.vboxVert)
        # self.setGeometry(400, 200, 600, 300)
        self.adjustSize()

        self.btnNext.clicked.connect(self.on_btnNext_clicked)
        self.btnBack.clicked.connect(self.on_btnBack_clicked)

    def on_btnNext_clicked(self):
        if self.i < len(self.lst) - 1:
            self.i += 1
        self.cleanData()

    def on_btnBack_clicked(self):
        if self.i > 0:
            self.i -= 1
        self.cleanData()

    def cleanData(self):
        self.labelTitle.setText(self.lst[self.i]['title'])
        self.labelInform.setText(self.lst[self.i]['inform'])
        self.labelExample.setText(self.lst[self.i]['example'])
        self.adjustSize()





if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, '../json/theory1.json'), encoding='utf-8') as f:
        data = json.load(f)

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Theory(data['test'])
    window.setWindowTitle("Theory1")
    window.show()
    sys.exit(app.exec_())
