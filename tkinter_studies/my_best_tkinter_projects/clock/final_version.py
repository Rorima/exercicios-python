import tkinter as tk
import time


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Clock")
        self.geometry("400x150")
        self.config(bg="#020202")

        self.center_label = tk.Label(
            self, 
            bg="#020202",
            font=("", 60),
            fg="#1ba400"
        )
        self.center_label.pack(expand=True)

        self.show_time()


    def show_time(self):
        ct = time.strftime("%H:%M:%S", time.localtime())
        self.center_label.config(text=f"{ct}")
        self.after(200, self.show_time)


if __name__ == "__main__":
    clock = App()
    clock.mainloop()
