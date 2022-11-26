import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from PyQt5.QtGui import QPainter, QColor

from random import randint

from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)

        self.connects()

    def connects(self):
        self.pushButton.clicked.connect(self.repaint)

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw(qp)
        # Завершаем рисование
        qp.end()

    def draw(self, qp):
        # Задаем кисть
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))

        def get_args_for_ellipse():
            x1, y1 = randint(50, 300), randint(100, 300)
            radius = randint(10, 200)
            return x1, y1, radius, radius

        x1, y1, radius, radius = get_args_for_ellipse()

        qp.drawEllipse(x1, y1, radius, radius)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())