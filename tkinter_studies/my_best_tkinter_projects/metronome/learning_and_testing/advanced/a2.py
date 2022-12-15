"""
Algorithm to figure out how the after method works.
"""
import tkinter as tk

c = 0


def count():
    a = root.after(1000, count)
    global c
    print(c)
    c += 1
    if c >= 5:
        root.after_cancel(a)
        print("Finished")


root = tk.Tk()

b = tk.Button(root, command=count)
b.pack(fill="both")

root.mainloop()
