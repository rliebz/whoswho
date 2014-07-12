import unittest
from whoswho.model import Name


class TestFullNames(unittest.TestCase):

    def setUp(self):
        self.name = Name('Robert Evan Liebowitz')

    def test_name_and_initials(self):
        self.assertEqual(self.name, 'R Evan Liebowitz')
        self.assertEqual(self.name, 'R. Evan Liebowitz')
        self.assertEqual(self.name, 'Robert E Liebowitz')
        self.assertEqual(self.name, 'Robert E. Liebowitz')
        self.assertEqual(self.name, 'R E Liebowitz')
        self.assertEqual(self.name, 'R. E. Liebowitz')
        self.assertEqual(self.name, 'R.E. Liebowitz')

    def test_wrong_number_initials(self):
        self.assertNotEqual(self.name, 'Robert E. E. Liebowitz')
        self.assertNotEqual(self.name, 'R.E.E. Liebowitz')


if __name__ == '__main__':
    unittest.main()