"""
Use magic methods.
"""


class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f"Person('{self.first_name}', '{self.last_name}', {self.age})"

    def __str__(self):
        return f'First name: {self.first_name}; last name: {self.last_name}; age: {self.age}'

    def __len__(self):
        return self.age

    def __add__(self, other):
        return f'{self.first_name} {other.first_name}'

    def __mul__(self, other):
        if isinstance(other, int):
            string = ''
            for _ in range(other):
                string += self.first_name + ' '
            return string
        return 'Impossible to multiply.'


person1 = Person('John', 'Doe', 27)
person2 = Person('Jane', 'Doe', 55)
print(repr(person1))
print(repr(person2))
print(str(person1))
print(len(person1))
print(person1 + person2)
print(person1 * 3)
