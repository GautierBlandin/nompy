from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from nompy.src.ndarray import ndarray


def __mul__(self: ndarray, other: ndarray):
    if self.shape == other.shape:
        data = []
        for i in range(self.size):
            data.append(self.data[i] * other.data[i])
        return ndarray(self.shape, data)
    else:
        raise ValueError("Unsupported Operation")