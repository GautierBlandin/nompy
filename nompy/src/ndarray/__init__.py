import nompy.src._size as _size
import nompy.src._shape as _shape


class ndarray:
    def __init__(self, shape, data, dtype:type = None, step_sizes=None):
        self.shape = shape
        self.data = data
        self.size = _size.compute_size(shape)
        if step_sizes is None:
            self.step_sizes = _shape.compute_step_size(shape)
        else:
            self.step_sizes = step_sizes
        if dtype is not None:
            self.dtype = dtype
        else:
            if len(data) > 0:
                self.dtype = type(data[0])
            else:
                self.dtype = int

    def __str__(self):
        return f'data: {self.data}, shape: {self.shape}, step_sizes: {self.step_sizes}'

    from ._getitem_ import __getitem__
    from ._setitem_ import __setitem__
    from ._mul_ import __mul__
    from ._matmul import __matmul__
    from .reshape import reshape
