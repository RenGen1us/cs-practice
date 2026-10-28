def count_items(values: list):
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts

def unique_sorted(values: list):
    return sorted(set(values))

def common(first: list, second: list):
    c = set(first) & set(second)
    return sorted(c)

def only_in_first(first: list, second: list):
    c = set(first) - set(second)
    return sorted(c)
