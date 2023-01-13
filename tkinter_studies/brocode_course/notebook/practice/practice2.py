"""
Review
Create a Notebook with two tabs.
"""
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x500")

notebook = ttk.Notebook(root)
notebook.pack()

frame1 = tk.Frame(notebook, width=600, height=480)
frame2 = tk.Frame(notebook, width=600, height=480)

frame1.pack()
frame2.pack()

notebook.add(frame1, text="Information")
notebook.add(frame2, text="Profile")

root.mainloop()
