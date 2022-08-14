from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nompy.src.ndarray import ndarray


def transpose(self: ndarray, permutation=None):
    from nompy.src.ndarray import ndarray
    if permutation is None:
        new_shape = list(reversed(self.shape))
        new_step_sizes = list(reversed(self.strides))
        if self.base is not None:
            return ndarray(new_shape, self.data, dtype=self.dtype, strides=new_step_sizes, base=self.base)
        else:
            return ndarray(new_shape, self.data, dtype=self.dtype, strides=new_step_sizes, base=self)
    else:
        new_step_sizes = [0] * len(self.strides)
        new_shape = [0] * len(self.shape)
        for i, p in enumerate(permutation):
            new_step_sizes[i] = self.strides[p]
            new_shape[i] = self.shape[p]
        if self.base is not None:
            return ndarray(new_shape, self.data, dtype=self.dtype, strides=new_step_sizes, base=self.base)
        else:
            return ndarray(new_shape, self.data, dtype=self.dtype, strides=new_step_sizes, base=self)
