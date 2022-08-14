import nompy as np


def test_arange():
    assert np.array_equal(np.arange(4), np.array([0, 1, 2, 3]))
    assert np.array_equal(np.arange(1, 4), np.array([1, 2, 3]))
    assert np.array_equal(np.arange(1, 4, 2), np.array([1, 3]))
    assert np.array_equal(np.arange(10, 0, -1), np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
