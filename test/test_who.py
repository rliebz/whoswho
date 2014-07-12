import unittest
from whoswho import who


class TestFullNames(unittest.TestCase):

    def setUp(self):
        self.name = 'Robert Evan Liebowitz'

    def test_name_and_initials(self):
        self.assertTrue(who.is_it(self.name, 'R. Evan Liebowitz'))
        self.assertTrue(who.is_it(self.name, 'Robert E. Liebowitz'))
        self.assertTrue(who.is_it(self.name, 'R. E. Liebowitz'))

    def test_different_number_initials(self):
        self.assertTrue(who.is_it(self.name, 'Robert Liebowitz'))
        self.assertTrue(who.is_it(self.name, 'R. Liebowitz'))
        self.assertFalse(who.is_it(self.name, 'Robert E. E. Liebowitz'))
        self.assertFalse(who.is_it(self.name, 'R. E. E. Liebowitz'))

    def test_different_initials(self):
        self.assertFalse(who.is_it(self.name, 'E. R. Liebowitz'))
        self.assertFalse(who.is_it(self.name, 'E. Liebowitz'))
        self.assertFalse(who.is_it(self.name, 'R. V. Liebowitz'))
        self.assertFalse(who.is_it(self.name, 'O. E. Liebowitz'))

    def test_suffixes(self):
        name = 'Jonathan James Johnston Jr'
        self.assertTrue(who.is_it(name, 'Jonathan James Johnston'))
        self.assertTrue(who.is_it(name, 'Jonathan James Johnston Jr'))
        self.assertTrue(who.is_it(name, 'Jonathan James Johnston, PhD'))
        self.assertFalse(who.is_it(name, 'Jonathan James Johnston, Sr'))
        self.assertFalse(who.is_it(name, 'Jonathan James Johnston, Sr, PhD'))
        self.assertTrue(who.is_it(name, 'Jonathan James Johnston, Jr, PhD'))


if __name__ == '__main__':
    unittest.main()