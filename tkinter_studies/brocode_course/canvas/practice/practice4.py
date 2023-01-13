"""
Create several circles inside each other.
"""
import tkinter as tk

root = tk.Tk()

cnvs = tk.Canvas(root, width=300, height=300)
cnvs.pack()

cnvs.create_oval(20, 20, 280, 280, fill="white", outline="black", width=3)
cnvs.create_oval(50, 50, 250, 250, fill="black")
cnvs.create_oval(80, 80, 220, 220, fill="white")
cnvs.create_oval(110, 110, 190, 190, fill="black")
cnvs.create_oval(140, 140, 160, 160, fill="white")

root.mainloop()
