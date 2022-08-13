import nompy as np


def test_reshape():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    A = A.reshape((3, 2))

    assert A.shape == (3, 2)
    assert A.size == 6
    assert A.step_sizes == [2, 1]
    assert A.data == [1, 2, 3, 4, 5, 6]
    assert A[0, 0] == 1
    assert A[0, 1] == 2
    assert A[1, 0] == 3
    assert A[1, 1] == 4
    assert A[2, 0] == 5
    assert A[2, 1] == 6

    try:
        A.reshape((3, 3))
        assert False
    except ValueError as e:
        pass

    A = A.reshape([6])
    assert A.shape == [6]
    assert A[0] == 1
    assert A[3] == 4

    A = A.reshape((2, 1, 3))
    assert A[0, 0, 0] == 1
    assert A[1, 0, 1] == 5