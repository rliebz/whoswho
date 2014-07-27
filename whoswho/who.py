from copy import deepcopy

from whoswho.model import Name
from whoswho.config import SETTINGS
from whoswho.utils import deep_update_dict


def match(fullname1, fullname2, strictness='default', options=None):
    """
    Takes two names and returns true if they describe the same person.

    :param string fullname1: first human name
    :param string fullname2: second human name
    :param string strictness: strictness settings to use
    :param dict options: custom strictness settings updates
    :return bool: the names match
    """

    if options is not None:
        settings = deepcopy(SETTINGS[strictness])
        deep_update_dict(settings, options)
    else:
        settings = SETTINGS[strictness]

    n1 = Name(fullname1)
    n2 = Name(fullname2)

    return n1.deep_compare(n2, settings)


def ratio(fullname1, fullname2, strictness='default', options=None):
    """
    Takes two names and returns true if they describe the same person.
    Uses difflib's sequence matching on a per-field basis for names

    :param string fullname1: first human name
    :param string fullname2: second human name
    :param string strictness: strictness settings to use
    :param dict options: custom strictness settings updates
    :return int: sequence ratio match (out of 100)
    """

    if options is not None:
        settings = deepcopy(SETTINGS[strictness])
        deep_update_dict(settings, options)
    else:
        settings = SETTINGS[strictness]

    n1 = Name(fullname1)
    n2 = Name(fullname2)

    return n1.ratio_deep_compare(n2, settings)