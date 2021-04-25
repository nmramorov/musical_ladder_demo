from PyQt5 import QtWidgets
import sys
from collections import deque
from itertools import combinations, product
from random import randint


import design
from player import Player


songs = ['samples/ape_the_bass.wav',
         'samples/etman.wav',
         'samples/fruit_dance.wav',
         'samples/fruit_dance2.wav',
         'samples/on_the_street.wav']


def get_songs_and_buttons_combination():
    combs = product(range(1, 14), repeat=3)
    song_combs = {comb: songs[randint(0, 4)] for comb in combs}
    return song_combs


def check_deque(f):
    def inner(*args, **kwargs):
        obj, _ = args
        f(obj, **kwargs)
        print(obj.deq)
        if len(obj.deq) == 3:
            buttons = tuple(obj.deq.popleft() for i in range(3))
            print('Song will be played now')
            Player(obj.buttons_to_songs[buttons]).play_midi()
            obj.deq.clear()

    return inner


class DemoGui(design.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.deq = deque(maxlen=3)
        self.buttons_to_songs = get_songs_and_buttons_combination()
        for i in range(1, 14):
            button = getattr(self, f'pushButton_{i}')
            button.clicked.connect(self.button_clicked)

    @check_deque
    def button_clicked(self):
        sender = self.sender()
        pressed_button = sender.text()
        if int(pressed_button) not in self.deq:
            self.deq.append(int(sender.text()))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = DemoGui()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
