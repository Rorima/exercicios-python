"""
Review study1
"""
import tkinter as tk

window = tk.Tk()

frame = tk.Frame(window)
frame.pack()

tk.Button(frame, text="W", font=("Arial", 20), width=3).pack(side='top')
tk.Button(frame, text="A", font=("Arial", 20), width=3).pack(side='left')
tk.Button(frame, text="S", font=("Arial", 20), width=3).pack(side='left')
tk.Button(frame, text="D", font=("Arial", 20), width=3).pack(side='left')

window.mainloop()
