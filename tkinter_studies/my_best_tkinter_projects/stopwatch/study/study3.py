import tkinter as tk
import time

start = False
first = ''
middle = ''
last = ''


def count():
    global start, first, last

    if start:
        start = False
        last = time.time()
        l.config(text=f"{last - first:.2f}")
    else:
        start = True
        first = time.time()
        middle_man()


def middle_man():
    global first, middle, last
    middle = time.time()
    if start:
        l.config(text=f"{middle - first:.2f}")
        root.after(98, middle_man)


root = tk.Tk()
root.geometry("300x300")

l = tk.Label(root)
l.pack(expand=True)

b1 = tk.Button(root, text="O", command=count)
b1.pack(ipady=30, ipadx=30, expand=True)



root.mainloop()
