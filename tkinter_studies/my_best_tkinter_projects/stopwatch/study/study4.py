"""
Try to add this feature:
When the screen is clicked, print "start"
When the screen is clicked again, print "stop"
If the screen is clicked twice, print "reset"

"""
import tkinter as tk


class App(tk.Tk):

    start = False

    def __init__(self):
        super().__init__()
        self.bind("<ButtonRelease-1>", self.start_stop)
        self.bind("<space>", self.start_stop)
        self.bind("<Double-ButtonRelease-1>", self.reset)
    
    
    def start_stop(self, event):
        if App.start:
            App.start = False
            print("Stop")
        else:
            App.start = True
            print("Start")
        
    
    def reset(self, event):
        print("Reset")


if __name__ == "__main__":
    root = App()
    root.mainloop()
