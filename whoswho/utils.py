import re
import unicodedata

from fuzzywuzzy import fuzz

from config import STRIPPED_CHARACTERS


def compare_name_component(list1, list2, settings, ratio=False):

    if not list1[0] or not list2[0]:
        result = not settings['required']
        return result * 100 if ratio else result

    if len(list1) != len(list2):
        return False

    num_names = len(list1)

    if ratio:
        result = 0
        for i in range(num_names):
            if settings['allow_prefix']:
                result += fuzz.partial_ratio(list1[i], list2[i])
            elif settings['allow_initials']:
                initials = equate_initial(list1[i], list2[i])
                result += 100 if initials else fuzz.ratio(list1[i], list2[i])
            else:
                result += fuzz.ratio(list1[i], list2[i])

        result /= num_names

    else:
        result = True
        for i in range(num_names):
            if settings['allow_prefix']:
                result &= equate_prefix(list1[i], list2[i])
            elif settings['allow_initials']:
                result &= equate_initial(list1[i], list2[i])
            else:
                result &= list1[i] == list2[i]

    return result


def equate_initial(name1, name2):
    """
    Evaluates whether names match, or one name is the initial of the other
    """
    if len(name1) == 0 or len(name2) == 0:
        return False

    if len(name1) == 1 or len(name2) == 1:
        return name1[0] == name2[0]

    return name1 == name2


def equate_prefix(name1, name2):
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

    if equate_prefix(name1, name2):
        return True

    return False


def make_ascii(word):
    """
    Converts unicode-specific characters to their equivalent ascii
    """
    ascii_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore')
    return unicode(ascii_word)


def strip_punctuation(word):
    """
    Strips punctuation from name and lower cases it
    """

    return word.translate(STRIPPED_CHARACTERS).lower()
