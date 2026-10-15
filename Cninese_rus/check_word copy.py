import sys
import json
import random
import os

from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class CheckWindow(QtWidgets.QWidget):

    def __init__(self, les):
        super().__init__()
        self.les = les
        self.num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(self.num)
        self.i = self.num.pop()

        with open(f'Cninese_rus\json\lesson{self.les}.json', encoding='utf-8') as f:
            self.data = json.load(f)

        self.mp = QMediaPlayer()
        self.setWindowTitle("Translate this phrase.")
        self.resize(350, 200)

        self.labelRus = QtWidgets.QLabel(
            self.data["test"][self.i]["russian"])
        self.labelRus.setWordWrap(True)
        self.labelRus.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelRus.setFont(QFont('Times', 14))
        self.labelRus.setStyleSheet(
            "border: 1px dashed black; border-radius: 10px;")

        self.btnAudio = QtWidgets.QPushButton("&Audio")
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.labelRus)
        vbox.addWidget(self.btnAudio)
        # vbox.addLayout(vbox)

        self.btnNext = QtWidgets.QPushButton("&Next >>")
        vbox.addWidget(self.btnNext)

        self.setLayout(vbox)

        self.btnAudio.clicked.connect(self.on_btnAudio_clicked)
        self.btnNext.clicked.connect(self.on_btnNext_clicked)

    def on_btnAudio_clicked(self):
        mc = QMediaContent(
            QtCore.QUrl.fromLocalFile(
                f'Cninese_rus\media\lesson{self.les}\{self.i+1}.mp3'))
        self.mp.setMedia(mc)
        self.mp.stop()
        self.mp.setVolume(50)
        self.mp.setPosition(0)
        self.mp.play()

    def on_btnNext_clicked(self):
        if self.num:
            self.i = self.num.pop()
            self.labelRus.setText(
                self.data["test"][self.i]["russian"])
        else:
            self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CheckWindow(1)
    desktop = QtWidgets.QApplication.desktop()
    x = (desktop.width() - window.width()) // 2
    y = (desktop.height() - window.height()) // 2
    window.move(x, y)
    window.show()
    sys.exit(app.exec_())
