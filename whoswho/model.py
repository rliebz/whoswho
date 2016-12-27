# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from nameparser import HumanName

from whoswho.config import (UNIQUE_SUFFIXES, MALE_TITLES, FEMALE_TITLES,
                            EQUIVALENT_SUFFIXES)
from whoswho.utils import make_ascii, strip_punctuation, compare_name_component


class Name(HumanName):

    def __init__(self, fullname):
        ascii_name = make_ascii(fullname)
        super(Name, self).__init__(ascii_name)

        # Format after parsing to preserve parsing logic
        self.title = strip_punctuation(self.title)
        self.first = strip_punctuation(self.first)
        self.middle = strip_punctuation(self.middle)
        self.last = strip_punctuation(self.last)
        self.suffix = strip_punctuation(self.suffix)
        self.nickname = strip_punctuation(self.nickname)

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
        if not self.title or not other.title:
            return True

        titles = set(self.title_list + other.title_list)

        return not (titles & MALE_TITLES and titles & FEMALE_TITLES)

    def _compare_suffix(self, other):
        """Return false if suffixes are mutually exclusive"""

        # If suffix is omitted, assume a match
        if not self.suffix or not other.suffix:
            return True

        # Check if more than one unique suffix
        suffix_set = set(self.suffix_list + other.suffix_list)
        unique_suffixes = suffix_set & UNIQUE_SUFFIXES
        for key in EQUIVALENT_SUFFIXES:
            if key in unique_suffixes:
                unique_suffixes.remove(key)
                unique_suffixes.add(EQUIVALENT_SUFFIXES[key])

        return len(unique_suffixes) < 2

    def _compare_components(self, other, settings, ratio=False):
        """Return comparison of first, middle, and last components"""

        first = compare_name_component(
            self.first_list,
            other.first_list,
            settings['first'],
            ratio,
        )

        if settings['check_nickname']:
            if first is False:
                first = compare_name_component(
                    self.nickname_list,
                    other.first_list,
                    settings['first'],
                    ratio
                ) or compare_name_component(
                    self.first_list,
                    other.nickname_list,
                    settings['first'],
                    ratio
                )
            elif ratio and first is not 100:
                first = max(
                    compare_name_component(
                        self.nickname_list,
                        other.first_list,
                        settings['first'],
                        ratio
                    ),
                    compare_name_component(
                        self.first_list,
                        other.nickname_list,
                        settings['first'],
                        ratio
                    ),
                    first,
                )

        middle = compare_name_component(
            self.middle_list,
            other.middle_list,
            settings['middle'],
            ratio,
        )

        last = compare_name_component(
            self.last_list,
            other.last_list,
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
            self.first and other.first
        first_weight = settings['first']['weight'] if first_is_used else 0

        middle_is_used = settings['middle']['required'] or \
            self.middle and other.middle
        middle_weight = settings['middle']['weight'] if middle_is_used else 0

        last_is_used = settings['last']['required'] or \
            self.last and other.last
        last_weight = settings['last']['weight'] if last_is_used else 0

        return first_weight, middle_weight, last_weight
