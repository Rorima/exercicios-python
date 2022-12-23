"""
Create a Notebook with two tabs.

"""
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x300")

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

general_information_frame = tk.Frame(notebook, width=400, height=280)
general_information_frame.pack(fill="both", expand=True)
profile_frame = tk.Frame(notebook, width=400, height=280)
profile_frame.pack(fill="both", expand=True)

notebook.add(general_information_frame, text="General Information")
notebook.add(profile_frame, text="Profile")

root.mainloop()
