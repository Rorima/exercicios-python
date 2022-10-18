"""
Review study1.py
"""
import tkinter as tk


def start_drag(event):
    widget = event.widget
    widget.startx = event.x
    widget.starty = event.y


def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startx + event.x
    y = widget.winfo_y() - widget.starty + event.y
    widget.place(x=x, y=y)


window = tk.Tk()
window.geometry("500x500")
window.resizable(False, False)

label1 = tk.Label(window, width=10, height=5, bg="red")
label1.place(x=50, y=50)
label1.bind("<Button-1>", start_drag)
label1.bind("<B1-Motion>", drag_motion)

label2 = tk.Label(window, width=10, height=5, bg="purple")
label2.place(x=100, y=100)
label2.bind("<Button-1>", start_drag)
label2.bind("<B1-Motion>", drag_motion)

window.mainloop()
