"""
Create a scale that will serve as the sliding bar
to choose the BPM.
"""
import tkinter as tk


def show_number(value):
    pass


root = tk.Tk()
root.geometry("500x500")

scale = tk.Scale(
    root, from_=30, 
    to=240, 
    length=400, 
    orient="horizontal",
    tickinterval=210,
    sliderlength=80,
    command=show_number
)
scale.set(60)
scale.pack(expand=1)

root.mainloop()
