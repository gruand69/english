import sys
import json
import random
import os

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class CheckWindow(QtWidgets.QWidget):

    def __init__(self, les):
        super().__init__()
        self.les = les
        self.num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(self.num)
        # print(self.num)
        self.i = self.num.pop()
        # print(self.i)
        # print(self.num)self.score = 0
        self.score = 0
        self.flag = True
        
        self.mp = QMediaPlayer()
        self.setWindowTitle("Choose correct word")
        self.resize(350, 200)

        self.vbox = QtWidgets.QVBoxLayout()
        self.radBtn_group = QtWidgets.QButtonGroup()
        self.btns = []
        self.radBtn = QtWidgets.QVBoxLayout()
        self.lst = self.shuffle_list(f'Cninese\json\lesson{self.les}.json')
        for i in range(0, 10, 1):
            btn = QtWidgets.QRadioButton(self.lst[i][1])
            self.radBtn.addWidget(btn)
            self.radBtn_group.addButton(btn)
            self.btns.append(btn)
        self.vbox.addLayout(self.radBtn)

        self.btnCheck = QtWidgets.QPushButton("&Check")
        self.btnAudio = QtWidgets.QPushButton("&Audio")
        hbox1 = QtWidgets.QHBoxLayout()
        hbox1.addWidget(self.btnCheck)
        hbox1.addWidget(self.btnAudio)
        self.vbox.addLayout(hbox1)

        # self.btnNext = QtWidgets.QPushButton("&Next >>")
        # self.vbox.addWidget(self.btnNext)

        self.setLayout(self.vbox)

        self.btnAudio.clicked.connect(self.on_btnAudio_clicked)
        self.btnCheck.clicked.connect(self.on_btnCheck_clicked)
        # self.btnNext.clicked.connect(self.on_btnNext_clicked)
        self.on_btnAudio_clicked()

    def on_btnAudio_clicked(self):
        mc = QMediaContent(
            QtCore.QUrl.fromLocalFile(
                f'Cninese\media\lesson{self.les}\{self.i+1}.mp3'))
        self.mp.setMedia(mc)
        self.mp.stop()
        self.mp.setVolume(50)
        self.mp.setPosition(0)
        self.mp.play()

    def shuffle_list(self, way):
        with open(way, encoding='utf-8') as f:
            data = json.load(f)
        lst = []
        for item in data['test']:
            i = []
            i.append(item['id'])
            i.append(item['english'])
            lst.append(i)
        random.shuffle(lst)
        return lst

    def on_btnCheck_clicked(self):
        n = self.radBtn_group.checkedButton().text()
        # print(n)
        # print(self.lst)
        for item in self.lst:
            if item[1] == n:
                m = item[0]
                break
        if m - 1 == self.i:
            if self.flag:
                self.score += 1
            QtWidgets.QMessageBox.information(self, 'Message', 'Excellent!')
            self.on_btnNext_clicked()
            self.on_btnAudio_clicked()
        else:
            self.flag = False
            QtWidgets.QMessageBox.information(
                self, 'Message', 'Not exactly, Try again!')

    def on_btnNext_clicked(self):
        if self.num:
            self.i = self.num.pop()
            # print(self.i)
            # print(self.num)
            self.flag = True
            
            for btn in self.btns:
                self.radBtn.removeWidget(btn)
            random.shuffle(self.btns)
            for btn in self.btns:
                self.radBtn.addWidget(btn)
        else:
            QtWidgets.QMessageBox.information(
                self, 'Mesage', f'Your result: {self.score} from 10.')
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
