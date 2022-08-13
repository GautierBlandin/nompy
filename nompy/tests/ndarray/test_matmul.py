from nompy.src.array_creation import array


def test_matrix_multiplication():
    A = array([[1, 2], [3, 4]])
    B = array([[5, 6], [7, 8]])
    C = A @ B
    assert C[0, 0] == 19
    assert C[0, 1] == 22
    assert C[1, 0] == 43
    assert C[1, 1] == 50