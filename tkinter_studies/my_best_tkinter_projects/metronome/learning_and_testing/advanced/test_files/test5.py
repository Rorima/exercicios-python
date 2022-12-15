"""
Changing the tempo internally and adding
time signatures.
"""
import tkinter as tk
import pygame

pygame.mixer.init()

has_started = False
counter = 1


def start_stop_metronome():
    """Start and stop the metronome and reset counter"""
    global has_started, counter
    has_started = not has_started
    if has_started:
        start_stop_button.config(text="stop")
        controller()
    else:
        counter = 1
        start_stop_button.config(text="start")


def controller(bpm=120):
    """Call two other functions and controll the time"""
    play_sound()
    count_beat(5)
    # Expression to turn bpm into milliseconds
    bpm = 60 / bpm * 1000
    id = root.after(int(bpm), controller)
    
    if not has_started:
        root.after_cancel(id)
        print("Finished")


def count_beat(time_signature=4):
    """Count the beat and change number_label"""
    global counter
    print(counter, end="\r")
    number_label.config(text=counter)
    if counter >= time_signature:
        counter = 1
    else:
        counter += 1


def play_sound():
    """Play the knock sound"""
    global counter
    if counter == 1:
        pygame.mixer.music.load("accent_knock.mp3")
        pygame.mixer.music.play(loops=0)
    else:
        pygame.mixer.music.load("normal_knock.mp3")
        pygame.mixer.music.play(loops=0)


root = tk.Tk()
root.geometry("500x600")

number_label = tk.Label(
    root,
    font=("times new romans", 60),
    text=counter
)
number_label.pack(expand=True)

start_stop_button = tk.Button(
    root, 
    font=("times new romans", 40),
    text="start", 
    command=start_stop_metronome)
start_stop_button.pack(expand=True)

root.mainloop()