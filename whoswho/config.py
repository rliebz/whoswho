# -*- coding: utf-8 -*-
from __future__ import unicode_literals


STRIPPED_CHARACTERS = dict.fromkeys(map(ord, ".'"), None)
"""
A dictionary of punctuation that may or may not appear in equivalent
names.
"""


UNIQUE_SUFFIXES = {
    'jr',
    'sr',
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
}
"""
Non-unique suffixes kept to ensure the set is up to date with nameparser
"""


MALE_TITLES = {
    'sir',
    'king',
    'master',
    'uncle',
    'brother',
    'father',
    'pope',
    'mr',
    'mister',
    'lord',
    'duke',
    'priest',
    'patriarch',
    'prince',
    'his',
    'archduke',
    'emperor',
    'tsar',
    'goodman',
    "marquis",
    "marquess",
    "marquise",
    'abbot',
}


FEMALE_TITLES = {
    'dame',
    'queen',
    'maid',
    'auntie',
    'aunt',
    'sister',
    'mother',
    'miss',
    'misses',
    'mrs',
    'ms',
    'madam',
    'madame',
    'lady',
    'dutchess',
    'priestess',
    'matriarch',
    'princess',
    'her',
    'archduchess',
    'empress',
    'tsarina',
    'goodwife',
    "marchioness",
    'abbess',
}
"""
Sets of titles that are either exclusively male or exclusively female,
which are subsets of nameparser's set of titles.

Below are all unsorted titles. This set is kept to be tested against the full
set of titles from nameparser in case it changes.
"""

# TODO: Gender-specific titles may still be in this list.
GENDERLESS_TITLES = {
    'dr',
    'doctor',
    'rev',
    'ab',
    '2ndlt',
    'amn',
    '1stlt',
    'a1c',
    'capt',
    'sra',
    'maj',
    'ssgt',
    'ltcol',
    'tsgt',
    'col',
    'briggen',
    '1stsgt',
    'majgen',
    'smsgt',
    'ltgen',
    'cmsgt',
    'ccmsgt',
    'cmsaf',
    'pvt',
    '2lt',
    'pv2',
    '1lt',
    'pfc',
    'cpt',
    'spc',
    'cpl',
    'ltc',
    'sgt',
    'ssg',
    'bg',
    'sfc',
    'mg',
    'msg',
    'ltg',
    '1sgt',
    'sgm',
    'csm',
    'sma',
    'wo1',
    'wo2',
    'wo3',
    'wo4',
    'wo5',
    'ens',
    'sa',
    'ltjg',
    'sn',
    'lt',
    'po3',
    'lcdr',
    'po1',
    'po2',
    'cdr',
    'cpo',
    'scpo',
    'mcpo',
    'vadm',
    'mcpoc',
    'adm',
    'mpco-cg',
    'lcpl',
    'gysgt',
    'bgen',
    'msgt',
    'mgysgt',
    'gen',
    'sgtmaj',
    'sgtmajmc',
    'wo-1',
    'cwo-2',
    'cwo-3',
    'cwo-4',
    'cwo-5',
    'rdml',
    'radm',
    'mcpon',
    'fadm',
    'cwo2',
    'cwo3',
    'cwo4',
    'cwo5',
    'rt',
    'representative',
    'rep',
    'senator',
    'cardinal',
    'secretary',
    'state',
    'foreign',
    'minister',
    'speaker',
    'president',
    'pres',
    'ceo',
    'cfo',
    'deputy',
    'dpty',
    'executive',
    'exec',
    'vice',
    'vc',
    'councillor',
    'manager',
    'mgr',
    'alderman',
    'delegate',
    'mayor',
    'lieutenant',
    'governor',
    'prefect',
    'prelate',
    'premier',
    'burgess',
    'ambassador',
    'envoy',
    "attaché",
    "chargé d'affaires",
    'provost',
    'viscount',
    'baron',
    'leader',
    'friar',
    'superior',
    'reverend',
    'bishop',
    'archbishop',
    'metropolitan',
    'presbyter',
    'catholicos',
    'vicar',
    'chaplain',
    'canon',
    'pastor',
    'primate',
    'servant',
    'venerable',
    'blessed',
    'saint',
    'member',
    'solicitor',
    'mufti',
    'grand',
    'chancellor',
    'barrister',
    'bailiff',
    'attorney',
    'advocate',
    'deacon',
    'archdeacon',
    'acolyte',
    'elder',
    'monsignor',
    'almoner',
    'prof',
    'colonel',
    'general',
    'commodore',
    'air',
    'corporal',
    'staff',
    'chief',
    'first',
    'sergeant',
    'admiral',
    'high',
    'rear',
    'brigadier',
    'captain',
    'group',
    'commander',
    'commander-in-chief',
    'wing',
    'adjutant',
    'director',
    'dir',
    'generalissimo',
    'resident',
    'surgeon',
    'officer',
    'controller',
    'academic',
    'analytics',
    'business',
    'credit',
    'financial',
    'information',
    'security',
    'knowledge',
    'marketing',
    'operating',
    'petty',
    'risk',
    'strategy',
    'technical',
    'warrant',
    'corporate',
    'customs',
    'field',
    'flag',
    'flying',
    'intelligence',
    'pilot',
    'police',
    'political',
    'revenue',
    'senior',
    'sr',
    'junior',
    'jr',
    'private',
    'principal',
    'prin',
    'coach',
    'nurse',
    'nanny',
    'docent',
    'lama',
    'druid',
    'archdruid',
    'rabbi',
    'rebbe',
    'buddha',
    'ayatollah',
    'imam',
    'bodhisattva',
    'mullah',
    'mahdi',
    'saoshyant',
    'tirthankar',
    'vardapet',
    'pharaoh',
    'sultan',
    'sultana',
    'maharajah',
    'maharani',
    'vizier',
    'chieftain',
    'comptroller',
    'courtier',
    'curator',
    'doyen',
    'edohen',
    'ekegbian',
    'elerunwon',
    'forester',
    'gentiluomo',
    'headman',
    'intendant',
    'lamido',
    'marcher',
    'prior',
    'pursuivant',
    'rangatira',
    'ranger',
    'registrar',
    'seigneur',
    'shehu',
    'sheikh',
    'sheriff',
    'subaltern',
    'subedar',
    'sysselmann',
    'timi',
    'treasurer',
    'verderer',
    'warden',
    'hereditary',
    'woodman',
    'bearer',
    'banner',
    'swordbearer',
    'apprentice',
    'journeyman',
    'adept',
    'akhoond',
    'arhat',
    'bwana',
    'bard',
    'hajji',
    'baba',
    'effendi',
    'giani',
    'gyani',
    'guru',
    'siddha',
    'pir',
    'murshid',
    'attache',
    'prime',
    'united',
    'states',
    'national',
    'associate',
    'assoc',
    'assistant',
    'asst',
    'supreme',
    'appellate',
    'judicial',
    "queen's",
    "king's",
    'bench',
    'right',
    'majesty',
    'kingdom',
    'royal',
    'honorable',
    'honourable',
    'hon',
    'magistrate',
    'mag',
    'judge',
    'designated',
    'us',
    'uk',
    'federal',
    'district',
    'arbitrator',
    'pro',
    'se',
    'law',
    'clerk',
    'docket',
    'pslc',
    'special',
    'municipal',
    'tax',
    'civil',
    'criminal',
    'family',
    'presiding',
    'division',
    'edmi',
    'discovery',
    'magistrate-judge',
    'mag-judge',
    'senior-judge',
    'mag/judge',
}