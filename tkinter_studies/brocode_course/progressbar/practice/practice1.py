"""
Create a progressbar and fill it gradually.
"""
import tkinter as tk
from tkinter import ttk


def fill_bar():
    if bar['value'] < 100:
        bar.after(20, fill_bar)
        bar['value'] += 1


window = tk.Tk()
window.geometry("500x300")

percent = tk.IntVar()

bar = ttk.Progressbar(window, orient="horizontal", length=300)
bar.pack(expand=True)

b = tk.Button(window, text="Download", command=fill_bar)
b.pack(expand=True)

window.mainloop()
