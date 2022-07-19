from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    dict_ = {}
    for i,e in enumerate(nums):
        if e in dict_:
            dict_[e] = dict_[e] + [i]
        else:
            dict_[e] = [i]

    for i,e in enumerate(nums):
        diff = target - e
        if diff in dict_:
            if diff == e:
                if len(dict_[diff]) == 2:
                    return dict_[diff]
            else:
                return [i] + dict_[diff]
        
print(twoSum([3,2,4], 6))
assert twoSum([2,7,11,15], 9) == [0,1]

print(twoSum([-1,-2,-3,-4,-5], -8))
