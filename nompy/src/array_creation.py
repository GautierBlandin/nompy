import nompy.src._size as _size
import nompy.src._shape as _shape
import nompy.src._flatten as _flatten


def zeros(shape: list[int], dtype: type = float):
    from nompy.src.ndarray import ndarray
    """
    Creates a nompy array of zeros with the given shape.
    """
    size = _size.compute_size(shape)
    data = [dtype(0)] * size
    return ndarray(shape, data)


def ones(shape: list[int], dtype: type = float):
    from nompy.src.ndarray import ndarray
    """
    Creates a nompy array of ones with the given shape.
    """
    size = _size.compute_size(shape)
    data = [dtype(1)] * size
    return ndarray(shape, data)


def array(data: list, dtype: type = float):
    from nompy.src.ndarray import ndarray
    """
    Create a nompy array with the given data and shape.
    """
    shape = _shape.compute_shape(data)
    flattened = _flatten.flatten(data)
    flattened = [dtype(x) for x in flattened]
    _shape.check_integrity(shape, flattened)
    return ndarray(shape, flattened)


def arange(arg1, end=None, step=None):
    """ Create a 1d nompy array with data identical to range(arg1, end, step). """
    if step is not None and end is not None:
        return array(list(range(arg1, end, step)))

    if end is not None:
        return array(list(range(arg1, end)))

    return array(list(range(arg1)))
