"""
Create a notepad with a menubar containig a file option, and set
"open" and "save as" as options.
"""
import tkinter as tk
from tkinter import filedialog


def open_file():

    text_area.delete("1.0", "end")

    file_path = filedialog.askopenfilename(
        title="Open File",
        defaultextension="*.txt",
        filetypes=(("Text Files", "*.txt"), ("All files", "*.*"))
    )
    
    if file_path == "":
        return
    else:
        f = open(file_path, 'r')
        text_area.insert("1.0", f.read())
        f.close()


def save_as_file():
    f = filedialog.asksaveasfile(
        title="Save File",
        defaultextension=".txt",
        filetypes=(("Text Files", ".txt"), ("All Files", ".*"))
    )
    if f == None:
        return
    else:
        f.write(text_area.get("1.0", "end"))
        f.close()


window = tk.Tk()
window.title("My Notepad")
window.geometry("600x500")
window.resizable(False, False)

menubar = tk.Menu(window)
window.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save As", command=save_as_file)

menubar.add_cascade(label="File", menu=file_menu)

text_area = tk.Text(
    window, 
    font=("Arial", 15),
    padx=20,
    pady=20)
text_area.pack()

window.mainloop()
