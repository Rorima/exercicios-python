import tkinter as tk


def get_coords(event):
    widget = event.widget
    widget.startx = event.x
    widget.starty = event.y


def drag_widget(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startx + event.x
    y = widget.winfo_y() - widget.starty + event.y
    widget.place(x=x, y=y)


window = tk.Tk()
window.geometry("300x300")

label1 = tk.Label(window, width=10, height=5, bg="red")
label1.place(x=10, y=10)
label1.bind("<Button-1>", get_coords)
label1.bind("<B1-Motion>", drag_widget)

label2 = tk.Label(window, width=10, height=5, bg="blue")
label2.place(x=100, y=10)
label2.bind("<Button-1>", get_coords)
label2.bind("<B1-Motion>", drag_widget)

label3 = tk.Label(window, width=10, height=5, bg="green")
label3.place(x=200, y=10)
label3.bind("<Button-1>", get_coords)
label3.bind("<B1-Motion>", drag_widget)

window.mainloop()
