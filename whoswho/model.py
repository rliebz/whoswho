from nameparser import HumanName

from config import UNIQUE_SUFFIXES, MALE_TITLES, FEMALE_TITLES
from utils import equate_prefix_to_name, strip_punctuation, make_ascii


class Name(object):

    def __init__(self, fullname):
        ascii_name = make_ascii(unicode(fullname))
        self.name = HumanName(ascii_name)

        # lower after parsing to preserve parsing logic
        self.name.title = strip_punctuation(self.name.title)
        self.name.first = strip_punctuation(self.name.first)
        self.name.middle = strip_punctuation(self.name.middle)
        self.name.last = strip_punctuation(self.name.last)
        self.name.suffix = strip_punctuation(self.name.suffix)

    def deep_compare(self, other):
        title = self._compare_title(other)
        first = self._compare_first(other)
        middle = self._compare_middle(other)
        last = self._compare_last(other)
        suffix = self._compare_suffix(other)

        return title and first and middle and last and suffix

    def _compare_title(self, other):

        # If title is omitted, assume a match
        if not self.name.title or not other.name.title:
            return True

        titles = set(self.name.title_list + other.name.title_list)

        return not (titles & MALE_TITLES and titles & FEMALE_TITLES)

    def _compare_first(self, other):
        return equate_prefix_to_name(self.name.first, other.name.first)

    def _compare_middle(self, other):

        # If middle initial is omitted, assume a match
        if not self.name.middle or not other.name.middle:
            return True

        # Compare list of middle initials
        if len(self.name.middle_list) != len(other.name.middle_list):
            return False

        result = True
        for i, name in enumerate(self.name.middle_list):
            result &= equate_prefix_to_name(name, other.name.middle_list[i])

        return result

    def _compare_last(self, other):
        return self.name.last == other.name.last

    def _compare_suffix(self, other):

        # If suffix is omitted, assume a match
        if not self.name.suffix or not other.name.suffix:
            return True

        # Check if more than one unique suffix
        suffix_list = self.name.suffix_list + other.name.suffix_list
        unique_suffixes = {s for s in suffix_list if s in UNIQUE_SUFFIXES}

        return len(unique_suffixes) < 2