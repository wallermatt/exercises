from typing import List

def calculate_median(nums: List[int]) -> float:
    nums_len = len(nums)
    if nums_len == 0:
        raise Exception("List contains not elements")
    if nums_len == 1:
        return nums[0]
    if nums_len % 2 == 1:
        return nums[int((nums_len - 1) / 2)]
    right = nums[int(nums_len / 2)]
    left = nums[int(nums_len / 2) - 1]
    return (left + right) / 2


def median_of_two_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    nums_total = sorted(nums1 + nums2)
    return calculate_median(nums_total)

assert calculate_median([1]) == 1
assert calculate_median([1, 2]) == 1.5
assert calculate_median([1, 2, 3]) == 2

print(median_of_two_sorted_arrays([1,3], [2]))
print(calculate_median([5,6,7,7,7,8]))
print(median_of_two_sorted_arrays([1,3], [5,6,7,7,7,8]))
print(median_of_two_sorted_arrays([1,3,9], [5,6,7,7,7,8]))
