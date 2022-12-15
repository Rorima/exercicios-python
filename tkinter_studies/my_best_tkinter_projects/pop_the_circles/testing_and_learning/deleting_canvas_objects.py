import tkinter as tk


def del_circle():
    c.delete(ball)


window = tk.Tk()

c = tk.Canvas(window, width=500, height=500)
c.pack()

ball = c.create_oval(0, 0, 100, 100)

b = tk.Button(window, command=del_circle, text="del", padx=50, pady=50)
b.pack()

window.mainloop()
