from tkinter import *
from tkinter.ttk import *
import time


def start():
    tasks = 10
    x = 0
    while (x < tasks):
        time.sleep(1)
        bar["value"] += 10
        x += 1
        percent.set(str(int((x/tasks)*100))+"%")
        text.set(str(x)+"/"+str(tasks)+" tasks completed.")
        window.update_idletasks()


window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient='horizontal', length=300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
taxtLabel = Label(window, textvariable=text).pack()

button = Button(window, text="download", command=start).pack()

window.mainloop()
