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
        print(nums1, nums2)
        if not nums1 and not nums2:
            return 0
        elif not nums1:
            return self.getArrayMedian(nums2)
        elif not nums2:
            return self.getArrayMedian(nums1)
        elif len(nums1) == 1 and len(nums2) == 1:
            return (nums1[0] + nums2[0]) / 2
        elif len(nums1) <= 2 or len(nums2) <= 2:
            return self.getArrayMedian(sorted(nums1 + nums2))


        median1 = self.getArrayMedian(nums1)
        median2 = self.getArrayMedian(nums2)

        if median1 == median2:
            return median1
        elif median1 < median2:
            return self.findMedianSortedArrays(self.get_right(nums1), self.get_left(nums2))
        elif median1 > median2:
            return self.findMedianSortedArrays(self.get_left(nums1), self.get_right(nums2))
            
    def getArrayMedian(self, nums):
        len_ = len(nums)
        if len_ == 1:
            return nums[0]
        if len_ % 2 == 1:
            return nums[len_ // 2]
        else:
            return (nums[len_ // 2] + nums[(len_// 2) - 1]) / 2

    def get_left(self, nums):
        len_ = len(nums)
        if len_ == 1:
            return []
        if len_ % 2 == 1:
            return nums[:(len_ // 2) +1]
        else:
            return nums[:len_ // 2] 

    def get_right(self, nums):
        len_ = len(nums)
        if len_ == 1:
            return []
        if len_ % 2 == 1:
            return nums[(len_ // 2):]
        else:
            return nums[len_ // 2:] 

s = Solution()

#print(s.joinTwoSortedArrays([1,2], [1,2]))
#print(s.joinTwoSortedArrays([1,2,3,7,11], [1,2,3,4]))
#print(s.getArrayMedia([1,2,3]))
#print(s.getArrayMedia([1,2,3,4]))

x = [1,2,5]
y = [3,4,6]
#assert s.findMedianSortedArrays(x,y) == 3.5

x = [1,2,3]
y = [4,5,6,7]
assert s.findMedianSortedArrays(x,y) == 4

assert s.findMedianSortedArrays([1, 2], [-1,3]) == 1.5


assert s.findMedianSortedArrays([1,3], [2]) == 2
assert s.findMedianSortedArrays([1, 2], [3,4]) == 2.5


