import unittest
from keyboard import MusicalKeyboard


class MusicalKeyboardTests(unittest.TestCase):

    def setUp(self):
        self.keyboard1 = MusicalKeyboard('Yamaha', 'PSR Series EW300', 'Black', 76)

    def test_change_color(self):
        self.assertEqual(self.keyboard1.change_color('White'),
                         'The color was successfully changed to white!')

    def test_print(self):
        self.assertEqual(self.keyboard1.display_brand(), 'YAMAHA')
        self.assertEqual(self.keyboard1.display_model(), 'PSR SERIES EW300')
        self.assertEqual(self.keyboard1.display_color(), 'Black')
        self.assertEqual(self.keyboard1.display_keys(), 76)


if __name__ == '__main__':
    unittest.main()
