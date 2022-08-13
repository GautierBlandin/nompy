import nompy as np


def test_add():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    c = a.__add__(b)
    print(c)
    assert c[0, 0] == 6
    assert c[0, 1] == 8
    assert c[1, 0] == 10
    assert c[1, 1] == 12
