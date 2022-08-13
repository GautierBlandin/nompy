from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from nompy.src.ndarray import ndarray


def __getitem__(self: ndarray, pos):
    if type(pos) == int and len(self.shape) == 1:
        return self.data[pos]

    elif len(pos) == len(self.shape):
        index = 0
        for i, p in enumerate(pos):
            index += p * self.step_sizes[i]
        return self.data[index]
    else:
        raise ValueError("Unsupported Operation")