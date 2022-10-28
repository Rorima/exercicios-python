import tkinter as tk
from tkinter import filedialog


def save_file():
    file = filedialog.asksaveasfile(defaultextension=".txt", 
                                    filetypes=[("text file", ".txt"),
                                               ("HTML file", ".html"),
                                               ("readme file", ".md"),
                                               ("all files", ".*")]
    )
    if file is None:
        return
    filetext = str(text_area.get("1.0", "end"))
    file.write(filetext)
    file.close()


window = tk.Tk()

save_button = tk.Button(
    window,
    text="Save",
    command=save_file
)
save_button.pack()

text_area = tk.Text(window)
text_area.pack()

window.mainloop()
