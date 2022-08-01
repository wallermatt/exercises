'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''
class Solution:
    def maxArea(self, array):
        max_area = 0
        max_height = 0
        for i, e in enumerate(array):
            if e <= max_height:
                continue
            inner_max_height = 0
            for j in range(len(array), 0, -1):
                idx = j - 1
                if idx <= i:
                    continue
                if inner_max_height >= array[idx]:
                    continue
                area = min(e,array[idx]) * (idx - i) 
                max_area = max(max_area, area)
                inner_max_height = array[idx]
            max_height = e
        return max_area


s = Solution()
assert s.maxArea([1,1]) == 1
assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49