# -*- coding: utf-8 -*-
from __future__ import unicode_literals


UNIQUE_SUFFIXES = set([
    'jr',
    'jnr',
    'sr',
    'snr',
    '2',
    'i',
    'ii',
    'iii',
    'iv',
    'v',
])
"""
A set of suffixes that should be mutually exclusive, which is a
subset of nameparser's set of suffixes.

Suffixes that are actually titles are included as suffixes by nameparser,
but differing titles do not necessarily indicate different people.
"""


EQUIVALENT_SUFFIXES = {
    'jnr': 'jr',
    'snr': 'sr',
}
"""
A dict of equivalent suffixes. Keys will be converted to values when
suffixes are compared.
"""


MISC_SUFFIXES = set([
    'esq',
    'esquire',
    'clu',
    'chfc',
    'cfp',
    'md',
    'phd',
    'mp',
    'qc',
    'dmd',
    'do',
    'dds',
    'dpm',
])
"""
Non-unique suffixes kept to ensure the set is up to date with nameparser
"""
