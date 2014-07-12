import sys
import unicodedata


def equate_initial_to_name(name1, name2):
    """
    Evaluates whether one name prefixes another
    """
    if len(name1) == 0 or len(name2) == 0:
        return False

    return name1.startswith(name2) or name2.startswith(name1)


def strip_punctuation(word):
    """
    Strips punctuation from name
    """
    table = dict.fromkeys(
        i for i in xrange(sys.maxunicode)
        if unicodedata.category(unichr(i)).startswith('P')
    )
    return word.translate(table)