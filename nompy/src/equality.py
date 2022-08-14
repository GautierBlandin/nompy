from nompy.src.ndarray import ndarray
from nompy.src._shape import iter_ndim_shape


def array_equal(arr: ndarray, other: ndarray):
    if not arr.shape == other.shape:
        return False

    for pos in iter_ndim_shape(arr.shape):
        if not arr[pos] == other[pos]:
            return False

    return True
