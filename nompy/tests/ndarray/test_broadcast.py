import nompy as np


def test_get_actual_post():
    a = np.array([[[1, 2], [3, 4]]])
    assert a.shape == [1, 2, 2]
    pos = [3, 4, 0, 1]
    assert a._get_actual_pos(pos) == [0, 0, 1]
    try:
        pos = [3, 4, 0, 2]
        a._get_actual_pos(pos)
        assert False
    except IndexError:
        pass


def test_get_broadcast_item():
    a = np.array([[[1, 2], [3, 4]]])
    assert a._get_broadcast_item([3, 4, 0, 1]) == 2
    assert a._get_broadcast_item([3, 4, 0, 0]) == 1
    assert a._get_broadcast_item([4, 4, 1, 0]) == 3
    assert a._get_broadcast_item([7, 4, 4, 1, 1]) == 4
