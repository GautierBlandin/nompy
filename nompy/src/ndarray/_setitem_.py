from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from nompy.src.ndarray import ndarray


import nompy.src.multi_index as multi_index


def __setitem__(self: ndarray, pos, value):
    if type(pos) == int and len(self.shape) == 1:
        if self.base is None:
            self.data[pos] = value
        else:
            self.base._set_from_1d_index(pos, value)

    elif len(pos) == len(self.shape):
        index = multi_index.pos_to_index(pos, self.strides)
        if self.base is None:
            self.data[index] = value
        else:
            self.base._get_from_1d_index(index, value)

    else:
        raise ValueError("Unsupported Operation")


def _set_from_1d_index(self: ndarray, index: int, value):
    pos = multi_index.index_to_pos(index, self.shape)
    self[pos] = value
