"""
Write a program that uses private methods.
"""


class People:
    def __init__(self, name):
        self.name = name
        self.email = self.__email_creator()

    def __email_creator(self):
        return self.name.lower() + '@email.com'


person = People('George')
print(person.name)
print(person.email)
