from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from nompy.src.ndarray import ndarray


import nompy.src._size as _size


def reshape(self: ndarray, shape):
    """ Reshapes the array to the given shape.

    Args:
        shape: The new shape of the array. Must be compatible with the current shape
            (i.e. the number of elements must remain the same).
    """
    from nompy.src.ndarray import ndarray
    if _size.compute_size(shape) == self.size:
        return ndarray(shape, self.data, base=self)
    else:
        raise ValueError("Incompatible shape")