import pygame
import tkinter as tk

pygame.mixer.init()


def play():
    pygame.mixer.music.load("duck.mp3")
    pygame.mixer.music.play(loops=0)


window = tk.Tk()
window.geometry("500x500")

b = tk.Button(window, text="Quack", font=("times new roman", 50, "bold"), command=play)
b.pack(expand=True)

window.mainloop()
