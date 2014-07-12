# -*- coding: utf-8 -*-
import unittest
from whoswho import who
from whoswho import config

from nameparser.config.titles import TITLES as NAMEPARSER_TITLES
from nameparser.config.suffixes import SUFFIXES as NAMEPARSER_SUFFIXES


class TestFullNames(unittest.TestCase):

    def setUp(self):
        self.name = 'Robert Evan Liebowitz'

    def test_unicode(self):
        self.assertTrue(who.is_it(self.name, u'attaché Robert Evan Liebowitz'))
        self.assertTrue(who.is_it(self.name, u'Rōbért Èvān Lîęböwitz'))

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

    def test_short_names(self):
        self.assertTrue(who.is_it(self.name, 'Rob Liebowitz'))
        # TODO: Should these be true?
        self.assertFalse(who.is_it(self.name, 'Bert Liebowitz'))
        self.assertFalse(who.is_it(self.name, 'Robbie Liebowitz'))

    def test_suffixes(self):
        name = 'Robert Liebowitz Jr'
        self.assertTrue(who.is_it(name, 'Robert Liebowitz'))
        self.assertTrue(who.is_it(name, 'Robert Liebowitz Jr'))
        self.assertTrue(who.is_it(name, 'Robert Liebowitz, PhD'))
        self.assertFalse(who.is_it(name, 'Robert Liebowitz, Sr'))
        self.assertFalse(who.is_it(name, 'Robert Liebowitz, Sr, PhD'))
        self.assertTrue(who.is_it(name, 'Robert Liebowitz, Jr, PhD'))

    def test_titles(self):
        name = 'Mr. Robert Liebowitz'
        self.assertTrue(who.is_it(name, 'Robert Liebowitz'))
        self.assertTrue(who.is_it(name, 'Sir Robert Liebowitz'))
        self.assertTrue(who.is_it(name, 'Dr. Robert Liebowitz'))
        self.assertFalse(who.is_it(name, 'Mrs. Robert Liebowitz'))


class TestConfig(unittest.TestCase):

    def test_titles_all_defined(self):
        """
        Check if list of titles is up to date with nameparser
        """
        all_titles = (
            config.MALE_TITLES |
            config.FEMALE_TITLES |
            config.GENDERLESS_TITLES
        )
        self.assertEqual(all_titles, NAMEPARSER_TITLES)

    def test_titles_all_defined(self):
        """
        Check if list of suffixes is up to date with nameparser
        """
        all_suffixes = (
            config.UNIQUE_SUFFIXES |
            config.MISC_SUFFIXES
        )
        self.assertEqual(all_suffixes, NAMEPARSER_SUFFIXES)

if __name__ == '__main__':
    unittest.main()