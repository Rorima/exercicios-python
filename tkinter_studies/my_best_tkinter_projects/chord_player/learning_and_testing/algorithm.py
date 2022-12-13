"""
Make a program where the chosen chord is played for 
2 seconds.

pygame.mixer.music.load("duck.mp3")
pygame.mixer.music.play(loops=0)
"""
import time
import pygame

pygame.mixer.init()


def play_chord(chord):
    pygame.mixer.music.load(f"{chord}.mp3")
    pygame.mixer.music.play(loops=0)

    time.sleep(2)

    pygame.mixer.music.load("nothing.mp3")
    pygame.mixer.music.play(loops=0)


play_chord("C major")
