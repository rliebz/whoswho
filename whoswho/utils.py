# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import re
import unicodedata
from difflib import SequenceMatcher

from whoswho.config import STRIPPED_CHARACTERS


def compare_name_component(list1, list2, settings, use_ratio=False):
    """
    Compare a list of names from a name component based on settings
    """
    if not list1[0] or not list2[0]:
        not_required = not settings['required']
        return not_required * 100 if use_ratio else not_required

    if len(list1) != len(list2):
        return False

    compare_func = _ratio_compare if use_ratio else _normal_compare
    return compare_func(list1, list2, settings)


def _ratio_compare(list1, list2, settings):
    ratio = 0
    for i, name1 in enumerate(list1):
        name2 = list2[i]

        # If initials don't match, result for this item is 0
        if (len(name1) == 1 or len(name2) == 1) and not equate_initial(name1, name2):
            continue

        if settings['allow_prefix']:
            ratio += 100 if equate_prefix(name1, name2) else seq_ratio(name1, name2)
        elif settings['allow_initials']:
            ratio += 100 if equate_initial(name1, name2) else seq_ratio(name1, name2)
        else:
            ratio += seq_ratio(name1, name2)

    return ratio / len(list1)


def _normal_compare(list1, list2, settings):
    result = True
    for i, name1 in enumerate(list1):
        name2 = list2[i]

        if settings['allow_prefix']:
            result &= equate_prefix(name1, name2)
        elif settings['allow_initials']:
            result &= equate_initial(name1, name2)
        else:
            result &= name1 == name2

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
    """
    Evaluates whether names match based on common nickname patterns

    This is not currently used in any name comparison
    """
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
    if sys.version_info < (3, 0, 0):
        word = unicode(word)
    else:
        word = str(word)

    normalized = unicodedata.normalize('NFKD', word)

    return normalized.encode('ascii', 'ignore').decode('utf-8')


def strip_punctuation(word):
    """
    Strips punctuation from name and lower cases it
    """

    return word.translate(STRIPPED_CHARACTERS).lower()


def seq_ratio(word1, word2):
    """
    Returns sequence match ratio for two words
    """
    raw_ratio = SequenceMatcher(None, word1, word2).ratio()
    return int(round(100 * raw_ratio))


def deep_update_dict(default, options):
    """
    Updates the values in a nested dict, while unspecified values will remain
    unchanged
    """
    for key in options.keys():
        default_setting = default.get(key)
        new_setting = options.get(key)
        if isinstance(default_setting, dict):
            deep_update_dict(default_setting, new_setting)
        else:
            default[key] = new_setting
