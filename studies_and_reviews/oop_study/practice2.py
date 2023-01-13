"""
Create a class with at least one class atribute.
"""

class Car: 
    counter = 0
    def __init__(self, name, year):
        Car.counter += 1
        self.id = Car.counter
        self.name = name
        self.year = year


red_race_car = Car('Lightning Macqueen', 2006)
hudson_hornet = Car('Doc Hudson', 1951)
porsche_carrera = Car('Sally Carrera', 2002)
print(f"Doc's ID: {hudson_hornet.id}.")
print(f"Total number of cars registered: {Car.counter}.")
