import sys
import json
import random
# import os
from pathlib import Path


from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class CheckWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.lst = self.shuffle_list()
        # print(self.lst)
        self.i = self.lst.pop()

        self.mp = QMediaPlayer()
        self.setWindowTitle("Translate this phrase.")
        self.resize(350, 200)

        self.labelRus = QtWidgets.QLabel(
            self.i["quest"])
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

    def shuffle_list(self):
        pathes = []
        for file in Path('Cninese/json/').rglob('lesson*.json'):
            pathes.append(file.absolute())
        task = []
        for path in pathes:
            j = int(path.name.split(".")[0][-1])
            with open(path, encoding='utf-8') as f:
                data = json.load(f)
                # temp = {}
                for i in range(0, len(data['test'])-1):
                    temp = {}
                    temp["les"] = j
                    temp["quest"] = data['test'][i]['english']
                    temp["id"] = data['test'][i]['id']
                    task.append(temp)
        random.shuffle(task)
        return (task[:10])

    def on_btnAudio_clicked(self):
        mc = QMediaContent(
            QtCore.QUrl.fromLocalFile(
                f'Cninese\media\lesson{self.i["les"]}\{self.i["id"]}.mp3'))
        self.mp.setMedia(mc)
        self.mp.stop()
        self.mp.setVolume(50)
        self.mp.setPosition(0)
        self.mp.play()

    def on_btnNext_clicked(self):
        if self.lst:
            self.i = self.lst.pop()
            self.labelRus.setText(
                self.i["quest"])
        else:
            self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CheckWindow()
    desktop = QtWidgets.QApplication.desktop()
    x = (desktop.width() - window.width()) // 2
    y = (desktop.height() - window.height()) // 2
    window.move(x, y)
    window.show()
    sys.exit(app.exec_())
