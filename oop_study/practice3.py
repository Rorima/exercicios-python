"""
Create a class that infects people with happiness and changes their behaviour.

"""
from random import choice


class HappyInfection:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greetings(self):
        print(f'Hello, {self.name}! Welcome to HAPPYLAND!')
    
    def tickle(self):
        print('Tickle, tickle, tickle!')
    
    def happify(self):
        self.name = choice(('Joy', 'Bliss', 'Laughter', 'Delight'))
        print(f'Now your name is {self.name}!')
        if self.age > 20:
            self.age = 20
            print(f'And your new age is {self.age}!')


person = HappyInfection('Dohn Joe', 99)
person.greetings()
person.tickle()
person.happify()
print()
human = HappyInfection('Nhoj Eod', -99)
human.greetings()
human.tickle()
human.happify()
