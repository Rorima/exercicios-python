import pygame
from random import randint

pygame.mixer.init()

class Ball:
    def __init__(self, canvas, score_label, highest_score_label):
        self.canvas = canvas
        self.check = False
        self.score_label = score_label
        self.score = 0
        self.highest_score_label = highest_score_label
        self.highest_score = 0
        
    def decide_color(self):
        """This function decides if the circle will be red or green"""
        red_chance = randint(1, 10)
        if red_chance == 1:
            self.random_circles("#CC0000")
            self.color = "red"
        else:
            self.random_circles("#4eea13")
            self.color = "green"

    def random_circles(self, color):
        """This function creates the circles"""
        self.x = randint(0, 400)
        self.y = randint(0, 400)
        self.diameter = 100

        self.delete_circle()

        self.ball = self.canvas.create_oval(self.x, self.y, self.x+self.diameter, self.y+self.diameter, fill=color)
    
    def delete_circle(self):
        if self.check:
            self.canvas.delete(self.ball)
        
        self.check = True

    def circle_click(self, event):
        x = event.x
        y = event.y
        if self.color == "green":
            # If the user clicks inside the green circle, he wins
            if (x > self.x) and (x < self.x+self.diameter) and (y > self.y) and (y < self.y+self.diameter):
                self.add_score()
                self.pop_sound()
                self.decide_color()
            else:
                # If the user clicks outisde the green circle, he loses
                self.duck_sound()
                self.reset_score()
        else:
            # If the user clicks inside the red circle, he loses
            if (x > self.x) and (x < self.x+self.diameter) and (y > self.y) and (y < self.y+self.diameter):
                self.reset_score()
                self.duck_sound()
            else:
                # If the user clicks outside the red circle, he wins
                self.add_score()
                self.pop_sound()
                self.decide_color()

    def add_score(self):
        self.score += 1
        self.score_label.config(text=self.score)
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.highest_score_label.config(text=f"Highest: {self.highest_score}")
        
    def reset_score(self):
        self.score = 0
        self.score_label.config(text=self.score)

    def pop_sound(self):
        pygame.mixer.music.load("pop.mp3")
        pygame.mixer.music.play(loops=0)
    
    def duck_sound(self):
        pygame.mixer.music.load("duck.mp3")
        pygame.mixer.music.play(loops=0)

#GaD