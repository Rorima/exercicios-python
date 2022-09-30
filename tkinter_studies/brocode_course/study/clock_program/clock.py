import tkinter as tk
import time


def update():
    time_string = time.strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = time.strftime("%A")
    day_label.config(text=day_string)

    date_string = time.strftime("%d/%m/%Y")
    date_label.config(text=date_string)

    window.after(1000, update)


window = tk.Tk()
window.config(background="black")

time_label = tk.Label(window, font=("Arial", 50), fg="#00FF00", bg="black")
time_label.pack()

day_label = tk.Label(window, font=("Arial", 25), fg="#00FF00", bg="black")
day_label.pack()

date_label = tk.Label(window, font=("Arial", 25), fg="#00FF00", bg="black")
date_label.pack()

update()

window.mainloop()
