"""
Create a metronome where the user can choose the time
signature and the BPM.
"""
import pygame
import time

pygame.mixer.init()


def play_metronome(bpm=60, time_signature=4):
    sec = 60 / bpm
    beat = 1
    while True:
        if beat == 1:
            pygame.mixer.music.load("accent_knock.mp3")
            pygame.mixer.music.play(loops=0)
        else:
            pygame.mixer.music.load("normal_knock.mp3")
            pygame.mixer.music.play(loops=0)
        
        beat += 1
        if beat > time_signature:
            beat = 1
        
        time.sleep(sec)


play_metronome(bpm=150, time_signature=6)
