from nameparser import HumanName
from fuzzywuzzy import fuzz

from config import UNIQUE_SUFFIXES, MALE_TITLES, FEMALE_TITLES
from utils import (equate_initial_to_name, equate_prefix_to_name, make_ascii,
                   strip_punctuation)


class Name(object):

    def __init__(self, fullname):
        ascii_name = make_ascii(unicode(fullname))
        self.name = HumanName(ascii_name)

        # Format after parsing to preserve parsing logic
        self.name.title = strip_punctuation(self.name.title)
        self.name.first = strip_punctuation(self.name.first)
        self.name.middle = strip_punctuation(self.name.middle)
        self.name.last = strip_punctuation(self.name.last)
        self.name.suffix = strip_punctuation(self.name.suffix)

    def deep_compare(self, other):
        """
        Compares each field of the name one at a time to see if they match.
        Each name field has context-specific comparison logic.

        :param Name other: other Name for comparison
        :return bool: whether the two names are compatible
        """

        # Exclusionary criteria
        title = self._compare_title(other)
        suffix = self._compare_suffix(other)

        if not title or not suffix:
            return False

        first = self._compare_first(other)
        middle = self._compare_middle(other)
        last = self._compare_last(other)

        return first and middle and last

    def ratio_deep_compare(self, other):
        """
        Compares each field of the name one at a time to see if they match.
        Each name field has context-specific comparison logic.

        :param Name other: other Name for comparison
        :return int: ratio fuzzy match (out of 100)
        """

        # Exclusionary criteria
        title = self._compare_title(other)
        suffix = self._compare_suffix(other)

        if not title or not suffix:
            return 0

        first = self._compare_first(other, ratio=True)
        middle = self._compare_middle(other, ratio=True)
        last = self._compare_last(other, ratio=True)

        # TODO: Make name weighting configurable
        first_weight = 1
        middle_weight = 1 if self.name.middle and other.name.middle else 0
        last_weight = 1
        total_weight = first_weight + middle_weight + last_weight

        name_weight = (
            first * first_weight + middle * middle_weight + last * last_weight
        ) / total_weight

        return name_weight

    def _compare_title(self, other):
        """Return False if titles have different gender associations"""

        # If title is omitted, assume a match
        if not self.name.title or not other.name.title:
            return True

        titles = set(self.name.title_list + other.name.title_list)

        return not (titles & MALE_TITLES and titles & FEMALE_TITLES)

    def _compare_first(self, other, ratio=False):
        """Compares first names allowing for partial-matching"""

        comparison = fuzz.partial_ratio if ratio else equate_prefix_to_name
        return comparison(self.name.first, other.name.first)

    def _compare_middle(self, other, ratio=False):
        """Compare middle name list allowing for initials"""

        # If middle initial is omitted, assume a match
        if not self.name.middle or not other.name.middle:
            return True

        # Compare list of middle initials
        if len(self.name.middle_list) != len(other.name.middle_list):
            return False

        result = True
        comparison = fuzz.partial_ratio if ratio else equate_initial_to_name
        for i, name in enumerate(self.name.middle_list):
            result *= comparison(name, other.name.middle_list[i])

        return result

    def _compare_last(self, other, ratio=False):
        """Compare last names directly"""

        comparison = fuzz.ratio if ratio else lambda x, y: x == y
        return comparison(self.name.last, other.name.last)

    def _compare_suffix(self, other):
        """Return false if suffixes are mutually exclusive"""

        # If suffix is omitted, assume a match
        if not self.name.suffix or not other.name.suffix:
            return True

        # Check if more than one unique suffix
        suffix_list = self.name.suffix_list + other.name.suffix_list
        unique_suffixes = {s for s in suffix_list if s in UNIQUE_SUFFIXES}

        return len(unique_suffixes) < 2