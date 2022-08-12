import nompy.src._broadcast as _broadcast


def test_is_broadcastable():
    shape1 = [1]
    shape2 = [1, 2, 3]

    assert _broadcast.is_broadcastable(shape1, shape2)
    assert _broadcast.is_broadcastable(shape2, shape1)

    shape1 = [1, 2]
    assert not _broadcast.is_broadcastable(shape1, shape2)

    shape1 = [5, 1, 3, 1]
    shape2 = [3, 3, 4]
    assert _broadcast.is_broadcastable(shape1, shape2)

    shape2 = [3, 4, 1]
    assert not _broadcast.is_broadcastable(shape1, shape2)


def test_broadcast():
    shape1 = [1, 2, 3]
    shape2 = [1]

    assert _broadcast.broadcast(shape1, shape2) == [1, 2, 3]
    shape2 = [3]
    assert _broadcast.broadcast(shape1, shape2) == [1, 2, 3]

    shape1 = [5, 3, 1, 3, 1, 6]
    shape2 = [2, 1, 4, 6]

    assert _broadcast.broadcast(shape1, shape2) == [5, 3, 2, 3, 4, 6]
