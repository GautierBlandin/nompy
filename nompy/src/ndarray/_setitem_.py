from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from nompy.src.ndarray import ndarray


def __setitem__(self: ndarray, pos, value):
    if type(pos) == int and len(self.shape) == 1:
        self.data[pos] = value
        return

    if len(pos) == len(self.shape):
        index = 0
        for i, p in enumerate(pos):
            index += p * self.step_sizes[i]
        self.data[index] = value
    else:
        raise ValueError("Unsupported Operation")