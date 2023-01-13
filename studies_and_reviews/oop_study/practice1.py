"""
Create your own class with the instance attribute of 'name'.
"""

class Person:
    def __init__(self, name):
        self.name = name


p1 = Person('Flash Godspeed')
p2 = Person('Shrek Greenland')
p3 = Person('Hulk Shrekson')

print(p1.name)
print(p2.name)
print(p3.name)
