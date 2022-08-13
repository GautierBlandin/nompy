from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from nompy.src.ndarray import ndarray


def transpose(self: ndarray, permutation=None):
    from nompy.src.ndarray import ndarray
    if permutation is None:
        new_shape = list(reversed(self.shape))
        new_step_sizes = list(reversed(self.step_sizes))
        return ndarray(new_shape, self.data, dtype=self.dtype, step_sizes=new_step_sizes)
    else:
        new_step_sizes = [0] * len(self.step_sizes)
        new_shape = [0] * len(self.shape)
        for i, p in enumerate(permutation):
            new_step_sizes[i] = self.step_sizes[p]
            new_shape[i] = self.shape[p]
        return ndarray(new_shape, self.data, dtype=self.dtype, step_sizes=new_step_sizes)
