import random
import os
import sys
from PyQt5 import QtWidgets, QtCore


class LessonList(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        vbox = QtWidgets.QVBoxLayout()

        self.radBtn_group = QtWidgets.QButtonGroup()
        self.btns = []
        for i in range(1, 15, 1):
            btn = QtWidgets.QRadioButton(f'lesson {i}')
            vbox.addWidget(btn)
            self.radBtn_group.addButton(btn)
            self.btns.append(btn)
        self.btns[0].setChecked(True)

        self.setLayout(vbox)
        # self.setGeometry(400, 200, 250, 175)

    def get_checked(self):
        n = self.btns.index(self.radBtn_group.checkedButton()) + 1
        return n


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LessonList()
    # window.setWindowTitle("Lesson1")
    window.show()
    sys.exit(app.exec_())
