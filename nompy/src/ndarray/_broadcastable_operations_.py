from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nompy.src.ndarray import ndarray

import nompy.src._broadcast as _broadcast


def __add__(self: ndarray, other):
    return _broadcast.broadcast_function(self, other, lambda x, y: x + y)


def __mul__(self: ndarray, other: ndarray):
    return _broadcast.broadcast_function(self, other, lambda x, y: x * y)


def __sub__(self: ndarray, other: ndarray):
    return _broadcast.broadcast_function(self, other, lambda x, y: x - y)


def __truediv__(self: ndarray, other: ndarray):
    return _broadcast.broadcast_function(self, other, lambda x, y: x / y)


def __floordiv__(self: ndarray, other: ndarray):
    return _broadcast.broadcast_function(self, other, lambda x, y: x // y)


def __mod__(self: ndarray, other: ndarray):
    return _broadcast.broadcast_function(self, other, lambda x, y: x % y)
