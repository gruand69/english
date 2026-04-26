# Необходимо включить "Lan Control" в приложении Mi Home/Yeelight
# Установите библиотеку pip install yeelight

from yeelight import Bulb, BulbException
import time

bulb_ip = "192.168.1.50"

try:
    bulb = Bulb(bulb_ip)

    # 1. Включить лампу
    print("Включаю лампу")
    bulb.turn_on()
    time.sleep(2)

    # 2. Установить яркость (1-100)
    print("Устанавливаю яркость 50 %")
    bulb.set_brightness(50)
    time.sleep(2)

    # 3. Изменить цвет (RGB: 0-255)
    print("Включаю синий цвет...")
    bulb.set_rgb(0, 0, 255)
    time.sleep(2)

    # 4. Установить цветовую температуру(2700К - 6500К)
    print("Включаю  теплый белый свет...")
    bulb.set_color_temp(2700)
    time.sleep(2)

    # 5. Выключить лампу
    print("Выключаю лампу")
    bulb.turn_off()
except BulbException as e:
    print(f"Ошибка управления лампой: {e}")

# Локальное управление (LAN Control): обязательно включите эту опцию
# в настройках лампы в приложении.
# Автономный поиск: Можно использовать from yeelight import discover_bulbs,
# чтобы найти адреса ламп в сети автоматически.
# Эффекты: Поддерживаются переходы с использованием параметра effect="smooth",
# например, bulb.set_rgb(255, 0, 0, effect="smooth", duration=1000)   

import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont, QTextCharFormat, QColor, QTextCursor


class DiffWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.label_quest = QtWidgets.QLabel("Button 1")
        self.label_quest.setWordWrap(True)
        self.label_quest.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_quest.setFont(QFont('Times', 14))
        # self.label_quest.setStyleSheet(
        #     "border: 1px dashed black; border-radius: 10px;")

        self.btnOn = QtWidgets.QPushButton("&On")
        self.btnOff = QtWidgets.QPushButton("O&ff")
        self.vboxLamp1 = QtWidgets.QHBoxLayout()
        self.vboxLamp1.addWidget(self.btnOn)
        self.vboxLamp1.addWidget(self.btnOff)

        # self.vboxNavBtn = QtWidgets.QHBoxLayout()

        # self.vboxNavBtn.addWidget(self.btnQuit)

        self.vboxVert = QtWidgets.QVBoxLayout()
        self.vboxVert.addWidget(self.label_quest)
        self.vboxVert.addLayout(self.vboxLamp1)

        self.setLayout(self.vboxVert)
        self.setGeometry(400, 200, 600, 300)

        # self.btnQuit.clicked.connect(QtWidgets.qApp.quit)
        self.btnOn.clicked.connect(self.On_button)
        self.btnOff.clicked.connect(self.Off_button)

    # def btnClosed(self):
    #     self.close()

    def On_button(self):
        pass

    def Off_button(self):
        pass

# class CheckWindow(QtWidgets.QDialog):
#     def __init__(self, question, response, parent=None):
#         self.question = question
#         self.response = response
#         QtWidgets.QWidget.__init__(self, parent)

#         self.labelRus = QtWidgets.QLabel(self.question)
#         self.labelRus.setWordWrap(True)
#         self.labelRus.setAlignment(
#             QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
#         self.labelRus.setFont(QFont('Times', 14))
#         self.labelRus.setStyleSheet(
#             "border: 1px dashed black; border-radius: 10px;")

#         self.textEdit = QtWidgets.QPlainTextEdit()
#         # self.labelEng.size()
#         # self.labelEng.setWordWrap(True)
#         # self.labelEng.setAlignment(
#         #     QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
#         self.textEdit.setFont(QFont('Times', 14))
#         self.textEdit.setStyleSheet(
#             "border: 1px dashed black; border-radius: 10px;")

#         self.btnCheck = QtWidgets.QPushButton("Check")
#         self.btnQuit = QtWidgets.QPushButton("&Close the window")

#         self.vboxLabel = QtWidgets.QVBoxLayout()
#         self.vboxLabel.addWidget(self.labelRus)
#         self.vboxLabel.addWidget(self.textEdit)

#         self.vboxNavBtn = QtWidgets.QHBoxLayout()
#         self.vboxNavBtn.addWidget(self.btnCheck)
#         self.vboxNavBtn.addWidget(self.btnQuit)

#         self.vboxVert = QtWidgets.QVBoxLayout()
#         self.vboxVert.addLayout(self.vboxLabel)
#         self.vboxVert.addLayout(self.vboxNavBtn)

#         self.setLayout(self.vboxVert)
#         self.setGeometry(400, 200, 600, 300)

#         # self.btnQuit.clicked.connect(QtWidgets.qApp.quit)
#         self.btnQuit.clicked.connect(self.btnClosed)
#         self.btnCheck.clicked.connect(self.on_btnCheck_clicked)

#     def on_btnCheck_clicked(self):
#         answer = self.textEdit.toPlainText()
#         if answer == self.response:
#             QtWidgets.QMessageBox.information(self, 'Mesage', 'Excellent!')
#         # else:
#         elif answer:
#             # self.textEdit.clear()
#             dialog = DiffWindow(self.response,
#                                 self.textEdit.toPlainText())
#             self.textEdit.clear()
#             dialog.exec_()
#             # QtWidgets.QMessageBox.information(self, 'Mesage', "You're wrong!")
#             # for i in range(len(self.response)-1):
#             #     if self.response[i] != answer[i]:
#             #         QtWidgets.QMessageBox.information(
#             #             self, 'Mesage', self.response[i])
#             #         break
#         else:
#             QtWidgets.QMessageBox.information(self, 'Mesage', 'Print something, please!')

    def btnClosed(self):
        self.close()


if __name__ == "__main__":
    dirname = os.path.dirname(__file__)
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = DiffWindow()
    window.setWindowTitle("Yeelight operating")
    # window.resize(300, 70)
    window.show()
    sys.exit(app.exec_())
