"""
Recreate study1.py
"""
import tkinter as tk
import time

WIDTH = 500
HEIGHT = 500

x_velocity = 10
y_velocity = 12

root = tk.Tk()

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

space_photo = tk.PhotoImage(file="programas/study/animations/space.png")
space = canvas.create_image(0, 0, image=space_photo, anchor="nw")

alien_photo = tk.PhotoImage(file="programas/study/animations/alien.png")
alien = canvas.create_image(0, 0, image=alien_photo, anchor="nw")

alien_width = alien_photo.width()
alien_height = alien_photo.height()

while True:
    coordinates = canvas.coords(alien)
    
    if coordinates[0] >= (WIDTH - alien_width) or coordinates[0] < 0:
        x_velocity = - x_velocity

    if coordinates[1] >= (HEIGHT - alien_height) or coordinates[1] < 0:
        y_velocity = - y_velocity

    canvas.move(alien, x_velocity, y_velocity)
    root.update()
    time.sleep(0.1)

root.mainloop()
