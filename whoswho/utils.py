import re
import unicodedata

from config import STRIPPED_CHARACTERS


def equate_initial_to_name(name1, name2):
    """
    Evaluates whether names match, or one name is the initial of the other
    """
    if len(name1) == 0 or len(name2) == 0:
        return False

    if len(name1) == 1 or len(name2) == 1:
        return name1[0] == name2[0]

    return name1 == name2


def equate_prefix_to_name(name1, name2):
    """
    Evaluates whether names match, or one name prefixes another
    """

    if len(name1) == 0 or len(name2) == 0:
        return False

    return name1.startswith(name2) or name2.startswith(name1)


def equate_nickname(name1, name2):

    # Convert '-ie' and '-y' to the root name
    nickname_regex = r'(.)\1(y|ie)$'
    root_regex = r'\1'

    name1 = re.sub(nickname_regex, root_regex, name1)
    name2 = re.sub(nickname_regex, root_regex, name2)

    if equate_prefix_to_name(name1, name2):
        return True

    return False


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
