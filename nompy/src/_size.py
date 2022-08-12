def compute_size(shape: list[int]):
    """
    Computes the size of an array with the given shape.
    """
    size = 1
    for i in shape:
        if i <= 0:
            raise ValueError("Shape must be a list of positive integers.")
        size *= i
    return size
