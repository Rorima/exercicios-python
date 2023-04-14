"""
1. Coordinates:
Write an algorithm that creates the coordinates of a chess board.

They go from a to h and from 1 to 8.
a ~ h = horizontal
1 ~ 8 = vertical

2. Colors:
Create a dictionary and add the coordinates as keys and make a function 
that will add the right colors to the right coordinates.

3. Organize:
Organize the code in OOP.
"""


class BlackWhite:
    def __init__(self):
        self.create_coordinates()
        self.display_dictionary()

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

        self.coordinates = dict()

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
        for k, v in self.coordinates.items():
            print(f"Key: {k}")
            print(f"Value: {v}")
            print()


if __name__ == "__main__":
    bw = BlackWhite()
