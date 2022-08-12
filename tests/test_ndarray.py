from src.array_creation import array


def test_get_item():
    arr = array([[1, 2, 3], [4, 5, 6]])

    assert arr[0, 0] == 1
    assert arr[0, 1] == 2
    assert arr[0, 2] == 3
    assert arr[1, 0] == 4
    assert arr[1, 1] == 5
    assert arr[1, 2] == 6

    arr2 = array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    assert arr2[0, 0, 0] == 1
    assert arr2[0, 0, 1] == 2
    assert arr2[0, 1, 0] == 3
    assert arr2[0, 1, 1] == 4
    assert arr2[1, 0, 0] == 5
    assert arr2[1, 0, 1] == 6
    assert arr2[1, 1, 0] == 7
    assert arr2[1, 1, 1] == 8


def test_matrix_multiplication():
    A = array([[1, 2], [3, 4]])
    B = array([[5, 6], [7, 8]])
    C = A @ B
    assert C[0, 0] == 19
    assert C[0, 1] == 22
    assert C[1, 0] == 43
    assert C[1, 1] == 50


def test_reshape():
    A = array([[1, 2, 3], [4, 5, 6]])
    A.reshape((3, 2))

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

    A.reshape([6])
    assert A.shape == [6]
    assert A[0] == 1
    assert A[3] == 4

    A.reshape((2, 1, 3))
    assert A[0, 0, 0] == 1
    assert A[1, 0, 1] == 5


