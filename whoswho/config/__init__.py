from .settings import *
from .suffixes import *
from .titles import *

# Punctuation that may or may not appear in equivalent names
STRIPPED_CHARACTERS = dict.fromkeys(map(ord, ".'"), None)

SETTINGS = {
    'default': DEFAULT_SETTINGS,
    'strict': STRICT_SETTINGS,
    'lenient': LENIENT_SETTINGS
}