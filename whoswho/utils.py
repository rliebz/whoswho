import sys
import unicodedata


def equate_initial_to_name(name1, name2):
    """
    Evaluates initials of first name
    """
    name1 = strip_punctuation(name1).lower()
    name2 = strip_punctuation(name2).lower()

    return name1 in name2 or name2 in name1


def strip_punctuation(word):
    """
    Strips punctuation for use in middle initial
    """
    table = dict.fromkeys(
        i for i in xrange(sys.maxunicode)
        if unicodedata.category(unichr(i)).startswith('P')
    )
    return word.translate(table)