def count_items(values: list):
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts

def unique_sorted(values: list):
    c = []
    for value in values:
        c.append(value)
    return sorted(set(c))


values = ["ошибка", "запуск", "ошибка", "проверка"]

print(count_items(values))   # {"ошибка": 2, "запуск": 1, "проверка": 1}
print(unique_sorted(values))  # ["запуск", "ошибка", "проверка"]

# common(["иванов", "петрова"], ["петрова", "котов"])        # ["петрова"]
# only_in_first(["иванов", "петрова"], ["петрова", "котов"]) # ["иванов"]