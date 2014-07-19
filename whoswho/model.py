# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from nameparser import HumanName

from whoswho.config import (UNIQUE_SUFFIXES, MALE_TITLES, FEMALE_TITLES,
                            EQUIVALENT_SUFFIXES)
from whoswho.utils import make_ascii, strip_punctuation, compare_name_component


class Name(object):

    def __init__(self, fullname):
        ascii_name = make_ascii(fullname)
        self.name = HumanName(ascii_name)

        # Format after parsing to preserve parsing logic
        self.name.title = strip_punctuation(self.name.title)
        self.name.first = strip_punctuation(self.name.first)
        self.name.middle = strip_punctuation(self.name.middle)
        self.name.last = strip_punctuation(self.name.last)
        self.name.suffix = strip_punctuation(self.name.suffix)

    def deep_compare(self, other, settings):
        """
        Compares each field of the name one at a time to see if they match.
        Each name field has context-specific comparison logic.

        :param Name other: other Name for comparison
        :return bool: whether the two names are compatible
        """

        if not self._is_compatible_with(other):
            return False

        first, middle, last = self._compare_components(other, settings)

        return first and middle and last

    def ratio_deep_compare(self, other, settings):
        """
        Compares each field of the name one at a time to see if they match.
        Each name field has context-specific comparison logic.

        :param Name other: other Name for comparison
        :return int: sequence ratio match (out of 100)
        """

        if not self._is_compatible_with(other):
            return 0

        first, middle, last = self._compare_components(other, settings, True)
        f_weight, m_weight, l_weight = self._determine_weights(other, settings)
        total_weight = f_weight + m_weight + l_weight

        result = (
            first * f_weight +
            middle * m_weight +
            last * l_weight
        ) / total_weight

        return result

    def _is_compatible_with(self, other):
        """
        Return True if names are not incompatible.

        This checks that the gender of titles and compatibility of suffixes
        """

        title = self._compare_title(other)
        suffix = self._compare_suffix(other)

        return title and suffix

    def _compare_title(self, other):
        """Return False if titles have different gender associations"""

        # If title is omitted, assume a match
        if not self.name.title or not other.name.title:
            return True

        titles = set(self.name.title_list + other.name.title_list)

        return not (titles & MALE_TITLES and titles & FEMALE_TITLES)

    def _compare_suffix(self, other):
        """Return false if suffixes are mutually exclusive"""

        # If suffix is omitted, assume a match
        if not self.name.suffix or not other.name.suffix:
            return True

        # Check if more than one unique suffix
        suffix_set = set(self.name.suffix_list + other.name.suffix_list)
        unique_suffixes = suffix_set & UNIQUE_SUFFIXES
        for key in EQUIVALENT_SUFFIXES.keys():
            if key in unique_suffixes:
                unique_suffixes.remove(key)
                unique_suffixes.add(EQUIVALENT_SUFFIXES[key])

        return len(unique_suffixes) < 2

    def _compare_components(self, other, settings, ratio=False):
        """Return comparison of first, middle, and last components"""

        first = compare_name_component(
            self.name.first_list,
            other.name.first_list,
            settings['first'],
            ratio,
        )
        middle = compare_name_component(
            self.name.middle_list,
            other.name.middle_list,
            settings['middle'],
            ratio,
        )
        last = compare_name_component(
            self.name.last_list,
            other.name.last_list,
            settings['last'],
            ratio,
        )

        return first, middle, last

    def _determine_weights(self, other, settings):
        """
        Return weights of name components based on whether or not they were
        omitted
        """

        # TODO: Reduce weight for matches by prefix or initials

        first_is_used = settings['first']['required'] or \
            self.name.first and other.name.first
        first_weight = settings['first']['weight'] if first_is_used else 0

        middle_is_used = settings['middle']['required'] or \
            self.name.middle and other.name.middle
        middle_weight = settings['middle']['weight'] if middle_is_used else 0

        last_is_used = settings['last']['required'] or \
            self.name.last and other.name.last
        last_weight = settings['last']['weight'] if last_is_used else 0

        return first_weight, middle_weight, last_weight
