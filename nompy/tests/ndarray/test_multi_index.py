import nompy.src.multi_index as multi_index


def test_pos_to_index():
    pos = [1, 0, 0, 1]
    strides = [1, 2, 4, 8]
    assert multi_index.pos_to_index(pos, strides) == 1 + 0 * 2 + 0 * 4 + 1 * 8


def test_index_to_pos():
    index = 1 + 0 * 2 + 0 * 4 + 1 * 8
    shape = [2, 2, 2, 2]
    assert multi_index.index_to_pos(index, shape) == [1, 0, 0, 1]
    index = 1 + 1 * 2 + 0 * 4 + 1 * 8
    assert multi_index.index_to_pos(index, shape) == [1, 0, 1, 1]
