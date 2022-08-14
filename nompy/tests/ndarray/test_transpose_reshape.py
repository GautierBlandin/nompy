import nompy as np


def test_transpose_reshape():
    a = np.array([[1, 2], [3, 4]])
    a = a.transpose()
    a = a.reshape([4])
    assert a[0] == 1
    assert a[1] == 3
    assert a[2] == 2
    assert a[3] == 4
    a = a.reshape([2, 2])
    assert a[0, 0] == 1
    assert a[0, 1] == 3
    assert a[1, 0] == 2
    assert a[1, 1] == 4
    a = a.transpose()
    assert a[0, 0] == 1
    assert a[0, 1] == 2
    assert a[1, 0] == 3
    assert a[1, 1] == 4

    a = np.array([[1, 2, 3], [4, 5, 6]])
    a = a.transpose()
    a = a.reshape((2, 3))
    assert a[0, 0] == 1
    assert a[0, 1] == 4
    assert a[0, 2] == 2
    assert a[1, 0] == 5
    assert a[1, 1] == 3
    assert a[1, 2] == 6
