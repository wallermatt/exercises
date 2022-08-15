'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''
from tabnanny import check
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        formatted_nums = []
        positions = {}
        for i, e in enumerate(nums):
            if e not in positions or len(positions[e]) < 3:
                formatted_nums += [e]
            else:
                continue
            if e not in positions:
                positions[e] = [i]
            else:
                positions[e] = positions[e] + [i]
        #print(positions, formatted_nums)
        nums = formatted_nums
        positions = {}
        for i,e in enumerate(nums):
            if e not in positions:
                positions[e] = [i]
            else:
                positions[e] = positions[e] + [i]
        zero_triplets = []
        check_used = set()
        for i, e1 in enumerate(nums):
            for j, e2 in enumerate(nums[i+1:]):
                if i+j+1 >= len(nums):
                    break
                reminder = 0 - e1 - e2
                zero_sum = sorted([e1, e2, reminder])
                key = str(zero_sum[0]) + str(zero_sum[1])+ str(zero_sum[2])
                if key in check_used:
                    continue
                if reminder in positions:
                    add = False
                    for p in positions[reminder]:
                        if p > i+1+j:
                            add = True
                            break
                    if add:
                        zero_triplets.append(zero_sum)
                        check_used.add(key)
        #print(zero_triplets)
        return zero_triplets

s = Solution()

#s.threeSum([0,0, -2, 5,6,7,8,99, 7, 1])  [-5, -4, -2, -1, -5, 3, 4, -4, -5, -2, -3, 0, -3, -1, 1]

print(s.threeSum([-5,-4,-2,-1,-5,3,4,-4,-5,-2,-3,0,-5,-3,-1,1]))


#[[-5,1,4],[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-2,-2,4],[-2,-1,3],[-1,0,1]]


assert s.threeSum([0,0,0]) == [[0,0,0]]
assert s.threeSum([0,1,1]) == []
assert s.threeSum([-1,0,1,2,-1,-4]) == [[-1,0,1], [-1,-1,2]]
