# -*- coding: utf-8 -*-
from __future__ import unicode_literals


UNIQUE_SUFFIXES = {
    'jr',
    'jnr',  # TODO: compatible with jr
    'sr',
    'snr',  # TODO: compatible with sr
    '2',
    'i',
    'ii',
    'iii',
    'iv',
    'v',
}
"""
A set of suffixes that should be mutually exclusive, which is a
subset of nameparser's set of suffixes.

Suffixes that are actually titles are included as suffixes by nameparser,
but differing titles do not necessarily indicate different people.
"""


MISC_SUFFIXES = {
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
}
"""
Non-unique suffixes kept to ensure the set is up to date with nameparser
"""
