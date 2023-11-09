__all__ = [
    'singular',
    'plural',
    'list',
]

import builtins
from .types import Plural

def singular(o):
    if isinstance(o, Plural) and len(o) == 1:
        p, = o
        return p
    else:
        return o

def plural(o):
    if isinstance(o, Plural):
        return o
    else:
        return [o]

def list(o):
    if isinstance(o, Plural):
        return builtins.list(o)
    else:
        return [o]
