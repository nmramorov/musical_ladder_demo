from players import playsound_player


class Player:
    def __init__(self, samples_path):
        self.players = {'playsound': playsound_player.play}
        self.samples_path = samples_path

    def play_midi(self):
        self.players['playsound'](self.samples_path)
