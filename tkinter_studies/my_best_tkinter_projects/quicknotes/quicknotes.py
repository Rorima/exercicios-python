from tkinter.filedialog import *
import tkinter as tk


def saveFile():
    new_file = asksaveasfile(mode = 'w', filetype = [('text files', '.txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()
    
def openFile():
    file = askopenfile(mode = 'r', filetype = [('text files', '*.txt')])
    if file is not None:
        content = file.read()
    try:
        entry.insert(INSERT, content)
    except UnboundLocalError:
        pass


canvas = tk.Tk()
canvas.iconbitmap('quicknotes.ico')
canvas.geometry("600x400")
canvas.title("Quicknote")
canvas.config(bg = "white")  # Background color
top = tk.Frame(canvas)
top.pack(padx = 10, pady = 5, anchor = 'nw')

b1 = tk.Button(canvas, text="Read", bg = "white", command = openFile)
b1.pack(in_ = top, side="left")

b2 = tk.Button(canvas, text="Save as", bg = "white", command = saveFile)
b2.pack(in_ = top, side="left")

entry = tk.Text(canvas,wrap = "word", bg = "#eaeaea", font = ("poppins", 15))
entry.pack(padx = 10, pady = 5, expand = True, fill = "both")

canvas.mainloop()
