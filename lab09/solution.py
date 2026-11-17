import numpy as np


def make_hours():
    return np.arange(0, 22, 3).tolist()


def vector_report(values):
    arr = np.asarray(values, dtype=float)
    return {
        "third": float(arr[2]),
        "last": float(arr[-1]),
        "middle": arr[2:6].tolist(),
        "every_second": arr[::2].tolist(),
        "reversed": arr[::-1].tolist(),
    }


def change_vector(values):
    result = np.asarray(values, dtype=float).copy()
    result[2:5] = 99
    result[::2] = -1
    return result.tolist()


def cap_above(values, limit):
    result = np.asarray(values, dtype=float).copy()
    result[result > limit] = limit
    return result.tolist()


def celsius_to_fahrenheit(values):
    arr = np.asarray(values, dtype=float)
    return (arr * 9 / 5 + 32).tolist()