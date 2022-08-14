from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nompy.src.ndarray import ndarray

import nompy.src.multi_index as multi_index


def __getitem__(self: ndarray, pos):
    if type(pos) == int and len(self.shape) == 1:
        if self.base is None:
            return self.data[pos]
        else:
            return self.base._get_from_1d_index(pos)

    elif len(pos) == len(self.shape):
        index = multi_index.pos_to_index(pos, self.strides)
        if self.base is None:
            return self.data[index]
        else:
            return self.base._get_from_1d_index(index)
    else:
        raise ValueError("Unsupported Operation")


def _get_from_1d_index(self: ndarray, index: int):
    pos = multi_index.index_to_pos(index, self.shape)
    return self[pos]
