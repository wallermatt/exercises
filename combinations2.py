


def combinations(nums, size):
    results = []
    if len(nums) == size:
        return [nums]
    if nums ==[]:
        return []
    if size == 0:
        return []
    if size == 1:
        return [[e] for e in nums]
    for i, j in enumerate(nums):
        for c in combinations(nums[i+1:], size - 1):
            results.append([j] + c)
    return results


def all_combinations(nums):
    size = len(nums)
    results = []
    for i in range(size):
        sub_results = combinations(nums, i+1)
        results += sub_results
    return results


assert combinations([], 1) == []
assert combinations([1,2,3],1) == [[1], [2], [3]]
#print(combinations([1,2,3],2))
assert combinations([1,2,3],2) == [[1, 2], [1, 3], [2, 3]]
#print(combinations([1,2,3],3))
print(all_combinations([1,2,3]))
