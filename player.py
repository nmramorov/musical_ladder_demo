from typing import TypeVar, List
from pathlib import Path
from midi2audio import FluidSynth
import os
import pygame


# T = TypeVar('T')
#
# PATH_TO_SAMPLES = Path('samples')
#
#
# def get_midi_file_names(path: T):
#     file_names = [path / f for f in os.listdir(path) if os.path.isfile(path / f)]
#     return file_names
#
#
# def convert_to_wav(files: List):
#     fs = FluidSynth()
#     for _file in files:
#         filename = _file.name
#         filename = filename.split('.')[0] + '.wav'
#         final_file = PATH_TO_SAMPLES / 'wavs' / filename
#         if final_file.exists:
#             continue
#         fs.midi_to_audio(_file,  final_file)
#
#
# files = get_midi_file_names(PATH_TO_SAMPLES)
# convert_to_wav(files)

# pygame.init()
#pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
file = 'samples/a3.mid'

#os.system(f'timidity {file} -Ow -o samples/wavs/a3.wav')
pygame.init()
pygame.mixer.init()

sound = pygame.mixer.Sound('samples/d5.mid')

sound.play()

#sound1 = pg.mixer.Sound('boom.wav')
while pygame.mixer.get_busy():
    pygame.time.delay(10)
