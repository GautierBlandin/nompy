import nompy.src._size as _size
import nompy.src._shape as _shape


class ndarray:
    def __init__(self, shape, data, dtype:type = None, strides=None, base=None):
        self.shape = shape
        self.data = data
        self.size = _size.compute_size(shape)
        if strides is None:
            self.strides = _shape.compute_step_size(shape)
        else:
            self.strides = strides
        if dtype is not None:
            self.dtype = dtype
        else:
            if len(data) > 0:
                self.dtype = type(data[0])
            else:
                self.dtype = int
        self.base = base

    def __str__(self):
        return f'data: {self.data}, shape: {self.shape}, step_sizes: {self.strides}'

    from ._getitem_ import __getitem__, _get_from_1d_index
    from ._setitem_ import __setitem__, _set_from_1d_index
    from ._matmul import __matmul__
    from .reshape import reshape
    from .broadcast import _get_actual_pos, _get_broadcast_item
    from ._broadcastable_operations_ import __add__, __mul__, __sub__, __truediv__, __floordiv__, __mod__
    from .transpose import transpose
