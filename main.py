import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic  # Импортируем uic
import random


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MyUi.ui', self)  # Загружаем дизайн
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        d = random.randint(0, 170)
        qp.drawEllipse(0, 0, d, d)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
