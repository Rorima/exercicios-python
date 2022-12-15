"""
Displaying beat on the screen.
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


def controller():
    """Call two other functions and controll the time"""
    play_sound()
    count_beat()
    id = root.after(1000, controller)
    
    if not has_started:
        root.after_cancel(id)
        print("Finished")


def count_beat():
    """Count the beat and change number_label"""
    global counter
    print(counter, end="\r")
    number_label.config(text=counter)
    if counter >= 4:
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