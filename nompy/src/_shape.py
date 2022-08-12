from nompy.src import _size


def compute_shape(data: list):
    """
    Computes the shape of the given data.
    """
    shape = []
    arr = data
    while type(arr) == list:
        if len(arr) == 0:
            raise ValueError("Every list in the data must have length > 0.")
        shape.append(len(arr))
        arr = arr[0]
    return shape


def compute_step_size(shape: list[int]) -> list[int]:
    """
    Computes the step size of an array with the given shape.
    """
    size = _size.compute_size(shape)
    step = size
    step_sizes = []
    for i in shape:
        step = step // i
        step_sizes.append(step)
    return step_sizes


def check_integrity(shape, data):
    """
    Checks the integrity of the given data.
    """
    size = _size.compute_size(shape)
    if len(data) != size:
        raise ValueError("The data has the wrong size.")
    return True
