from .settings import *     # noqa
from .suffixes import *     # noqa
from .titles import *       # noqa

# Punctuation that may or may not appear in equivalent names
STRIPPED_CHARACTERS = dict.fromkeys(map(ord, ".'"), None)

SETTINGS = {
    'default': DEFAULT_SETTINGS,
    'strict': STRICT_SETTINGS,
    'lenient': LENIENT_SETTINGS
}
