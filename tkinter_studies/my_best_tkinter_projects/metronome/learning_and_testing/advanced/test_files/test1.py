"""
Implementing a simple GUI and the algorithm.
"""
import tkinter as tk
import pygame

pygame.mixer.init()

a = False
c = 0


def reverse():
    global a
    a = not a
    if a:
        count()


def count():
    global c
    c += 1
    id = root.after(1000, count)
    print(c)
    play_sound()
    if not a:
        root.after_cancel(id)
        print("Finished")


def play_sound():
    pygame.mixer.music.load("normal_knock.mp3")
    pygame.mixer.music.play(loops=0)



root = tk.Tk()

b = tk.Button(root, command=reverse)
b.pack(fill="both")

root.mainloop()