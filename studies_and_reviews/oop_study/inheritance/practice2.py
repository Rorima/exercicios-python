"""
Create a single inheritance class and use one method from a parent class.
"""


class Animal:
    
    def __init__(self, breed):
        self.breed = breed
        self.living = True
        
    def is_alive(self):
        if self.living:
            return f'{self.breed} is alive.'
        return f'{self.breed} is dead.'


class Dog(Animal):
    
    def __init__(self, breed, has_owner=False):
        Animal.__init__(self, breed)
        self.has_owner = has_owner


doggy = Dog('American Bulldog', has_owner=True)
print(doggy.is_alive())
