import tkinter as tk


def create_dependent():
    new_window = tk.Toplevel()
    new_window.mainloop()


def create_independent():
    new_window = tk.Tk()
    new_window.geometry("300x300")
    tk.Button(new_window, text="Kill previous window", command=old_window.destroy).pack()
    new_window.mainloop()


old_window = tk.Tk()
old_window.geometry("300x300")

tk.Button(old_window, text="Create new window", command=create_dependent).pack()
tk.Button(old_window, text="Create Tk independent window", command=create_independent).pack()
old_window.mainloop()
