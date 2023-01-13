"""
Review the previous exercise
"""

import tkinter as tk
from tkinter import ttk


def fill_bar():
    if bar["value"] < 100:
        bar["value"] += 1
        bar.after(15, fill_bar)
        percent.set(str(int(bar["value"])) + "%")


root = tk.Tk()
root.geometry("300x300")

percent = tk.StringVar()

bar = ttk.Progressbar(root, orient="horizontal", length=200)
bar.pack(expand=True)

percent_label = tk.Label(root, textvariable=percent)
percent_label.pack()

b = tk.Button(root, text="Fill Bar", command=fill_bar)
b.pack(expand=True)

root.mainloop()
