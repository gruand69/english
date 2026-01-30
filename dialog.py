import os
import json
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from check_phrase import CheckWindow


class MyWindow(QtWidgets.QWidget):
    def __init__(self, lst, parent=None):
        self.lst = lst
        self.i = 0
        self.mp = QMediaPlayer()
        QtWidgets.QWidget.__init__(self, parent)

        self.labelRus = QtWidgets.QLabel(self.lst[self.i]['question'])
        # self.labelRus.size()
        self.labelRus.setWordWrap(True)
        self.labelRus.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelRus.setFont(QFont('Times', 14))
        self.labelRus.setStyleSheet(
            "border: 1px dashed black; border-radius: 10px;")

        self.labelEng = QtWidgets.QLabel(self.lst[self.i]['response'])
        # self.labelEng.size()
        self.labelEng.setWordWrap(True)
        self.labelEng.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelEng.setFont(QFont('Times', 14))
        self.labelEng.setStyleSheet(
            "border: 1px dashed black; border-radius: 10px;")

        self.btnBack = QtWidgets.QPushButton("<< &Back")
        self.btnForw = QtWidgets.QPushButton("&Forward >>")
        self.btnCheck = QtWidgets.QPushButton("&Prase")
        self.btnAudio = QtWidgets.QPushButton("&Audio")
        self.btnQuit = QtWidgets.QPushButton("&Close the window")

        self.vboxLabel = QtWidgets.QVBoxLayout()
        self.vboxLabel.addWidget(self.labelRus)
        self.vboxLabel.addWidget(self.labelEng)

        self.vboxNavBtn = QtWidgets.QHBoxLayout()
        self.vboxNavBtn.addWidget(self.btnBack)
        self.vboxNavBtn.addWidget(self.btnForw)

        self.vboxVert = QtWidgets.QVBoxLayout()
        self.vboxVert.addLayout(self.vboxLabel)
        self.vboxVert.addLayout(self.vboxNavBtn)

        self.vboxManBtn = QtWidgets.QVBoxLayout()
        self.vboxManBtn.addWidget(self.btnCheck)
        self.vboxManBtn.addWidget(self.btnAudio)
        self.vboxManBtn.addWidget(self.btnQuit)

        self.MainLayout = QtWidgets.QHBoxLayout()
        self.MainLayout.addLayout(self.vboxVert)
        self.MainLayout.addLayout(self.vboxManBtn)

        self.setLayout(self.MainLayout)
        self.setGeometry(400, 200, 600, 300)

        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)
        self.btnBack.clicked.connect(self.on_btnBack_clicked)
        self.btnForw.clicked.connect(self.on_btnForw_clicked)
        self.btnCheck.clicked.connect(self.on_btnCheck_clicked)
        self.btnAudio.clicked.connect(self.on_btnAudio_clicked)

    def on_btnAudio_clicked(self):
        mc = QMediaContent(QtCore.QUrl.fromLocalFile(
            f"/home/gruand69/Dev/english/media/dialog1/{self.i+1}.mp3"))
        self.mp.setMedia(mc)
        self.mp.stop()
        self.mp.setVolume(50)
        self.mp.setPosition(0)
        self.mp.play()

    def on_btnCheck_clicked(self):
        dialog = CheckWindow(self.lst[self.i]['question'],
                             self.lst[self.i]['response'])
        dialog.exec_()

    def on_btnForw_clicked(self):
        if self.i < len(self.lst) - 1:
            self.i += 1
            self.labelRus.setText(self.lst[self.i]['question'])
            self.labelEng.setText(self.lst[self.i]['response'])

    def on_btnBack_clicked(self):
        if self.i > 0:
            self.i -= 1
            self.labelRus.setText(self.lst[self.i]['question'])
            self.labelEng.setText(self.lst[self.i]['response'])


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    with open(os.path.join(dirname, 'json/dialog1.json')) as f:
        data = json.load(f)
    # print(data['test'][1])

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow(data['test'])
    window.setWindowTitle("OOP-style creating the window")
    # window.resize(300, 70)
    window.show()
    sys.exit(app.exec_())
