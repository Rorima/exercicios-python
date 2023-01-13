"""
Create a submenu for the file menu
"""
import tkinter as tk

window = tk.Tk()
menubar = tk.Menu(window)
window.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)

file_menu.add_command(label="New")
file_menu.add_separator()

sub_menu_preferences = tk.Menu(file_menu, tearoff=False)
sub_menu_preferences.add_command(label="Change Theme")
sub_menu_preferences.add_command(label="Change Language")

file_menu.add_cascade(label="Preferences", menu=sub_menu_preferences)

menubar.add_cascade(label="File", menu=file_menu)

window.mainloop()
