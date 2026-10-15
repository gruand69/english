import os
import json
import sys
from PyQt5 import QtCore, QtWidgets

from lesson_list import LessonList
from central_widget import MyWindow
from check_word import CheckWindow


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chinese Practice")
        self.resize(750, 500)

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QtWidgets.QGridLayout()
        self.central_widget.setLayout(self.layout)

        self.sub_win1 = LessonList()
        self.layout.addWidget(self.sub_win1, 0, 0)

        with open('Cninese_rus\json\lesson1.json', encoding='utf-8') as f:
            data = json.load(f)
        self.sub_win2 = MyWindow(data['test'])
        self.layout.addWidget(self.sub_win2, 0, 1)

        btnDlg = QtWidgets.QPushButton("&Dialog")
        btnEx = QtWidgets.QPushButton("&Exerсize")

        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(btnDlg)
        hbox.addWidget(btnEx)

        self.layout.addLayout(hbox, 1, 0, 1, 0)

        btnDlg.clicked.connect(self.on_btnDlg)

        btnEx.clicked.connect(self.on_btnEx)

    def on_btnDlg(self):
        n = self.sub_win1.get_checked()
        try:
            with open(f'Cninese_rus\json\lesson{n}.json', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            return
        # 1. Координаты целевой ячейки
        row, column = 0, 1

        # 2. Ищем старый элемент в этой позиции
        item = self.layout.itemAtPosition(row, column)

        if item is not None:
            old_widget = item.widget()
            if old_widget:
                # 3. Удаляем из макета и уничтожаем виджет
                self.layout.removeWidget(old_widget)
                old_widget.deleteLater()

        # 4. Создаем новый виджет
        # new_label = QLabel("✨ НОВЫЙ ТЕКСТ! ✨")

        # 5. Вставляем его на то же место
        # self.layout.addWidget(new_label, row, column)
        self.sub_win2 = MyWindow(data['test'], n)
        self.layout.addWidget(self.sub_win2, row, column)

    # def open_file(self, l, k):
    #     dirname = os.path.dirname(__file__)
    #     with open(os.path.join(
    #          dirname, f'../json/lesson{l}/ex{k}.json'), encoding='utf-8') as f:
    #         data = json.load(f)
    #     return data

    def on_btnEx(self):
        # pass
        n = self.sub_win1.get_checked()
        # m = self.sub_win3.get_checked()
        print(n)
        # # dirname = os.path.dirname(__file__)

        try:
            window = CheckWindow(n)
        except FileNotFoundError:
            pass
        # desktop = QtWidgets.QApplication.desktop()
        # x = (desktop.width() - window.width()) // 2
        # y = (desktop.height() - window.height()) // 2
        # window.move(x, y)
        # window.show()

        #     if m == 1:
        #         data = self.open_file(n, m)
        #         sign = (
        #             "Choose the most appropriate short answer " +
        #             "for each question.")
        #         window = Ex1(data['test'], sign)
        #     elif m == 2:
        #         data = self.open_file(n, m)
        #         sign = ("Match each remark in the first column with an " +
        #                 'appropriate response from the second column. ' +
        #                 'Note: Some remarks have more than one appropriate ' +
        #                 'response.')
        #         window = Ex2(data['test'], sign)
        #     elif m == 3:
        #         data = self.open_file(n, m)
        #         sign = (
        #             'Write a tag answer for each of the following questions (Yes.. . No.. .)')
        #         window = Ex3(data['test'], sign)
        #         window.setWindowTitle("Ex3")
        #     elif m == 4:
        #         data = self.open_file(n, m)
        #         window = Ex4(data['test'])
        #         window.setWindowTitle("Ex4")
        #     elif m == 5:
        #         data = self.open_file(n, m)
        #         sign = ('Match the words or expressions in the first column ' +
        #             'with words or expressions in the second column ' +
        #             'that have a similar meaning. Note: There may be ' +
        #             'more than one match for each expression.')
        #         window = Ex2(data['test'], sign)
        #         window.setWindowTitle("Ex5")
        #     if m == 6:
        #         data = self.open_file(n, m)
        #         sign = ("Circle the most appropriate response to each remark.")
        #         window = Ex1(data['test'], sign)
        #     elif m == 7:
        #         data = self.open_file(n, m)
        #         sign = (
        #             'Write a remark or question for each of the following responses.')
        #         window = Ex7(data['test'], sign)
        #     elif m == 8:
        #         data = self.open_file(n, m)
        #         window = Ex8(data['test'])
        #     else:
        #         pass
        # elif n == 2:
        #     if m == 1:
        #         data = self.open_file(n, m)
        #         sign = (
        #             'Write a question using like for each of the following answers.')
        #         window = Ex7(data['test'], sign)
        #     if m == 2:
        #         data = self.open_file(n, m)
        #         sign = (
        #             'Fill in each blank with the correct form of say, speak, or tell, as appropriate.')
        #         window = Ex9(data['test'], sign)
        #     elif m == 3:
        #         data = self.open_file(n, m)
        #         sign = (
        #             'Change each question to a statement beginning with "Tell me . . . "')
        #         window = Ex3(data['test'], sign)
        #         window.setWindowTitle("Ex3")
        #     elif m == 4:
        #         data = self.open_file(n, m)
        #         sign = ('Match the words or expressions in the first column ' +
        #             'with words or expressions in the second column ' +
        #             'that have a similar meaning. Note: There may be ' +
        #             'more than one match for each expression.')
        #         window = Ex2(data['test'], sign)
        #         window.setWindowTitle("Ex4")
        #     if m == 5:
        #         data = self.open_file(n, m)
        #         sign = (
        #                 "Choose the word or expression that best completes " +
        #                 "each of the following sentences.")
        #         window = Ex1(data['test'], sign)
        #     if m == 6:
        #         data = self.open_file(n, m)
        #         sign = ("Choose  the most appropriate response " +
        #                 "to each of the following questions or " +
        #                 "statements.")
        #         window = Ex1(data['test'], sign)
        # else:
        #     pass
        try:
            # 1. Координаты целевой ячейки
            row, column = 0, 1

            # 2. Ищем старый элемент в этой позиции
            item = self.layout.itemAtPosition(row, column)

            if item is not None:
                old_widget = item.widget()
                if old_widget:
                    # 3. Удаляем из макета и уничтожаем виджет
                    self.layout.removeWidget(old_widget)
                    old_widget.deleteLater()

        # 4. Создаем новый виджет
        # new_label = QLabel("✨ НОВЫЙ ТЕКСТ! ✨")

        # 5. Вставляем его на то же место
        # self.layout.addWidget(new_label, row, column)
        # self.sub_win2 = MyWindow(data['test'], n)
            self.layout.addWidget(window, row, column)
        except UnboundLocalError:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    # window.setWindowTitle("Practice Makes Perfect English Conversation")
    # window.resize(750, 500)
    desktop = QtWidgets.QApplication.desktop()
    x = (desktop.width() - window.width()) // 2
    y = (desktop.height() - window.height()) // 2
    window.move(x, y)
    window.show()
    sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton, QVBoxLayout
# from PyQt5.QtCore import Qt

# class SubWindow(QWidget):
#     """Класс для создания внутреннего окна без рамки"""
#     def __init__(self, title, color):
#         super().__init__()
#         # Применяем флаг окна без рамки
#         self.setWindowFlags(Qt.FramelessWindowHint)
#         self.setStyleSheet(f"background-color: {color}; border: 2px solid black;")
        
#         # Добавляем внутренние элементы (заголовок и кнопку)
#         layout = QVBoxLayout()
#         label = QLabel(title)
#         label.setAlignment(Qt.AlignCenter)
#         btn = QPushButton("Закрыть")
#         btn.clicked.connect(self.close)
        
#         layout.addWidget(label)
#         layout.addWidget(btn)
#         self.setLayout(layout)

# class MainWindow(QMainWindow):
#     """Главное окно приложения"""
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Главное окно")
#         self.setGeometry(100, 100, 600, 400)

#         # Центральный виджет главного окна
#         self.central_widget = QWidget()
#         self.setCentralWidget(self.central_widget)
        
#         # Сетка для удобного размещения внутренних окон
#         layout = QGridLayout()
#         self.central_widget.setLayout(layout)
        
#         # Создаем и добавляем Первое окно без рамки
#         self.sub_win1 = SubWindow("Окно 1", "lightgray")
#         layout.addWidget(self.sub_win1, 0, 0)
        
#         # Создаем и добавляем Второе окно без рамки
#         self.sub_win2 = SubWindow("Окно 2", "lightblue")
#         layout.addWidget(self.sub_win2, 0, 1)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
