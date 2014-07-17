from model import Name


def is_it(fullname1, fullname2):
    """
    Takes two names and returns true if they describe the same person.

    :param string fullname1: first human name
    :param string fullname2: second human name
    :return bool: the names match
    """

    n1 = Name(fullname1)
    n2 = Name(fullname2)

    return n1.deep_compare(n2)


def can_it_be(fullname1, fullname2):
    """
    Takes two names and returns true if they describe the same person.
    Uses fuzzywuzzy's fuzzy matching on a per-field basis for names

    :param string fullname1: first human name
    :param string fullname2: second human name
    :return int: ratio fuzzy match (out of 100)
    """

    n1 = Name(fullname1)
    n2 = Name(fullname2)

    return n1.ratio_deep_compare(n2)