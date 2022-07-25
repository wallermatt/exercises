'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        joined_array = self.joinTwoSortedArrays(nums1, nums2)
        return self.getArrayMedian(joined_array)

    def joinTwoSortedArrays(self, num1, num2):
        joined_array = []
        while num1 or num2:
            if not num1:
                joined_array += num2
                return joined_array
            elif not num2:
                joined_array += num1
                return joined_array
            elif num1[0] <= num2[0]:
                joined_array.append(num1[0])
                num1 = num1[1:]
            elif num1[0] > num2[0]:
                joined_array.append(num2[0])
                num2 = num2[1:]
        return joined_array
            
    def getArrayMedian(self, nums):
        len_ = len(nums)
        if len_ == 1:
            return nums[0]
        if len_ % 2 == 1:
            return nums[len_ // 2]
        else:
            return (nums[len_ // 2] + nums[(len_// 2) - 1]) / 2

s = Solution()

#print(s.joinTwoSortedArrays([1,2], [1,2]))
#print(s.joinTwoSortedArrays([1,2,3,7,11], [1,2,3,4]))
#print(s.getArrayMedia([1,2,3]))
#print(s.getArrayMedia([1,2,3,4]))



assert s.findMedianSortedArrays([1,3], [2]) == 2
assert s.findMedianSortedArrays([1, 2], [3,4]) == 2.5


