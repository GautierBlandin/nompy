from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from nompy.src.ndarray import ndarray


def _get_actual_pos(self: ndarray, pos):
    """ Return item at given broadcast position
    """
    actual_pos = []
    for i in range(1, len(pos) + 1):
        p = pos[-i]
        if i > len(self.shape):
            break
        if self.shape[-i] == 1:
            actual_pos.append(0)
        elif p < self.shape[-i]:
            actual_pos.append(p)
        else:
            raise IndexError("Index out of range")
    actual_pos.reverse()
    return actual_pos


def _get_broadcast_item(self: ndarray, pos):
    actual_pos = self._get_actual_pos(pos)
    return self[actual_pos]
