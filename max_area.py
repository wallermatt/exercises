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
2 <= n <= 10^5
0 <= height[i] <= 10^4

[1]

[1,2] = 1

[1,2,1] = 2

[1,2,2] = 2

[1,3,3] = 3

[]

'''
class Solution:
    def maxArea(self, height):
        len_ = len(height)
        biggest = 0
        right = {}
        for i in range(len_ -1, 0, -1):
            if height[i] > biggest:
                right[height[i]] = i
                biggest = height[i]
        biggest = 0
        left = {}
        for i in range(len_):
            if height[i] > biggest:
                left[height[i]] = i
                biggest = height[i]
        max_area = 0
        for l in left:
            for r in right:
                area = min(l,r) * (right[r] - left[l])
                if area > max_area:
                    max_area = area
        return max_area
        

    def maxArea2(self, height):
        furthest = {}
        max_area = 0
        biggest = 0
        for i,e in enumerate(height):
            for n in furthest:
                area = min(n,e) * (i - furthest[n])
                if area > max_area:
                    max_area = area
            if e > biggest:
                furthest[e] = i
                biggest = e
        return max_area

    def maxArea3(self, height):
        len_ = len(height)
        biggest = 0
        right = []
        for i in range(len_ -1, 0, -1):
            if height[i] > biggest:
                right = [[height[i], i]] + right
                biggest = height[i]
        biggest = 0
        left = []
        for i in range(len_):
            if height[i] > biggest:
                left = [[height[i], i]] + left
                biggest = height[i]
        max_area = 0
        for l in left:
            max_height = 0
            max_idx = 0
            for r in right:
                area = min(l[0],r[0]) * (r[1] - l[1])
                if area > max_area:
                    max_area = area
                    max_height = r[0]
            print(l, r, max_area, "left: ", left, "right: ", right)
            if max_height:
                new_right = [e for e in right if e[0] <= max_height or e[1] <= l[1]]
                right = new_right
        return max_area
            


s = Solution()
assert s.maxArea3([177,112,74,197,90,16,4,61,103,133,198,4,121,143,55,138,47,167,165,159,93,85,53,118,127,171,137,65,135,45,151,64,109,25,61,152,194,65,165,97,199,163,53,72,58,108,10,105,27,127,64,120,164,70,190,91,41,127,109,176,172,12,193,34,38,54,138,184,120,103,33,71,66,86,143,125,146,105,182,173,184,199,46,148,69,36,192,110,116,53,38,40,65,31,74,103,86,12,39,158]) == 15936

assert s.maxArea3([4,4,2,11,0,11,5,11,13,8]) == 55
assert s.maxArea3([1,1]) == 1
assert s.maxArea3([1,8,6,2,5,4,8,3,7]) == 49

#assert s.maxArea2([1,1]) == 1
#assert s.maxArea2([1,8,6,2,5,4,8,3,7]) == 49