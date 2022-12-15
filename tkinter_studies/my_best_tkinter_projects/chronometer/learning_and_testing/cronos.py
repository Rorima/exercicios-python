"""
This was an attempt to create a OO approach to
the stopwatch, but it didn't work, so I ditched it.
"""
# DITCH THIS

class Cronometro():
    
    def __init__(self, label, button):
        self.label = label
        self.button = button
        self.button.config(command=self.start)
        self.start_c = False

   
