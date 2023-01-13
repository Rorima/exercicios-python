"""
Create two triangles with black outlines.
"""
import tkinter as tk

root = tk.Tk()

cnvs = tk.Canvas(root, width=500, height=500)
cnvs.pack()

frst_trngl = [250, 50, 350, 150, 150, 150]
scnd_trngl = [250, 450, 150, 350, 350, 350]

cnvs.create_polygon(frst_trngl, fill="white", outline="black", width=10)
cnvs.create_polygon(scnd_trngl, fill="white", outline="black", width=10)

root.mainloop()
