# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import nose
from nose.tools import *
import unittest

from whoswho import who, config

from nameparser.config.titles import TITLES as NAMEPARSER_TITLES
from nameparser.config.suffixes import SUFFIXES as NAMEPARSER_SUFFIXES


class TestMatch(unittest.TestCase):

    def setUp(self):
        self.name = 'Robert Evan Liebowitz'

    def test_string(self):
        # Only relevant for python 2.X
        assert_true(who.match(self.name, str('Robert Liebowitz')))

    def test_unicode(self):
        name = self.name
        assert_true(who.match(name, 'attaché Robert Evan Liebowitz'))
        assert_true(who.match(name, 'Rōbért Èvān Lîęböwitz'))
        assert_false(who.match(name, 'Rōbért Èvān Lęîböwitz'))

    def test_name_and_initials(self):
        assert_true(who.match(self.name, 'R. Evan Liebowitz'))
        assert_true(who.match(self.name, 'Robert E. Liebowitz'))
        assert_true(who.match(self.name, 'R. E. Liebowitz'))

    def test_different_number_initials(self):
        assert_true(who.match(self.name, 'Robert Liebowitz'))
        assert_true(who.match(self.name, 'R. Liebowitz'))
        assert_false(who.match(self.name, 'Robert E. E. Liebowitz'))
        assert_false(who.match(self.name, 'R. E. E. Liebowitz'))
        assert_true(who.match('R.E.E. Liebowitz', 'R. E. E. Liebowitz'))

    def test_different_initials(self):
        assert_false(who.match(self.name, 'E. R. Liebowitz'))
        assert_false(who.match(self.name, 'E. Liebowitz'))
        assert_false(who.match(self.name, 'R. V. Liebowitz'))
        assert_false(who.match(self.name, 'O. E. Liebowitz'))

    def test_short_names(self):
        assert_true(who.match(self.name, 'Rob Liebowitz'))
        # TODO: Should these be true?
        assert_false(who.match(self.name, 'Bert Liebowitz'))
        assert_false(who.match(self.name, 'Robbie Liebowitz'))

    def test_suffixes(self):
        name = 'Robert Liebowitz Jr'
        assert_true(who.match(name, 'Robert Liebowitz'))
        assert_true(who.match(name, 'Robert Liebowitz Jr'))
        assert_true(who.match(name, 'Robert Liebowitz, PhD'))
        assert_false(who.match(name, 'Robert Liebowitz, Sr'))
        assert_false(who.match(name, 'Robert Liebowitz, Sr, PhD'))
        assert_true(who.match(name, 'Robert Liebowitz, Jr, PhD'))

    def test_equivalent_suffixes(self):
        name = 'Robert Liebowitz Jr'
        assert_true(who.match(name, 'Robert Liebowitz Jnr'))
        assert_false(who.match(name, 'Robert Liebowitz Snr'))

    def test_titles(self):
        name = 'Mr. Robert Liebowitz'
        assert_true(who.match(name, 'Robert Liebowitz'))
        assert_true(who.match(name, 'Sir Robert Liebowitz'))
        assert_true(who.match(name, 'Dr. Robert Liebowitz'))
        assert_false(who.match(name, 'Mrs. Robert Liebowitz'))

    def test_nickname(self):
        name = 'Robert "Evan" Liebowitz'
        assert_true(who.match(name, 'Evan Liebowitz'))
        assert_true(who.match('Evan Liebowitz', name))
        assert_false(who.match(name, 'Wrongbert Lieobwitz'))
        assert_false(who.match(name, 'Robert Evan'))
        assert_false(who.match(name, 'Evan Liebowitz',
                               options={'check_nickname': False}))


class TestRatio(unittest.TestCase):

    def setUp(self):
        self.name = 'Robert Evan Liebowitz'

    def test_string(self):
        # Only relevant for python 2.X
        assert_equal(who.ratio(self.name, str('Robert Liebowitz')), 100)

    def test_unicode(self):
        name = self.name
        assert_equal(who.ratio(name, 'attaché Robert Evan Liebowitz'), 100)
        assert_equal(who.ratio(name, 'Rōbért Èvān Lîęböwitz'), 100)
        assert_true(who.ratio(name, 'Rōbért Èvān Lęîböwitz') < 100)

    def test_name_and_initials(self):
        assert_equal(who.ratio(self.name, 'R. Evan Liebowitz'), 100)
        assert_equal(who.ratio(self.name, 'Robert E. Liebowitz'), 100)
        assert_equal(who.ratio(self.name, 'R. E. Liebowitz'), 100)

    def test_different_number_initials(self):
        assert_equal(who.ratio(self.name, 'Robert Liebowitz'), 100)
        assert_equal(who.ratio(self.name, 'R. Liebowitz'), 100)
        assert_true(who.ratio(self.name, 'Robert E. E. Liebowitz') < 100)
        assert_true(who.ratio(self.name, 'R. E. E. Liebowitz') < 100)
        assert_equal(who.ratio('R.E.E. Liebowitz', 'R. E. E. Liebowitz'), 100)

    def test_different_initials(self):
        assert_true(who.ratio(self.name, 'E. R. Liebowitz') < 100)
        assert_true(who.ratio(self.name, 'E. Liebowitz') < 100)
        assert_true(who.ratio(self.name, 'R. V. Liebowitz') < 100)
        assert_true(who.ratio(self.name, 'O. E. Liebowitz') < 100)
        assert_true(who.ratio(self.name, 'E. R. Liebowitz') <
                    who.ratio(self.name, 'E. E. Liebowitz'))
        assert_true(who.ratio(self.name, 'E. R. Liebowitz') <
                    who.ratio(self.name, 'R. R. Liebowitz'))
        assert_true(who.ratio(self.name, 'E. R. Liebowitz') <
                    who.ratio(self.name, 'E. Liebowitz'))

    def test_short_names(self):
        assert_true(who.ratio(self.name, 'Rob Liebowitz'))
        assert_true(who.ratio(self.name, 'Bert Liebowitz') < 100)
        assert_true(who.ratio(self.name, 'Robbie Liebowitz') < 100)
        assert_true(who.ratio(self.name, 'xxxxx Liebowitz') <
                    who.ratio(self.name, 'Bobby Liebowitz'))

    def test_suffixes(self):
        name = 'Robert Liebowitz Jr'
        assert_equal(who.ratio(name, 'Robert Liebowitz'), 100)
        assert_equal(who.ratio(name, 'Robert Liebowitz Jr'), 100)
        assert_equal(who.ratio(name, 'Robert Liebowitz, PhD'), 100)
        assert_false(who.ratio(name, 'Robert Liebowitz, Sr'))
        assert_false(who.ratio(name, 'Robert Liebowitz, Sr, PhD'))
        assert_equal(who.ratio(name, 'Robert Liebowitz, Jr, PhD'), 100)
        # Suffix doesn't change a match
        assert_equal(who.ratio(name, 'Zachary Liebowitz, Jr'),
                     who.ratio(name, 'Zachary Liebowitz'))

    def test_equivalent_suffixes(self):
        name = 'Robert Liebowitz Jr'
        assert_equal(who.ratio(name, 'Robert Liebowitz Jnr'), 100)
        assert_false(who.ratio(name, 'Robert Liebowitz Snr'))

    def test_titles(self):
        name = 'Mr. Robert Liebowitz'
        assert_equal(who.ratio(name, 'Robert Liebowitz'), 100)
        assert_equal(who.ratio(name, 'Sir Robert Liebowitz'), 100)
        assert_equal(who.ratio(name, 'Dr. Robert Liebowitz'), 100)
        assert_false(who.ratio(name, 'Mrs. Robert Liebowitz'))
        # Title doesn't change a match
        assert_equal(who.ratio(name, 'Dr. Zachary Liebowitz'),
                     who.ratio(name, 'Zachary Liebowitz'))

    def test_nickname(self):
        name = 'Robert "Evan" Liebowitz'
        assert_equal(who.ratio(name, 'Evan Liebowitz'), 100)
        assert_equal(who.ratio('Evan Liebowitz', name), 100)
        assert_true(who.ratio(name, 'Wrongbert Lieobwitz') < 100)
        assert_true(who.ratio(name, 'Robert Evan') < 100)
        assert_true(who.ratio(name, 'Evan Liebowitz',
                              options={'check_nickname': False}) < 100)
        assert_true(who.ratio(name, 'xxxx Liebowitz') <
                    who.ratio(name, 'xvax Liebowitz'))
        assert_equal(who.ratio(name, 'xxxx Liebowitz'),
                     who.ratio(name, 'xvax Liebowitz', 'strict'))


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
        assert_equal(all_titles, NAMEPARSER_TITLES)

    def test_suffixes_all_defined(self):
        """
        Check if list of suffixes is up to date with nameparser
        """
        all_suffixes = (
            config.UNIQUE_SUFFIXES |
            config.MISC_SUFFIXES
        )
        assert_equal(all_suffixes, NAMEPARSER_SUFFIXES)


if __name__ == '__main__':
    nose.main()