"""
Review
Create a Notebook with two tabs.
"""
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x300")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

frame1 = tk.Frame(notebook)
frame1.pack(expand=True, fill="both")
frame2 = tk.Frame(notebook)
frame2.pack(expand=True, fill="both")

notebook.add(frame1, text="Information")
notebook.add(frame2, text="Profile")

root.mainloop()
