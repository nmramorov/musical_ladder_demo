from PyQt5 import QtWidgets
import sys
from collections import deque

import design


def check_deque(f):
    def inner(*args, **kwargs):
        obj, _ = args
        f(obj, **kwargs)
        print(obj.deq)
        if len(obj.deq) == 3:
            print('The song will be played')
            obj.deq.clear()

    return inner


class DemoGui(design.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.deq = deque(maxlen=3)
        for i in range(1, 14):
            button = getattr(self, f'pushButton_{i}')
            button.clicked.connect(self.button_clicked)

    @check_deque
    def button_clicked(self):
        sender = self.sender()
        pressed_button = sender.text()
        if pressed_button not in self.deq:
            self.deq.append(sender.text())


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = DemoGui()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
