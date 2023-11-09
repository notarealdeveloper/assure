__all__ = [
    'vector',
    'vectors',
]

import numpy as np

def vector(o):
    if not hasattr(o, 'ndim'):
        raise ValueError
    if o.ndim == 1:
        return o
    if o.ndim > 1:
        return o.squeeze()
    raise TypeError

def vectors(o):
    if isinstance(o, (list, tuple)):
        return np.stack([vector(p) for p in o])
    if hasattr(o, 'ndim'):
        if o.ndim == 1:
            return o[None, ...]
        if o.ndim == 2:
            return o
        if o.ndim > 2:
            raise ValueError
    raise TypeError
