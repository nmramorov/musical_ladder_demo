from player import Player
from os import listdir
from pathlib import Path
from threading import Thread


notes = Path('samples/notes')


class StepsListener:
    def __init__(self):
        self.player = Player(notes)
        self.tracks = {i + 1: Thread(target=track, name=f'Note {track}') for i, track in enumerate(sorted(listdir(notes)))}

    def 




