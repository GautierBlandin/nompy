import nompy as np


def test_get_item():
    arr = np.array([[1, 2, 3], [4, 5, 6]])

    assert arr[0, 0] == 1
    assert arr[0, 1] == 2
    assert arr[0, 2] == 3
    assert arr[1, 0] == 4
    assert arr[1, 1] == 5
    assert arr[1, 2] == 6

    arr2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    assert arr2[0, 0, 0] == 1
    assert arr2[0, 0, 1] == 2
    assert arr2[0, 1, 0] == 3
    assert arr2[0, 1, 1] == 4
    assert arr2[1, 0, 0] == 5
    assert arr2[1, 0, 1] == 6
    assert arr2[1, 1, 0] == 7
    assert arr2[1, 1, 1] == 8