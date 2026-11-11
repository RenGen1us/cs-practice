import numpy as np

print("=== Задание 1 ===")
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)
print("line:", line)
print("zeros:", zeros)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)

print("\n=== Задание 2 ===")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2-5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])

print("\n=== Задание 3 ===")
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("Форма:", temperatures.shape)
print("Число измерений:", temperatures.ndim)
print("Число элементов:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])
center = temperatures[:2, 1:3]
print("Центральный фрагмент 2x2:\n", center)
print("Форма центрального фрагмента:", center.shape)

print("\n=== Задание 4 ===")
matrix = np.arange(1, 26).reshape(5, 5)
print("matrix:\n", matrix)

part = matrix[:3]
print("Первые три строки:\n", part)
print("shape:", part.shape)

part = matrix[-2:]
print("Последние две строки:\n", part)
print("shape:", part.shape)

part = matrix[:, :2]
print("Первые два столбца:\n", part)
print("shape:", part.shape)

part = matrix[1:4, 2:5]
print("Строки 1-3, столбцы 2-4:\n", part)
print("shape:", part.shape)

part = matrix[-2:, -2:]
print("Угловой блок 2x2 справа снизу:\n", part)
print("shape:", part.shape)

print("\n=== Задание 5 ===")

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print("vector:", vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("small_matrix:\n", small_matrix)

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1
print("changed_hours:", changed_hours)
print("hours (исходный):", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print("changed_matrix:\n", changed_matrix)
print("matrix (исходная):\n", matrix)

print("\n=== Задание 6 ===")
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("numbers.shape:", numbers.shape)
print("table.shape:", table.shape)
print("transposed.shape:", transposed.shape)