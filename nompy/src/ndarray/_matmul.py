from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from nompy.src.ndarray import ndarray


def __matmul__(self: ndarray, other):
    from nompy.src.array_creation import array
    if not len(self.shape) == 2 or not len(other.shape) == 2:
        raise ValueError("Unsupported Operation")
    if self.shape[1] == other.shape[0]:
        result = [[0] * other.shape[1] for _ in range(self.shape[0])]
        for i in range(self.shape[0]):
            for j in range(other.shape[1]):
                for k in range(self.shape[1]):
                    result[i][j] += self[i, k] * other[k, j]
        return array(result)
    else:
        raise ValueError("Incompatible matrix sizes")