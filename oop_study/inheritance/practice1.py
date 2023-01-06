"""
Create two classes that inherit from another class.
"""


class Person:
    
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
    
    def fullname(self):
        return f'{self.name} {self.last_name}'
    
    def greetings(self):
        return f"Hello! My name is {self.name} and I'm {self.age} years old."


class Medic(Person):
    
    def __init__(self, name, last_name, age, specialization):
        super().__init__(name, last_name, age)
        self.specialization = specialization
        
    def show_specialization(self):
        return f'My specialization is {self.specialization}.'


class Musician(Person):
    
    def __init__(self, name, last_name, age, instrument):
        super().__init__(name, last_name, age)
        self.instrument = instrument
    
    def show_instrument(self):
        return f'I play {self.instrument}.'


person1 = Person('John', 'Doe', 30)
medic1 = Medic('Ludwig', 'Wiglud', 55, 'General')
musician1 = Musician('Victor', 'Wooten', 57, 'Bass Guitar')

print(person1.greetings())
print(person1.fullname())
print()

print(medic1.greetings())
print(medic1.show_specialization())
print()

print(musician1.greetings())
print(musician1.show_instrument())
