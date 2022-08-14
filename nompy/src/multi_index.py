from nompy.src._shape import compute_step_size


def pos_to_index(pos, strides):
    index = 0
    for i, p in enumerate(pos):
        index += p * strides[i]
    return index


def index_to_pos(index, shape):
    base_strides = compute_step_size(shape)
    pos = []
    for i, s in enumerate(base_strides):
        pos.append(index // s)
        index = index % s
    return pos

