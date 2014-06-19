import sys
import unicodedata

table = dict.fromkeys(i for i in xrange(sys.maxunicode)
                              if unicodedata.category(unichr(i)).startswith('P'))

from nameparser import HumanName


class Name(object):

    def __init__(self, fullname):
        self.name = HumanName(fullname)

    def __eq__(self, other):
        other = convert_to_name(other)
        result = self.deep_compare(other)

        return result

    def __ne__(self, other):
        result = self.__eq__(other)
        return not result

    def deep_compare(self, other):
        first = self._compare_first(other)
        middle = self._compare_middle(other)
        last = self._compare_last(other)
        result = first and middle and last
        return result

    def _compare_first(self, other):
        return equate_initial_to_name(self.name.first, other.name.first)

    def _compare_middle(self, other):

        # If middle initial is omitted, assume a match
        if not self.name.middle or not other.name.middle:
            return True

        # Compare list of middle initials
        if len(self.name.middle_list) != len(other.name.middle_list):
            return False

        result = True
        for i, name in enumerate(self.name.middle_list):
            result &= equate_initial_to_name(name, other.name.middle_list[i])

        return result

    def _compare_last(self, other):
        return self.name.last == other.name.last


def convert_to_name(stringable):
    try:
        name_string = unicode(stringable)
    except UnicodeDecodeError:
        return NotImplemented
    return Name(name_string)


def equate_initial_to_name(name1, name2):
    """
    Evaluates initials of first name
    """
    name1 = strip_punctuation(name1).lower()
    name2 = strip_punctuation(name2).lower()

    return name1 in name2 or name2 in name1


def strip_punctuation(word):
    """Strips punctuation for use in middle initial"""
    return word.translate(table)
