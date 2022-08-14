import nompy as np


def test_dot():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    assert np.dot(a, b) == 32
