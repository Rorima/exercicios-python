import tkinter as tk
from tkinter import ttk

window = tk.Tk()

notebook = ttk.Notebook(window)

tab1 = tk.Frame(notebook)  # new frame for tab1
tab2 = tk.Frame(notebook)  # new frame for tab2

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="tab 2")
notebook.pack(expand=True, fill="both")  # It will expand to fill any space not otherwise used
                                         # Fill space on x and y axis

tk.Label(tab1, text="Hello! This is tab 1", width=50, height=25).pack()
tk.Label(tab2, text="Goodbye! This is tab 2", width=50, height=25).pack()

window.mainloop()
