from PyQt5 import QtWidgets
import sys
from collections import deque


import design


def check_deque(f):
    def inner(*args, **kwargs):
        obj, _ = args
        print(obj)
        if len(obj.deq) == 3:
            print('the song will be played')
        else:
            f(obj, **kwargs)

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
        print(sender.text() + ' was pressed')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = DemoGui()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
