#!/usr/bin/env python3

__all__ = [
    'read',
    'bytes',
]

import os
import builtins

def read(arg):
    if hasattr(arg, 'read'):
        return arg.read()
    elif os.path.exists(arg):
        return open(arg, 'rb').read()
    else:
        return arg

def bytes(arg):
    # TODO: don't call read in here, add more functions and fix the users
    arg = read(arg)
    if isinstance(arg, str):
        arg = arg.encode()
    if isinstance(arg, builtins.bytes):
        return arg
    cls = type(arg)
    raise FileNotFoundError(f"Could not cast to bytes: {cls.__name__!r}")
