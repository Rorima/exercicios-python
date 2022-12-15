"""
I successfully figured out a way to start and stop using the
after method.
"""
import tkinter as tk

a = False
c = 0


def reverse():
    global a
    a = not a
    if a:
        count()


def count():
    global c
    c += 1
    id = root.after(1000, count)
    print(c)
    if not a:
        root.after_cancel(id)
        print("Finished")


root = tk.Tk()

b = tk.Button(root, command=reverse)
b.pack(fill="both")

root.mainloop()
