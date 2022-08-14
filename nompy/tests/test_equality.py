import nompy as np


def test_equality():
    assert np.array_equal(np.array([1, 2, 3]), np.array([1, 2, 3]))
    assert not np.array_equal(np.array([1, 2, 3]), np.array([1, 2, 4]))
    assert not np.array_equal(np.array([1, 2, 3]), np.array([1, 2, 3, 4]))
    assert np.array_equal(np.array([[1, 2, 3], [4, 5, 6]]), np.array([[1, 2, 3], [4, 5, 6]]))
    assert np.array_equal(np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]), np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]))
    assert np.array_equal(np.array([[1, 2], [3, 4]]), np.array([[1, 3], [2, 4]]).transpose())
