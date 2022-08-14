import nompy as np


def test_norm():
    a = np.array([3, 4])
    assert np.linalg.norm(a) == 5
    assert np.linalg.norm(np.array([1, 0, 0])) == 1
    assert np.linalg.norm(np.array([1, 1, 0])) == 2 ** 0.5
