# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from nose.tools import *
import unittest

from whoswho.model import Name


class TestFullNames(unittest.TestCase):

    def setUp(self):
        self.name = 'Rôbert E. Liebowitz'

    def test_init(self):
        n = Name(self.name)
        assert_equal(n.name.title_list, [''])
        assert_equal(n.name.first_list, ['robert'])
        assert_equal(n.name.middle_list, ['e'])
        assert_equal(n.name.last_list, ['liebowitz'])
        assert_equal(n.name.suffix_list, [''])
        assert_equal(n.name.nickname_list, [''])
