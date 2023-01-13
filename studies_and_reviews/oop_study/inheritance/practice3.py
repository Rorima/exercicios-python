"""
Use multiple inheritance.

"""


class Person:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        return f"Hello! My name is {self.name}"


class Engineer(Person):

    def __init__(self, name):
        super().__init__(name)
        self.branch = None

    def introduction(self):
        return f"Hello! My name is {self.name} and I'm an engineer!"


class Programmer(Person):

    def __init__(self, name):
        super().__init__(name)
        self.prog_lang = None

    def introduction(self):
        return f"Hello! My name is {self.name} and I'm a programmer!"


class SmartPerson(Programmer, Engineer):

    def __init__(self, name, hobby):
        super().__init__(name)
        self.hobby = hobby


dennis = SmartPerson('Dennis', 'singing')
dennis.prog_lang = 'Python'
dennis.branch = 'Chemical'

print(dennis.prog_lang)
print(dennis.branch)

print(dennis.say_hi())
print(dennis.introduction())
