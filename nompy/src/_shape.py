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


def iter_ndim_shape(shape):
    pos = [0] * len(shape)
    size = _size.compute_size(shape)
    for _ in range(size):
        yield pos
        pos = _increment_pos(pos, shape)


def _increment_pos(pos, shape):
    for i in range(1, len(pos) + 1):
        if pos[-i] < shape[-i] - 1:
            pos[-i] += 1
            break
        elif pos[-i] == shape[-i] - 1:
            pos[-i] = 0
    return pos
