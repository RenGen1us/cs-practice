def count_items(values: list):
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts

def unique_sorted(values: list):
    return sorted(set(values))

def common(first: list, second: list):
    p = []
    for item in first:
        if item in second:
            p.append(item)
    return sorted(p)

def only_in_first(first: list, second: list):
    p = []
    for item in first:
        if item not in second:
            p.append(item)
    return sorted(p)
