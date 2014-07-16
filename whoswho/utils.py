import unicodedata
from config import STRIPPED_CHARACTERS


def equate_prefix_to_name(name1, name2):
    """
    Evaluates whether one name prefixes another
    """

    if len(name1) == 0 or len(name2) == 0:
        return False

    return name1.startswith(name2) or name2.startswith(name1)


def make_ascii(word):
    """
    Converts unicode-specific characters to their equivalent ascii
    """
    ascii_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore')
    return unicode(ascii_word)


# TODO: Can/should this handle hyphens?
def strip_punctuation(word):
    """
    Strips punctuation from name and lower cases it
    """

    return word.translate(STRIPPED_CHARACTERS).lower()
