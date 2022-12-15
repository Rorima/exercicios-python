"""
DONE: Add a way to choose the tempo. Create a function for it. You can use the test_function.py to do that.


# Initilizing
pygame.mixer.init()

pygame.mixer.music.load("duck.mp3")
pygame.mixer.music.play(loops=0)
"""
import pygame
import time

pygame.mixer.init()


def play_metronome(bpm=60):
    sec = 60 / bpm
    while True:
        # Remember to change the path to the sound
        pygame.mixer.music.load("normal_knock.mp3")
        pygame.mixer.music.play(loops=0)
        time.sleep(sec)


if __name__ == "__main__":
    play_metronome(bpm=120)
