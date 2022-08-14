from nompy.src.ndarray import ndarray


def norm(arr: ndarray):
    if not len(arr.shape) == 1:
        raise ValueError("Norm can only be applied to 1d arrays")
    result = 0
    for i in range(arr.shape[0]):
        result += arr[i] ** 2
    return result ** 0.5
