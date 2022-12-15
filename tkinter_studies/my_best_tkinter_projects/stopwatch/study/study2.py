import tkinter as tk
import time

start = False
first = ''
last = ''


def count():
    global start, first, last

    if start:
        start = False
        last = time.time()
        l.config(text=last - first)
    else:
        start = True
        first = time.time()


root = tk.Tk()
root.geometry("300x300")

l = tk.Label(root)
l.pack(expand=True)

b1 = tk.Button(root, text="O", command=count)
b1.pack(ipady=30, ipadx=30, expand=True)



root.mainloop()
