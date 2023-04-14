"""
The program tests you whether a square on the 
chessboard is black or white.
"""
from random import choice
from os import system
from time import sleep


class BlackWhite:
    def __init__(self):
        self.total = 0
        self.misses = 0
        self.coordinates = dict()
        self.create_coordinates()
        # self.display_dictionary()
        self.menu()

    def menu(self):
        """Test the user."""
        c_list = list(self.coordinates.keys())

        while True:
            system("cls||clear")
            square = choice(c_list)

            print("Type 'quit' to quit.")
            print(f"The square {square} is black or white?")
            answer = input()
            answer = answer.lower()

            if answer == "quit" or answer == "exit":
                break
            elif answer[0] == "w":
                answer = "white"
            elif answer[0] == "b":
                answer = "black"

            if answer == self.coordinates[square]:
                print("You got it!")
            else:
                print("No...")
                self.misses += 1

            self.total += 1
            sleep(1)

        print(f"Score: {self.total - self.misses}/{self.total}.")

    def create_coordinates(self):
        """Create coordinates"""
        numbers = (1, 2, 3, 4, 5, 6, 7, 8)
        letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

        a = [(f'a{num}') for num in numbers]
        b = [(f'b{num}') for num in numbers]
        c = [(f'c{num}') for num in numbers]
        d = [(f'd{num}') for num in numbers]
        e = [(f'e{num}') for num in numbers]
        f = [(f'f{num}') for num in numbers]
        g = [(f'g{num}') for num in numbers]
        h = [(f'h{num}') for num in numbers]

        coord_tuple = (a, b, c, d, e, f, g, h)

        c = 0
        for l in coord_tuple:
            if c % 2 == 0:
                self.__colorize(self.coordinates, l, False)
            else:
                self.__colorize(self.coordinates, l)

            c += 1

    def __colorize(self, dictionary, coord_list, white_color_first=True):
        """Add black or white as a value for a key in a dictionary."""
        alternate = True if white_color_first else False

        for item in coord_list:
            dictionary[item] = "white" if alternate else "black"
            alternate = not alternate

    def display_dictionary(self):
        """Display self.coordinates"""
        for k, v in self.coordinates.items():
            print(f"Key: {k}")
            print(f"Value: {v}")
            print()


if __name__ == "__main__":
    bw = BlackWhite()
