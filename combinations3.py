from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    size = len(nums)
    results = {}
    for i in range(size):
        if i == 0:
            continue
        sub_results = combinations(nums, i+1, 0)
        for s in sub_results:
            s_sum = sum(nums[i] for i in s)
            diff = target - s_sum
            if diff == 0:
                return s
            else:
                if diff in results:
                    if not results[diff].intersection(set(s)):
                        return sorted(list(results[diff]) + s)
            results[s_sum] = set(s)

    
def combinations(nums, size, offset):
    results = []
    if len(nums) == size:
        return [[e + offset for e in range(len(nums))]]
    if nums ==[]:
        return []
    if size == 0:
        return []
    if size == 1:
        return [[e + offset] for e in range(len(nums))]
    for i, j in enumerate(nums):
        for c in combinations(nums[i+1+offset:], size - 1, offset + i + 1):
            results.append([i + offset] + c)
    return results

#assert twoSum([1,2,3], 6) == [0,1,2]
#assert twoSum([2,7,11,15], 9) == [0,1]

print(twoSum([-1,-2,-3,-4,-5], -8))
