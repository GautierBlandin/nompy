from nompy.src.ndarray import ndarray


def dot(arr: ndarray, other: ndarray):
    if not len(arr.shape) == 1 or not len(arr.shape) == 1:
        raise ValueError("Dot product can only be applied to two 1d arrays")
    if not arr.shape[0] == other.shape[0]:
        raise ValueError("Incompatible vector sizes: dot product only works on array of same size")
    result = 0
    for i in range(arr.shape[0]):
        result += arr[i] * other[i]
    return result
