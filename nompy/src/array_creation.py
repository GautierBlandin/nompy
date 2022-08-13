import nompy.src._size as _size
import nompy.src._shape as _shape
import nompy.src._flatten as _flatten


def zeros(shape: list[int]):
    from nompy.src.ndarray import ndarray
    """
    Creates a nompy array of zeros with the given shape.
    """
    size = _size.compute_size(shape)
    data = [0] * size
    return ndarray(shape, data)


def ones(shape: list[int]):
    from nompy.src.ndarray import ndarray
    """
    Creates a nompy array of ones with the given shape.
    """
    size = _size.compute_size(shape)
    data = [1] * size
    return ndarray(shape, data)


def array(data: list):
    from nompy.src.ndarray import ndarray
    """
    Creates a nompy array with the given data and shape.
    """
    shape = _shape.compute_shape(data)
    flattened = _flatten.flatten(data)
    _shape.check_integrity(shape, flattened)
    return ndarray(shape, flattened)
