# -*- coding: utf-8 -*-
import nose
from nose.tools import *
import unittest

from whoswho import who, config, utils

from nameparser.config.titles import TITLES as NAMEPARSER_TITLES
from nameparser.config.suffixes import SUFFIXES as NAMEPARSER_SUFFIXES


class TestFullNames(unittest.TestCase):

    def setUp(self):
        self.name = 'Robert Evan Liebowitz'

    def test_unicode(self):
        assert_true(who.is_it(self.name, u'attaché Robert Evan Liebowitz'))
        assert_true(who.is_it(self.name, u'Rōbért Èvān Lîęböwitz'))
        assert_false(who.is_it(self.name, u'Rōbért Èvān Lęîböwitz'))

    def test_name_and_initials(self):
        assert_true(who.is_it(self.name, 'R. Evan Liebowitz'))
        assert_true(who.is_it(self.name, 'Robert E. Liebowitz'))
        assert_true(who.is_it(self.name, 'R. E. Liebowitz'))

    def test_different_number_initials(self):
        assert_true(who.is_it(self.name, 'Robert Liebowitz'))
        assert_true(who.is_it(self.name, 'R. Liebowitz'))
        assert_false(who.is_it(self.name, 'Robert E. E. Liebowitz'))
        assert_false(who.is_it(self.name, 'R. E. E. Liebowitz'))
        assert_true(who.is_it('R.E.E. Liebowitz', 'R. E. E. Liebowitz'))

    def test_different_initials(self):
        assert_false(who.is_it(self.name, 'E. R. Liebowitz'))
        assert_false(who.is_it(self.name, 'E. Liebowitz'))
        assert_false(who.is_it(self.name, 'R. V. Liebowitz'))
        assert_false(who.is_it(self.name, 'O. E. Liebowitz'))

    def test_short_names(self):
        assert_true(who.is_it(self.name, 'Rob Liebowitz'))
        # TODO: Should these be true?
        assert_false(who.is_it(self.name, 'Bert Liebowitz'))
        assert_false(who.is_it(self.name, 'Robbie Liebowitz'))

    def test_suffixes(self):
        name = 'Robert Liebowitz Jr'
        assert_true(who.is_it(name, 'Robert Liebowitz'))
        assert_true(who.is_it(name, 'Robert Liebowitz Jr'))
        assert_true(who.is_it(name, 'Robert Liebowitz, PhD'))
        assert_false(who.is_it(name, 'Robert Liebowitz, Sr'))
        assert_false(who.is_it(name, 'Robert Liebowitz, Sr, PhD'))
        assert_true(who.is_it(name, 'Robert Liebowitz, Jr, PhD'))

    def test_titles(self):
        name = 'Mr. Robert Liebowitz'
        assert_true(who.is_it(name, 'Robert Liebowitz'))
        assert_true(who.is_it(name, 'Sir Robert Liebowitz'))
        assert_true(who.is_it(name, 'Dr. Robert Liebowitz'))
        assert_false(who.is_it(name, 'Mrs. Robert Liebowitz'))


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

    def test_titles_all_defined(self):
        """
        Check if list of suffixes is up to date with nameparser
        """
        all_suffixes = (
            config.UNIQUE_SUFFIXES |
            config.MISC_SUFFIXES
        )
        assert_equal(all_suffixes, NAMEPARSER_SUFFIXES)


class TestUtils(unittest.TestCase):

    def test_equate_prefix_to_name(self):
        assert_true(utils.equate_prefix_to_name('r', 'robert'))
        assert_true(utils.equate_prefix_to_name('rob', 'robert'))
        assert_false(utils.equate_prefix_to_name('robbie', 'robert'))
        assert_false(utils.equate_prefix_to_name('bert', 'robert'))

    def test_make_ascii(self):
        assert_equal(
            utils.make_ascii(u"foo bar .,?;'!@#$%^&*()"),
            "foo bar .,?;'!@#$%^&*()"
        )
        assert_equal(
            utils.make_ascii(u'äèîõù'),
            'aeiou'
        )

    def test_strip_punctuation(self):
        assert_equal(
            utils.strip_punctuation(u'abcde aeiou'),
            u'abcde aeiou'
        )
        assert_equal(
            utils.strip_punctuation(u"abcde.' aeiou"),
            u'abcde aeiou'
        )


if __name__ == '__main__':
    nose.main()