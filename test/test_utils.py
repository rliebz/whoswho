# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from nose.tools import *
import unittest

from whoswho import utils


class TestUtils(unittest.TestCase):

    def test_equate_prefix_to_name(self):
        assert_true(utils.equate_prefix('r', 'robert'))
        assert_true(utils.equate_prefix('rob', 'robert'))
        assert_false(utils.equate_prefix('robbie', 'robert'))
        assert_false(utils.equate_prefix('bert', 'robert'))

    def test_make_ascii(self):
        assert_equal(
            utils.make_ascii("foo bar .,?;'!@#$%^&*()"),
            "foo bar .,?;'!@#$%^&*()"
        )
        assert_equal(
            utils.make_ascii('äèîõù'),
            'aeiou'
        )

    def test_strip_punctuation(self):
        assert_equal(
            utils.strip_punctuation('abcde aeiou'),
            'abcde aeiou'
        )
        assert_equal(
            utils.strip_punctuation("abcde.' aeiou"),
            'abcde aeiou'
        )

    def test_equate_nickname(self):
        assert_true(utils.equate_nickname('robert', 'rob'))
        assert_true(utils.equate_nickname('robert', 'robby'))
        assert_true(utils.equate_nickname('robert', 'robbie'))
        assert_true(utils.equate_nickname('robbie', 'robby'))
        assert_false(utils.equate_nickname('robert', 'robin'))
        assert_false(utils.equate_nickname('harold', 'harriet'))

    def test_deep_update_dict(self):
        default = {'one': 1, 'two': 2, 'three': {'four': 4, 'five': 5}}
        utils.deep_update_dict(default, {'one': 'a', 'three': {'four': 'b'}})
        assert_equal(default['one'], 'a')
        assert_equal(default['two'], 2)
        assert_equal(type(default['three']), dict)
        assert_equal(default['three']['four'], 'b')
        assert_equal(default['three']['five'], 5)

