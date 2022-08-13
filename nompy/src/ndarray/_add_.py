from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from nompy.src.ndarray import ndarray


def __add__(self: ndarray, other):
    from nompy.src.ndarray import ndarray
    if isinstance(other, ndarray):
        if self.shape == other.shape:
            data = []
            for i in range(self.size):
                data.append(self.data[i] + other.data[i])
            return ndarray(self.shape, data)
        else:
            raise ValueError("Unsupported Operation")
    elif isinstance(other, self.dtype):
        data = []
        for i in range(self.size):
            data.append(self.data[i] + other)
        return ndarray(self.shape, data)
    else:
        try:  # Try to convert other to the same type as self
            other = self.dtype(other)
            data = []
            for i in range(self.size):
                data.append(self.data[i] + other)
            return ndarray(self.shape, data)
        except Exception:
            raise ValueError("Invalid data type")
