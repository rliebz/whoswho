from __future__ import unicode_literals

UNIQUE_SUFFIXES = {
    'JR',
    'SR',
    '2',
    'I',
    'II',
    'III',
    'IV',
    'V',
}
"""
This is a set of suffixes that should be mutually exclusive, which is a
subset of nameparser's list of suffixes.

Suffixes that are actually titles are included as suffixes by nameparser,
but differing titles do not necessarily indicate different people.
"""

STRIPPED_CHARACTERS = dict.fromkeys(map(ord, ".'"), None)
"""
This is a dictionary of punctuation that may or may not appear in equivalent
names.
"""