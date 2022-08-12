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
