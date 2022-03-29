"""
Write a program using static methods.
"""


class Insect:

    def __init__(self, species):
        self.species = species

    @staticmethod
    def warning():
        print('WARNING! INSTECTS!')
        print('(Insect noises intensifies.)')


bug1 = Insect('Fly')
Insect.warning()
