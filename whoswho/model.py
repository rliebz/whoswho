import string

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
        return self.name.first == other.name.first

    def _compare_middle(self, other):

        own_middle = self.name.middle
        other_middle = self.name.middle

        # If middle initial is omitted, assume a match
        if not own_middle or not other_middle:
            return True

        return own_middle == other_middle

    def _compare_last(self, other):
        return self.name.last == other.name.last


def convert_to_name(stringable):
    try:
        name_string = unicode(stringable)
    except UnicodeDecodeError:
        return NotImplemented
    return Name(name_string)


def strip_punctuation(word):
    """Strips punctuation for use in middle initial"""
    return word.translate(string.maketrans("",""), string.punctuation)

print 'hi'