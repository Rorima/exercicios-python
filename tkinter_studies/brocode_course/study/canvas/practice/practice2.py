"""
Create three squares on a canvas.
"""
import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

canvas.create_rectangle(50, 450, 150, 350, fill="white", outline="purple", width=10)
canvas.create_rectangle(450, 450, 350, 350, fill="black", outline="lightgreen", width=10)
canvas.create_rectangle(200, 50, 300, 150, fill="gray", outline="lightblue", width=10)

root.mainloop()
