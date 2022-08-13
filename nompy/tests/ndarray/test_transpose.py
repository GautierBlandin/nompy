import nompy as np


def test_transpose():
    a = np.array([[1, 2], [3, 4]])
    a = a.transpose()
    assert a.shape == [2, 2]
    assert a[0, 0] == 1
    assert a[0, 1] == 3
    assert a[1, 0] == 2
    assert a[1, 1] == 4

    a = np.array([[1, 2, 3], [4, 5, 6]])
    a = a.transpose()
    assert a.shape == [3, 2]
    assert a[0, 0] == 1
    assert a[0, 1] == 4
    assert a[1, 0] == 2
    assert a[1, 1] == 5
    assert a[2, 0] == 3
    assert a[2, 1] == 6

    a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    a = a.transpose([0, 2, 1])
    assert a.shape == [2, 2, 2]
    assert a[0, 0, 0] == 1
    assert a[0, 0, 1] == 3
    assert a[0, 1, 0] == 2
    assert a[0, 1, 1] == 4
    assert a[1, 0, 0] == 5
    assert a[1, 0, 1] == 7
    assert a[1, 1, 0] == 6
    assert a[1, 1, 1] == 8
