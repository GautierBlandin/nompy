from nompy.src.array_creation import zeros, array
from nompy.src._shape import iter_ndim_shape

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from nompy.src.ndarray import ndarray


def is_broadcastable(shape1, shape2):
    n = min(len(shape1), len(shape2))
    for i in range(1, n+1):
        if shape1[-i] != shape2[-i] and shape1[-i] != 1 and shape2[-i] != 1:
            return False
    return True


def broadcast(shape1, shape2):
    if not is_broadcastable(shape1, shape2):
        raise ValueError("Shapes are not broadcastable.")

    n = min(len(shape1), len(shape2))
    m = max(len(shape1), len(shape2))

    if len(shape1) == n:
        larger = shape2
    else:
        larger = shape1

    shape = [0] * m
    for i in range(1, n+1):
        if shape1[-i] == 1:
            shape[-i] = shape2[-i]
        elif shape2[-i] == 1:
            shape[-i] = shape1[-i]
        elif shape1[-i] == shape2[-i]:
            shape[-i] = shape1[-i]
    for i in range(n+1, m+1):
        shape[-i] = larger[-i]
    return shape


def broadcast_function_array(array1, array2, operation):
    if is_broadcastable(array1.shape, array2.shape):
        result_shape = broadcast(array1.shape, array2.shape)
        result = zeros(result_shape)
        for pos in iter_ndim_shape(result.shape):
            result[pos] = operation(array1._get_broadcast_item(pos), array2._get_broadcast_item(pos))
        return result
    else:
        raise ValueError("Unsupported Operation")


def broadcast_function_value(arr, value, operation):
    if isinstance(value, arr.dtype):
        return broadcast_function_array(array([value]), arr, operation)
    else: # Try to convert value to the same type as arr
        try:
            value = arr.dtype(value)
            return broadcast_function_array(array([value]), arr, operation)
        except Exception:
            raise ValueError("Invalid data type")


def broadcast_function(arr, other, operation):
    from nompy.src.ndarray import ndarray
    if isinstance(other, ndarray):
        return broadcast_function_array(arr, other, operation)
    else:
        return broadcast_function_value(arr, other, operation)
