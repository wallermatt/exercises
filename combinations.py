

DIGITS = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]

def combinations(n):
    results = []
    if n == 0:
        return []
    if n == 1:
        return DIGITS
    for j in DIGITS:
        for c in combinations(n - 1):
            results.append(j + c)
    return results


assert combinations(0) == []
assert combinations(1) == DIGITS
print(len(combinations(2)))
print(len(combinations(3)))
print(combinations(3))
