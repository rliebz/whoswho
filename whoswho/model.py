from nameparser import HumanName

from config import UNIQUE_SUFFIXES, MALE_TITLES, FEMALE_TITLES
from utils import make_ascii, strip_punctuation, compare_name_component


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

    def deep_compare(self, other, settings):
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

        first = compare_name_component(
            self.name.first_list,
            other.name.first_list,
            settings['first'],
        )
        middle = compare_name_component(
            self.name.middle_list,
            other.name.middle_list,
            settings['middle'],
        )
        last = compare_name_component(
            self.name.last_list,
            other.name.last_list,
            settings['last'],
        )

        return first and middle and last

    def ratio_deep_compare(self, other, settings):
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

        first = compare_name_component(
            self.name.first_list,
            other.name.first_list,
            settings['first'],
            ratio=True,
        )
        middle = compare_name_component(
            self.name.middle_list,
            other.name.middle_list,
            settings['middle'],
            ratio=True,
        )
        last = compare_name_component(
            self.name.last_list,
            other.name.last_list,
            settings['last'],
            ratio=True,
        )

        # TODO: Find a prettier way to handle weight
        first_is_used = settings['first']['required'] or \
            self.name.first and other.name.first
        first_weight = settings['first']['weight'] if first_is_used else 0

        middle_is_used = settings['middle']['required'] or \
            self.name.middle and other.name.middle
        middle_weight = settings['middle']['weight'] if middle_is_used else 0

        last_is_used = settings['last']['required'] or \
            self.name.last and other.name.last
        last_weight = settings['last']['weight'] if last_is_used else 0

        total_weight = first_weight + middle_weight + last_weight

        result = (
            first * first_weight +
            middle * middle_weight +
            last * last_weight
        ) / total_weight

        return result

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
        suffix_list = self.name.suffix_list + other.name.suffix_list
        unique_suffixes = {s for s in suffix_list if s in UNIQUE_SUFFIXES}

        return len(unique_suffixes) < 2