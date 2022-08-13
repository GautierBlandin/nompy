from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from nompy.src.ndarray import ndarray


import nompy.src._size as _size
import nompy.src._shape as _shape


def reshape(self: ndarray, shape):
    """ Reshapes the array to the given shape.

    Args:
        shape: The new shape of the array. Must be compatible with the current shape
            (i.e. the number of elements must remain the same).
    """
    if _size.compute_size(shape) == self.size:
        self.shape = shape
        self.step_sizes = _shape.compute_step_size(shape)
    else:
        raise ValueError("Incompatible shape")