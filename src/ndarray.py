from __future__ import annotations
from typing import Union

import src._size as _size
import src._shape as _shape


class ndarray:
    def __init__(self, shape, data, dtype:type = None):
        self.shape = shape
        self.data = data
        self.size = _size.compute_size(shape)
        self.step_sizes = _shape.compute_step_size(shape)
        if dtype is not None:
            self.dtype = dtype
        else:
            if len(data > 0):
                self.dtype = type(data[0])
            else:
                self.dtype = int

    def __getitem__(self, pos):
        if type(pos) == int and len(self.shape) == 1:
            return self.data[pos]

        if len(pos) == len(self.shape):
            index = 0
            for i, p in enumerate(pos):
                index += p * self.step_sizes[i]
            return self.data[index]
        else:
            raise ValueError("Unsupported Operation")

    def __setitem__(self, pos, value):
        if type(pos) == int and len(self.shape) == 1:
            self.data[pos] = value
            return

        if len(pos) == len(self.shape):
            index = 0
            for i, p in enumerate(pos):
                index += p * self.step_sizes[i]
            self.data[index] = value
        else:
            raise ValueError("Unsupported Operation")

    def __str__(self):
        return f'data: {self.data}, shape: {self.shape}'

    def __add__(self, other):
        if type(other) == ndarray:
            if self.shape == other.shape:
                data = []
                for i in range(self.size):
                    data.append(self.data[i] + other.data[i])
                return ndarray(self.shape, data)
            else:
                raise ValueError("Unsupported Operation")
        elif type(other) == self.dtype:
            data = []
            for i in range(self.size):
                data.append(self.data[i] + other)
            return ndarray(self.shape, data)

    def __mul__(self, other: ndarray):
        if self.shape == other.shape:
            data = []
            for i in range(self.size):
                data.append(self.data[i] * other.data[i])
            return ndarray(self.shape, data)
        else:
            raise ValueError("Unsupported Operation")

    def __matmul__(self, other):
        from src.array_creation import array
        if not len(self.shape) == 2 or not len(other.shape) == 2:
            raise ValueError("Unsupported Operation")
        if self.shape[1] == other.shape[0]:
            result = [[0] * other.shape[1] for _ in range(self.shape[0])]
            for i in range(self.shape[0]):
                for j in range(other.shape[1]):
                    for k in range(self.shape[1]):
                        result[i][j] += self[i, k] * other[k, j]
            return array(result)
        else:
            raise ValueError("Incompatible matrix sizes")

    def reshape(self, shape):
        """ Reshapes the array to the given shape.

        Args:
            shape: The new shape of the array. Must be compatible with the current shape
                (i.e. the number of elements must remain the same).
        """
        if _size.compute_size(shape) == self.size:
            self.shape = shape
            self.step_sizes = _shape.compute_step_size(shape)
        else:
            raise ValueError("Incompatible shape")
