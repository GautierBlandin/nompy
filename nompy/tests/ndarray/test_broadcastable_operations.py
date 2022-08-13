import nompy as np


def test_add():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    c = a + b
    assert c[0, 0] == 6
    assert c[0, 1] == 8
    assert c[1, 0] == 10
    assert c[1, 1] == 12

    a = np.array([[1, 2], [3, 4]])
    b = np.array([[1], [2]])
    c = a + b
    assert c[0, 0] == 2
    assert c[0, 1] == 3
    assert c[1, 0] == 5
    assert c[1, 1] == 6


def test_sub():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    c = a - b
    assert c[0, 0] == -4
    assert c[0, 1] == -4
    assert c[1, 0] == -4
    assert c[1, 1] == -4

    a = np.array([[1, 2], [3, 4]])
    b = np.array([[1], [2]])
    c = a - b
    assert c[0, 0] == 0
    assert c[0, 1] == 1
    assert c[1, 0] == 1
    assert c[1, 1] == 2
