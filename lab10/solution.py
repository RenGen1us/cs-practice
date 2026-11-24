import numpy as np


def make_table(rows, columns):
    return np.arange(rows * columns).reshape(rows, columns).tolist()


def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    arr = np.asarray(matrix, dtype=float)
    return arr[row_start:row_stop, column_start:column_stop].tolist()


def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    result = np.asarray(matrix, dtype=float).copy()
    result[row_start:row_stop, column_start:column_stop] = value
    return result.tolist()


def matrix_vector_product(matrix, vector):
    return (np.asarray(matrix, dtype=float) @ np.asarray(vector, dtype=float)).tolist()


def matrix_multiply(left, right):
    return (np.asarray(left, dtype=float) @ np.asarray(right, dtype=float)).tolist()


def transpose_matrix(matrix):
    return np.asarray(matrix, dtype=float).T.tolist()


def solve_system(matrix, vector):
    x = np.linalg.solve(np.asarray(matrix, dtype=float), np.asarray(vector, dtype=float))
    return np.round(x, 6).tolist()


def tensor_channel_mean(tensor):
    return np.asarray(tensor, dtype=float).mean(axis=-1).tolist()


def point_distance(first, second):
    diff = np.asarray(first, dtype=float) - np.asarray(second, dtype=float)
    return round(float(np.linalg.norm(diff)), 6)